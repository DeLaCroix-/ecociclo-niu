# Servicios Section — Raw Greenshift HTML Extraction

**Source:** `https://ecociclo.es/` (fetched 2026-06-28)
**Target row:** `#gspb_row-id-gsbp-b0a856b`
**Section span:** Lines 756–971 of the fetched HTML (~215 lines)

---

## 1. Page-Level Custom CSS for Servicios Cards

Found in a `<style>` block in `<head>` (lines 320–353), these classes are applied to service cards but are *not* inline Greenshift styles — they are custom theme overrides:

```css
/* Clase para el contenedor de cada servicio */
.servicios-ecociclo-fijo {
    display: flex !important;
    flex-direction: column !important;
    height: 100% !important;
    gap: 10px !important;
}

/* LA CLAVE: Reserva el hueco de 3 líneas exactas */
.servicios-ecociclo-fijo h3 {
    /* 1.2 (line-height) x 3 (líneas) = 3.6em */
    min-height: 3.6em !important;
    line-height: 1.2em !important;
    margin-top: 5px !important;
    margin-bottom: 10px !important;
    display: flex !important;
    align-items: flex-start !important; /* Mantiene el texto arriba del hueco */
    overflow: hidden;
}

/* La imagen se mantiene en su sitio sin ser pisada */
.servicios-ecociclo-fijo img {
    height: 200px !important;
    width: 100% !important;
    object-fit: cover !important;
    flex-shrink: 0 !important; /* Impide que el texto la aplaste */
}
```

Also present earlier:
```css
.tarjeta-producto-ecociclo img {
    order: -1;
    height: 200px !important;
    object-fit: cover !important;
}
```

---

## 2. Outer Row: `#gspb_row-id-gsbp-b0a856b`

### 2.1 CSS Variables & Theme Tokens Used

| Variable | Fallback |
|---|---|
| `--gs-row-column-padding` | `15px min(3vw,20px)` |
| `--theme-container-width` | `1200px` |
| `--theme-normal-container-max-width` | `1200px` |
| `--wp--preset--color--palette-color-8` | `var(--theme-palette-color-8, #ffffff)` |
| `--wp--preset--color--palette-color-3` | `var(--theme-palette-color-3, #65C132)` (green) |
| `--wp--preset--color--palette-color-2` | `var(--theme-palette-color-2, #45891E)` (dark green) |
| `--wp--preset--color--palette-color-7` | `var(--theme-palette-color-7, #00312D)` (dark teal) |
| `--wp--preset--color--palette-color-5` | `var(--theme-palette-color-5, #EAFDE7)` (light green) |
| `--gs-root-animation-opacity` | `0` |
| `--gs-root-animation-transform` | varies by element |

### 2.2 Outer Row `<style>` (line 756)

```css
#gspb_row-id-gsbp-b0a856b{justify-content:space-between;margin-top:0px;margin-bottom:0px;display:flex;flex-wrap:wrap;}
#gspb_row-id-gsbp-b0a856b > .gspb_row__content{display:flex;justify-content:space-between;margin:0 auto;width:100%;flex-wrap:wrap;}
.gspb_row{position:relative;}
div[id^=gspb_col-id]{box-sizing:border-box;position:relative;}
div[id^=gspb_col-id]{padding:var(--gs-row-column-padding,15px min(3vw,20px));}
body.gspb-bodyfront #gspb_row-id-gsbp-b0a856b > .gspb_row__content{width:var(--theme-container-width,1200px);}
body.gspb-bodyfront #gspb_row-id-gsbp-b0a856b > .gspb_row__content{max-width:var(--theme-normal-container-max-width,1200px);}
#gspb_row-id-gsbp-b0a856b > .gspb_backgroundOverlay{position:absolute;top:0;left:0;width:100%;height:100%;z-index:-1;}
#gspb_row-id-gsbp-b0a856b > .gspb_backgroundOverlay{opacity:0.18}
#gspb_row-id-gsbp-b0a856b > .gspb_backgroundOverlay{background-image:url(https://ecociclo.es/wp-content/uploads/2026/03/19.webp);}
#gspb_row-id-gsbp-b0a856b{isolation:isolate;}
```

### 2.3 Outer Row HTML (line 757)

```html
<section class="wp-block-greenshift-blocks-row alignfull gspb_row gspb_row-id-gsbp-b0a856b block__row" id="gspb_row-id-gsbp-b0a856b">
  <div class="gspb_backgroundOverlay"></div>
  <div class="gspb_row__content">
    ...
  </div>
</section>
```

