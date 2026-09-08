"""Rebuild the bundled vector artwork; no network or image libraries required.

These are original geometric interpretations, not official theatrical posters.
Run from the project root: python scripts/build_posters.py
"""
import sys
from html import escape
from pathlib import Path
from textwrap import wrap

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from database.seed import MOVIES

PALETTES = [
    ("#164d70", "#e8c764", "#e08243"), ("#273d48", "#d6b365", "#b64534"),
    ("#973b58", "#f6d4b4", "#d9868d"), ("#1d4648", "#eee1a3", "#64a5a1"),
    ("#23352c", "#d4b979", "#798e72"), ("#253e4c", "#e2c5a1", "#719ba1"),
    ("#394c69", "#f0d989", "#bc797d"), ("#5b412e", "#e4ca9a", "#b78a50"),
    ("#162548", "#e5c575", "#876296"), ("#824235", "#f2d1a0", "#b68268"),
    ("#17464b", "#d3c89d", "#78978b"), ("#3c493b", "#e5d4b4", "#89976d"),
    ("#102a38", "#e5d8ad", "#6b8b98"), ("#203941", "#e4d4ae", "#547b85"),
    ("#4c261e", "#f0c375", "#c8793d"), ("#241d42", "#ead3b2", "#bf414e"),
    ("#303c31", "#e5bc6f", "#a97444"), ("#282e3b", "#d7c091", "#79889b"),
    ("#683b2f", "#edc18b", "#af7153"), ("#274957", "#e9d29a", "#8fb1b4"),
    ("#17494c", "#e7d6af", "#87a69a"), ("#344d36", "#e8dfb8", "#8b9c75"),
    ("#294c61", "#e5d5b6", "#8db1b3"), ("#543b2a", "#e4c983", "#b46b47"),
]


