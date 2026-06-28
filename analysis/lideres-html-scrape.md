# Ecociclo.es — Líderes Section: Full HTML Scrape & Analysis

**Source URL:** `https://ecociclo.es/`  
**Section CSS selector:** `#gspb_row-id-gsbp-022f526` (Greenshift Row block)  
**Date scraped:** 2026-06-28  
**Raw extract:** `analysis/lideres-raw.html` (152 lines, ~64KB)  

---

## 1. Section Overview

The "Líderes" section is a Greenshift-powered WordPress block section located at the top of the Ecociclo homepage. It serves as a hero/value-proposition area featuring:

- An **overhead badge** ("Experiencia Comprobada")
- A main **h2 heading** ("Líderes en gestión de residuos en Barcelona")
- A **subheadline** with key stats
- **3 benefit columns** in the left column (Experiencia Real, Capacidad Logística, Seguridad Legal)
- A **center image column** (circular photo)
- **3 stat columns** in the right column (2.500+ servicios, Respuesta rápida, Compromiso ambiental)
- **Floating decorative images** (leaf icons with rotation animations)
- **Entrance animations** via AOS (Animate on Scroll) library on every block

### BEM-Class Naming Convention

All blocks use Greenshift's unique ID pattern: `gspb_{block-type}-id-gsbp-{hex_suffix}`. CSS is injected inline via `<style>` blocks immediately before each element.

---

## 2. DOM Tree Structure (Indented)

```
section#gspb_row-id-gsbp-022f526.gspb_row.alignfull (ROOT — hidden on mobile)
└── div.gspb_row__content
    └── div#gspb_col-id-gsbp-a9bcb7b.gspb_row__col--12 (padding: 70px 0)
        ├── div#gspb_row-id-gsbp-f70b4b8.gspb_row (header row, padding-bottom: 40px)
        │   └── div.gspb_row__content
        │       └── div#gspb_col-id-gsbp-9095bc9.gspb_row__col--6 (50% width)
        │           ├── div.wp-block-group (flex, centered, nowrap)
        │           │   ├── div#gspb_image-id-gsbp-c43f16c.gspb_image
        │           │   │   └── img (ECOICLO.webp, 28px wide, zoom-in animation)
        │           │   └── span.gsbp-3bd435e.overhead-span "Experiencia Comprobada"
        │           ├── h2#gspb_heading-id-gsbp-1a3e8ff "Líderes en gestión de residuos en Barcelona"
        │           └── div#gspb_text-id-gsbp-e3dddc1.gspb_text (subheadline with <br>s)
        │
        ├── div#gspb_image-id-gsbp-dfecbd0 (FLOATING — position:absolute top:155px left:50px)
        │   └── img (ECOICLO-_1_.webp, 150px height, fade-down-right, rotateZ 98deg)
        ├── div#gspb_image-id-gsbp-3eb7889 (FLOATING — position:absolute top:160px right:0)
        │   └── img (ECOICLO-_1_.webp, 150px height, fade-up-left, rotateZ 50deg)
        │
        ├── div#gspb_row-id-gsbp-f1ac644.gspb_row (main content: 3 columns)
        │   └── div.gspb_row__content
        │       ├── div#gspb_col-id-gsbp-be4bf76.gspb_row__col--4 (LEFT — 33.3%)
        │       │   ├── div#gspb_row-id-gsbp-14b9a1b (row: icon + text)
        │       │   │   └── div.gspb_row__content
        │       │   │       ├── div#gspb_col-id-gsbp-baf7437.gspb_row__col--9 (75%)
        │       │   │       │   ├── h3 "Experiencia Real"
        │       │   │       │   └── p (description)
        │       │   │       └── div#gspb_col-id-gsbp-13a8dfc.gspb_row__col--3 (25%)
        │       │   │           └── div#gspb_iconBox-id-gsbp-b24de70 (green circle + SVG icon)
        │       │   ├── div#gspb_row-id-gsbp-7a0b8b6 (row: icon + text)
        │       │   │   └── div.gspb_row__content
        │       │   │       ├── div#gspb_col-id-gsbp-1b6f2e9.gspb_row__col--9
        │       │   │       │   ├── h3 "Capacidad Logística"
        │       │   │       │   └── p (description)
        │       │   │       └── div#gspb_col-id-gsbp-153a048.gspb_row__col--3
        │       │   │           └── div#gspb_iconBox-id-gsbp-e3a84d4 (green circle + SVG icon)
        │       │   └── div#gspb_row-id-gsbp-dfeaa7f (row: icon + text)
        │       │       └── div.gspb_row__content
        │       │           ├── div#gspb_col-id-gsbp-d62e5f0.gspb_row__col--9
        │       │           │   ├── h3 "Seguridad Legal"
        │       │           │   └── p (description)
        │       │           └── div#gspb_col-id-gsbp-b3adac4.gspb_row__col--3
        │       │               └── div#gspb_iconBox-id-gsbp-fe1c007 (green circle + SVG icon)
        │       │
        │       ├── div#gspb_col-id-gsbp-4de3498.gspb_row__col--4 (CENTER — 33.3%)
        │       │   └── div#gspb_image-id-gsbp-9e7307d.gspb_image
        │       │       └── img (15.webp, 1080x1080, zoom-out animation, scale 1.2)
        │       │
        │       └── div#gspb_col-id-gsbp-f0cadb8.gspb_row__col--4 (RIGHT — 33.3%)
        │           ├── div#gspb_row-id-gsbp-3df73a6 (row: icon + text)
        │           │   └── div.gspb_row__content
        │           │       ├── div#gspb_col-id-gsbp-bb0ac29.gspb_row__col--3
        │           │       │   └── div#gspb_iconBox-id-gsbp-45765af (green circle + SVG)
        │           │       └── div#gspb_col-id-gsbp-87b731c.gspb_row__col--9
        │           │           ├── h3 "Más de 2.500 servicios realizados"
        │           │           └── p (description)
        │           ├── div#gspb_row-id-gsbp-fa20448 (row: icon + text)
        │           │   └── div.gspb_row__content
        │           │       ├── div#gspb_col-id-gsbp-483735f.gspb_row__col--3
        │           │       │   └── div#gspb_iconBox-id-gsbp-82c10b8 (green circle + SVG)
        │           │       └── div#gspb_col-id-gsbp-7d516f1.gspb_row__col--9
        │           │           ├── h3 "Respuesta rápida en Cataluña"
        │           │           └── p (description)
        │           └── div#gspb_row-id-gsbp-f788947 (row: icon + text)
        │               └── div.gspb_row__content
        │                   ├── div#gspb_col-id-gsbp-d66e4d7.gspb_row__col--3
        │                   │   └── div#gspb_iconBox-id-gsbp-db0474a (green circle + SVG)
        │                   └── div#gspb_col-id-gsbp-f164c4b.gspb_row__col--9
        │                       ├── h3 "Compromiso ambiental"
        │                       └── p (description)
```