**Key class names:** `wp-block-greenshift-blocks-row`, `alignfull`, `gspb_row`, `block__row`
**Background:** `.gspb_backgroundOverlay` with `background-image: url(19.webp)` at 0.18 opacity
**Layout:** flex row, contained within 1200px max-width

---

## 3. First Inner Column: `#gspb_col-id-gsbp-5f43acc` (full width, line 757–758)

```css
#gspb_col-id-gsbp-5f43acc.gspb_row__col--12{width:100%;}
@media (max-width:689.98px){#gspb_col-id-gsbp-5f43acc.gspb_row__col--12{width:100%;}}
.gspb_row #gspb_col-id-gsbp-5f43acc.gspb_row__col--12{padding-top:70px;}
```

```html
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--12 gspb_col-id-gsbp-5f43acc block__row-column" id="gspb_col-id-gsbp-5f43acc">
```

**Class names:** `wp-block-greenshift-blocks-row-column`, `gspb_row__col--12`, `block__row-column`

---

## 4. Header Row: `#gspb_row-id-gsbp-876532f` (Swiper H2 + Description)

### 4.1 Row `<style>`

```css
#gspb_row-id-gsbp-876532f{justify-content:space-between;margin-top:0px;margin-bottom:0px;display:flex;flex-wrap:wrap;}
#gspb_row-id-gsbp-876532f > .gspb_row__content{display:flex;justify-content:space-between;margin:0 auto;width:100%;flex-wrap:wrap;}
.gspb_row{position:relative;}
div[id^=gspb_col-id]{box-sizing:border-box;position:relative;}
div[id^=gspb_col-id]{padding:var(--gs-row-column-padding,15px min(3vw,20px));}
body.gspb-bodyfront #gspb_row-id-gsbp-876532f > .gspb_row__content{width:var(--theme-container-width,1200px);}
body.gspb-bodyfront #gspb_row-id-gsbp-876532f > .gspb_row__content{max-width:var(--theme-normal-container-max-width,1200px);}
```

### 4.2 Left Column (55%): `#gspb_col-id-gsbp-34c905c`

```css
#gspb_col-id-gsbp-34c905c.gspb_row__col--8{width:66.66666666666667%;}
@media (max-width:689.98px){#gspb_col-id-gsbp-34c905c.gspb_row__col--8{width:100%;}}
@media (min-width:1000px){body.gspb-bodyfront #gspb_col-id-gsbp-34c905c.gspb_row__col--8{width:calc(55% - 0px - 0px)}}
.gspb_row #gspb_col-id-gsbp-34c905c.gspb_row__col--8{padding-right:160px;}
@media (max-width:689.98px){.gspb_row #gspb_col-id-gsbp-34c905c.gspb_row__col--8{padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;}}
body #gspb_col-id-gsbp-34c905c.gspb_row__col--8{display:flex;flex-direction:column;row-gap:10px;}
```

**Contents:**
- **EcoCiclo-brand leaf icon** (`#gspb_image-id-gsbp-368c9b4`):
  - Image: `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO.webp`
  - Width: 28px, renders at auto height
  - AOS animation: `zoom-in`, `ease-in-back`, 800ms
  - Transition: scale 0.6 → 1 with cubic-bezier(0.6, -0.28, 0.735, 0.045)

- **Overhead span** (`.gsbp-b9ee22d`):
  - Text: "Soluciones integrales a medida"
  - Color: `var(--wp--preset--color--palette-color-3)` = green `#65C132`
  - AOS animation: `fade-left`, `ease-out-cubic`, 800ms
  - Transform: `translate3d(calc(max(50px,15%)),0,0)` → 0
  - Transition: cubic-bezier(0.25, 0.46, 0.45, 0.94)

- **H2 heading** (`#gspb_heading-id-gsbp-6158ef2`):
  - HTML: `<h2><strong>¿Qué hacemos </strong><br><strong>en ecociclo?</strong></h2>`
  - Text-transform: uppercase
  - AOS: `fade-left`, ease, 800ms, once
  - Transform: `translate3d(calc(max(50px,15%)),0,0)` → 0

### 4.3 Right Column (45%): `#gspb_col-id-gsbp-07f393f`

