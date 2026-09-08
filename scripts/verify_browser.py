"""Optional browser validation: pip install -r requirements-browser.txt first.

Uses installed Microsoft Edge. Start Flask separately before running this script.
Screenshots and a report are written to artifacts/ (ignored by git).
"""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:5000"
OUTPUT = Path("artifacts")


def no_overflow(page):
    assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), page.url


def screenshot(page, name):
    # Full-page captures do not scroll: visit sections so reveal effects run first.
    for section in page.locator('.reveal').all():
        section.evaluate("el => el.scrollIntoView({behavior: 'instant', block: 'center'})")
        page.wait_for_function("el => !el.classList.contains('pending')", arg=section.element_handle())
    page.evaluate("window.scrollTo({top: 0, behavior: 'instant'})")
    page.wait_for_function("Array.from(document.querySelectorAll('.reveal')).every(el => !el.classList.contains('pending'))")
    page.screenshot(path=str(OUTPUT / name), full_page=True, animations="disabled")


def main():
    OUTPUT.mkdir(exist_ok=True)
    errors = []
    checks = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000}, device_scale_factor=1)
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(BASE, wait_until="networkidle")
        assert page.locator(".mood-card").count() == 6
        assert page.locator(".movie-card").count() == 5
        assert page.evaluate("Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)")
        no_overflow(page)
        screenshot(page, "home-desktop.png")
        checks.append("Desktop home, assets, six moods, local posters, no overflow")

        page.locator('.mood-card[value="happy"]').hover(position={"x": 20, "y": 20})
        page.wait_for_timeout(400)
        assert "rotateX" in page.locator('.mood-card[value="happy"]').get_attribute("style")
        checks.append("Desktop pointer tilt responds")
        for mood in ["happy", "sad", "romantic", "excited", "bored", "relaxed"]:
            page.goto(BASE)
            page.locator(f'.mood-card[value="{mood}"]').click()
            page.wait_for_url("**/recommend")
            assert page.locator(".movie-card").count() == 4
            assert page.locator(f'.mood-card[value="{mood}"]').get_attribute("aria-pressed") == "true"
        screenshot(page, "recommend-desktop.png")
        checks.append("All six mood buttons submit and show four matching results")

        page.goto(BASE + "/movies")
        page.get_by_role("link", name="Sci-Fi", exact=True).click()
        assert page.locator(".movie-card").count() == 3
        page.get_by_role("link", name="View details: Interstellar", exact=True).click()
        assert page.locator("h1").inner_text() == "Interstellar"
        screenshot(page, "detail-desktop.png")
        page.get_by_role("link", name="More like this").click()
        assert page.url.endswith("#similar")
        checks.append("Catalog, genre chip, card navigation, details, similar anchor")

        page.goto(BASE + "/search")
        page.get_by_role("searchbox").fill("wormhole")
        page.get_by_role("button", name="Search").click()
        assert page.locator(".movie-card").count() == 1
        page.get_by_role("searchbox").fill("zzzzzzzzz")
        page.get_by_role("button", name="Search").click()
        assert page.get_by_role("heading", name="No movies found.").is_visible()
        page.get_by_role("searchbox").fill("")
        page.get_by_role("button", name="Search").click()
        assert page.get_by_role("heading", name="Every great night starts somewhere.").is_visible()
        page.goto(BASE + "/random")
        assert "/movie/" in page.url
        assert page.locator(".detail-poster").is_visible()
        checks.append("Search submit, no results, empty query, Surprise me")

        page.locator(".detail-poster").evaluate("img => img.src = '/static/intentionally-missing.svg'")
        page.wait_for_function("document.querySelector('.detail-poster').src.endsWith('poster-fallback.svg') && document.querySelector('.detail-poster').naturalWidth > 0")
        checks.append("Broken image replaced by local fallback")

        for width in [320, 390, 768, 1024, 1440]:
            page.set_viewport_size({"width": width, "height": 900})
            for path in ["/", "/movies", "/movie/13", "/recommend?mood=romantic", "/search?q=zzzz", "/movie/999"]:
                page.goto(BASE + path)
                no_overflow(page)
        checks.append("Six page types at 320, 390, 768, 1024, 1440 px without horizontal overflow")

        mobile = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True, device_scale_factor=1)
        phone = mobile.new_page()
        phone.on("pageerror", lambda error: errors.append(str(error)))
        phone.goto(BASE)
        phone.get_by_role("button", name="Menu").click()
        assert phone.locator("#nav-links").is_visible()
        phone.keyboard.press("Escape")
        assert not phone.locator("#nav-links").is_visible()
        phone.get_by_role("button", name="Menu").click()
        phone.get_by_role("navigation", name="Main navigation").get_by_role("link", name="Movies", exact=True).click()
        assert phone.locator(".movie-card").count() == 24
        assert phone.locator(".movie-overlay").first.evaluate("el => getComputedStyle(el).opacity") == "1"
        screenshot(phone, "movies-mobile.png")
        phone.goto(BASE)
        screenshot(phone, "home-mobile.png")
        checks.append("Touch mobile navigation, Escape, catalog, always-visible detail action")

        page.emulate_media(reduced_motion="reduce")
        page.goto(BASE)
        assert page.locator(".poster-track").evaluate("el => getComputedStyle(el).animationName") == "none"
        page.locator(".mood-card").first.hover()
        assert page.locator(".mood-card").first.evaluate("el => getComputedStyle(el).transform") == "none"
        page.keyboard.press("Tab")
        assert page.locator(".skip-link").evaluate("el => el === document.activeElement")
        checks.append("Reduced motion disables poster animation and tilt; keyboard skip link")

        no_js = browser.new_context(java_script_enabled=False, viewport={"width": 390, "height": 844})
        plain = no_js.new_page()
        plain.goto(BASE)
        assert plain.get_by_role("navigation", name="Main navigation").is_visible()
        plain.locator('.mood-card[value="happy"]').click()
        assert plain.locator(".movie-card").count() == 4
        checks.append("Mobile navigation and recommendations work without JavaScript")
        assert errors == [], errors
        browser.close()
    report = {"browser": "Microsoft Edge (headless)", "checks": checks, "javascript_errors": errors}
    (OUTPUT / "browser-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