---

## 3. Component Inventory

### 3.1 Greenshift Block Types Used

| Block Type | Count | CSS Class Pattern |
|---|---|---|
| **Row** (`gspb_row`) | 9 | `gspb_row-id-gsbp-{suffix}` |
| **Row Column** (`gspb_row__col`) | 17 | `gspb_col-id-gsbp-{suffix}` |
| **Heading** (`gspb_heading`) | 13 | `gspb_heading-id-gsbp-{suffix}` |
| **Image** (`gspb_image`) | 4 | `gspb_image-id-gsbp-{suffix}` |
| **IconBox** (`gspb_iconBox`) | 6 | `gspb_iconBox-id-gsbp-{suffix}` |
| **Text** (`gspb_text`) | 2 | `gspb_text-id-gsbp-{suffix}` |
| **Custom CSS classes** (`gsbp-{hex}`) | 2 | `gsbp-3bd435e`, `gsbp-e6b5bfb` |
| **Core Group** (`wp-block-group`) | 1 | — |

### 3.2 Content Inventory

| Element | Content |
|---|---|
| Overhead span (green) | "Experiencia Comprobada" |
| h2 heading (uppercase, centered) | "Líderes en gestión de residuos en Barcelona" |
| Description text | "Más de **10 años de trayectoria** y **más de 2.500 servicios realizados** nos posicionan como una empresa especializada en vaciados, limpiezas y **gestión de residuos en Barcelona** para empresas, industria y espacios profesionales." |
| **Left column — h3** | "Experiencia Real" |
| Left — p | "Llevamos más de una década ayudando a empresas a vaciar, limpiar y gestionar residuos de forma profesional y organizada." |
| **Left column — h3** | "Capacidad Logística" |
| Left — p | "Podemos actuar en servicios puntuales, urgentes o planificados en naves, oficinas, locales, terrenos y espacios industriales." |
| **Left column — h3** | "Seguridad Legal" |
| Left — p | "Cada intervención se prepara con criterio profesional para ofrecer orden, tranquilidad y una gestión responsable." |
| **Center** — image | `15.webp` (1080×1080, zoom-out animation, scale 1.2) |
| **Right column — h3** | "**Más de 2.500 servicios realizados**" |
| Right — p | "Nuestra experiencia práctica nos permite adaptarnos a distintos tipos de clientes, residuos y espacios" |
| **Right column — h3** | "**Respuesta rápida en Cataluña**" |
| Right — p | "Priorizamos la agilidad para que las empresas recuperen operatividad y espacio útil lo antes posible." |
| **Right column — h3** | "**Compromiso ambiental**" |
| Right — p | "Apostamos por una gestión responsable de los residuos y por una forma de trabajar eficaz, seria y sostenible." |
| **Floating image 1** | `ECOICLO-_1_.webp` — position:absolute top:155px left:50px, rotateZ 98deg |
| **Floating image 2** | `ECOICLO-_1_.webp` — position:absolute top:160px right:0px, rotateZ 50deg |