```css
#gspb_col-id-gsbp-07f393f.gspb_row__col--4{width:33.333333333333336%;}
@media (max-width:689.98px){#gspb_col-id-gsbp-07f393f.gspb_row__col--4{width:100%;}}
@media (min-width:1000px){body.gspb-bodyfront #gspb_col-id-gsbp-07f393f.gspb_row__col--4{width:calc(45% - 0px - 0px)}}
body #gspb_col-id-gsbp-07f393f.gspb_row__col--4{display:flex;align-items:center;}
```

**Contents:**
- **Description text** (`#gspb_heading-id-gsbp-994f396`):
  - Text: "Nos encargamos del **vaciado de naves industriales, locales y oficinas**, asegurando una gestión de residuos responsable y eficiente."
  - Align: right on desktop, left on mobile
  - Color: `var(--wp--preset--color--palette-color-4)` = `#192a3d`
  - Padding-left: 50px (0 on mobile)
  - AOS: `fade-left`, delay 100ms, ease, 800ms, once

---

## 5. Swiper Slider: `#gspb_slider-id-gsbp-2eac162`

### 5.1 Slider Configuration (`<style>` + data attributes)

```css
.gspb_slider-id-gsbp-2eac162 .swiper-slide-inner{min-height:480px;}
.gspb_slider-id-gsbp-2eac162{width:100%;}
.gspb_slider-id-gsbp-2eac162 .swiper-slide-inner{justify-content:center;}
.gspb_slider-id-gsbp-2eac162 .swiper-button-prev,.gspb_slider-id-gsbp-2eac162 .swiper-button-next{top:40%;}
.gspb_slider-id-gsbp-2eac162 .swiper-slide-inner{align-items:center;}
.gspb_slider-id-gsbp-2eac162 .swiper-button-prev,.gspb_slider-id-gsbp-2eac162 .swiper-button-next{width:44px;height:44px;line-height:44px;}
.gspb_slider-id-gsbp-2eac162 .swiper-button-prev:after,.gspb_slider-id-gsbp-2eac162 .swiper-button-next:after{font-size:20px;}
.gspb_slider-id-gsbp-2eac162 .swiper-button-prev,.gspb_slider-id-gsbp-2eac162 .swiper-button-next{visibility:hidden}
.gspb_slider-id-gsbp-2eac162:hover .swiper-button-prev,.gspb_slider-id-gsbp-2eac162:hover .swiper-button-next{visibility:visible}
.gspb_slider-id-gsbp-2eac162 .gspb-sliderlink{position:absolute;top:0;left:0;right:0;bottom:0;z-index:3}
.gspb_slider-id-gsbp-2eac162 .swiper-slide-inner > div{position:relative}
.gspb_slider-id-gsbp-2eac162 .swiper-pagination{bottom:2px!important;text-align:center!important}
.gspb_slider-id-gsbp-2eac162 .swiper-scrollbar{visibility:hidden;height:6px;display:none}
.gspb_slider-id-gsbp-2eac162 .swiper-pagination-bullet{width:7px;height:7px;border-radius:100px;background-color:var(--wp--preset--color--palette-color-3,#65C132);transition:width 0.4s ease-out}
.gspb_slider-id-gsbp-2eac162 .swiper-pagination-bullet-active{width:21px;background-color:var(--wp--preset--color--palette-color-2,#45891E)}
.gspb_slider-id-gsbp-2eac162 .swiper-button-prev{background-color:#65c23257;color:var(--wp--preset--color--palette-color-8,#ffffff);box-shadow:20px 20px 60px #58667d5e}
.gspb_slider-id-gsbp-2eac162 .swiper-button-next{background-color:#65c23257;color:var(--wp--preset--color--palette-color-8,#ffffff);box-shadow:20px 20px 60px #58667d5e}
.gspb_slider-id-gsbp-2eac162 [data-spacebetween]{padding-top:0px;padding-bottom:0px}
```

**Data attribute config on `.gs-swiper-init`:**
- `data-slidesperview="3"` / `data-slidesperviewxs="1"`
- `data-spacebetween="10"` (all breakpoints)
- `data-speed="400"`, `data-loop="false"`, `data-vertical="false"`
- `data-autoheight="false"`, `data-grabcursor="false"`, `data-freemode="false"`
- `data-centered="false"`, `data-autoplay="false"`, `data-autodelay="4000"`
- `data-mousewheel="true"`

### 5.2 Navigation Elements

```html
<div class="swiper-pagination"></div>
<div class="swiper-button-prev"></div>
<div class="swiper-button-next"></div>
<div class="swiper-scrollbar"></div>
```

