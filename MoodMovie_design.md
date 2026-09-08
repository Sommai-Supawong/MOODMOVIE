# 🎬 MoodMovie — Design System & UI/UX Specification

เอกสารนี้กำหนดแนวทางการออกแบบเว็บไซต์ **MoodMovie — Movie Recommendation by Mood**  
โดยเน้นภาพลักษณ์แบบ **Dark Cinematic + Premium Gold + Glass UI + Liquid Glass + 3D Motion**

เป้าหมายคือให้เว็บไซต์มีความรู้สึกเหมือนแพลตฟอร์มหนังระดับพรีเมียม แต่มีเอกลักษณ์เฉพาะตัวจากการใช้ Mood, Motion และ Interaction ที่ตอบสนองต่อผู้ใช้แบบนุ่มนวล

---

# 1. Design Direction

## Main Concept

```text
Dark Cinematic
+
Premium Gold
+
Glassmorphism
+
Liquid Glass
+
3D Interaction
+
Smooth Motion
```

MoodMovie ควรให้ความรู้สึกดังนี้

- ลึกลับ
- พรีเมียม
- ทันสมัย
- Cinematic
- Interactive
- Immersive
- Smooth
- ไม่แออัด
- มีมิติ
- ดูเป็น Product จริง

---

# 2. Visual Identity

## Primary Mood

ใช้พื้นหลังสีดำหรือดำอมเทาเป็นหลัก

```text
Black
Charcoal Black
Deep Graphite
Dark Gray
```

สี Accent ใช้ **Yellow Gold / Warm Gold**

```text
Gold
Amber Gold
Soft Yellow Gold
```

Glass UI ใช้พื้นหลังโปร่งใสผสม Blur

---

# 3. Color Palette

## Main Colors

| Role | Color | Hex |
|---|---|---|
| Main Background | Deep Black | `#070707` |
| Secondary Background | Graphite | `#111111` |
| Card Background | Glass Black | `rgba(255,255,255,0.06)` |
| Main Gold | Premium Gold | `#F5C451` |
| Bright Gold | Highlight Gold | `#FFD76A` |
| Dark Gold | Deep Gold | `#C99A2E` |
| Main Text | Soft White | `#F5F5F5` |
| Secondary Text | Gray | `#B5B5B5` |
| Muted Text | Dark Gray | `#777777` |
| Border | Glass Border | `rgba(255,255,255,0.10)` |

---

## Gradient Colors

### Gold Gradient

```css
background: linear-gradient(
  135deg,
  #F5C451,
  #FFD76A,
  #C99A2E
);
```

### Dark Background Gradient

```css
background:
  radial-gradient(
    circle at top,
    rgba(245, 196, 81, 0.08),
    transparent 35%
  ),
  linear-gradient(
    180deg,
    #070707,
    #0D0D0D,
    #070707
  );
```

---

# 4. Typography

แนะนำใช้ Font แบบ Modern Sans Serif

ตัวอย่าง

```text
Inter
Manrope
DM Sans
Plus Jakarta Sans
Outfit
```

หากรองรับภาษาไทย

```text
Noto Sans Thai
Sarabun
Prompt
IBM Plex Sans Thai
```

---

## Typography Scale

| Element | Size |
|---|---|
| Hero Title | `56–72px` |
| Section Title | `36–48px` |
| Card Title | `20–24px` |
| Body | `15–18px` |
| Small Text | `12–14px` |
| Button | `14–16px` |

---

## Hero Style

```css
.hero-title {
  font-size: clamp(3rem, 7vw, 5.5rem);
  font-weight: 700;
  letter-spacing: -0.04em;
  line-height: 0.95;
}
```

Highlight บางคำด้วย Gold

```html
Find a movie that matches your
<span class="gold-text">mood.</span>
```

---

# 5. Background Design

พื้นหลังเป็นส่วนสำคัญของ MoodMovie

ไม่ควรเป็นพื้นหลังดำเรียบเพียงอย่างเดียว

ให้ใช้ Layer หลายชั้น

```text
Base Black
     ↓
Dark Gradient
     ↓
Blurred Movie Posters
     ↓
Glow
     ↓
Glass Overlay
     ↓
Noise Texture
```

---

# 6. Moving Movie Background

หน้า Hero สามารถมี Movie Posters ที่เคลื่อนแบบช้า ๆ อยู่ด้านหลัง

Concept

```text
Poster
Poster
Poster
Poster
Poster
   ↓
Horizontal Slow Movement
```

