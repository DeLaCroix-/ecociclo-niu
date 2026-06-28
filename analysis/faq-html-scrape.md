# FAQ Section HTML Scrape Analysis — ecociclo.es

**Source URL:** `https://ecociclo.es/`
**Date fetched:** 2026-06-28
**Identifier:** `gspb_row-id-gsbp-b8efaa8`
**Raw extract saved to:** `analysis/faq-raw.html` (~47.8 KB, 94 lines)

---

## 1. Overview

The FAQ section is a Greenshift Blocks section rendered server-side by WordPress. The HTML is **fully inline** — all styles, SVG icons, and microdata are embedded directly in the page source. No client-side JS hydration is needed to render the static content (though Greenshift's JS handles accordion toggle interactivity and AOS scroll animations).

### Section Bounds
- **Start:** Line 1408 — `<style>` block for `#gspb_row-id-gsbp-b8efaa8`
- **End:** Line 1501 — `</div></section>`
- **Total raw HTML size:** ~47,778 characters

---

## 2. Section Structure (DOM Tree)

```
<section#gspb_row-id-gsbp-b8efaa8>            ← Outer FAQ wrapper (full-width Greenshift row)
  <div.gspb_backgroundOverlay>                ← CSS background image layer
  <div.gspb_row__content>                     ← Constrained content container (1200px max)
    <div#gspb_col-id-gsbp-19d72d6.gspb_row__col--12>  ← Column 1: Header area
      ├── <div.wp-block-group>                ← Flex group: icon + tagline
      │     ├── <style> + <img>               ← Ecociclo logo icon (28px)
      │     └── <style> + <span.overhead-span> ← "Centro de Ayuda y Soporte"
      ├── <style> + <h2>                      ← "Preguntas frecuentes sobre gestión de residuos en barcelona"
      └── <style> + <div.gspb_text>           ← Subtitle text
    └── <div#gspb_col-id-gsbp-ef43a72.gspb_row__col--12>  ← Column 2: Accordions
          └── <div#gspb_row-id-gsbp-835b31f>  ← Inner row: 50/50 split
                ├── <div#gspb_col-id-gsbp-9a45e64.gspb_row__col--6>  ← LEFT column
                │     └── <div#gspb_accordion-id-gsbp-5baa306>       ← Accordion 1 (4 items)
                │           ├── AccordionItem #1 (gsopen) — "¿Qué tipo de servicios ofrece Ecociclo en Cataluña?"
                │           ├── AccordionItem #2 (gsclose) — "¿Trabajáis solo con empresas o también con particulares?"
                │           ├── AccordionItem #3 (gsclose) — "¿Prestáis servicio en toda Cataluña?"
                │           └── AccordionItem #4 (gsclose) — "¿Puedo solicitar presupuesto sin compromiso?"
                └── <div#gspb_col-id-gsbp-f6f07d6.gspb_row__col--6>  ← RIGHT column
                      └── <div#gspb_accordion-id-gsbp-1eb2f19>       ← Accordion 2 (4 items)
                            ├── AccordionItem #5 (gsclose) — "¿Podéis actuar con rapidez?"
                            ├── AccordionItem #6 (gsclose) — "¿Qué tipo de espacios podéis vaciar o limpiar?"
                            ├── AccordionItem #7 (gsclose) — "¿Gestionáis residuos no peligrosos y también residuos especiales?"
                            └── AccordionItem #8 (gsclose) — "¿Qué diferencia a Ecociclo de otras empresas?"
```

---

## 3. `<style>` Blocks Inventory

The FAQ section contains **22 inline `<style>` blocks** (each Greenshift component injects its own `<style>` tag). Categorized:

### 3a. Row/Section Styles (4 blocks)

| ID | Purpose |
|----|---------|
| `#gspb_row-id-gsbp-b8efaa8` | Outer FAQ section: flex layout, padding (70px, 40px mobile), background image `20.webp`, isolation |
| `#gspb_col-id-gsbp-19d72d6` | Header column: 100% width, flex column, 10px row-gap |
| `#gspb_col-id-gsbp-ef43a72` | Accordions column: 100% width |
| `#gspb_row-id-gsbp-835b31f` | Inner accordion row: flex layout, 1200px container |

### 3b. Accordion Column Split Styles (2 blocks)

| ID | Purpose |
|----|---------|
| `#gspb_col-id-gsbp-9a45e64` | Left accordion column: 50% width (100% mobile) |
| `#gspb_col-id-gsbp-f6f07d6` | Right accordion column: 50% width (100% mobile) |

### 3c. Accordion Container Styles (2 blocks) — CRITICAL for replication

| ID | Key Properties |
|----|---------------|
| `#gspb_accordion-id-gsbp-5baa306` | — `.gsclose > .content` → `overflow:hidden; opacity:0`<br>— `.gsopen > .content` → `opacity:1; max-height:5000px`<br>— Title: `#f9f9f9` bg, `10px` border-radius, `2px solid` border (`#00000012`)<br>— Content: `#EAFDE7` bg (desktop), `#ffffff` (mobile/tablet)<br>— Content border-radius: `0 0 10px 10px`<br>— Content border: `2px solid var(--palette-color-4, #192a3d)`, top: `1px solid transparent`<br>— Toggle icon: `20px`, fill `#ffffff`, hover fill `#fffffc`, `4px` stroke-width<br>— Toggle rotation: `.gsopen span.iconfortoggle { transform:rotate(90deg) }`<br>— Title padding: `15px 20px`<br>— Content text padding: `15px 20px`<br>— Item margin-bottom: `10px`<br>— Text align: `left`<br>— AOS animation: `fade-up`, `0.8s` duration |
| `#gspb_accordion-id-gsbp-1eb2f19` | **Identical to above** (same styles, different ID) |

### 3d. Accordion Item Styles (8 blocks, one per FAQ item)

Each accordion item has its own `<style>` block. All 8 share the same pattern:
- Title `background-color`: `var(--palette-color-7, #00312D)` (dark green)
- Title text color: `var(--palette-color-8, #ffffff)` (white)
- Toggle icon bars color: `var(--palette-color-8, #ffffff)`
- Question icon (SVG): `16×16px`, `fill: currentColor` (items 2–8) or `fill: #ffffff` (item 1 — gsopen)
- Question icon padding-right: `10px`
- Display: `inline-flex`, centered

**Exception:** First accordion item (`gsbp-a47e1ea`) has `fill: var(--palette-color-8, #ffffff)` instead of `fill: currentColor` for its question icon SVG.

### 3e. Header/Decor Styles (6 blocks)

| ID | Purpose |
|----|---------|
| `#gspb_image-id-gsbp-c5fbc75` | Logo icon: 28px width, AOS zoom-in animation |
| `.gsbp-46b953b` | "Centro de Ayuda y Soporte" span: green color, 14px mobile, fade-left animation |
| `#gspb_heading-id-gsbp-0a2b80d` | H2 heading: uppercase, center-aligned |
| `.gspb_text-id-gsbp-f282491` | Subtitle text: center-aligned |

---

## 4. Accordion HTML Structure (Per Item)

Each accordion item follows this exact pattern:

```html
<style>/* item-specific title/toggle colors */</style>
<div class="wp-block-greenshift-blocks-accordionitem gs-accordion-item gspb_accordionitem-{ID} {gsopen|gsclose}"
     id="gspb_accordionitem-{ID}"
     itemscope itemtype="https://schema.org/Question">
  <div id="gs-trigger-{ACCORDION_ID}-{N}"
       class="gs-accordion-item__title"
       aria-expanded="{true|false}"
       role="button" tabindex="0"
       aria-controls="gspb-accordion-item-content-{ID}">
    <!-- Question icon (SVG circle with "?") -->
    <span class="icontitle">
      <svg width="15" height="15" viewBox="0 0 1024 1024">...</svg>
    </span>
    <!-- Question text -->
    <div class="gs-accordion-item__heading">{QUESTION_TEXT}</div>
    <!-- Schema.org Question microdata -->
    <meta content="{QUESTION_TEXT}"/>
    <!-- Toggle chevron icon (SVG) -->
    <span class="iconfortoggle">
      <svg width="15" height="15" viewBox="0 0 1024 1024">...</svg>
    </span>
  </div>
  <!-- Answer content (hidden when gsclose) -->
  <div aria-labelledby="gs-trigger-{ACCORDION_ID}-{N}"
       class="gs-accordion-item__content"
       itemscope itemtype="https://schema.org/Answer"
       id="gspb-accordion-item-content-{ID}">
    <div class="gs-accordion-item__text">
      <p>{ANSWER_HTML}</p>
    </div>
  </div>
</div>
```

**Key details:**
- The `gsopen`/`gsclose` class on the outer div controls initial visibility
- `aria-expanded` matches the open/close state
- Each item has `itemscope itemtype="https://schema.org/Question"` and `https://schema.org/Answer` for SEO structured data
- Toggle chevron rotates 90° when `.gsopen` via CSS `transform: rotate(90deg)`

---

## 5. CSS Color Variables (Design Tokens)

The FAQ section uses these WordPress/Greenshift CSS custom properties:

| Variable | Fallback | Used For |
|----------|----------|----------|
| `--wp--preset--color--palette-color-3` / `--theme-palette-color-3` | `#65C132` | Green accent (tagline "Centro de Ayuda") |
| `--wp--preset--color--palette-color-7` / `--theme-palette-color-7` | `#00312D` | Accordion title background (dark green) |
| `--wp--preset--color--palette-color-8` / `--theme-palette-color-8` | `#ffffff` | Accordion title text + toggle icon color |
| `--wp--preset--color--palette-color-5` / `--theme-palette-color-5` | `#EAFDE7` | Accordion content background (desktop) |
| `--wp--preset--color--palette-color-4` / `--theme-palette-color-4` | `#192a3d` | Accordion content border color |
| `--wp--preset--color--border` | `#00000012` | Accordion title border color |
| `--wp--preset--color--text-on-secondary` | `#fffffc` | Toggle icon hover fill |
| `--wp--preset--color--text-on-secondary-hover` | `#fffffd` | (Used in adjacent CTA section) |
| `--theme-container-width` | `1200px` | Content max-width |
| `--gs-root-animation-easing` | `cubic-bezier(0.42,0,0.58,1)` | AOS animation easing |
| `--gs-row-column-padding` | `15px min(3vw,20px)` | Column padding |

---

## 6. Responsive Breakpoints

| Breakpoint | Target | Changes |
|-----------|--------|---------|
| `max-width: 999.98px` | Tablet | Accordion content bg → `#ffffff`; image heights → `auto` |
| `max-width: 689.98px` | Mobile | Section padding `70px→40px`; columns `50%→100%`; tagline font `→14px`; accordion content bg → `#ffffff` |

---

## 7. FAQ Content (All 8 Questions & Answers)

### Left Column (Accordion `gsbp-5baa306`)

1. **¿Qué tipo de servicios ofrece Ecociclo en Cataluña?** *(open by default)*
   > Ofrecemos servicios de vaciado, limpieza, retirada de residuos, gestión de residuos banales, residuos especiales líquidos, residuos especiales sólidos, limpieza de terrenos, retirada de fibrocemento y otras soluciones ambientales para empresas.

2. **¿Trabajáis solo con empresas o también con particulares?**
   > Principalmente trabajamos con empresas, industria, locales, oficinas, almacenes y espacios profesionales, aunque también realizamos determinados servicios para particulares según el tipo de intervención.

3. **¿Prestáis servicio en toda Cataluña?**
   > Sí, Ecociclo ofrece servicios de **gestión de residuos en Cataluña**, adaptándose a la ubicación, al volumen de trabajo y a las necesidades logísticas de cada cliente.

4. **¿Puedo solicitar presupuesto sin compromiso?**
   > Sí. Estudiamos cada caso y preparamos una propuesta adaptada al servicio necesario y sin compromiso.

### Right Column (Accordion `gsbp-1eb2f19`)

5. **¿Podéis actuar con rapidez?**
   > Sí. Siempre que la planificación lo permita, priorizamos una respuesta ágil para que el cliente pueda resolver el problema cuanto antes.

6. **¿Qué tipo de espacios podéis vaciar o limpiar?**
   > Trabajamos en naves industriales, locales, oficinas, almacenes, pisos, terrenos, parcelas, solares y otros espacios que necesitan vaciado, limpieza o retirada de residuos.

7. **¿Gestionáis residuos no peligrosos y también residuos especiales?**
   > Sí. En Ecociclo trabajamos tanto con residuos banales o no peligrosos como con residuos especiales líquidos y sólidos, ajustando el servicio a cada caso.

8. **¿Qué diferencia a Ecociclo de otras empresas?**
   > Nuestra experiencia, con **más de 10 años** y **más de 2.500 servicios realizados**, junto con una operativa rápida, profesional y orientada a empresa, nos permite ofrecer una solución más sólida y completa en Cataluña.

---

## 8. Key Observations for Replication

1. **Greenshift inline `<style>` pattern:** Every block (row, column, accordion, accordion item, heading, text, image) injects its own `<style>` tag immediately before the HTML element. This is Greenshift's default server-side rendering behavior.

2. **Accordion JS dependency:** The toggle behavior relies on Greenshift's frontend JS (class toggling `gsopen`/`gsclose`, `aria-expanded`, and the `max-height` transition). Static HTML alone won't toggle.

3. **AOS animations:** Elements use `data-aos` attributes (fade-up, fade-left, zoom-in) with Greenshift's custom CSS variables for opacity/transform transitions. These require AOS library or Greenshift JS.

4. **SVG icons are inline:** Both the question-mark circle and the chevron toggle arrow are inline SVGs (not icon fonts or external files).

5. **Schema.org structured data:** Every question uses `itemscope itemtype="https://schema.org/Question"` on the item wrapper and `https://schema.org/Answer` on the content div, with `<meta>` tags for the question text.

6. **Background image:** The section has a CSS background (`20.webp`) applied via `.gspb_backgroundOverlay` with `z-index: -1` and `isolation: isolate` on the parent.

7. **Two identical accordions, 4 items each:** The left and right accordions use identical CSS rules but different IDs. The items alternate between `gsopen` (first item only, left column) and `gsclose` (all others).

---

## 9. Files Produced

| File | Description |
|------|-------------|
| `analysis/faq-html-scrape.md` | This analysis document |
| `analysis/faq-raw.html` | Complete raw HTML extract (lines 1408–1501 from ecociclo.es) |
