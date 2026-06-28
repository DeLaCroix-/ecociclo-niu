# CTA Section Greenshift HTML Extraction — ecociclo.es

**Source**: `https://ecociclo.es/`
**Date scraped**: 2026-06-28
**Section ID**: `gspb_row-id-gsbp-9ffae62`
**Framework**: Greenshift (WordPress block plugin) + Blocksy theme + AOS animations

---

## Resolved Color Palette (CSS Custom Properties)

These are defined in the page's global `:root` block (line 79 of source):

| CSS Variable | Chain | Fallback Value |
|---|---|---|
| `--wp--preset--color--palette-color-7` | → `--theme-palette-color-7` | `#00312D` (dark green) |
| `--wp--preset--color--palette-color-3` | → `--theme-palette-color-3` | `#65C132` (bright green) |
| `--wp--preset--color--palette-color-2` | → `--theme-palette-color-2` | `#45891E` (darker green hover) |
| `--wp--preset--color--text-on-secondary-hover` | (direct) | `#fffffd` (near-white) |
| `--wp--preset--color--palette-color-5` | → `--theme-palette-color-5` | `#EAFDE7` (light green) |
| `--gs-root-animation-opacity` | **Runtime JS** | `0` (set by Greenshift AOS) |
| `--gs-root-animation-transform` | **Runtime JS** | varies (set by Greenshift AOS) |
| `--gs-root-animation-easing` | **Runtime JS** | `cubic-bezier(0.42,0,0.58,1)` |
| `--theme-container-width` | **Blocksy theme** | `1200px` |
| `--theme-normal-container-max-width` | **Blocksy theme** | `1200px` |
| `--gs-row-column-padding` | **Greenshift default** | `15px min(3vw, 20px)` |

External stylesheets referenced:
- `blocksy-dynamic-global-css` — theme variables including `--theme-palette-color-*`, `--theme-container-width`, etc.
- `wp-block-library-css` — WordPress core block styles
- `ct-main-styles-css` — Blocksy theme main
- `ct-elementor-styles-css` — Elementor integration

---

## Complete Raw HTML (Lines 1374–1405)

### Outer Row `<style>` Block

```css
#gspb_row-id-gsbp-9ffae62{justify-content:space-between;margin-top:0px;margin-bottom:0px;display:flex;flex-wrap:wrap;}#gspb_row-id-gsbp-9ffae62 > .gspb_row__content{display:flex;justify-content:space-between;margin:0 auto;width:100%;flex-wrap:wrap;}.gspb_row{position:relative;}div[id^=gspb_col-id]{box-sizing:border-box;position:relative;}div[id^=gspb_col-id]{padding:var(--gs-row-column-padding,15px min(3vw,20px));}#gspb_row-id-gsbp-9ffae62{background-color:var(--wp--preset--color--palette-color-7,var(--theme-palette-color-7,#00312D));}#gspb_row-id-gsbp-9ffae62 > .gspb_backgroundOverlay{position:absolute;top:0;left:0;width:100%;height:100%;z-index:-1;}#gspb_row-id-gsbp-9ffae62 > .gspb_backgroundOverlay{opacity:0.55}#gspb_row-id-gsbp-9ffae62 > .gspb_backgroundOverlay{background-image:url(https://ecociclo.es/wp-content/uploads/2026/03/14.webp);background-size:cover;background-repeat:no-repeat;}#gspb_row-id-gsbp-9ffae62{isolation:isolate;}
```

### Section Opener + Column `<style>` Block

```html
<section class="wp-block-greenshift-blocks-row alignfull gspb_row gspb_row-id-gsbp-9ffae62" id="gspb_row-id-gsbp-9ffae62"><div class="gspb_backgroundOverlay"></div><style>#gspb_col-id-gsbp-b8abaec.gspb_row__col--12{width:100%;}@media (max-width:689.98px){#gspb_col-id-gsbp-b8abaec.gspb_row__col--12{width:100%;}}.gspb_row #gspb_col-id-gsbp-b8abaec.gspb_row__col--12{padding-top:70px;padding-bottom:70px;}@media (max-width:689.98px){.gspb_row #gspb_col-id-gsbp-b8abaec.gspb_row__col--12{padding-top:40px;padding-bottom:40px;}}</style>
```

### Inner Column + Inner Row `<style>` Block