ตัวอย่าง Layout

```text
─────────────────────────────────

  Movie Poster   Movie Poster

        Movie Poster

 Movie Poster       Movie Poster

─────────────────────────────────
```

ใช้ Blur

```css
background-filter:
  blur(6px);
```

หรือ

```css
filter:
  blur(3px)
  brightness(0.4);
```

Opacity

```css
opacity: 0.3;
```

---

# 7. Infinite Poster Motion

Movie Poster Background เคลื่อนต่อเนื่อง

```css
.poster-track {
  animation: posterScroll 40s linear infinite;
}

@keyframes posterScroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}
```

เพื่อให้ Smooth ควรใช้

```text
transform
opacity
```

เป็นหลัก

หลีกเลี่ยง Animation ที่ต้อง Reflow บ่อย

---

# 8. Glassmorphism

Card หลักของระบบใช้ Glass UI

```css
.glass-card {
  background:
    rgba(255, 255, 255, 0.06);

  border:
    1px solid rgba(255,255,255,0.12);

  backdrop-filter:
    blur(20px);

  -webkit-backdrop-filter:
    blur(20px);

  border-radius:
    24px;

  box-shadow:
    0 20px 60px rgba(0,0,0,0.35);
}
```

---

# 9. Liquid Glass

Liquid Glass ใช้ใน Component สำคัญ เช่น

```text
Navigation
Mood Selector
Floating Button
Modal
Filter Menu
Movie Detail Overlay
```

Concept

```text
Glass
+
Refraction
+
Gradient Light
+
Soft Highlight
+
Blur
```

ตัวอย่าง

```css
.liquid-glass {
  position: relative;

  background:
    linear-gradient(
      135deg,
      rgba(255,255,255,0.10),
      rgba(255,255,255,0.03)
    );

  backdrop-filter:
    blur(24px) saturate(140%);

  border:
    1px solid rgba(255,255,255,0.12);

  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.12),
    0 20px 50px rgba(0,0,0,0.35);
}
```

---

# 10. Glass Highlight

เพิ่ม Highlight ด้านบนของ Glass Card

```css
.glass-card::before {
  content: "";

  position: absolute;

  inset: 0;

  border-radius: inherit;

  background:
    linear-gradient(
      120deg,
      rgba(255,255,255,0.15),
      transparent 30%
    );

  pointer-events: none;
}
```

---

# 11. Gold Buttons

ปุ่มหลักใช้สีทอง

ตัวอย่าง

```text
Explore Movies
Find My Mood
Surprise Me
View Details
```

CSS

```css
.primary-button {
  background:
    linear-gradient(
      135deg,
      #F5C451,
      #FFD76A
    );

  color: #090909;

  border: none;

  border-radius: 999px;

  padding:
    14px 24px;

  font-weight: 700;

  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}
```

Hover

```css
.primary-button:hover {
  transform:
    translateY(-3px)
    scale(1.03);

  box-shadow:
    0 10px 35px rgba(245,196,81,0.35);
}
```

---

# 12. Secondary Button

```css
.secondary-button {
  background:
    rgba(255,255,255,0.05);

  border:
    1px solid rgba(255,255,255,0.12);

  color:
    #F5F5F5;

  backdrop-filter:
    blur(15px);
}
```

Hover

```css
.secondary-button:hover {
  border-color:
    rgba(245,196,81,0.6);

  color:
    #F5C451;
}
```

---

# 13. Navbar Design

Navbar ใช้ Floating Glass Navigation

```text
─────────────────────────────────────

 MoodMovie

 Home
 Discover
 Moods
 Movies

                       Search   🎲

─────────────────────────────────────
```

Style

```text
Floating
Rounded
Transparent
Blur
Thin Border
```

ตัวอย่าง

```css
.navbar {
  position: fixed;

  top: 20px;

  left: 50%;

  transform:
    translateX(-50%);

  width:
    min(1100px, 92%);

  background:
    rgba(10,10,10,0.55);

  backdrop-filter:
    blur(22px);

  border:
    1px solid rgba(255,255,255,0.08);

  border-radius:
    20px;
}
```

---

# 14. Hero Section

Hero เป็นส่วนที่สร้าง First Impression

ตัวอย่าง Layout

```text
                    MOVIE POSTERS
              MOVING IN BACKGROUND


              How are you feeling?

            Find a movie that matches
                   your mood.

         Discover movies based on how
               you feel right now.


            [ Find My Mood ]

              [ Surprise Me ]



       Happy   Sad   Romantic   Excited
```