---

## 6. The 8 Service Cards (swiper slides)

All 8 cards share an identical structural pattern. Each is a `swiper-slide` containing:

### 6.1 Per-Card Structure (Template)

```
swiper-slide
└── swiper-slide-inner (gspb_sliderinner-id-gsbp-XXXXXXX)
    └── .slider-content-zone
        └── gspb_container (gspb_container-gsbp-YYYYYYY) .caja-hover
            ├── gspb_iconBox (.caja-hover__iconbox)
            │   └── .gspb_iconBox__wrapper[display:inline-flex]
            │       └── <img src="https://ecociclo.es/wp-content/uploads/2026/03/35.webp">
            ├── h3 (.caja-hover__heading) — service title
            ├── p (.caja-hover__heading)  — service description
            └── wp-block-button → <a> "Ver Servicio"
```

### 6.2 Shared Card Container Styles

Every card container (`.caja-hover`) has **identical** styling:

```css
.gspb_container-id-gsbp-XXXXXXX{flex-direction:column;box-sizing:border-box;}
.gspb_container-id-gsbp-XXXXXXX.gspb_container > p:last-of-type{margin-bottom:0}
.gspb_container-id-gsbp-XXXXXXX.gspb_container{position:relative;}
body.gspb-bodyfront #gspb_container-id-gsbp-XXXXXXX.gspb_container{align-self:center;}
.gspb_container-id-gsbp-XXXXXXX.gspb_container{transition:all 0.2s ease;}
.gspb_container-id-gsbp-XXXXXXX.gspb_container:hover{transform:scale(1.01);}
.gspb_container-id-gsbp-XXXXXXX.gspb_container{margin-top:5px;margin-right:5px;margin-bottom:5px;margin-left:5px;
  padding-top:40px;padding-right:40px;padding-bottom:40px;padding-left:40px;}
.gspb_container-id-gsbp-XXXXXXX.gspb_container{border-top-left-radius:15px;border-top-right-radius:15px;
  border-bottom-right-radius:15px;border-bottom-left-radius:15px;}
.gspb_container-id-gsbp-XXXXXXX.gspb_container{border-style:solid;border-width:1px;
  border-color:var(--wp--preset--color--palette-color-3,#65C132);}
.gspb_container-id-gsbp-XXXXXXX.gspb_container > .gspb_backgroundOverlay{border-top-left-radius:15px;
  border-top-right-radius:15px;border-bottom-right-radius:15px;border-bottom-left-radius:15px;}
.gspb_container-id-gsbp-XXXXXXX.gspb_container{background-color:var(--wp--preset--color--palette-color-7,#00312D);}
.gspb_container-id-gsbp-XXXXXXX.gspb_container:hover{background-color:var(--wp--preset--color--palette-color-5,#EAFDE7);}
.gspb_container-id-gsbp-XXXXXXX.gspb_container{box-sizing:border-box;}
```

**Key hover behavior:** Background toggles from dark teal (`#00312D`) to light green (`#EAFDE7`) on hover, with `transform: scale(1.01)`.

### 6.3 Shared Icon Box Styles

Every icon box has **identical** styling:

```css
#gspb_iconBox-id-gsbp-XXXXXXX svg{width:72px;}
#gspb_iconBox-id-gsbp-XXXXXXX{justify-content:flex-start;display:flex;}
#gspb_iconBox-id-gsbp-XXXXXXX img{height:40px!important;width:40px!important;min-width:40px!important;}
#gspb_iconBox-id-gsbp-XXXXXXX img,#gspb_iconBox-id-gsbp-XXXXXXX img path{fill:#ffffff !important;}
#gspb_iconBox-id-gsbp-XXXXXXX img{margin:0px !important;}
#gspb_iconBox-id-gsbp-XXXXXXX .gspb_iconBox__wrapper{border-radius:10px;}
#gspb_iconBox-id-gsbp-XXXXXXX .gspb_iconBox__wrapper{border-color:var(--wp--preset--color--palette-color-3,#65C132);}
#gspb_iconBox-id-gsbp-XXXXXXX .gspb_iconBox__wrapper{background-color:var(--wp--preset--color--palette-color-3,#65C132);}
#gspb_iconBox-id-gsbp-XXXXXXX .gspb_iconBox__wrapper{padding:20px}
#gspb_iconBox-id-gsbp-XXXXXXX .gspb_iconBox__wrapper{margin-bottom:0px;}
```