```html
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--12 gspb_col-id-gsbp-b8abaec" id="gspb_col-id-gsbp-b8abaec"><style>#gspb_row-id-gsbp-423aa83{justify-content:space-between;margin-top:0px;margin-bottom:0px;display:flex;flex-wrap:wrap;}#gspb_row-id-gsbp-423aa83 > .gspb_row__content{display:flex;justify-content:space-between;margin:0 auto;width:100%;flex-wrap:wrap;}.gspb_row{position:relative;}div[id^=gspb_col-id]{box-sizing:border-box;position:relative;}div[id^=gspb_col-id]{padding:var(--gs-row-column-padding,15px min(3vw,20px));}body.gspb-bodyfront #gspb_row-id-gsbp-423aa83 > .gspb_row__content{width:var(--theme-container-width,1200px);}body.gspb-bodyfront #gspb_row-id-gsbp-423aa83 > .gspb_row__content{max-width:var(--theme-normal-container-max-width,1200px);}</style>
```

### Inner Row + Left (Empty) Column `<style>` Block

```html
<div class="wp-block-greenshift-blocks-row gspb_row gspb_row-id-gsbp-423aa83" id="gspb_row-id-gsbp-423aa83"><div class="gspb_row__content"> <style>#gspb_col-id-gsbp-42d8970.gspb_row__col--6{width:50%;}@media (max-width:689.98px){#gspb_col-id-gsbp-42d8970.gspb_row__col--6{width:100%;}}@media (max-width:689.98px){body.gspb-bodyfront #gspb_col-id-gsbp-42d8970.gspb_row__col--6{display:none !important;}}</style>
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--6 gspb_col-id-gsbp-42d8970" id="gspb_col-id-gsbp-42d8970"></div>
```

### Right (Content) Column `<style>` Block

```html

<style>#gspb_col-id-gsbp-89c27ca.gspb_row__col--6{width:50%;}@media (max-width:689.98px){#gspb_col-id-gsbp-89c27ca.gspb_row__col--6{width:100%;}}body #gspb_col-id-gsbp-89c27ca.gspb_row__col--6{display:flex;flex-direction:column;align-items:stretch;row-gap:10px;}</style>
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--6 gspb_col-id-gsbp-89c27ca" id="gspb_col-id-gsbp-89c27ca">
```

### Icon + Overhead Label Row

```html
<div class="wp-block-group is-horizontal is-content-justification-left is-nowrap is-layout-flex wp-container-core-group-is-layout-f2ef6b81 wp-block-group-is-layout-flex" style="min-height:0px;margin-top:0;margin-bottom:0;padding-top:0;padding-right:0px;padding-bottom:0;padding-left:0px"><style>#gspb_image-id-gsbp-25fb174{text-align:left;}#gspb_image-id-gsbp-25fb174 img{object-fit:fill;}#gspb_image-id-gsbp-25fb174 img{vertical-align:top;}#gspb_image-id-gsbp-25fb174 img{display:inline-block;box-sizing:border-box;max-width:100%;height:auto;}#gspb_image-id-gsbp-25fb174{margin-bottom:0px;}#gspb_image-id-gsbp-25fb174 img{transition-duration:0.8s;}#gspb_image-id-gsbp-25fb174 img{transition-timing-function:cubic-bezier(0.6,-0.28,0.735,0.045);}#gspb_image-id-gsbp-25fb174 img{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform;}#gspb_image-id-gsbp-25fb174 img.aos-animate,#gspb_image-id-gsbp-25fb174 img[data-gs-aos]{opacity:1;transform:translateZ(0) scale(1);}#gspb_image-id-gsbp-25fb174 img{transform:var(--gs-root-animation-transform,scale(0.6));}#gspb_image-id-gsbp-25fb174 img{width:28px;}#gspb_image-id-gsbp-25fb174,#gspb_image-id-gsbp-25fb174 img{height:auto;}@media (max-width:999.98px){#gspb_image-id-gsbp-25fb174,#gspb_image-id-gsbp-25fb174 img{height:auto;}}@media (max-width:689.98px){#gspb_image-id-gsbp-25fb174,#gspb_image-id-gsbp-25fb174 img{height:auto;}}@media (max-width:689.98px){#gspb_image-id-gsbp-25fb174,#gspb_image-id-gsbp-25fb174 img{height:auto;}}</style>
<div class="wp-block-greenshift-blocks-image gspb_image gspb_image-id-gsbp-25fb174" id="gspb_image-id-gsbp-25fb174"><img loading="lazy" loading="lazy" decoding="async" src="https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO.webp" data-src="" alt="" loading="lazy" width="28" height="1080" data-aos="zoom-in" data-aos-easing="ease-in-back" data-aos-duration="800"/></div>


<style>.gsbp-e6b5bfb{color:var(--wp--preset--color--palette-color-3,var(--theme-palette-color-3,#65C132));margin-top:0px;margin-bottom:0px;margin-left:0px;margin-right:0px;padding-top:0px;padding-bottom:0px;padding-left:0px;padding-right:0px;}@media (max-width:689.98px){.gsbp-e6b5bfb{font-size:14px;}}.gsbp-e6b5bfb{transition-duration:0.8s;}.gsbp-e6b5bfb{transition-timing-function:cubic-bezier(0.25,0.46,0.45,0.94);}.gsbp-e6b5bfb{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}.gsbp-e6b5bfb.aos-animate,.gsbp-e6b5bfb[data-gs-aos]{opacity:1;transform:translateZ(0);}.gsbp-e6b5bfb{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}</style>
<span data-aos="fade-left" data-aos-easing="ease-out-cubic" data-aos-duration="800" class="overhead-span gsbp-e6b5bfb">Transformación Ambiental</span>
</div>
```