---

# 15. Hero Animation

เมื่อเปิดเว็บไซต์

ลำดับ Animation

```text
Background Fade In
        ↓
Logo Fade
        ↓
Hero Title Slide Up
        ↓
Subtitle Fade
        ↓
Buttons Slide Up
        ↓
Mood Cards Appear
```

ใช้ Delay เล็กน้อย

```text
0ms
100ms
200ms
300ms
400ms
```

---

# 16. Mood Selector

Mood Selector เป็น Component สำคัญที่สุดของระบบ

ตัวอย่าง

```text
😊
Happy

😢
Sad

❤️
Romantic

🔥
Excited

😴
Bored

😌
Relaxed
```

ใช้ Card แบบ Glass

---

# 17. Mood Card

```css
.mood-card {
  background:
    rgba(255,255,255,0.05);

  backdrop-filter:
    blur(18px);

  border:
    1px solid rgba(255,255,255,0.08);

  border-radius:
    24px;

  transition:
    transform 0.35s cubic-bezier(.2,.8,.2,1),
    border-color 0.35s ease,
    box-shadow 0.35s ease;
}
```

---

# 18. 3D Mood Hover

เมื่อ Mouse อยู่บน Mood Card

```text
Card Tilt
+
Scale
+
Gold Glow
+
Emoji Float
```

ตัวอย่าง

```css
.mood-card:hover {
  transform:
    perspective(900px)
    rotateX(5deg)
    rotateY(-6deg)
    translateY(-8px)
    scale(1.03);

  border-color:
    rgba(245,196,81,0.5);

  box-shadow:
    0 20px 50px rgba(0,0,0,0.4),
    0 0 30px rgba(245,196,81,0.12);
}
```

---

# 19. Cursor-Based 3D Tilt

สามารถใช้ JavaScript คำนวณตำแหน่ง Mouse

Concept

```text
Mouse X
Mouse Y
   ↓
Calculate Rotation
   ↓
rotateX()
rotateY()
```

ควรจำกัดค่าการหมุน

```text
ประมาณ 3°–8°
```

เพื่อไม่ให้ Motion รุนแรงเกินไป

---

# 20. Movie Card Design

Movie Card ใช้ Poster เป็นพระเอก

ตัวอย่าง

```text
┌──────────────────────────┐
│                          │
│       MOVIE POSTER       │
│                          │
│                          │
├──────────────────────────┤
│                          │
│ Interstellar             │
│ Sci-Fi • 2014            │
│                          │
│ ⭐ 8.7                   │
│                          │
└──────────────────────────┘
```

---

# 21. Movie Card Hover

Default

```text
Poster
Movie Title
Genre
Rating
```

Hover

```text
Poster Zoom
Card Raise
Gold Border
Info Overlay
View Detail Button
```

ตัวอย่าง

```css
.movie-card:hover {
  transform:
    translateY(-10px)
    scale(1.02);

  box-shadow:
    0 25px 70px rgba(0,0,0,0.45);
}
```

Poster

```css
.movie-card:hover img {
  transform:
    scale(1.08);
}
```

---

# 22. Cinematic Image Zoom

Movie Poster ควรมี

```css
.movie-poster {
  transition:
    transform 0.6s cubic-bezier(.2,.8,.2,1);
}
```

Animation ควรช้าเล็กน้อยเพื่อให้รู้สึก Premium

---

# 23. Movie Overlay

เมื่อ Hover

```css
.movie-overlay {
  position:
    absolute;

  inset:
    0;

  background:
    linear-gradient(
      transparent,
      rgba(0,0,0,0.95)
    );
}
```

---

# 24. Movie Grid

Desktop

```text
5 Columns
```

Laptop

```text
4 Columns
```

Tablet

```text
2–3 Columns
```

Mobile

```text
2 Columns
```

---

# 25. Horizontal Movie Carousel

Recommendation Section สามารถเลื่อนแนวนอนได้

```text
Recommended for You

←

Movie
Movie
Movie
Movie
Movie

→
```

ใช้

```css
overflow-x:
  auto;

scroll-snap-type:
  x mandatory;
```

---

# 26. Smooth Scroll

```css
html {
  scroll-behavior:
    smooth;
}
```

Section Transition สามารถเพิ่ม Fade In เมื่อ Scroll เข้ามาใน Viewport

---

# 27. Scroll Reveal Animation

Element เริ่มต้น

```css
.reveal {
  opacity:
    0;

  transform:
    translateY(30px);
}
```