**Note:** Every card uses the SAME icon image: `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` (40×40 in a 72px wrapper, green background `#65C132` rounded 10px).

### 6.4 Shared H3 Heading Styles

```css
#gspb_heading-id-gsbp-XXXXXXX{font-size:25px;}
#gspb_heading-id-gsbp-XXXXXXX{color:var(--wp--preset--color--palette-color-8,#ffffff);}
#gspb_heading-id-gsbp-XXXXXXX{margin:0;padding-top:20px;padding-right:0;padding-bottom:10px;padding-left:0;}
#gspb_heading-id-gsbp-XXXXXXX{transition:all 0.5s ease-out;transform:scale(1.01);}
```

### 6.5 Shared Description `<p>` Styles

```css
#gspb_heading-id-gsbp-XXXXXXX{color:var(--wp--preset--color--palette-color-8,#ffffff);}
#gspb_heading-id-gsbp-XXXXXXX{padding-bottom:15px;}
```

### 6.6 Card 1 — VACIADOS Y LIMPIEZA

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-894033a` |
| Container | `gspb_container-id-gsbp-f853f73` |
| IconBox | `gspb_iconBox-id-gsbp-009484e` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-d0465ca` |
| H3 text | `<strong>VACIADOS </strong><br><strong>Y LIMPIEZA</strong>` |
| Description | `gspb_heading-id-gsbp-7092ff2` |
| Description text | "Vaciado de naves industriales, pisos, trasteros, locales y oficina." |
| CTA link | `https://ecociclo.es/vaciado-de-naves-industrialesy-locales/` |
| CTA text | "Ver Servicio" |
| CSS classes | `caja-hover`, `caja-hover__iconbox`, `caja-hover__heading`, `wp-block-button`, `wp-block-button__link`, `wp-element-button`, `has-custom-width`, `wp-block-button__width-100` |

### 6.7 Card 2 — GESTIÓN DE RESIDUOS BANALES

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-5b4d4cd` |
| Container | `gspb_container-id-gsbp-1700fb0` |
| IconBox | `gspb_iconBox-id-gsbp-9736ac0` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-01b5628` |
| H3 text | `<strong><strong>GESTIÓN DE RESIDUOS BANALES</strong></strong>` (double `<strong>` — likely editor bug) |
| Description | `gspb_heading-id-gsbp-831955c` |
| Description text | "Contenedores para la gestión de residuos industriales" |
| CTA link | `https://ecociclo.es/gestion-residuos-banales-barcelona/` |

### 6.8 Card 3 — RESIDUOS ESPECIALES LÍQUIDOS

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-60b8eb7` |
| Container | `gspb_container-id-gsbp-82ffee5` |
| IconBox | `gspb_iconBox-id-gsbp-061ee6b` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-f7c3bf3` |
| H3 text | `<strong>RESIDUOS ESPECIALES LÍQUIDOS</strong>` |
| Description | `gspb_heading-id-gsbp-1161d75` |
| Description text | "Gestión y transporte de residuos especiales líquidos" |
| CTA link | `https://ecociclo.es/gestion-transporte-residuos-especiales-liquidos-barcelona/` |

### 6.9 Card 4 — RESIDUOS ESPECIALES SÓLIDOS

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-e2e373b` |
| Container | `gspb_container-id-gsbp-e3b9ddc` |
| IconBox | `gspb_iconBox-id-gsbp-2f29e52` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-6fca1f0` |
| H3 text | `<strong>RESIDUOS ESPECIALES SÓLIDOS</strong>` |
| Description | `gspb_heading-id-gsbp-5d1c00b` |
| Description text | "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do " (**placeholder lorem ipsum!**) |
| CTA link | `https://ecociclo.es/gestion-transporte-residuos-especiales-solidos-barcelona/` |

### 6.10 Card 5 — RETIRADA DE FIBROCEMENTO

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-12c35dd` |
| Container | `gspb_container-id-gsbp-77cde74` |
| IconBox | `gspb_iconBox-id-gsbp-62f6d85` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-1109a12` |
| H3 text | `<strong>RETIRADA DE FIBROCEMENTO</strong>` |
| Description | `gspb_heading-id-gsbp-6b5e7d3` |
| Description text | "Servicio profesional de retirada de fibrocemento y uralita en Barcelona" |
| CTA link | `https://ecociclo.es/retirada-fibrocemento-uralita-barcelona/` |