---

## 4. CSS Architecture

### 4.1 Style Block Strategy

Each Greenshift element has its own `<style>` block placed *immediately* before the corresponding HTML element. There are **~40+ discrete `<style>` blocks** within this section alone. This is Greenshift's default output pattern — no external stylesheets for block-specific rules.

### 4.2 Row Layout Pattern (repeated for all 9 rows)

```css
#gspb_row-id-gsbp-{suffix} {
  justify-content: space-between;
  margin-top: 0px;
  margin-bottom: 0px;
  display: flex;
  flex-wrap: wrap;
}
#gspb_row-id-gsbp-{suffix} > .gspb_row__content {
  display: flex;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  flex-wrap: wrap;
}
.gspb_row { position: relative; }
div[id^=gspb_col-id] {
  box-sizing: border-box;
  position: relative;
  padding: var(--gs-row-column-padding, 15px min(3vw, 20px));
}
```

### 4.3 Color Tokens (CSS Custom Properties)

The section references WordPress theme color presets:

| CSS Variable | Fallback Value | Purpose |
|---|---|---|
| `--wp--preset--color--palette-color-3` | `#65C132` | Primary green (span text, icon backgrounds) |
| `--wp--preset--color--palette-color-8` | `#ffffff` | White (icon SVG fill color) |
| `--theme-palette-color-3` | `#65C132` | Same green, theme-level |
| `--theme-palette-color-8` | `#ffffff` | Same white, theme-level |

### 4.4 Responsive Breakpoints

| Breakpoint | Max Width | Typical Behavior |
|---|---|---|
| Mobile | **689.98px** | Columns go to 100% width; text alignment → center; root row gets `display:none !important`; floating images shrink to 50px |
| Tablet | **999.98px** | Icon backgrounds switch to `#e2eefd` (light blue) |
| Desktop (min) | **1000px** | Full column widths active (25%/33.3%/50%/75%) |

**Key mobile behavior:** The entire Líderes section is **hidden on mobile** (`display:none !important` at ≤689.98px).

### 4.5 Absolute-Positioned Floating Images

Two decorative leaf images are positioned absolutely within the section:

| Image | Position | Dimensions | Animation |
|---|---|---|---|
| `gspb_image-id-gsbp-dfecbd0` | `top:155px; left:50px` | `height:150px` (mobile: 50px, left: 30px) | `fade-down-right` → `rotateZ(98deg)` |
| `gspb_image-id-gsbp-3eb7889` | `top:160px; right:0px` | `height:150px` (mobile: 50px) | `fade-up-left` → `rotateZ(50deg)`, transform-origin: top right |

---

## 5. Animation System (AOS Integration)

### 5.1 How It Works

Greenshift uses the **AOS (Animate on Scroll)** library. Each animated element gets `data-aos-*` attributes and corresponding CSS:

1. **Hidden state:** `opacity: var(--gs-root-animation-opacity, 0)` + a transform (e.g., `translate3d(...)`, `scale(...)`)
2. **Animate state:** When `.aos-animate` class is added (or `[data-gs-aos]`), opacity → 1 and transform → `translateZ(0)` / `scale(1)`
3. **Transition:** `transition-duration: 0.8s`, various `transition-timing-function` values

### 5.2 Animation Variants Found

| Animation Name | `data-aos` Value | Default Transform (hidden) | Easing | # Uses |
|---|---|---|---|---|
| Fade Right | `fade-right` | `translate3d(calc(max(50px,15%) * -1), 0, 0)` | `ease` | 6 (left-col h3s and ps) |
| Fade Left | `fade-left` | `translate3d(calc(max(50px,15%)), 0, 0)` | `ease` / `ease-out-cubic` | 8 (right-col, overhead span) |
| Zoom In | `zoom-in` | `scale(0.6)` | `ease-in-back` / `ease-in-out-back` | 8 (icons, logo image) |
| Zoom Out | `zoom-out` | `scale(1.2)` | `ease` | 1 (center image) |
| Fade Up | `fade-up` | `translate3d(0, calc(max(50px,15%)), 0)` | `ease` | 1 (CTA button in next section) |
| Fade Down-Right | `fade-down-right` | `translate3d(calc(max(50px,15%)*-1), calc(max(50px,15%)*-1), 0)` | `ease` | 1 (floating leaf left) |
| Fade Up-Left | `fade-up-left` | `translate3d(calc(max(50px,15%)), calc(max(50px,15%)), 0)` | `ease` | 1 (floating leaf right) |

### 5.3 Staggered Delays for Cascading Effect

The left-column items use **staggered delays** on their descriptions so they appear one after another:

| Element | `data-aos-delay` |
|---|---|
| Left h3 "Experiencia Real" | 0ms (no delay attr) |
| Left p (description) | 100ms |
| Left h3 "Capacidad Logística" | 200ms |
| Left p | 300ms |
| Left h3 "Seguridad Legal" | 400ms |
| Left p | 500ms |

Same stagger pattern applies to the right column items.

### 5.4 Transition Timing Functions

| Function | Usage |
|---|---|
| `cubic-bezier(0.42, 0, 0.58, 1)` | Default Greenshift easing — headings, text blocks, fade animations |
| `cubic-bezier(0.6, -0.28, 0.735, 0.045)` | Logo/icon images with `zoom-in` (sharp back-easing) |
| `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | Overhead spans (smooth ease-out) |
| `cubic-bezier(0.68, -0.55, 0.265, 1.55)` | IconBox wrappers (elastic back-easing for pop-in) |

---

## 6. IconBox Component Pattern

Each of the 6 icon boxes follows an identical pattern:

```html
<style>/* All iconBox CSS rules */</style>
<div class="wp-block-greenshift-blocks-iconbox gspb_iconBox gspb_iconBox-id-{suffix}">
  <div class="gspb_iconBox__wrapper"
       style="display:inline-flex"
       data-aos="zoom-in"
       data-aos-delay="{0|100|200}"
       data-aos-easing="ease-in-out-back"
       data-aos-duration="800">
    <svg width="72" height="72" viewBox="0 0 1024 1024">
      <path style="fill:#565D66" d="M1000 16h-55.422c-..."
    </svg>
  </div>