เมื่อ Visible

```css
.reveal.active {
  opacity:
    1;

  transform:
    translateY(0);

  transition:
    0.7s cubic-bezier(.2,.8,.2,1);
}
```

---

# 28. Recommended Movie Section

ตัวอย่าง Layout

```text
Because you're feeling

😌 Relaxed

─────────────────────────────────

Movies for your mood

Spirited Away
About Time
The Secret Life of Walter Mitty

─────────────────────────────────
```

ใช้ Mood เป็น Accent ด้านบน

---

# 29. Search Design

Search Bar ใช้ Glass Pill

```text
┌────────────────────────────────┐
│ 🔍 Search movies...            │
└────────────────────────────────┘
```

Focus

```text
Border Gold
Glow
Expand Slightly
```

---

# 30. Search Interaction

```css
.search-input:focus {
  border-color:
    #F5C451;

  box-shadow:
    0 0 0 4px rgba(245,196,81,0.1);
}
```

---

# 31. Filter UI

Filter ใช้ Chip

```text
All
Action
Comedy
Drama
Romance
Sci-Fi
Mystery
Animation
```

Default

```text
Glass Gray
```

Selected

```text
Gold Background
Black Text
```

---

# 32. Movie Detail Page

Movie Detail ใช้ Cinematic Hero

```text
BACKGROUND MOVIE IMAGE
blur + dark overlay


        Poster

       Interstellar

Sci-Fi • Drama • 2014

⭐ 8.7

Description...

[ Back ]
[ Similar Movies ]
```

---

# 33. Movie Detail Glass Panel

Detail Panel ใช้ Glass

```css
.movie-detail-panel {
  background:
    rgba(15,15,15,0.55);

  border:
    1px solid rgba(255,255,255,0.1);

  backdrop-filter:
    blur(30px);

  border-radius:
    30px;
}
```

---

# 34. 3D Poster Effect

Poster สามารถมีมิติเล็กน้อย

```css
.movie-detail-poster {
  transform:
    perspective(1200px)
    rotateY(-4deg);

  box-shadow:
    30px 30px 80px rgba(0,0,0,0.5);
}
```

Hover

```css
.movie-detail-poster:hover {
  transform:
    perspective(1200px)
    rotateY(0)
    translateY(-6px);
}
```

---

# 35. Loading Animation

เมื่อระบบกำลังหา Recommendation

ไม่ควรใช้ Spinner ธรรมดา

แนะนำ

```text
Movie Reel Animation
Gold Orb
Glass Pulse
Poster Shuffle
```

ข้อความ

```text
Finding movies for your mood...
```

---

# 36. Recommendation Transition

เมื่อ User เลือก Mood

Animation Flow

```text
Mood Card Click

      ↓

Card Compress

      ↓

Gold Pulse

      ↓

Background Blur

      ↓

Loading

      ↓

Movie Cards Reveal
```

---

# 37. Page Transition

เมื่อเปลี่ยนหน้า

ใช้

```text
Fade
Blur
Scale
```

ตัวอย่าง

```css
.page-enter {
  opacity:
    0;

  transform:
    scale(0.98);

  filter:
    blur(5px);
}

.page-enter-active {
  opacity:
    1;

  transform:
    scale(1);

  filter:
    blur(0);
}
```

---

# 38. Hover Glow

Gold Glow ใช้เฉพาะจุดสำคัญ

เช่น

```text
Button
Active Mood
Active Navigation
Movie Rating
Selected Genre
```

หลีกเลี่ยงการใส่ Glow ทุกจุด

เพราะจะทำให้เว็บไซต์ดูรก

---

# 39. Mouse Spotlight

เพิ่ม Spotlight ตาม Mouse ใน Background

Concept

```text
Mouse
 ↓
Soft Gold Light
 ↓
Move around page
```

CSS

```css
background:
  radial-gradient(
    600px circle at var(--mouse-x) var(--mouse-y),
    rgba(245,196,81,0.06),
    transparent 40%
  );
```

---

# 40. Floating Particles

พื้นหลังสามารถมี Particle เล็ก ๆ

```text
Dust
Film Grain
Gold Dust
```

Opacity ต่ำมาก

```text
0.02 – 0.08
```

เพื่อให้เว็บไซต์ดูมีชีวิตแต่ไม่รบกวน Content

---

# 41. Film Grain

เพิ่ม Noise Texture เล็กน้อย

```css
.noise {
  opacity:
    0.025;

  mix-blend-mode:
    soft-light;
}
```