### 6.11 Card 6 — LIMPIEZA DE TERRENOS

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-b6f7ac0` |
| Container | `gspb_container-id-gsbp-e9e64cb` |
| IconBox | `gspb_iconBox-id-gsbp-2e30425` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-dd1e945` |
| H3 text | `<strong>LIMPIEZA </strong><br><strong>DE TERRENOS</strong>` |
| Description | `gspb_heading-id-gsbp-c3c174c` |
| Description text | "Servicio de limpieza y desbroce de terrenos y parcelas" |
| CTA link | `https://ecociclo.es/limpieza-terrenos-barcelona/` |

### 6.12 Card 7 — LIMPIEZA DE SÍNDROME DE DIÓGENES

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-10202e7` |
| Container | `gspb_container-id-gsbp-70a2515` |
| IconBox | `gspb_iconBox-id-gsbp-5aae9c1` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-f68e10f` |
| H3 text | `<strong>LIMPIEZA DE síndrome de DIÓGENES</strong>` |
| H3 extra | `text-transform:uppercase;` |
| Description | `gspb_heading-id-gsbp-0cf5a3f` |
| Description text | `<strong>Limpieza de lugares afectados por el síndrome de Diógenes</strong>` |
| CTA link | `https://ecociclo.es/limpieza-diogenes-barcelona/` |

### 6.13 Card 8 — TRASVASES Y ACONDICIONAMIENTO

| Asset | ID / Value |
|---|---|
| Swiper inner | `gspb_sliderinner-id-gsbp-07add9d` |
| Container | `gspb_container-id-gsbp-6b70e72` |
| IconBox | `gspb_iconBox-id-gsbp-dd4dd35` |
| Icon image | `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` |
| H3 | `gspb_heading-id-gsbp-fec60d0` |
| H3 text | `<strong>trasvases y acondicionamiento</strong>` |
| H3 extra | `text-transform:uppercase;` |
| Description | `gspb_heading-id-gsbp-6fc3ba7` |
| Description text | "Realizamos el de **trasvase de residuos peligrosos y no peligrosos**" |
| CTA link | `https://ecociclo.es/trasvases-acondicionamiento-residuos-peligrosos-no-peligrosos-barcelona/` |

---

## 7. "Ver todos los servicios" CTA (lines 965–970)

### 7.1 Column: `#gspb_col-id-gsbp-2f82108`

```css
#gspb_col-id-gsbp-2f82108.gspb_row__col--12{width:100%;}
@media (max-width:689.98px){#gspb_col-id-gsbp-2f82108.gspb_row__col--12{width:100%;}}
.gspb_row #gspb_col-id-gsbp-2f82108.gspb_row__col--12{padding-bottom:70px;}
body #gspb_col-id-gsbp-2f82108.gspb_row__col--12{display:flex;flex-direction:column;
  justify-content:center;align-content:flex-start;align-items:center;row-gap:20px;}
```

### 7.2 Container: `#gspb_container-id-gsbp-be37113`

```css
.gspb_container-id-gsbp-be37113{flex-direction:column;box-sizing:border-box;}
#gspb_container-id-gsbp-be37113.gspb_container > p:last-of-type{margin-bottom:0}
#gspb_container-id-gsbp-be37113.gspb_container{position:relative;}
body.gspb-bodyfront #gspb_container-id-gsbp-be37113.gspb_container{align-self:center;}
#gspb_container-id-gsbp-be37113.gspb_container{display:flex;justify-content:center;
  align-content:center;align-items:center;}
#gspb_container-id-gsbp-be37113.gspb_container{margin:0;}
#gspb_container-id-gsbp-be37113.gspb_container{box-sizing:border-box;}
```

### 7.3 Button: `.gsbp-dd80886`

```css
.gsbp-dd80886{
  border-top-left-radius:30px;border-bottom-left-radius:30px;
  border-top-right-radius:30px;border-bottom-right-radius:30px;
  align-self:start;
  padding-top:10px;padding-bottom:10px;padding-left:25px;padding-right:25px;
  display:inline-block;
  background-color:var(--wp--preset--color--palette-color-3,#65C132);
  border-radius:15px;
  border-style:solid;border-width:0px;border-color:#1a1a1a;
  box-shadow:0 1px 3px 0 #00000005;
  color:#ffffff;
  transition:0.25s;
  text-decoration:none;
}
.gsbp-dd80886:hover{
  box-shadow:0 8px 15px 0 #00000040;
  transform:translateY(-3px);
  color:#ffffff;
  background-color:var(--wp--preset--color--palette-color-2,#45891E);
}
.gsbp-dd80886:focus,.gsbp-dd80886:active{
  box-shadow:0 1px 0 0 #00000040;
  transform:translateY(3px);
}
/* AOS animation */
.gsbp-dd80886{transition-duration:0.8s;}
.gsbp-dd80886{transition-timing-function:cubic-bezier(0.42,0,0.58,1);}
.gsbp-dd80886{opacity:var(--gs-root-animation-opacity,0);
  transition-property:opacity,transform,filter;}
.gsbp-dd80886.aos-animate,.gsbp-dd80886[data-gs-aos]{opacity:1;transform:translateZ(0);}
.gsbp-dd80886{transform:translate3d(0,calc(max(50px,15%)),0);}
```

