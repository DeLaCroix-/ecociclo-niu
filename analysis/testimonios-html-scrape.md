# Testimonios Section — Raw HTML Scrape Analysis

**Source:** `https://ecociclo.es/`  
**Fetch date:** 2026-06-28  
**Method:** `curl -sL https://ecociclo.es/`  
**Section identifier:** `gspb_row-id-gsbp-a640774`  
**Lines in source:** 1504–1527 (24 lines, 15,656 bytes)  
**Raw extract saved to:** `analysis/testimonios-raw.html`

---

## 1. Section Overview

The Testimonios section is a Greenshift Blocks row (`alignfull`) containing:

| Component | Greenshift ID | Description |
|-----------|--------------|-------------|
| Row wrapper | `gspb_row-id-gsbp-a640774` | Full-width row, 70px padding top/bottom |
| Column 1 (header) | `gspb_col-id-gsbp-bf75f66` | 100% width, contains icon + label + heading |
| ECOCICLO icon | `gspb_image-id-gsbp-77dc34e` | 28px wide logo, AOS zoom-in animation |
| Overhead label | `.gsbp-7bd6998` | Green (#65C132) "Testimonios" span, fade-left animation |
| Heading | `gspb_heading-id-gsbp-33b7e3d` | "Confianza avalada por más de 2.500 servicios" |
| Column 2 (reviews) | `gspb_col-id-gsbp-7363f21` | 100% width, Trustindex Google reviews widget |

---

## 2. Greenshift CSS Patterns

### 2.1 Row Container (`#gspb_row-id-gsbp-a640774`)

```css
#gspb_row-id-gsbp-a640774 {
  justify-content: space-between;
  margin-top: 0px;
  margin-bottom: 0px;
  display: flex;
  flex-wrap: wrap;
  padding-top: 70px;
  padding-bottom: 70px;
}
#gspb_row-id-gsbp-a640774 > .gspb_row__content {
  display: flex;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  flex-wrap: wrap;
}
body.gspb-bodyfront #gspb_row-id-gsbp-a640774 > .gspb_row__content {
  width: var(--theme-container-width, 1200px);
  max-width: var(--theme-normal-container-max-width, 1200px);
}
```

### 2.2 Base Greenshift Patterns (present in every block)

```css
.gspb_row { position: relative; }
div[id^=gspb_col-id] {
  box-sizing: border-box;
  position: relative;
  padding: var(--gs-row-column-padding, 15px min(3vw, 20px));
}
```

### 2.3 Logo Image Animation (`#gspb_image-id-gsbp-77dc34e`)

```css
#gspb_image-id-gsbp-77dc34e img {
  width: 28px;
  transition-duration: 0.8s;
  transition-timing-function: cubic-bezier(0.6, -0.28, 0.735, 0.045);
  opacity: var(--gs-root-animation-opacity, 0);
  transform: var(--gs-root-animation-transform, scale(0.6));
}
#gspb_image-id-gsbp-77dc34e img.aos-animate,
#gspb_image-id-gsbp-77dc34e img[data-gs-aos] {
  opacity: 1;
  transform: translateZ(0) scale(1);
}
```

Image uses `data-aos="zoom-in" data-aos-easing="ease-in-back" data-aos-duration="800"`.

### 2.4 Overhead Label (`.gsbp-7bd6998`)

```css
.gsbp-7bd6998 {
  color: var(--wp--preset--color--palette-color-3, var(--theme-palette-color-3, #65C132));
  transition-duration: 0.8s;
  transition-timing-function: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  opacity: var(--gs-root-animation-opacity, 0);
  transform: var(--gs-root-animation-transform, translate3d(calc(max(50px, 15%)), 0, 0));
}
.gsbp-7bd6998.aos-animate, .gsbp-7bd6998[data-gs-aos] {
  opacity: 1;
  transform: translateZ(0);
}
@media (max-width: 689.98px) { .gsbp-7bd6998 { font-size: 14px; } }
```

Span uses `data-aos="fade-left" data-aos-easing="ease-out-cubic" data-aos-duration="800"`.

### 2.5 Heading (`#gspb_heading-id-gsbp-33b7e3d`)

```css
#gspb_heading-id-gsbp-33b7e3d {
  text-transform: uppercase;
  text-align: center !important;
  margin: 0;
}
```

---

## 3. AOS Animation Attributes Observed

| Element | `data-aos` | `data-aos-easing` | `data-aos-duration` |
|---------|-----------|-------------------|---------------------|
| Logo image | `zoom-in` | `ease-in-back` | `800` |
| Overhead span | `fade-left` | `ease-out-cubic` | `800` |

---

## 4. Trustindex Widget — Full Analysis

### 4.1 Widget Wrapper

The Trustindex widget is placed inside a Greenshift column block as a raw `<pre class="ti-widget">` containing a `<template>` element. The loader script replaces this at runtime.

```html
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--12 gspb_col-id-gsbp-7363f21"
     id="gspb_col-id-gsbp-7363f21">
  <pre class="ti-widget">
    <template id="trustindex-google-widget-html">
      <!-- full widget HTML here -->
    </template>
  </pre>
  <div data-src="https://cdn.trustindex.io/loader.js?wp-widget"
       data-template-id="trustindex-google-widget-html"
       data-css-url="https://ecociclo.es/wp-content/uploads/trustindex-google-widget.css?1782427180">
  </div>
</div>
```

### 4.2 Widget Configuration Data Attributes

On the root `.ti-widget` div:

| Attribute | Value | Notes |
|-----------|-------|-------|
| `data-no-translation` | `true` | Prevents auto-translation |
| `data-time-locale` | `hace %d %s\|hoy\|día\|días\|semana\|...` | Spanish relative time format |
| `data-plugin-version` | `13.3.1` | Trustindex plugin version |
| `data-layout-id` | `4` | Layout 4 = slider |
| `data-layout-category` | `slider` | Slider-based display |
| `data-set-id` | `ligth-border` | Style preset (note: typo "ligth" not "light") |
| `data-pid` | *(empty)* | No specific profile ID |
| `data-language` | `es` | Spanish |
| `data-css-version` | `2` | CSS version |
| `data-review-target-width` | `300` | 300px review card width |
| `data-pager-autoplay-timeout` | `6` | 6-second autoplay |

### 4.3 Widget Structure (Slider Layout)

```
.ti-widget.ti-goog
└── .ti-widget-container.ti-col-3          (3-column responsive)
    └── .ti-reviews-container
        ├── .ti-controls
        │   ├── .ti-next  (next arrow)
        │   └── .ti-prev  (previous arrow)
        ├── .ti-reviews-container-wrapper
        │   └── .ti-review-item × 4        (see reviews below)
        └── .ti-controls-line
            └── .dot
```

### 4.4 Review Card Structure (per item)

```
.ti-review-item[data-time][data-empty="0"][data-id]
└── .ti-inner
    ├── .ti-review-header
    │   ├── .ti-platform-icon > trustindex-image (Google icon)
    │   ├── .ti-profile-img > trustindex-image (reviewer avatar)
    │   └── .ti-profile-details
    │       ├── .ti-name (reviewer name)
    │       └── .ti-date (date, filled by JS)
    ├── span.ti-stars
    │   └── trustindex-image.ti-star × 5
    ├── .ti-review-content (review text + <!-- R-CONTENT --> marker)
    └── span.ti-read-more
```

### 4.5 Reviews Extracted

4 Google reviews found in template:

| # | Reviewer | Date (UTC) | Date (readable) |
|---|----------|-----------|-----------------|
| 1 | Barbara Yuste | 1766448000 | 2025-12-23 |
| 2 | Natalia Rivallo Pena | 1708560000 | 2024-02-22 |
| 3 | Wils Casallas | 1695168000 | 2023-09-20 |
| 4 | Maria Lluisa Lopez Robles | 1661904000 | 2022-08-31 |

All 4 reviews have `data-empty="0"` (contain text), `data-id="cfcd208495d565ef66e7dff9f98764da"` (MD5 hash placeholder?), and `source-Google`.

Review text fragments visible (truncated in source):
- **Barbara Yuste:** "…Incluso encontraron cosas antiguas que no sabíamos que estaban y nos las entregaron. Súper recomendables!"
- **Maria Lluisa Lopez Robles:** "…Recomendamos V.P.B."

### 4.6 Trustindex Assets

| Asset | URL |
|-------|-----|
| Loader JS | `https://cdn.trustindex.io/loader.js?wp-widget` |
| Widget CSS | `https://ecociclo.es/wp-content/uploads/trustindex-google-widget.css?1782427180` |
| Google icon | `https://cdn.trustindex.io/assets/platform/Google/icon.svg` |
| Star SVG | `https://cdn.trustindex.io/assets/platform/Google/star/f.svg` (×5 per review) |
| Avatar CDN | `https://lh3.googleusercontent.com/a/...` (Google user content) |
| Loader in footer | `<script src="https://cdn.trustindex.io/loader.js?ver=1" async>` |

### 4.7 Trustindex Runtime Mechanism

1. Server renders a `<pre class="ti-widget">` with a `<template>` containing the full widget HTML (4 inline reviews with all stars/images)
2. A sibling `<div>` carries `data-src`, `data-template-id`, and `data-css-url`
3. At page load, `trustindex-loader-js` (loaded async from `cdn.trustindex.io/loader.js`) reads the `data-*` attributes, fetches the CSS, and replaces the template content with the interactive slider widget
4. The `<template>` content serves as no-JS fallback

---

## 5. Full Raw HTML

The complete raw HTML is stored at:

**`analysis/testimonios-raw.html`** (24 lines, 15,656 bytes)

Key lines:
- **Line 1:** Empty `<style>` tags + row-wide Greenshift CSS block
- **Line 2:** `<section>` opening + first column with its CSS
- **Lines 4–5:** Logo image group (ECOCICLO icon + CSS)
- **Lines 8–9:** "Testimonios" overhead label (span + CSS)
- **Lines 13–14:** Heading "Confianza avalada por más de 2.500 servicios" (h2 + CSS)
- **Lines 18–22:** Trustindex widget column (column CSS + `<pre>` with template + loader div)
- **Lines 23–24:** Closing `</div>` and `</section>`