ช่วยให้พื้นหลังดำไม่ดู Flat

---

# 42. Depth System

ใช้ Depth 3 ระดับ

## Level 1

```text
Background
```

## Level 2

```text
Glass Container
Sections
```

## Level 3

```text
Mood Cards
Movie Cards
Buttons
Floating Elements
```

---

# 43. Border Radius System

```text
Small
12px

Medium
18px

Large
24px

Extra Large
32px

Pill
999px
```

---

# 44. Shadow System

Card

```css
box-shadow:
  0 20px 50px rgba(0,0,0,0.35);
```

Hover

```css
box-shadow:
  0 30px 80px rgba(0,0,0,0.5);
```

Gold Glow

```css
box-shadow:
  0 0 40px rgba(245,196,81,0.15);
```

---

# 45. Animation Timing

แนะนำใช้ Duration

```text
Micro Interaction
150–250ms

Hover
250–400ms

Card Transition
350–500ms

Page Reveal
500–800ms

Background Motion
20–60s
```

---

# 46. Easing

แนะนำ

```css
cubic-bezier(.2,.8,.2,1)
```

สำหรับ Animation หลัก

หรือ

```css
ease-out
```

สำหรับ Hover

---

# 47. Animation Principles

Animation ต้อง

```text
Smooth
Subtle
Purposeful
Responsive
```

ไม่ควร

```text
Bounce มากเกิน
Rotate มากเกิน
Flash
Fast Zoom
Aggressive Motion
```

---

# 48. Event Animation

ตัวอย่าง Event สำคัญ

## Click Mood

```text
Scale Down
→ Glow
→ Ripple
→ Loading
→ Result Reveal
```

## Hover Movie

```text
Tilt
→ Poster Zoom
→ Overlay
→ Information Reveal
```

## Click Filter

```text
Gold Fill
→ Movie Grid Fade
→ New Cards Reveal
```

## Search

```text
Input Glow
→ Loading
→ Search Result Fade In
```

---

# 49. Mobile Design

Mobile ไม่ควรใช้ 3D Effect ที่ซับซ้อนเกินไป

ควรลด

```text
Mouse Tilt
Large Parallax
Heavy Blur
Background Video
```

ใช้แทนด้วย

```text
Tap Animation
Fade
Scale
Slide
```

---

# 50. Responsive Layout

## Desktop

```text
Max Width
1200–1400px
```

## Tablet

```text
Padding
24–32px
```

## Mobile

```text
Padding
16–20px
```

---

# 51. Accessibility

Text Contrast ต้องชัด

ไม่ควรใช้

```text
Dark Gray Text
on
Black Background
```

กับข้อความสำคัญ

Gold ใช้เป็น Accent ไม่ควรใช้กับ Body Text จำนวนมาก

---

# 52. Reduced Motion

รองรับผู้ใช้ที่ไม่ต้องการ Animation

```css
@media (
  prefers-reduced-motion:
  reduce
) {

  * {
    animation-duration:
      0.01ms !important;

    transition-duration:
      0.01ms !important;
  }
}
```

---

# 53. Performance Guidelines

Glassmorphism และ Blur ใช้ GPU สูง

จึงไม่ควรใช้

```text
backdrop-filter
```

กับ Element จำนวนมากเกินไป

แนะนำใช้เฉพาะ

```text
Navbar
Hero Panel
Mood Selector
Modal
Movie Detail
```

---

# 54. Recommended Page Structure

```text
MoodMovie

│
├── Navigation
│
├── Hero
│
├── Mood Selector
│
├── Recommended Movies
│
├── Trending Movies
│
├── Browse by Genre
│
├── Surprise Me
│
└── Footer
```

---

# 55. Homepage Wireframe

```text
┌──────────────────────────────────────────┐
│              GLASS NAVBAR                │
│ MoodMovie   Home Movies Moods   Search   │
└──────────────────────────────────────────┘


          MOVING POSTER BACKGROUND


           How are you feeling?

        Find a movie that matches
                 your mood.

     [ Find My Mood ] [ Surprise Me ]


────────────────────────────────────────────

              Choose your mood

   😊        😢       ❤️       🔥
 Happy      Sad    Romantic  Excited

        😴                 😌
       Bored             Relaxed


────────────────────────────────────────────

          Recommended for tonight

 Movie       Movie       Movie       Movie

────────────────────────────────────────────

             Browse by genre

 Action  Comedy  Drama  Sci-Fi  Romance

────────────────────────────────────────────
```