def scene(index, ink, accent):
    """Simple screen-printed motifs grouped by subject, with individual details."""
    stars = ''.join(f'<circle cx="{(n*73+index*19)%370+15}" cy="{(n*47)%290+30}" r="1" fill="{ink}" opacity=".5"/>' for n in range(35))
    if index in (13, 19):
        return stars + f'<circle cx="275" cy="170" r="76" fill="{accent}"/><path d="M0 368Q140 270 400 355V600H0Z" fill="{accent}" opacity=".6"/><ellipse cx="205" cy="292" rx="20" ry="25" fill="{ink}"/><path d="M186 320h38l13 72h-20l-12-43-10 43h-19z" fill="{ink}"/><path d="M100 430 225 377 400 417V600H0Z" fill="#070d12" opacity=".65"/>'
    if index == 9:
        return stars + f'<circle cx="285" cy="100" r="39" fill="{ink}" opacity=".85"/><path d="M0 390Q180 355 400 375V600H0Z" fill="#101322"/><path d="M63 326h270v5H63zM88 326V162h5v164M67 162h46l-9-27H77z" fill="{ink}"/><circle cx="191" cy="276" r="10" fill="#080d18"/><path d="m184 286-12 44 32 0-8-43 39 8 3-8-38-13z" fill="#080d18"/><circle cx="241" cy="277" r="10" fill="#080d18"/><path d="m235 288-19 42h43l-14-43 38-20-5-7-33 16z" fill="#080d18"/><path d="m180 327-10 35m27-35 18 25m18-25-9 35m22-35 16 35" stroke="#080d18" stroke-width="8"/>'
    if index in (3, 21):
        return f'<circle cx="295" cy="110" r="49" fill="{ink}" opacity=".6"/><path d="M0 370 65 275 117 340 187 238 259 330 334 270 400 344V600H0Z" fill="{accent}" opacity=".5"/><path d="M77 210h246v198H77z" fill="{accent}"/><path d="m56 212 144-97 145 97z" fill="{ink}" opacity=".9"/><path d="M143 148h114v260H143z" fill="{ink}" opacity=".75"/><path d="m132 148 68-61 69 61z" fill="{accent}"/>' + ''.join(f'<rect x="{x}" y="{y}" width="17" height="28" rx="6" fill="#273137"/>' for x in (97,161,222,286) for y in (231,285,339))
    if index in (14, 20):
        return f'<circle cx="205" cy="180" r="114" fill="{ink}" opacity=".55"/>' + ''.join(f'<path d="M{x} 410V{130+(x*13)%160}h35V410" fill="{accent}" stroke="#162932" stroke-width="2"/>' for x in range(0,400,40)) + f'<path d="m0 600 193-240h14l193 240" fill="#121e24"/><path d="m200 580 0-205" stroke="{ink}" stroke-width="2" stroke-dasharray="12 20"/>'
    if index in (17, 18):
        return f'<circle cx="200" cy="245" r="130" fill="none" stroke="{ink}" stroke-width="2"/><circle cx="200" cy="245" r="111" fill="none" stroke="{accent}" stroke-width="18"/><path d="M125 350V176h150v174" fill="#111c1d"/><path d="m126 177 37 24v148h-37zm148 0-37 24v148h37" fill="{accent}"/><ellipse cx="200" cy="285" rx="24" ry="34" fill="{ink}"/><path d="m200 288-15 62h30z" fill="{ink}"/><path d="M200 355 88 440h224z" fill="{ink}" opacity=".28"/>'
    if index in (12, 22, 23):
        return f'<circle cx="286" cy="138" r="65" fill="{ink}" opacity=".8"/><path d="m0 340 126-193 95 147 58-72 121 130V600H0" fill="{accent}"/><path d="m0 389 118-82 135 54 147-52V600H0" fill="#1c3336"/><path d="m0 449 155-46 245 52V600H0" fill="{accent}" opacity=".5"/>' + (f'<ellipse cx="211" cy="333" rx="54" ry="66" fill="{ink}"/><path d="m168 285 7-47 20 36m35 0 20-36 7 47" fill="{ink}"/><circle cx="192" cy="306" r="5" fill="#25382c"/><circle cx="229" cy="306" r="5" fill="#25382c"/>' if index == 22 else '<circle cx="173" cy="355" r="8" fill="#111e23"/><path d="m170 363-7 41h24l-10-41z" fill="#111e23"/>')
    if index in (1, 6, 7, 16):
        return stars + f'<circle cx="200" cy="250" r="118" fill="{accent}"/><circle cx="200" cy="250" r="91" fill="none" stroke="{ink}" stroke-width="2"/><path d="m200 141 24 76 79 0-64 46 25 76-64-47-64 47 25-76-64-46h79z" fill="{ink}" opacity=".8"/>'
    if index in (2, 24):
        return f'<circle cx="200" cy="250" r="129" fill="{ink}" opacity=".85"/><path d="M74 270h252v86H74zM101 211h176l49 59H74z" fill="{accent}"/><path d="M116 224h67v44h-67zm83 0h67l40 44H199z" fill="#243e43"/><circle cx="125" cy="358" r="27" fill="#1c2528"/><circle cx="278" cy="358" r="27" fill="#1c2528"/><path d="M30 389h340" stroke="{ink}" stroke-width="2"/>'
    if index == 15:
        return f'<circle cx="270" cy="166" r="100" fill="{ink}"/><path d="M0 326 121 277 278 333 400 260V600H0Z" fill="{accent}"/><path d="m0 389 185-36 215 61V600H0Z" fill="#321f1c"/><path d="M116 326h168v44H96zM145 295h91l33 32H131z" fill="#221d1d"/><circle cx="134" cy="371" r="23" fill="#171819"/><circle cx="255" cy="371" r="23" fill="#171819"/>'
    return f'<circle cx="200" cy="216" r="110" fill="{accent}" opacity=".6"/><path d="M0 386Q200 314 400 386V600H0Z" fill="#152727" opacity=".8"/><path d="M61 169h278v220H61z" fill="none" stroke="{ink}" stroke-width="3"/><path d="M200 170v218" stroke="{ink}" stroke-width="2"/><circle cx="168" cy="286" r="15" fill="{ink}"/><path d="m155 301-13 78h46l-12-78z" fill="{ink}"/><circle cx="229" cy="286" r="15" fill="{ink}"/><path d="m218 301-18 78h57l-18-78z" fill="{ink}"/>'


def build():
    output = Path(__file__).resolve().parents[1] / "static" / "images" / "posters"
    output.mkdir(parents=True, exist_ok=True)
    for index, row in enumerate(MOVIES, 1):
        title, year, _, _, _, genre, _ = row
        background, ink, accent = PALETTES[index-1]
        lines = wrap(title.upper(), width=19)
        size = 30 if len(title) < 30 else 25
        lettering = ''.join(
            f'<text x="200" y="{462+n*34}" text-anchor="middle" fill="{ink}" '
            f'font-family="Georgia,serif" font-weight="bold" '
            f'font-size="{min(size, 330 / (len(line) * .72)):.1f}">{escape(line)}</text>'
            for n, line in enumerate(lines)
        )
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" role="img" aria-label="{escape(title)} illustrated poster">
<rect width="400" height="600" fill="{background}"/>
{scene(index, ink, accent)}
<rect x="18" y="18" width="364" height="564" fill="none" stroke="{ink}" stroke-opacity=".4"/>
<text x="200" y="48" text-anchor="middle" fill="{ink}" font-family="sans-serif" font-size="9" letter-spacing="4">THE MOODMOVIE COLLECTION</text>
<rect x="25" y="419" width="350" height="146" fill="{background}" opacity=".94"/>
{lettering}
<text x="200" y="558" text-anchor="middle" fill="{ink}" font-family="sans-serif" font-size="10" letter-spacing="3">{year} · {genre.upper()}</text>
</svg>'''
        (output / f"{index:02d}.svg").write_text(svg, encoding="utf-8")
    print(f"Built {len(MOVIES)} local SVG posters.")


if __name__ == "__main__":
    build()