```html
<a data-aos="fade-up" data-aos-easing="ease" data-aos-duration="800"
   class="gs-parent-hover gs_button gsbp-dd80886"
   href="https://ecociclo.es/servicios/"
   data-type="button-component">
  <strong>Ver todos los servicios</strong>
</a>
```

**Classes:** `gs-parent-hover`, `gs_button`, `gsbp-dd80886`
**AOS:** `fade-up`, ease, 800ms
**Hover:** lifts -3px with shadow, background darkens to `#45891E`
**Active:** presses down +3px

---

## 8. Complete Class Name Inventory

### Greenshift Block Classes
| Class | Purpose |
|---|---|
| `wp-block-greenshift-blocks-row` | Greenshift row block |
| `wp-block-greenshift-blocks-row-column` | Greenshift column block |
| `wp-block-greenshift-blocks-container` | Greenshift container block |
| `wp-block-greenshift-blocks-image` | Greenshift image block |
| `wp-block-greenshift-blocks-iconbox` | Greenshift icon box block |
| `wp-block-greenshift-blocks-swiper` | Greenshift SwiperJS block |
| `wp-block-greenshift-blocks-swipe` | Greenshift swipe/slide inner |
| `gspb_row` | Generic row |
| `gspb_row__content` | Row inner content wrapper |
| `gspb_row__col--12`, `--8`, `--4`, `--6`, `--2`, `--10` | Column width classes |
| `gspb_row__col--xs-2`, `--xs-10` | Mobile column widths |
| `block__row` | Block row modifier |
| `block__row-column` | Block column modifier |
| `block__container` | Block container modifier |
| `block__heading` | Block heading modifier |
| `block__text` | Block text modifier |
| `alignfull` | Full-width alignment |
| `gspb_backgroundOverlay` | Background overlay div |
| `gspb_container` | Container block |
| `gspb_image` | Image block |
| `gspb_iconBox` | Icon box block |
| `gspb_iconBox__wrapper` | Icon box inner wrapper |
| `gspb_heading` | Heading block |
| `gspb_text` | Text block |
| `gspb_slider` (or `gs-swiper`) | Swiper slider wrapper |
| `gs-swiper-init` | Swiper initialization div |
| `swiper` / `swiper-wrapper` / `swiper-slide` | SwiperJS classes |
| `swiper-slide-inner` | Slide inner wrapper |
| `slider-content-zone` | Slide content area |
| `swiper-pagination` / `swiper-button-prev` / `swiper-button-next` | Swiper nav |
| `gspb-bodyfront` | Body class for Greenshift frontend |

### Custom Application Classes
| Class | Purpose |
|---|---|
| `caja-hover` | Service card container — triggers hover effects |
| `caja-hover__iconbox` | Icon box inside service card |
| `caja-hover__heading` | Headings inside service card |
| `overhead-span` | Decorative "overline" span (green tagline) |
| `gs-parent-hover` | Parent hover trigger for button |
| `gs_button` | Greenshift button |

### WordPress Core Classes
| Class | Purpose |
|---|---|
| `wp-block-group` | Gutenberg group |
| `wp-block-buttons` | Gutenberg buttons wrapper |
| `wp-block-button` | Gutenberg button |
| `wp-block-button__link` | Gutenberg button link |
| `wp-element-button` | Gutenberg button element |
| `wp-block-button__width-100` | Full-width button |
| `has-custom-width` | Custom width modifier |
| `is-layout-flex` | Flex layout |
| `is-content-justification-left` | Content alignment |
| `is-nowrap` | No wrap |
| `wp-container-core-group-is-layout-04d78b61` | Auto-generated unique group layout |

---

## 9. Complete Image URL Inventory