---

# 56. Mood Selection State

## Default

```text
Glass
White Text
Low Border
```

## Hover

```text
3D Tilt
Gold Border
Glow
Emoji Scale
```

## Selected

```text
Gold Gradient
Black Text
Soft Glow
```

---

# 57. Movie Card State

## Default

```text
Poster
Title
Rating
```

## Hover

```text
Poster Zoom
3D Tilt
Overlay
Genre
View Button
```

## Active

```text
Scale Down
Gold Border
```

---

# 58. Navigation State

Default

```text
White / Gray
```

Hover

```text
Gold
```

Active

```text
Gold
+
Small Underline / Glow Dot
```

---

# 59. Design Tokens

```css
:root {

  --bg-main:
    #070707;

  --bg-secondary:
    #111111;

  --gold:
    #F5C451;

  --gold-light:
    #FFD76A;

  --gold-dark:
    #C99A2E;

  --text-primary:
    #F5F5F5;

  --text-secondary:
    #B5B5B5;

  --text-muted:
    #777777;

  --glass:
    rgba(255,255,255,0.06);

  --glass-border:
    rgba(255,255,255,0.10);

  --radius-sm:
    12px;

  --radius-md:
    18px;

  --radius-lg:
    24px;

  --radius-xl:
    32px;

  --transition:
    0.35s cubic-bezier(.2,.8,.2,1);
}
```

---

# 60. Recommended Component Structure

```text
components/

├── Navbar
├── Hero
├── MoodCard
├── MoodSelector
├── MovieCard
├── MovieCarousel
├── GenreFilter
├── SearchBar
├── GlassPanel
├── GoldButton
├── MovieDetail
├── LoadingAnimation
└── Footer
```

---

# 61. JavaScript Interaction Modules

```text
static/js/

├── main.js
├── tilt.js
├── scroll-animation.js
├── cursor-glow.js
├── carousel.js
└── page-transition.js
```

---

# 62. CSS Structure

```text
static/css/

├── variables.css
├── reset.css
├── layout.css
├── components.css
├── animations.css
├── glass.css
├── movie-card.css
├── mood-card.css
└── responsive.css
```

---

# 63. Homepage Interaction Flow

```text
User opens website

        ↓

Hero Animation

        ↓

User moves mouse

        ↓

Background Spotlight follows

        ↓

User hovers Mood

        ↓

3D Tilt + Gold Glow

        ↓

User clicks Mood

        ↓

Click Animation

        ↓

Loading

        ↓

Recommended Movies

        ↓

Movie Cards Reveal

        ↓

User hovers Movie

        ↓

Poster Zoom + 3D Tilt

        ↓

User clicks Movie

        ↓

Smooth Page Transition

        ↓

Movie Detail
```

---

# 64. Visual Priority

ลำดับสิ่งที่ควรโดดเด่นที่สุด

```text
1. Hero Title
2. Mood Selector
3. Gold CTA
4. Movie Posters
5. Movie Information
6. Navigation
7. Background Decoration
```

Background Animation ต้องไม่แย่งสายตาจาก Content

---

# 65. Final Visual Style

MoodMovie ควรมีภาพรวมประมาณ

```text
BLACK CINEMATIC BACKGROUND

        +

SOFT GOLD LIGHT

        +

GLASS INTERFACE

        +

MOVING MOVIE POSTERS

        +

3D HOVER

        +

LIQUID GLASS

        +

SMOOTH ANIMATION
```

---

# 66. Design Summary

MoodMovie ใช้ Design Language แบบ

> **Cinematic Dark Glass**

โดยมี Dark Theme เป็นพื้นฐาน

```text
Main Background
→ Black

Accent
→ Premium Gold

Components
→ Glassmorphism

Navigation / Modal
→ Liquid Glass

Movie / Mood Card
→ 3D Hover

Background
→ Moving Blurred Posters

Interaction
→ Smooth Motion

Page Transition
→ Fade + Blur + Scale
```

สิ่งสำคัญคือเว็บไซต์ต้องดู

```text
Premium
Modern
Smooth
Immersive
Cinematic
Interactive
```

แต่ต้องไม่ใส่ Effect มากจนทำให้ UX ซับซ้อนหรือ Performance ลดลง

---

# 🎬 MoodMovie

> **Find a movie that matches your mood.**

### Design Theme

**Dark Cinematic • Premium Gold • Glass UI • Liquid Glass • 3D Motion**

Built for a smooth and immersive movie discovery experience.