</div>
```

**Key CSS properties for the wrapper:**
- `background-color: var(--wp--preset--color--palette-color-3, #65C132)` → green
- `border-radius: 10px`
- `padding: 20px`
- SVG fill: `var(--wp--preset--color--palette-color-8, #ffffff)` → white
- SVG size: 35×35px (overrides the 72×72 viewBox)
- Hover fill stays white

All 6 icon boxes use **the exact same SVG path** (a refresh/recycle icon).

---

## 7. Image Assets Referenced

| URL | Dimensions | Usage |
|---|---|---|
| `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO.webp` | 28×1080 | Small logo icon (in group with overhead span) |
| `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO-_1_.webp` | 610×150 | Floating decorative leaf icons (×2 instances) |
| `https://ecociclo.es/wp-content/uploads/2026/03/15.webp` | 1080×1080 | Center column hero image |

---

## 8. Key CSS Fragments (for Recreation)

### 8.1 Root Row (Hidden on Mobile)

```css
#gspb_row-id-gsbp-022f526 {
  justify-content: space-between;
  margin-top: 0px;
  margin-bottom: 0px;
  display: flex;
  flex-wrap: wrap;
}
body.gspb-bodyfront #gspb_row-id-gsbp-022f526 > .gspb_row__content {
  width: var(--theme-container-width, 1200px);
  max-width: var(--theme-normal-container-max-width, 1200px);
}
@media (max-width: 689.98px) {
  body #gspb_row-id-gsbp-022f526 {
    display: none !important;
  }
}
```

### 8.2 Outer Column

```css
#gspb_col-id-gsbp-a9bcb7b.gspb_row__col--12 {
  width: 100%;
  padding-top: 70px;
  padding-bottom: 70px;
}
```

### 8.3 Header Row (Logo + Heading + Subheadline)

```css
#gspb_row-id-gsbp-f70b4b8 {
  align-items: center;
  justify-content: center;
  align-content: center;
  padding-top: 0px;
  padding-bottom: 40px;
}
#gspb_col-id-gsbp-9095bc9.gspb_row__col--6 {
  width: 50%;
  display: flex;
  flex-direction: column;
  row-gap: 10px;
}
```

### 8.4 Overhead Span

```css
.gsbp-3bd435e {
  color: var(--wp--preset--color--palette-color-3, #65C132);
  margin: 0;
  padding: 0;
  transition-duration: 0.8s;
  transition-timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  opacity: var(--gs-root-animation-opacity, 0);
  transition-property: opacity, transform, filter;
  transform: var(--gs-root-animation-transform, translate3d(calc(max(50px,15%)), 0, 0));
}
.gsbp-3bd435e.aos-animate, .gsbp-3bd435e[data-gs-aos] {
  opacity: 1;
  transform: translateZ(0);
}
```

### 8.5 Main Heading

```css
#gspb_heading-id-gsbp-1a3e8ff {
  text-transform: uppercase;
  text-align: center !important;
  margin: 0;
}
```

### 8.6 3-Column Content Row

```css
#gspb_col-id-gsbp-be4bf76.gspb_row__col--4 {
  width: 33.333333333333336%;   /* left */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  row-gap: 20px;
}
#gspb_col-id-gsbp-4de3498.gspb_row__col--4 {
  width: 33.333333333333336%;   /* center */
  display: flex;
  align-items: center;
}
#gspb_col-id-gsbp-f0cadb8.gspb_row__col--4 {
  width: 33.333333333333336%;   /* right */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  row-gap: 20px;
}
```

### 8.7 Icon Row (9/3 Split Inside Each Column)

```css
#gspb_col-id-gsbp-baf7437.gspb_row__col--9 { width: 75%; }  /* text */
#gspb_col-id-gsbp-13a8dfc.gspb_row__col--3 { width: 25%;   /* icon */
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### 8.8 Sub-Items (h3 + p)

```css
#gspb_heading-id-gsbp-f9dfff3 {
  font-size: 20px;
  text-align: right !important;
  margin: 0;
  /* animation: fade-right, 0.8s, cubic-bezier(0.42,0,0.58,1) */
}
#gspb_heading-id-gsbp-9d78138 {
  font-weight: 100 !important;
  text-align: right !important;
  margin: 0;
  padding: 0;
  /* animation: fade-right, delay 0.1s */
}
```

Note: Left column items use `text-align: right !important`; right column items use `text-align: left !important`.

---

## 9. Archival Notes

- The raw HTML is saved at `/home/ubuntu/ecociclo-niu/analysis/lideres-raw.html` (lines 1220–1371 of the full page source)
- Full page source: `/home/ubuntu/ecociclo-niu/analysis/ecociclo-full.html` (1773 lines, 461KB)
- The section is **entirely self-contained** — all styles are inline `<style>` blocks, no external dependencies beyond the Greenshift plugin runtime and AOS library
- Mobile is **display:none** for this section — it's desktop-only
- The icon SVG is a Font Awesome-style recycle/refresh icon reused 6 times
- This section is followed immediately by a CTA section (`gspb_row-id-gsbp-9ffae62`) with a dark background image, heading "Recupera tu espacio hoy mismo", and a "Solicitar presupuesto" button