| URL | Usage |
|---|---|
| `https://ecociclo.es/wp-content/uploads/2026/03/19.webp` | Section background overlay (opacity 0.18) |
| `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO.webp` | EcoCiclo brand leaf icon (28px wide, in header row) |
| `https://ecociclo.es/wp-content/uploads/2026/03/35.webp` | Service card icon (same on ALL 8 cards, 40×40px) |

---

## 10. Data Attributes Inventory

### AOS (Animate on Scroll) Animation Attributes
| Attribute | Values used |
|---|---|
| `data-aos` | `fade-left`, `fade-up`, `zoom-in` |
| `data-aos-easing` | `ease`, `ease-out-cubic`, `ease-in-back` |
| `data-aos-duration` | `800` (all) |
| `data-aos-delay` | `100` (one instance) |
| `data-aos-once` | `true` (on H2 heading) |

### GS Root Animation Transform Variables
| Variable | Value |
|---|---|
| `--gs-root-animation-opacity` | `0` (initial hidden) |
| `--gs-root-animation-transform` | `scale(0.6)` or `translate3d(...)` |
| `--gs-root-animation-easing` | `cubic-bezier(0.42, 0, 0.58, 1)` |

### Swiper Data Attributes
| Attribute | Value |
|---|---|
| `data-slidesperview` | `3` |
| `data-slidesperviewxs` | `1` |
| `data-slidespergroup` | `1` |
| `data-spacebetween` | `10` |
| `data-spacebetweenmd` | `10` |
| `data-spacebetweensm` | `10` |
| `data-spacebetweenxs` | `10` |
| `data-speed` | `400` |
| `data-loop` | `false` |
| `data-vertical` | `false` |
| `data-verticalheight` | `500px` |
| `data-autoheight` | `false` |
| `data-grabcursor` | `false` |
| `data-freemode` | `false` |
| `data-centered` | `false` |
| `data-autoplay` | `false` |
| `data-autodelay` | `4000` |
| `data-effect` | `""` (empty) |
| `data-coverflowshadow` | `false` |
| `data-mousewheel` | `true` |

### Other Data Attributes
| Attribute | Value | Element |
|---|---|---|
| `data-type` | `button-component` | "Ver todos los servicios" link |
| `data-src` | `""` | Images (lazy-load placeholder) |

---

## 11. Color Palette Summary

| Token | Computed Value | Usage |
|---|---|---|
| `--palette-color-3` / `--theme-palette-color-3` | `#65C132` (green) | Icon boxes, card borders, button bg, overhead span |
| `--palette-color-2` / `--theme-palette-color-2` | `#45891E` (dark green) | Button hover, active pagination bullet |
| `--palette-color-7` / `--theme-palette-color-7` | `#00312D` (dark teal) | Card backgrounds |
| `--palette-color-5` / `--theme-palette-color-5` | `#EAFDE7` (light green) | Card hover backgrounds |
| `--palette-color-8` / `--theme-palette-color-8` | `#ffffff` | Card text, headings, icon fill |
| `--palette-color-4` / `--theme-palette-color-4` | `#192a3d` (dark blue) | Description text in header area |

---

## 12. Notable Observations

1. **Placeholder text:** Card 4 (Residuos Especiales Sólidos) contains **Lorem ipsum** placeholder text in production.
2. **Double `<strong>`:** Card 2 has nested `<strong><strong>` tags — an editor artifact.
3. **Identical icons:** All 8 service cards use the exact same icon image (`35.webp`), served as an `<img>` tag (not SVG inline), within a green rounded square wrapper.
4. **No `servicios-ecociclo-fijo` in output:** The custom CSS classes defined in `<head>` (`.servicios-ecociclo-fijo`, etc.) do NOT appear in the actual Greenshift markup. The cards use `caja-hover` instead. These custom classes appear to be for a different template/page.
5. **Mobile overrides:** Every icon box overrides background to `#e2eefd` at ≤999.98px and ≤689.98px — three identical media queries (likely a Greenshift editor artifact).
6. **GS animation system:** Greenshift uses CSS custom properties (`--gs-root-animation-*`) combined with `.aos-animate` class toggling to animate elements into view.
7. **Swiper buttons hidden by default:** Navigation arrows have `visibility:hidden` and only appear on hover.
8. **Inline styles:** Only one inline style used: `style="display:inline-flex"` on `.gspb_iconBox__wrapper` divs and `style="position:relative"` on the swiper wrapper.