### Heading `<style>` Block + H2

```html

<style>#gspb_heading-id-gsbp-383a6f1{transition-duration:0.8s;}#gspb_heading-id-gsbp-383a6f1{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_heading-id-gsbp-383a6f1{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}#gspb_heading-id-gsbp-383a6f1.aos-animate,#gspb_heading-id-gsbp-383a6f1[data-gs-aos]{opacity:1;transform:translateZ(0);}#gspb_heading-id-gsbp-383a6f1{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}#gspb_heading-id-gsbp-383a6f1{text-transform:uppercase;}#gspb_heading-id-gsbp-383a6f1{color:var(--wp--preset--color--text-on-secondary-hover,#fffffd);}#gspb_heading-id-gsbp-383a6f1{margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;}@media (max-width:689.98px){#gspb_heading-id-gsbp-383a6f1{margin-bottom:0px;}}</style>
<h2 id="gspb_heading-id-gsbp-383a6f1" class="gspb_heading gspb_heading-id-gsbp-383a6f1 " data-aos="fade-left" data-aos-easing="ease" data-aos-duration="800">Recupera tu espacio hoy mismo en cualquier punto de barcelona</h2>
```

### Body Text `<style>` Block + DIV

```html

<style>.gspb_text-id-gsbp-4d4b5fe{transition-duration:0.8s;}.gspb_text-id-gsbp-4d4b5fe{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}.gspb_text-id-gsbp-4d4b5fe{transition-delay:0s;}.gspb_text-id-gsbp-4d4b5fe.aos-animate,.gspb_text-id-gsbp-4d4b5fe[data-gs-aos]{transition-delay:0.1s;--gs-root-animation-delay:0.1s;}.gspb_text-id-gsbp-4d4b5fe{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}.gspb_text-id-gsbp-4d4b5fe.aos-animate,.gspb_text-id-gsbp-4d4b5fe[data-gs-aos]{opacity:1;transform:translateZ(0);}.gspb_text-id-gsbp-4d4b5fe{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}.gspb_text-id-gsbp-4d4b5fe{color:var(--wp--preset--color--text-on-secondary-hover,#fffffd);}.gspb_text-id-gsbp-4d4b5fe{padding-top:10px!important;padding-bottom:20px!important;}</style>
<div id="gspb_text-id-gsbp-4d4b5fe" class="gspb_text gspb_text-id-gsbp-4d4b5fe " data-aos="fade-left" data-aos-delay="100" data-aos-easing="ease" data-aos-duration="800">No dejes que la acumulación de residuos, materiales o elementos innecesarios afecte la imagen, la seguridad o el funcionamiento de tu empresa. En Ecociclo te ayudamos con una solución profesional de <strong>gestión de residuos en Cataluña</strong>, adaptada a tus necesidades y con respuesta rápida.</div>
```

