# HERO SECTION — Greenshift Block Extraction
# Source: https://ecociclo.es/
# Greenshift Row ID: gspb_row-id-gsbp-87fe861
# Date extracted: 2026-06-28
# Method: Technology B — Direct HTML + REST API + Playwright Computed Styles

================================================================================
                          SECTION ARCHITECTURE
================================================================================

  ┌─────────────────────────────────────────────────────────────────────┐
  │  <section id="gspb_row-id-gsbp-87fe861">                             │
  │  HERO ROW (full width, flex wrap, bg #888 fallback)                 │
  │  Background image: 23.webp, cover, 50% 49%, fixed attachment        │
  │  Height: 726.55px (computed at 1440px viewport)                     │
  │                                                                     │
  │  ┌─ gspb_backgroundOverlay (empty/transparent)                      │
  │  │                                                                  │
  │  ├─ gspb_col-id-gsbp-6af6a8a  (12-col, 100%, padding 160px 20px 0) │
  │  │  │                                                               │
  │  │  └─ gspb_row-id-gsbp-ef8b9d5  (nested row, theme-container max) │
  │  │     │                                                            │
  │  │     ├─ COL 1: gspb_col-id-gsbp-0cc5f26  (33.33%, 430px)         │
  │  │     │   ├─ H1: gspb_heading-id-gsbp-435af4e                     │
  │  │     │   ├─ P:  gspb_text-id-gsbp-6c529be                        │
  │  │     │   └─ CTA container → gsbp-b5caa74 button                  │
  │  │     │                                                            │
  │  │     ├─ COL 2: gspb_col-id-gsbp-5372409  (33.33%, 430px)         │
  │  │     │   └─ gspb_image-id-gsbp-83c61e6 → 25.webp (320×1080)     │
  │  │     │                                                            │
  │  │     └─ COL 3: gspb_col-id-gsbp-ae5d3d4  (33.33%, 430px)         │
  │  │         ├─ Card 1: gspb_container-id-gsbp-deabda5               │
  │  │         │   └─ Row gsbp-a3eec92: icon 25% | text 75%           │
  │  │         ├─ Card 2: gspb_container-id-gsbp-4ab0947               │
  │  │         │   └─ Row gsbp-b903de7: icon 25% | text 75%           │
  │  │         └─ Card 3: gspb_container-id-gsbp-55b93bd               │
  │  │             └─ Row gsbp-cda7cdc: icon 25% | text 75%           │
  └─────────────────────────────────────────────────────────────────────┘

================================================================================
                    COLUMN LAYOUT (computed at 1440px)
================================================================================

  COL 1 (Text - 33.33%):    x=75,   y=160, w=430, h=566.5
    padding: 70px 20px 15px | flex column | gap: 10px | bg: transparent
  COL 2 (Image - 33.33%):   x=505,  y=160, w=430, h=566.5
    padding: 0 | flex row | justify: center | align: flex-end
  COL 3 (Cards - 33.33%):   x=935,  y=160, w=430, h=566.5
    padding: 15px 20px 15px 60px | flex column | justify: center | align: flex-end | gap: 20px

================================================================================
                     HERO ROW — RAW INLINE STYLES
================================================================================

#gspb_row-id-gsbp-87fe861 {
    justify-content: space-between;
    margin-top: 0px;
    margin-bottom: 0px;
    display: flex;
    flex-wrap: wrap;
}
#gspb_row-id-gsbp-87fe861 > .gspb_row__content {
    display: flex;
    justify-content: space-between;
    margin: 0 auto;
    width: 100%;
    flex-wrap: wrap;
}
.gspb_row { position: relative; }
div[id^=gspb_col-id] { box-sizing: border-box; position: relative; }
div[id^=gspb_col-id] { padding: var(--gs-row-column-padding, 15px min(3vw, 20px)); }

#gspb_row-id-gsbp-87fe861 {
    background-color: #888888;            /* fallback before image loads */
    background-size: cover;
    background-repeat: no-repeat;
    background-position: 50% 49%;
}
#gspb_row-id-gsbp-87fe861.gs-active-view {
    background-image: url(https://ecociclo.es/wp-content/uploads/2026/03/23.webp);
}
#gspb_row-id-gsbp-87fe861 {
    background-attachment: fixed;
}
#gspb_row-id-gsbp-87fe861:hover {
    background-size: cover;
}
#gspb_row-id-gsbp-87fe861 > .gspb_backgroundOverlay {
    background-size: cover;
    background-repeat: no-repeat;
}

================================================================================
              COMPUTED STYLES (Playwright getComputedStyle)
================================================================================