### CTA Button `<style>` Block + Anchor

```html

<style>.gsbp-115c306{border-top-left-radius:30px;border-bottom-left-radius:30px;border-top-right-radius:30px;border-bottom-right-radius:30px;align-self:start;padding-top:10px;padding-bottom:10px;padding-left:25px;padding-right:25px;display:inline-block;background-color:var(--wp--preset--color--palette-color-3,var(--theme-palette-color-3,#65C132));border-radius:15px;border-style:solid;border-width:0px;border-color:#1a1a1a;box-shadow:0 1px 3px 0 #00000005;color:#ffffff;transition:0.25s;text-decoration:none;}.gsbp-115c306:hover{box-shadow:0 8px 15px 0 #00000040;transform:translateY(-3px);color:#ffffff;background-color:var(--wp--preset--color--palette-color-2,var(--theme-palette-color-2,#45891E));}.gsbp-115c306:focus,.gsbp-115c306:active{box-shadow:0 1px 0 0 #00000040;transform:translateY(3px);}.gsbp-115c306{transition-duration:0.8s;}.gsbp-115c306{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}.gsbp-115c306{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}.gsbp-115c306.aos-animate,.gsbp-115c306[data-gs-aos]{opacity:1;transform:translateZ(0);}.gsbp-115c306{transform:var(--gs-root-animation-transform,translate3d(0,calc(max(50px,15%)),0));}</style>
<a data-aos="fade-up" data-aos-easing="ease" data-aos-duration="800" class="gs-parent-hover gs_button  gsbp-115c306" href="https://ecociclo.es/contacto/" data-type="button-component"><strong>Solicitar presupuesto</strong></a>
```

### Closing Tags

```html
</div>
 </div></div>
</div>
</section>
```

---

## Section Structure Summary

```
<section#gspb_row-id-gsbp-9ffae62>          ← Full-width row, dark green bg (#00312D), bg image overlay
  <div.gspb_backgroundOverlay />            ← 55% opacity overlay with 14.webp
  <div#gspb_col-id-gsbp-b8abaec.col--12>   ← Single full-width column (70px/40px padding)
    <div#gspb_row-id-gsbp-423aa83>          ← Constrained inner row (1200px max-width)
      <div.gspb_row__content>
        <div#gspb_col-id-gsbp-42d8970.col--6 />  ← Empty spacer (hidden on mobile)
        <div#gspb_col-id-gsbp-89c27ca.col--6>    ← Content column (flex column, 10px row-gap)
          <div.wp-block-group>                    ← Horizontal flex group
            <img ECOCICLO.webp width=28 />        ← Small logo icon (zoom-in animation)
            <span>Transformación Ambiental</span> ← Green overhead label (fade-left)
          </div>
          <h2>Recupera tu espacio…</h2>           ← UPPERCASE white heading (fade-left)
          <div.gspb_text>No dejes que…</div>      ← White body text (fade-left, 100ms delay)
          <a.gsbp-115c306>Solicitar presupuesto</a> ← Green button → /contacto/ (fade-up)
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## Key CSS Details (Resolved)

### Row Background
- **Background color**: `#00312D` (dark green) via `--wp--preset--color--palette-color-7`
- **Background overlay image**: `https://ecociclo.es/wp-content/uploads/2026/03/14.webp`
- **Overlay opacity**: 0.55
- **Isolation**: `isolate` (creates new stacking context for overlay z-index)

### Column Padding
- **Desktop**: `padding-top: 70px; padding-bottom: 70px;`
- **Mobile** (`max-width: 689.98px`): `padding-top: 40px; padding-bottom: 40px;`

### Layout Constraints
- **Inner row max-width**: `var(--theme-normal-container-max-width, 1200px)` (from Blocksy theme)
- **Column width**: 100% (`col--12` outer, `col--6` split inner)

### Left Column (Empty Spacer)
- **Desktop**: 50% width
- **Mobile** (`max-width: 689.98px`): `display: none !important` — hidden on mobile

### Right Column (Content)
- **Desktop**: 50% width
- **Mobile**: 100% width
- **Layout**: `display: flex; flex-direction: column; align-items: stretch; row-gap: 10px;`

### ECOCICLO Icon
- **Image**: `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO.webp`
- **Width**: 28px, height auto
- **Animation (AOS)**: `zoom-in` with `ease-in-back`, 800ms duration
- **Initial state**: `opacity: 0; transform: scale(0.6)` (set via `--gs-root-animation-*`)
- **Animated state**: `opacity: 1; transform: translateZ(0) scale(1)`

### Overhead Label "Transformación Ambiental"
- **Color**: `#65C132` (bright green) via `--wp--preset--color--palette-color-3`
- **Animation (AOS)**: `fade-left` with `ease-out-cubic`, 800ms
- **Initial**: `opacity: 0; transform: translate3d(calc(max(50px,15%)), 0, 0)`
- **Animated**: `opacity: 1; transform: translateZ(0)`
- **Mobile**: font-size 14px

### Heading H2
- **Text**: "Recupera tu espacio hoy mismo en cualquier punto de barcelona"
- **Color**: `#fffffd` (near-white) via `--wp--preset--color--text-on-secondary-hover`
- **Text-transform**: `uppercase`
- **Animation (AOS)**: `fade-left`, ease, 800ms
- **Initial**: `opacity: 0; transform: translate3d(calc(max(50px,15%)), 0, 0)`
- **Animated**: `opacity: 1; transform: translateZ(0)`

### Body Text
- **Text**: "No dejes que la acumulación de residuos…" (includes `<strong>gestión de residuos en Cataluña</strong>`)
- **Color**: `#fffffd` (near-white) via `--wp--preset--color--text-on-secondary-hover`
- **Animation (AOS)**: `fade-left`, ease, 800ms, 100ms delay
- **Padding**: `padding-top: 10px !important; padding-bottom: 20px !important;`

### CTA Button
- **Text**: "Solicitar presupuesto" (bold)
- **Link**: `https://ecociclo.es/contacto/`
- **Background**: `#65C132` (bright green) via `--wp--preset--color--palette-color-3`
- **Text color**: `#ffffff`
- **Border-radius**: 30px on all corners, then overridden to 15px
- **Padding**: 10px top/bottom, 25px left/right
- **Animation (AOS)**: `fade-up`, ease, 800ms
- **Initial**: `opacity: 0; transform: translate3d(0, calc(max(50px,15%)), 0)`
- **Hover**: `box-shadow: 0 8px 15px 0 rgba(0,0,0,0.25); transform: translateY(-3px); background-color: #45891E`
- **Active/Focus**: `box-shadow: 0 1px 0 0 rgba(0,0,0,0.25); transform: translateY(3px)`

---

## AOS Animation Pattern

All elements use Greenshift's AOS (Animate on Scroll) system. The pattern:

1. **Initial (hidden)** state set via CSS custom properties:
   - `opacity: var(--gs-root-animation-opacity, 0)` → defaults to 0
   - `transform: var(--gs-root-animation-transform, …)` → preset transform
2. **`data-aos` attributes** on each element specify animation type, easing, duration, delay
3. When element scrolls into view, Greenshift JS adds class `.aos-animate` or attribute `[data-gs-aos]`
4. Those selectors set `opacity: 1; transform: translateZ(0)` — making the element fully visible

Animation types used in this section:
- `zoom-in` (image icon)
- `fade-left` (overhead label, heading, body text)
- `fade-up` (CTA button)

---

## Responsive Breakpoints

| Breakpoint | Applied To |
|---|---|
| `max-width: 999.98px` | Image height reset |
| `max-width: 689.98px` | Column width changes (100%), padding reduction, left column hidden, label font-size |

---

## Notes

- All CSS for this section is **inline** — `<style>` blocks embedded directly alongside HTML elements (Greenshift block pattern). No separate stylesheet needed for this section's styles.
- The `--gs-root-animation-*` variables are set **dynamically by JavaScript** at runtime (Greenshift's `frontend.js`). They are not present in the static HTML source.
- Theme-level variables like `--theme-palette-color-7`, `--theme-container-width`, etc. come from Blocksy's dynamic CSS (`blocksy-dynamic-global-css` stylesheet at `wp-content/uploads/blocksy/css/global.css`).
- There are 9 total `<style>` blocks inside this section (one per Greenshift block: row, column, inner-row, column, image, span, heading, text, button).
- The background image `14.webp` is applied via a `.gspb_backgroundOverlay` div with `z-index: -1` and the parent row has `isolation: isolate` to create a stacking context.