HERO CONTAINER (#gspb_row-id-gsbp-87fe861):
  - background-color: rgb(136, 136, 136)   // #888888 fallback
  - background-image: url("https://ecociclo.es/wp-content/uploads/2026/03/23.webp")
  - background-size: cover
  - background-position: 50% 49%
  - background-attachment: fixed
  - background-repeat: no-repeat
  - display: flex
  - justify-content: space-between
  - flex-wrap: wrap
  - min-height: 0px (not set — height driven by content)
  - padding: 0px
  - margin: 0px
  - position: relative
  - overflow: visible

================================================================================
                     H1 HEADING
================================================================================

  Text: "Gestión de residuos en Barcelona para empresas, industria y locales"
  Tag: H1 (wrapped in <strong>)
  Rect: x=95, y=230, w=540, h=171 (extends into COL2 via negative margin)
  
  Computed:
    font-size: 38px
    font-weight: 700
    font-family: "SoinSans-Bold", sans-serif
    color: rgb(255, 255, 255)          // #ffffff
    text-transform: uppercase
    line-height: 57px                  // 1.5
    margin: 0px -150px 0px 0px        // negative right margin to extend across columns
    padding: 0px

  Inline style (#gspb_heading-id-gsbp-435af4e):
    text-transform: uppercase;
    font-size: 38px;
    @media (max-width:689.98px) { font-size: 30px; }
    color: var(--wp--preset--color--palette-color-8, var(--theme-palette-color-8, #ffffff));
    margin-top: 0px;
    margin-right: -150px;
    margin-bottom: 0px;
    margin-left: 0px;
    @media (max-width:689.98px) { margin-right: 0px; }

================================================================================
                     DESCRIPTION TEXT
================================================================================

  Text: "En Ecociclo ayudamos a empresas, naves industriales, locales, oficinas 
         y almacenes con servicios de gestión de residuos en Barcelona, 
         vaciados, limpiezas técnicas y soluciones ambientales adaptadas 
         a cada necesidad."
  Rect: x=95, y=411, w=450, h=115.2
  
  Computed:
    font-size: 18px
    font-weight: 400
    font-family: "SoinSans-Roman", sans-serif
    color: rgb(255, 255, 255)
    line-height: 28.8px              // 1.6
    margin: 0px -60px 0px 0px

  Inline style (.gspb_text-id-gsbp-6c529be):
    color: var(--wp--preset--color--palette-color-8, var(--theme-palette-color-8, #ffffff));
    margin-right: -60px !important;
    margin-bottom: 0px !important;
    @media (max-width:689.98px) { margin-right: 0px !important; }

================================================================================
                     CTA BUTTON
================================================================================

  Text: "Solicitar presupuesto" (wrapped in <strong>)
  Link: https://ecociclo.es/contacto/
  Rect: x=95, y=551.2, w=203, h=48.8
  
  Computed:
    font-size: 18px
    font-weight: 400
    font-family: "SoinSans-Roman", sans-serif
    color: rgb(255, 255, 255)
    background-color: rgb(101, 193, 50)    // #65C132
    border-radius: 15px
    padding: 10px 25px
    box-shadow: rgba(0,0,0,0.02) 0px 1px 3px 0px
    border-width: 0px
    border-color: rgb(26, 26, 26)
    display: inline-block

  Inline style (.gsbp-b5caa74):
    border-radius: 15px;
    align-self: start;
    padding: 10px 25px;
    display: inline-block;
    background-color: var(--wp--preset--color--palette-color-3, var(--theme-palette-color-3, #65C132));
    border: 0px solid #1a1a1a;
    box-shadow: 0 1px 3px 0 #00000005;
    color: #ffffff;
    transition: 0.25s;
    text-decoration: none;
    transition-duration: 0.8s;
    transition-timing-function: var(--gs-root-animation-easing, cubic-bezier(0.42,0,0.58,1));

  HOVER:
    box-shadow: 0 8px 15px 0 #00000040;
    transform: translateY(-3px);
    color: #ffffff;
    background-color: var(--wp--preset--color--palette-color-2, var(--theme-palette-color-2, #45891E));

  ACTIVE/FOCUS:
    box-shadow: 0 1px 0 0 #00000040;
    transform: translateY(3px);

  ANIMATION (AOS):
    data-aos="fade-up" data-aos-easing="ease" data-aos-duration="800"
    opacity: var(--gs-root-animation-opacity, 0);
    transform: var(--gs-root-animation-transform, translate3d(0, calc(max(50px, 15%)), 0));
    .aos-animate { opacity: 1; transform: translateZ(0); }

================================================================================
                     OVERLAY IMAGE (COL 2)
================================================================================

  Source: https://ecociclo.es/wp-content/uploads/2026/03/25.webp
  Natural size: 610 × 1080
  Display size: 320 × 566.5 (height: auto)
  Rect: x=560, y=160, w=320, h=566.5
  Alt text: (empty)
  Positioning: bottom-aligned via column align-items: flex-end

  Inline style (#gspb_image-id-gsbp-83c61e6 img):
    vertical-align: top;
    display: inline-block;
    box-sizing: border-box;
    max-width: 100%;
    height: auto;
    width: 320px;
    @media (max-width:999.98px) { height: auto; }
    @media (max-width:689.98px) { height: auto; }

================================================================================
                  FEATURE CARDS (COL 3)
================================================================================

  Each card is a gspb_container with:
    - background-color: rgb(234, 253, 231)  // #EAFDE7 (palette-5)
    - border-radius: 10px
    - display: flex; flex-direction: column
    - No padding/margin on container (padding/margin on inner elements)
    
  Each card contains a nested row (gspb_row) with 2 columns:
    - Icon col: 25% (33.33% nominal, calc(25% 0px 0px) computed)
    - Text col: 75% (66.67% nominal, calc(75% 0px 0px) computed)

  Icon container:
    - background-color: rgb(101, 193, 50)   // #65C132 (palette-3)
    - border-radius: 5px
    - padding: 8px

  Icon SVG:
    - 40×40px, fill: rgb(255, 255, 255)     // #ffffff

  Card text:
    - font-size: 15px
    - font-weight: 400
    - font-family: "SoinSans-Roman", sans-serif
    - color: rgb(0, 49, 45)                  // #00312D

  --- Card 1 ---
  ID: gspb_container-id-gsbp-deabda5
  Row ID: gspb_row-id-gsbp-a3eec92
  Icon col: gspb_col-id-gsbp-6bed9f4 (25%)
    Icon container: gspb_container-id-gsbp-f52f363
    Icon: gspb_iconBox-id-gsbp-a32001d (RAEE/smartphone icon, viewBox 0 0 1024 1024)
  Text col: gspb_col-id-gsbp-32cb071 (75%)
    Text: "Gestión legal de  residuos electrónicos"
    Heading ID: gspb_heading-id-gsbp-8a28e84
  Computed rect: x=995, y=294.3, w=350, h=86

  --- Card 2 ---
  ID: gspb_container-id-gsbp-4ab0947
  Row ID: gspb_row-id-gsbp-b903de7
  Icon col: gspb_col-id-gsbp-f3580ed (25%)
    Icon container: gspb_container-id-gsbp-ee766dd
    Icon: gspb_iconBox-id-gsbp-17dda08 (shield/check icon, viewBox 0 0 1024 1024)
  Text col: gspb_col-id-gsbp-9567c2c (75%)
    Text: "Operaciones 100% aseguradas y garantizadas."
    Heading ID: gspb_heading-id-gsbp-6f5a69e
  Computed rect: x=995, y=400.3, w=350, h=86

  --- Card 3 ---
  ID: gspb_container-id-gsbp-55b93bd
  Row ID: gspb_row-id-gsbp-cda7cdc
  Icon col: gspb_col-id-gsbp-631230f (25%)
    Icon container: gspb_container-id-gsbp-213c063
    Icon: gspb_iconBox-id-gsbp-a8a137d (eye icon, viewBox 0 0 1152 1024)
  Text col: gspb_col-id-gsbp-ae3f81a (75%)
    Text: "Sabes donde termina cada residuo"
    Heading ID: gspb_heading-id-gsbp-23cf16c
  Computed rect: x=1004, y=506.3, w=341, h=86

================================================================================
                  RESPONSIVE BREAKPOINTS
================================================================================

  @media (max-width: 999.98px):
    - Overlay image height: auto

  @media (max-width: 689.98px):
    - Hero padding-bottom: 20px
    - COL 1 (text): 100% width, padding-top: 4px
    - COL 2 (image): 100% width
    - COL 3 (cards): 100% width, padding: 0
    - H1 font-size: 30px, margin-right: 0
    - Description margin-right: 0
    - Card icon col: 25% width (maintains)
    - Card text col: 75% width (maintains)

================================================================================
                  PALETTE COLORS USED
================================================================================

  --palette-color-2 (#45891E):  CTA button hover background
  --palette-color-3 (#65C132):  CTA button background, icon container background
  --palette-color-5 (#EAFDE7):  Feature card background
  --palette-color-8 (#ffffff):  All text, icon fill

================================================================================
                  FONTS USED
================================================================================

  SoinSans-Bold (weight 700):   H1 heading
  SoinSans-Roman (weight 400):  Description text, CTA button, card text

================================================================================
                  IMAGES TO DOWNLOAD
================================================================================

  1. Hero background: https://ecociclo.es/wp-content/uploads/2026/03/23.webp
     (saved as /images/23.webp)

  2. Hero overlay figure: https://ecociclo.es/wp-content/uploads/2026/03/25.webp
     Natural: 610×1080, Display: 320×auto
     (saved as /images/25.webp)
