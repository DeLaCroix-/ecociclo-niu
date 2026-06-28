# Filosofía Section — Raw Greenshift HTML Scrape Analysis

**Source:** `https://ecociclo.es/`  
**Scrape method:** `curl` + direct HTML regex/grep parsing  
**Date scraped:** 2026-06-28  
**Section ID:** `gspb_row-id-gsbp-d281619`  
**Section label:** "Nuestra Filosofía"

---

## 1. Section Overview

The Filosofía section is a Greenshift-powered WordPress block section on the ecociclo.es homepage. It spans **lines 664–753** of the scraped HTML (~90 lines). It's a two-column layout: a large stock photo on the left, and text + icon-grid + CTA button on the right.

### Component Tree

```
<section#gspb_row-id-gsbp-d281619>                    ← Outer full-width row
  <div.gspb_row__content>                             ← Constrained container
    <div#gspb_col-id-gsbp-f135a48>                    ← Column 12/12
      <div#gspb_row-id-gsbp-425d88c>                  ← Inner row
        <div#gspb_col-id-gsbp-028184b>                ← Left col (55% at >=1000px)
          <div#gspb_image-id-gsbp-7c27e75>            ← Main hero image
        <div#gspb_col-id-gsbp-deba916>                ← Right col (45% at >=1000px)
          <div#gspb_image-id-gsbp-f03f6e2>            ← Decorative badge (absolute, rotated)
          <div.wp-block-group>                         ← Inline flex group
            <div#gspb_image-id-gsbp-1e88121>          ← Leaf icon (28px)
            <span.gsbp-73d4613>                        ← Overhead label "Nuestra Filosofía"
          <h2#gspb_heading-id-gsbp-4656fc2>           ← Main heading
          <div#gspb_text-id-gsbp-2f34b6c>             ← Body text
          <div#gspb_container-id-gsbp-f10e825>        ← CSS Grid (2 cols)
            ┌─ <div#gspb_container-id-gsbp-7780c7d>   ← Grid item (1,1)
            │    ├─ iconbox#gspb-f098b3f (checkmark SVG)
            │    └─ <p#gspb_heading-id-gsbp-b69d217>  ← "Residuo Cero"
            ├─ <div#gspb_container-id-gsbp-814ade3>   ← Grid item (2,1)
            │    ├─ iconbox#gspb-afd9a98 (checkmark SVG)
            │    └─ <p#gspb_heading-id-gsbp-5a4bed0>  ← "Garantía Legal Certificada"
            ├─ <div#gspb_container-id-gsbp-7059d69>   ← Grid item (1,2)
            │    ├─ iconbox#gspb-a7a55a1 (checkmark SVG)
            │    └─ <p#gspb_heading-id-gsbp-4f30e34>  ← "Acción en 24/48h"
            └─ <div#gspb_container-id-gsbp-6b71524>   ← Grid item (2,2)
                 ├─ iconbox#gspb-6d54635 (checkmark SVG)
                 └─ <p#gspb_heading-id-gsbp-23f04f0>  ← "Recuperación de Activos"
          <div#gspb_container-id-gsbp-f9e8fa9>        ← CTA wrapper
            <a.gsbp-8bce4f6>                           ← Button → /quienes-somos/
```

---

## 2. Raw HTML (Complete Section — lines 664–753)

```html
<style>#gspb_row-id-gsbp-d281619{justify-content:space-between;margin-top:0px;margin-bottom:0px;display:flex;flex-wrap:wrap;}#gspb_row-id-gsbp-d281619 > .gspb_row__content{display:flex;justify-content:space-between;margin:0 auto;width:100%;flex-wrap:wrap;}.gspb_row{position:relative;}div[id^=gspb_col-id]{box-sizing:border-box;position:relative;}div[id^=gspb_col-id]{padding:var(--gs-row-column-padding,15px min(3vw,20px));}body.gspb-bodyfront #gspb_row-id-gsbp-d281619 > .gspb_row__content{width:var(--theme-container-width,1200px);}body.gspb-bodyfront #gspb_row-id-gsbp-d281619 > .gspb_row__content{max-width:var(--theme-normal-container-max-width,1200px);}#gspb_row-id-gsbp-d281619{padding-top:50px;padding-bottom:40px;}@media (max-width:689.98px){#gspb_row-id-gsbp-d281619{padding-top:10px;padding-bottom:20px;}}</style>
<section class="wp-block-greenshift-blocks-row alignfull gspb_row gspb_row-id-gsbp-d281619 block__row" id="gspb_row-id-gsbp-d281619"><div class="gspb_row__content"> <style>#gspb_col-id-gsbp-f135a48.gspb_row__col--12{width:100%;}@media (max-width:689.98px){#gspb_col-id-gsbp-f135a48.gspb_row__col--12{width:100%;}}</style>
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--12 gspb_col-id-gsbp-f135a48 block__row-column" id="gspb_col-id-gsbp-f135a48"><style>#gspb_row-id-gsbp-425d88c{justify-content:space-between;margin-top:0px;margin-bottom:0px;display:flex;flex-wrap:wrap;}#gspb_row-id-gsbp-425d88c > .gspb_row__content{display:flex;justify-content:space-between;margin:0 auto;width:100%;flex-wrap:wrap;}.gspb_row{position:relative;}div[id^=gspb_col-id]{box-sizing:border-box;position:relative;}div[id^=gspb_col-id]{padding:var(--gs-row-column-padding,15px min(3vw,20px));}body.gspb-bodyfront #gspb_row-id-gsbp-425d88c > .gspb_row__content{width:var(--theme-container-width,1200px);}body.gspb-bodyfront #gspb_row-id-gsbp-425d88c > .gspb_row__content{max-width:var(--theme-normal-container-max-width,1200px);}</style>
<div class="wp-block-greenshift-blocks-row gspb_row gspb_row-id-gsbp-425d88c block__row" id="gspb_row-id-gsbp-425d88c"><div class="gspb_row__content"> <style>#gspb_col-id-gsbp-028184b.gspb_row__col--6{width:50%;}@media (max-width:689.98px){#gspb_col-id-gsbp-028184b.gspb_row__col--6{width:100%;}}@media (min-width:1000px){body.gspb-bodyfront #gspb_col-id-gsbp-028184b.gspb_row__col--6{width:calc(55% - 0px - 0px)}}.gspb_row #gspb_col-id-gsbp-028184b.gspb_row__col--6{padding-top:0px;padding-right:20px;padding-bottom:0px;padding-left:0px;}body #gspb_col-id-gsbp-028184b.gspb_row__col--6{display:flex;flex-direction:column;justify-content:center;align-content:center;align-items:flex-start;}</style>
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--6 gspb_col-id-gsbp-028184b block__row-column" id="gspb_col-id-gsbp-028184b"><style>#gspb_image-id-gsbp-7c27e75 img{vertical-align:top;}#gspb_image-id-gsbp-7c27e75 img{display:inline-block;box-sizing:border-box;max-width:100%;height:auto;}#gspb_image-id-gsbp-7c27e75 img{transition-duration:0.8s;}#gspb_image-id-gsbp-7c27e75 img{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_image-id-gsbp-7c27e75 img{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}#gspb_image-id-gsbp-7c27e75 img.aos-animate,#gspb_image-id-gsbp-7c27e75 img[data-gs-aos]{opacity:1;transform:translateZ(0);}#gspb_image-id-gsbp-7c27e75 img{width:458px;}#gspb_image-id-gsbp-7c27e75,#gspb_image-id-gsbp-7c27e75 img{height:custom;}</style>
<div class="wp-block-greenshift-blocks-image gspb_image gspb_image-id-gsbp-7c27e75 block__image" id="gspb_image-id-gsbp-7c27e75"><img decoding="async" src="https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO-2.webp" data-src="" alt="Soluciones integrales de limpieza técnica Gestión de residuos en Barcelona." loading="lazy" width="458" data-aos="fade" data-aos-easing="ease" data-aos-duration="800"/></div>
</div>


<style>#gspb_col-id-gsbp-deba916.gspb_row__col--6{width:50%;}@media (max-width:689.98px){#gspb_col-id-gsbp-deba916.gspb_row__col--6{width:100%;}}@media (min-width:1000px){body.gspb-bodyfront #gspb_col-id-gsbp-deba916.gspb_row__col--6{width:calc(45% - 0px - 0px)}}.gspb_row #gspb_col-id-gsbp-deba916.gspb_row__col--6{padding-top:50px;}body.gspb-bodyfront #gspb_col-id-gsbp-deba916.gspb_row__col--6{position:relative;}body #gspb_col-id-gsbp-deba916.gspb_row__col--6{display:flex;flex-direction:column;row-gap:10px;}</style>
<div class="wp-block-greenshift-blocks-row-column gspb_row__col--6 gspb_col-id-gsbp-deba916 block__row-column" id="gspb_col-id-gsbp-deba916"><style>#gspb_image-id-gsbp-f03f6e2{text-align:right;}#gspb_image-id-gsbp-f03f6e2 img{vertical-align:top;}#gspb_image-id-gsbp-f03f6e2 img{display:inline-block;box-sizing:border-box;max-width:100%;height:auto;}#gspb_image-id-gsbp-f03f6e2 img{transition-duration:0.8s;}#gspb_image-id-gsbp-f03f6e2 img{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_image-id-gsbp-f03f6e2 img{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}#gspb_image-id-gsbp-f03f6e2 img.aos-animate,#gspb_image-id-gsbp-f03f6e2 img[data-gs-aos]{opacity:1;transform:translateZ(0);}#gspb_image-id-gsbp-f03f6e2 img{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),calc(max(50px,15%)),0));}body.gspb-bodyfront #gspb_image-id-gsbp-f03f6e2{position:absolute;top:0px;right:0px;}@media (max-width:689.98px){body.gspb-bodyfront #gspb_image-id-gsbp-f03f6e2{right:20px;}}#gspb_image-id-gsbp-f03f6e2 img.aos-animate,#gspb_image-id-gsbp-f03f6e2 img[data-gs-aos]{transition:all 0.5s cubic-bezier(0.42,0,0.58,1);transform:translateX(0px) translateY(0px) rotateZ(30deg);}#gspb_image-id-gsbp-f03f6e2 img{width:auto;}@media (max-width:999.98px){#gspb_image-id-gsbp-f03f6e2 img{width:auto;}}@media (max-width:689.98px){#gspb_image-id-gsbp-f03f6e2 img{width:auto;}}@media (max-width:689.98px){#gspb_image-id-gsbp-f03f6e2 img{width:auto;}}#gspb_image-id-gsbp-f03f6e2,#gspb_image-id-gsbp-f03f6e2 img{height:110px;}@media (max-width:689.98px){#gspb_image-id-gsbp-f03f6e2,#gspb_image-id-gsbp-f03f6e2 img{height:74px;}}</style>
<div class="wp-block-greenshift-blocks-image gspb_image gspb_image-id-gsbp-f03f6e2 block__image" id="gspb_image-id-gsbp-f03f6e2"><img loading="lazy" loading="lazy" decoding="async" src="https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO-_1_.webp" data-src="" alt="" loading="lazy" width="610" height="110" data-aos="fade-up-left" data-aos-easing="ease" data-aos-duration="800"/></div>



<div class="wp-block-group is-content-justification-left is-nowrap is-layout-flex wp-container-core-group-is-layout-04d78b61 wp-block-group-is-layout-flex" style="min-height:0px;margin-top:0;margin-bottom:0;padding-top:0;padding-right:0;padding-bottom:0;padding-left:0"><style>#gspb_image-id-gsbp-1e88121{text-align:left;}#gspb_image-id-gsbp-1e88121 img{object-fit:fill;}#gspb_image-id-gsbp-1e88121 img{vertical-align:top;}#gspb_image-id-gsbp-1e88121 img{display:inline-block;box-sizing:border-box;max-width:100%;height:auto;}#gspb_image-id-gsbp-1e88121{margin-bottom:0px;}#gspb_image-id-gsbp-1e88121 img{transition-duration:0.8s;}#gspb_image-id-gsbp-1e88121 img{transition-timing-function:cubic-bezier(0.6,-0.28,0.735,0.045);}#gspb_image-id-gsbp-1e88121 img{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform;}#gspb_image-id-gsbp-1e88121 img.aos-animate,#gspb_image-id-gsbp-1e88121 img[data-gs-aos]{opacity:1;transform:translateZ(0) scale(1);}#gspb_image-id-gsbp-1e88121 img{transform:var(--gs-root-animation-transform,scale(0.6));}#gspb_image-id-gsbp-1e88121 img{width:28px;}#gspb_image-id-gsbp-1e88121,#gspb_image-id-gsbp-1e88121 img{height:auto;}@media (max-width:999.98px){#gspb_image-id-gsbp-1e88121,#gspb_image-id-gsbp-1e88121 img{height:auto;}}@media (max-width:689.98px){#gspb_image-id-gsbp-1e88121,#gspb_image-id-gsbp-1e88121 img{height:auto;}}@media (max-width:689.98px){#gspb_image-id-gsbp-1e88121,#gspb_image-id-gsbp-1e88121 img{height:auto;}}</style>
<div class="wp-block-greenshift-blocks-image gspb_image gspb_image-id-gsbp-1e88121" id="gspb_image-id-gsbp-1e88121"><img loading="lazy" loading="lazy" decoding="async" src="https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO.webp" data-src="" alt="" loading="lazy" width="28" height="1080" data-aos="zoom-in" data-aos-easing="ease-in-back" data-aos-duration="800"/></div>


<style>.gsbp-73d4613{color:var(--wp--preset--color--palette-color-3,var(--theme-palette-color-3,#65C132));margin-top:0px;margin-bottom:0px;margin-left:0px;margin-right:0px;padding-top:0px;padding-bottom:0px;padding-left:0px;padding-right:0px;}@media (max-width:689.98px){.gsbp-73d4613{font-size:14px;}}.gsbp-73d4613{transition-duration:0.8s;}.gsbp-73d4613{transition-timing-function:cubic-bezier(0.25,0.46,0.45,0.94);}.gsbp-73d4613{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}.gsbp-73d4613.aos-animate,.gsbp-73d4613[data-gs-aos]{opacity:1;transform:translateZ(0);}.gsbp-73d4613{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}</style>
<span data-aos="fade-left" data-aos-easing="ease-out-cubic" data-aos-duration="800" class="overhead-span gsbp-73d4613">Nuestra Filosofía</span>
</div>


<style>#gspb_heading-id-gsbp-4656fc2{text-transform:uppercase;}#gspb_heading-id-gsbp-4656fc2{color:var(--wp--preset--color--palette-color-7,var(--theme-palette-color-7,#00312D));}#gspb_heading-id-gsbp-4656fc2{margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;}</style>
<h2 id="gspb_heading-id-gsbp-4656fc2" class="block__heading gspb_heading gspb_heading-id-gsbp-4656fc2 "><strong><strong>Más que una limpieza, una empresa de gestión ambiental en BARCELONA</strong></strong></h2>


<style>.gspb_text-id-gsbp-2f34b6c{color:var(--wp--preset--color--palette-color-7,var(--theme-palette-color-7,#00312D));}.gspb_text-id-gsbp-2f34b6c{padding-top:10px!important;padding-bottom:20px!important;}</style>
<div id="gspb_text-id-gsbp-2f34b6c" class="gspb_text gspb_text-id-gsbp-2f34b6c block__text">En Ecociclo entendemos que una empresa no necesita solo retirar residuos. Necesita una solución eficaz, bien organizada y capaz de resolver el problema de principio a fin. Por eso ofrecemos un servicio completo de <strong>gestión de residuos en Barcelona </strong>para empresas que buscan rapidez, orden y seguridad en cada intervención.</div>


<style>.gspb_container-id-gsbp-f10e825{flex-direction:column;box-sizing:border-box;}#gspb_container-id-gsbp-f10e825.gspb_container > p:last-of-type{margin-bottom:0}#gspb_container-id-gsbp-f10e825.gspb_container{position:relative;}#gspb_container-id-gsbp-f10e825.gspb_container{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));row-gap:20px;column-gap:35px;}@media (max-width:689.98px){#gspb_container-id-gsbp-f10e825.gspb_container{grid-template-columns:repeat(1,minmax(0,1fr));}}#gspb_container-id-gsbp-f10e825.gspb_container{margin-bottom:0px;}#gspb_container-id-gsbp-f10e825.gspb_container{box-sizing:border-box;}</style>
<div class="wp-block-greenshift-blocks-container gspb_container gspb_container-gsbp-f10e825 block__container" id="gspb_container-id-gsbp-f10e825">
  <!-- GRID ITEM 1: Residuo Cero -->
  <style>.gspb_container-id-gsbp-7780c7d{flex-direction:column;box-sizing:border-box;}#gspb_container-id-gsbp-7780c7d.gspb_container > p:last-of-type{margin-bottom:0}#gspb_container-id-gsbp-7780c7d.gspb_container{position:relative;}body.gspb-bodyfront #gspb_container-id-gsbp-7780c7d.gspb_container{grid-column-start:1;grid-column-end:2;grid-row-start:1;grid-row-end:2;}@media (max-width:689.98px){body.gspb-bodyfront #gspb_container-id-gsbp-7780c7d.gspb_container{grid-column-start:1;grid-column-end:2;grid-row-start:1;grid-row-end:2;}}#gspb_container-id-gsbp-7780c7d.gspb_container{display:flex;flex-direction:row;}#gspb_container-id-gsbp-7780c7d.gspb_container{margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;}#gspb_container-id-gsbp-7780c7d.gspb_container{box-sizing:border-box;}</style>
  <div class="wp-block-greenshift-blocks-container gspb_container gspb_container-gsbp-7780c7d block__container" id="gspb_container-id-gsbp-7780c7d">
    <div class="wp-block-group block__group is-content-justification-left is-nowrap is-layout-flex wp-container-core-group-is-layout-1afc5d38 wp-block-group-is-layout-flex" style="padding-right:0;padding-left:0">
      <style>#gspb_iconBox-id-gsbp-f098b3f svg{width:72px;}#gspb_iconBox-id-gsbp-f098b3f{justify-content:center;display:flex;}#gspb_iconBox-id-gsbp-f098b3f svg{height:30px!important;width:30px!important;min-width:30px!important;}#gspb_iconBox-id-gsbp-f098b3f svg,#gspb_iconBox-id-gsbp-f098b3f svg path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-f098b3f svg{margin:0px !important;}#gspb_iconBox-id-gsbp-f098b3f svg:hover,#gspb_iconBox-id-gsbp-f098b3f svg:hover path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-f098b3f .gspb_iconBox__wrapper{transition-duration:0.8s;}#gspb_iconBox-id-gsbp-f098b3f .gspb_iconBox__wrapper{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_iconBox-id-gsbp-f098b3f .gspb_iconBox__wrapper{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform;}#gspb_iconBox-id-gsbp-f098b3f .gspb_iconBox__wrapper.aos-animate,#gspb_iconBox-id-gsbp-f098b3f .gspb_iconBox__wrapper[data-gs-aos]{opacity:1;transform:translateZ(0) scale(1);}#gspb_iconBox-id-gsbp-f098b3f .gspb_iconBox__wrapper{transform:var(--gs-root-animation-transform,scale(0.6));}</style>
      <div class="wp-block-greenshift-blocks-iconbox gspb_iconBox gspb_iconBox-id-gsbp-f098b3f block__iconbox" id="gspb_iconBox-id-gsbp-f098b3f"><div class="gspb_iconBox__wrapper" style="display:inline-flex" data-aos="zoom-in" data-aos-easing="ease" data-aos-duration="800"><svg class="" style="display:inline-block;vertical-align:middle" width="72" height="72" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path style="fill:#565D66" d="M1008 512c0 273.934-222.066 496-496 496s-496-222.066-496-496 222.066-496 496-496 496 222.066 496 496zM454.628 774.628l368-368c12.496-12.496 12.496-32.758 0-45.254l-45.254-45.254c-12.496-12.498-32.758-12.498-45.256 0l-300.118 300.116-140.118-140.118c-12.496-12.496-32.758-12.496-45.256 0l-45.254 45.254c-12.496 12.496-12.496 32.758 0 45.254l208 208c12.498 12.498 32.758 12.498 45.256 0.002z"></path></svg></div></div>

      <style>#gspb_heading-id-gsbp-b69d217{transition-duration:0.8s;}#gspb_heading-id-gsbp-b69d217{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_heading-id-gsbp-b69d217{transition-delay:0s;}#gspb_heading-id-gsbp-b69d217.aos-animate,#gspb_heading-id-gsbp-b69d217[data-gs-aos]{transition-delay:0.1s;--gs-root-animation-delay:0.1s;}#gspb_heading-id-gsbp-b69d217{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}#gspb_heading-id-gsbp-b69d217.aos-animate,#gspb_heading-id-gsbp-b69d217[data-gs-aos]{opacity:1;transform:translateZ(0);}#gspb_heading-id-gsbp-b69d217{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}#gspb_heading-id-gsbp-b69d217,#gspb_heading-id-gsbp-b69d217 .gsap-g-line{text-align:left!important;}#gspb_heading-id-gsbp-b69d217{font-weight:bold!important;}#gspb_heading-id-gsbp-b69d217{color:var(--wp--preset--color--palette-color-7,var(--theme-palette-color-7,#00312D));}#gspb_heading-id-gsbp-b69d217{margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;}</style>
      <p id="gspb_heading-id-gsbp-b69d217" class="block__heading gspb_heading gspb_heading-id-gsbp-b69d217 " data-aos="fade-left" data-aos-delay="100" data-aos-easing="ease" data-aos-duration="800">Residuo Cero</p>
    </div>
  </div>

  <!-- GRID ITEM 2: Garantía Legal Certificada -->
  <style>.gspb_container-id-gsbp-814ade3{flex-direction:column;box-sizing:border-box;}#gspb_container-id-gsbp-814ade3.gspb_container > p:last-of-type{margin-bottom:0}#gspb_container-id-gsbp-814ade3.gspb_container{position:relative;}body.gspb-bodyfront #gspb_container-id-gsbp-814ade3.gspb_container{grid-column-start:2;grid-column-end:3;grid-row-start:1;grid-row-end:2;}@media (max-width:689.98px){body.gspb-bodyfront #gspb_container-id-gsbp-814ade3.gspb_container{grid-column-start:1;grid-column-end:2;grid-row-start:2;grid-row-end:3;}}#gspb_container-id-gsbp-814ade3.gspb_container{box-sizing:border-box;}</style>
  <div class="wp-block-greenshift-blocks-container gspb_container gspb_container-gsbp-814ade3 block__container" id="gspb_container-id-gsbp-814ade3">
    <div class="wp-block-group block__group is-content-justification-left is-nowrap is-layout-flex wp-container-core-group-is-layout-1afc5d38 wp-block-group-is-layout-flex" style="padding-right:0;padding-left:0">
      <style>#gspb_iconBox-id-gsbp-afd9a98 svg{width:72px;}#gspb_iconBox-id-gsbp-afd9a98{justify-content:center;display:flex;}#gspb_iconBox-id-gsbp-afd9a98 svg{height:30px!important;width:30px!important;min-width:30px!important;}#gspb_iconBox-id-gsbp-afd9a98 svg,#gspb_iconBox-id-gsbp-afd9a98 svg path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-afd9a98 svg{margin:0px !important;}#gspb_iconBox-id-gsbp-afd9a98 svg:hover,#gspb_iconBox-id-gsbp-afd9a98 svg:hover path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper{transition-duration:0.8s;}#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper{transition-delay:0s;}#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper.aos-animate,#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper[data-gs-aos]{transition-delay:0.2s;--gs-root-animation-delay:0.2s;}#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform;}#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper.aos-animate,#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper[data-gs-aos]{opacity:1;transform:translateZ(0) scale(1);}#gspb_iconBox-id-gsbp-afd9a98 .gspb_iconBox__wrapper{transform:var(--gs-root-animation-transform,scale(0.6));}</style>
      <div class="wp-block-greenshift-blocks-iconbox gspb_iconBox gspb_iconBox-id-gsbp-afd9a98 block__iconbox" id="gspb_iconBox-id-gsbp-afd9a98"><div class="gspb_iconBox__wrapper" style="display:inline-flex" data-aos="zoom-in" data-aos-delay="200" data-aos-easing="ease" data-aos-duration="800"><svg class="" style="display:inline-block;vertical-align:middle" width="72" height="72" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path style="fill:#565D66" d="M1008 512c0 273.934-222.066 496-496 496s-496-222.066-496-496 222.066-496 496-496 496 222.066 496 496zM454.628 774.628l368-368c12.496-12.496 12.496-32.758 0-45.254l-45.254-45.254c-12.496-12.498-32.758-12.498-45.256 0l-300.118 300.116-140.118-140.118c-12.496-12.496-32.758-12.496-45.256 0l-45.254 45.254c-12.496 12.496-12.496 32.758 0 45.254l208 208c12.498 12.498 32.758 12.498 45.256 0.002z"></path></svg></div></div>

      <style>#gspb_heading-id-gsbp-5a4bed0{transition-duration:0.8s;}#gspb_heading-id-gsbp-5a4bed0{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_heading-id-gsbp-5a4bed0{transition-delay:0s;}#gspb_heading-id-gsbp-5a4bed0.aos-animate,#gspb_heading-id-gsbp-5a4bed0[data-gs-aos]{transition-delay:0.3s;--gs-root-animation-delay:0.3s;}#gspb_heading-id-gsbp-5a4bed0{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}#gspb_heading-id-gsbp-5a4bed0.aos-animate,#gspb_heading-id-gsbp-5a4bed0[data-gs-aos]{opacity:1;transform:translateZ(0);}#gspb_heading-id-gsbp-5a4bed0{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}#gspb_heading-id-gsbp-5a4bed0,#gspb_heading-id-gsbp-5a4bed0 .gsap-g-line{text-align:left!important;}#gspb_heading-id-gsbp-5a4bed0{font-weight:bold!important;}#gspb_heading-id-gsbp-5a4bed0{color:var(--wp--preset--color--palette-color-7,var(--theme-palette-color-7,#00312D));}#gspb_heading-id-gsbp-5a4bed0{margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;}</style>
      <p id="gspb_heading-id-gsbp-5a4bed0" class="block__heading gspb_heading gspb_heading-id-gsbp-5a4bed0 " data-aos="fade-left" data-aos-delay="300" data-aos-easing="ease" data-aos-duration="800">Garantía Legal Certificada</p>
    </div>
  </div>

  <!-- GRID ITEM 3: Acción en 24/48h -->
  <style>.gspb_container-id-gsbp-7059d69{flex-direction:column;box-sizing:border-box;}#gspb_container-id-gsbp-7059d69.gspb_container > p:last-of-type{margin-bottom:0}#gspb_container-id-gsbp-7059d69.gspb_container{position:relative;}body.gspb-bodyfront #gspb_container-id-gsbp-7059d69.gspb_container{grid-column-start:1;grid-column-end:2;grid-row-start:2;grid-row-end:3;}@media (max-width:689.98px){body.gspb-bodyfront #gspb_container-id-gsbp-7059d69.gspb_container{grid-column-start:1;grid-column-end:2;grid-row-start:3;grid-row-end:4;}}#gspb_container-id-gsbp-7059d69.gspb_container{box-sizing:border-box;}</style>
  <div class="wp-block-greenshift-blocks-container gspb_container gspb_container-gsbp-7059d69 block__container" id="gspb_container-id-gsbp-7059d69">
    <div class="wp-block-group block__group is-content-justification-left is-nowrap is-layout-flex wp-container-core-group-is-layout-1afc5d38 wp-block-group-is-layout-flex" style="padding-right:0;padding-left:0">
      <style>#gspb_iconBox-id-gsbp-a7a55a1 svg{width:72px;}#gspb_iconBox-id-gsbp-a7a55a1{justify-content:center;display:flex;}#gspb_iconBox-id-gsbp-a7a55a1 svg{height:30px!important;width:30px!important;min-width:30px!important;}#gspb_iconBox-id-gsbp-a7a55a1 svg,#gspb_iconBox-id-gsbp-a7a55a1 svg path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-a7a55a1 svg{margin:0px !important;}#gspb_iconBox-id-gsbp-a7a55a1 svg:hover,#gspb_iconBox-id-gsbp-a7a55a1 svg:hover path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper{transition-duration:0.8s;}#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper{transition-delay:0s;}#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper.aos-animate,#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper[data-gs-aos]{transition-delay:0.1s;--gs-root-animation-delay:0.1s;}#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform;}#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper.aos-animate,#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper[data-gs-aos]{opacity:1;transform:translateZ(0) scale(1);}#gspb_iconBox-id-gsbp-a7a55a1 .gspb_iconBox__wrapper{transform:var(--gs-root-animation-transform,scale(0.6));}</style>
      <div class="wp-block-greenshift-blocks-iconbox gspb_iconBox gspb_iconBox-id-gsbp-a7a55a1 block__iconbox" id="gspb_iconBox-id-gsbp-a7a55a1"><div class="gspb_iconBox__wrapper" style="display:inline-flex" data-aos="zoom-in" data-aos-delay="100" data-aos-easing="ease" data-aos-duration="800"><svg class="" style="display:inline-block;vertical-align:middle" width="72" height="72" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path style="fill:#565D66" d="M1008 512c0 273.934-222.066 496-496 496s-496-222.066-496-496 222.066-496 496-496 496 222.066 496 496zM454.628 774.628l368-368c12.496-12.496 12.496-32.758 0-45.254l-45.254-45.254c-12.496-12.498-32.758-12.498-45.256 0l-300.118 300.116-140.118-140.118c-12.496-12.496-32.758-12.496-45.256 0l-45.254 45.254c-12.496 12.496-12.496 32.758 0 45.254l208 208c12.498 12.498 32.758 12.498 45.256 0.002z"></path></svg></div></div>

      <style>#gspb_heading-id-gsbp-4f30e34{transition-duration:0.8s;}#gspb_heading-id-gsbp-4f30e34{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_heading-id-gsbp-4f30e34{transition-delay:0s;}#gspb_heading-id-gsbp-4f30e34.aos-animate,#gspb_heading-id-gsbp-4f30e34[data-gs-aos]{transition-delay:0.2s;--gs-root-animation-delay:0.2s;}#gspb_heading-id-gsbp-4f30e34{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}#gspb_heading-id-gsbp-4f30e34.aos-animate,#gspb_heading-id-gsbp-4f30e34[data-gs-aos]{opacity:1;transform:translateZ(0);}#gspb_heading-id-gsbp-4f30e34{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}#gspb_heading-id-gsbp-4f30e34,#gspb_heading-id-gsbp-4f30e34 .gsap-g-line{text-align:left!important;}#gspb_heading-id-gsbp-4f30e34{font-weight:bold!important;}#gspb_heading-id-gsbp-4f30e34{color:var(--wp--preset--color--palette-color-7,var(--theme-palette-color-7,#00312D));}#gspb_heading-id-gsbp-4f30e34{margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;}</style>
      <p id="gspb_heading-id-gsbp-4f30e34" class="block__heading gspb_heading gspb_heading-id-gsbp-4f30e34 " data-aos="fade-left" data-aos-delay="200" data-aos-easing="ease" data-aos-duration="800">Acción en 24/48h</p>
    </div>
  </div>

  <!-- GRID ITEM 4: Recuperación de Activos -->
  <style>.gspb_container-id-gsbp-6b71524{flex-direction:column;box-sizing:border-box;}#gspb_container-id-gsbp-6b71524.gspb_container > p:last-of-type{margin-bottom:0}#gspb_container-id-gsbp-6b71524.gspb_container{position:relative;}body.gspb-bodyfront #gspb_container-id-gsbp-6b71524.gspb_container{grid-column-start:2;grid-column-end:3;grid-row-start:2;grid-row-end:3;}@media (max-width:689.98px){body.gspb-bodyfront #gspb_container-id-gsbp-6b71524.gspb_container{grid-column-start:1;grid-column-end:2;grid-row-start:4;grid-row-end:5;}}#gspb_container-id-gsbp-6b71524.gspb_container{box-sizing:border-box;}</style>
  <div class="wp-block-greenshift-blocks-container gspb_container gspb_container-gsbp-6b71524 block__container" id="gspb_container-id-gsbp-6b71524">
    <div class="wp-block-group block__group is-content-justification-left is-nowrap is-layout-flex wp-container-core-group-is-layout-1afc5d38 wp-block-group-is-layout-flex" style="padding-right:0;padding-left:0">
      <style>#gspb_iconBox-id-gsbp-6d54635 svg{width:72px;}#gspb_iconBox-id-gsbp-6d54635{justify-content:center;display:flex;}#gspb_iconBox-id-gsbp-6d54635 svg{height:30px!important;width:30px!important;min-width:30px!important;}#gspb_iconBox-id-gsbp-6d54635 svg,#gspb_iconBox-id-gsbp-6d54635 svg path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-6d54635 svg{margin:0px !important;}#gspb_iconBox-id-gsbp-6d54635 svg:hover,#gspb_iconBox-id-gsbp-6d54635 svg:hover path{fill:var(--theme-link-initial-color,currentColor) !important;}#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper{transition-duration:0.8s;}#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper{transition-delay:0s;}#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper.aos-animate,#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper[data-gs-aos]{transition-delay:0.3s;--gs-root-animation-delay:0.3s;}#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform;}#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper.aos-animate,#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper[data-gs-aos]{opacity:1;transform:translateZ(0) scale(1);}#gspb_iconBox-id-gsbp-6d54635 .gspb_iconBox__wrapper{transform:var(--gs-root-animation-transform,scale(0.6));}</style>
      <div class="wp-block-greenshift-blocks-iconbox gspb_iconBox gspb_iconBox-id-gsbp-6d54635 block__iconbox" id="gspb_iconBox-id-gsbp-6d54635"><div class="gspb_iconBox__wrapper" style="display:inline-flex" data-aos="zoom-in" data-aos-delay="300" data-aos-easing="ease" data-aos-duration="800"><svg class="" style="display:inline-block;vertical-align:middle" width="72" height="72" viewBox="0 0 1024 1024" xmlns="http://www.w3.org/2000/svg"><path style="fill:#565D66" d="M1008 512c0 273.934-222.066 496-496 496s-496-222.066-496-496 222.066-496 496-496 496 222.066 496 496zM454.628 774.628l368-368c12.496-12.496 12.496-32.758 0-45.254l-45.254-45.254c-12.496-12.498-32.758-12.498-45.256 0l-300.118 300.116-140.118-140.118c-12.496-12.496-32.758-12.496-45.256 0l-45.254 45.254c-12.496 12.496-12.496 32.758 0 45.254l208 208c12.498 12.498 32.758 12.498 45.256 0.002z"></path></svg></div></div>

      <style>#gspb_heading-id-gsbp-23f04f0{transition-duration:0.8s;}#gspb_heading-id-gsbp-23f04f0{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}#gspb_heading-id-gsbp-23f04f0{transition-delay:0s;}#gspb_heading-id-gsbp-23f04f0.aos-animate,#gspb_heading-id-gsbp-23f04f0[data-gs-aos]{transition-delay:0.4s;--gs-root-animation-delay:0.4s;}#gspb_heading-id-gsbp-23f04f0{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}#gspb_heading-id-gsbp-23f04f0.aos-animate,#gspb_heading-id-gsbp-23f04f0[data-gs-aos]{opacity:1;transform:translateZ(0);}#gspb_heading-id-gsbp-23f04f0{transform:var(--gs-root-animation-transform,translate3d(calc(max(50px,15%)),0,0));}#gspb_heading-id-gsbp-23f04f0,#gspb_heading-id-gsbp-23f04f0 .gsap-g-line{text-align:left!important;}#gspb_heading-id-gsbp-23f04f0{font-weight:bold!important;}#gspb_heading-id-gsbp-23f04f0{color:var(--wp--preset--color--palette-color-7,var(--theme-palette-color-7,#00312D));}#gspb_heading-id-gsbp-23f04f0{margin-top:0px;margin-right:0px;margin-bottom:0px;margin-left:0px;padding-top:0px;padding-right:0px;padding-bottom:0px;padding-left:0px;}</style>
      <p id="gspb_heading-id-gsbp-23f04f0" class="block__heading gspb_heading gspb_heading-id-gsbp-23f04f0 " data-aos="fade-left" data-aos-delay="400" data-aos-easing="ease" data-aos-duration="800">Recuperación de Activos</p>
    </div>
  </div>
</div>


<style>.gspb_container-id-gsbp-f9e8fa9{flex-direction:column;box-sizing:border-box;}#gspb_container-id-gsbp-f9e8fa9.gspb_container > p:last-of-type{margin-bottom:0}#gspb_container-id-gsbp-f9e8fa9.gspb_container{position:relative;}#gspb_container-id-gsbp-f9e8fa9.gspb_container{padding-top:20px;}#gspb_container-id-gsbp-f9e8fa9.gspb_container{box-sizing:border-box;}</style>
<div class="wp-block-greenshift-blocks-container gspb_container gspb_container-gsbp-f9e8fa9 block__container" id="gspb_container-id-gsbp-f9e8fa9"><style>.gsbp-8bce4f6{border-top-left-radius:30px;border-bottom-left-radius:30px;border-top-right-radius:30px;border-bottom-right-radius:30px;align-self:start;padding-top:10px;padding-bottom:10px;padding-left:25px;padding-right:25px;display:inline-block;background-color:var(--wp--preset--color--palette-color-3,var(--theme-palette-color-3,#65C132));border-radius:15px;border-style:solid;border-width:0px;border-color:#1a1a1a;box-shadow:0 1px 3px 0 #00000005;color:#ffffff;transition:0.25s;text-decoration:none;}.gsbp-8bce4f6:hover{box-shadow:0 8px 15px 0 #00000040;transform:translateY(-3px);color:#ffffff;background-color:var(--wp--preset--color--palette-color-2,var(--theme-palette-color-2,#45891E));}.gsbp-8bce4f6:focus,.gsbp-8bce4f6:active{box-shadow:0 1px 0 0 #00000040;transform:translateY(3px);}.gsbp-8bce4f6{transition-duration:0.8s;}.gsbp-8bce4f6{transition-timing-function:var(--gs-root-animation-easing,cubic-bezier(0.42,0,0.58,1));}.gsbp-8bce4f6{opacity:var(--gs-root-animation-opacity,0);transition-property:opacity,transform,filter;}.gsbp-8bce4f6.aos-animate,.gsbp-8bce4f6[data-gs-aos]{opacity:1;transform:translateZ(0);}.gsbp-8bce4f6{transform:var(--gs-root-animation-transform,translate3d(0,calc(max(50px,15%)),0));}</style>
<a data-aos="fade-up" data-aos-easing="ease" data-aos-duration="800" class="gs-parent-hover gs_button  gsbp-8bce4f6" href="https://ecociclo.es/quienes-somos/" data-type="button-component"><strong>Conoce más sobre nosotros</strong></a>
</div>
</div>
 </div></div>
</div>
 </div></section>
```

---

## 3. Image URLs

All images referenced in the Filosofía section:

| # | URL | Usage | Dimensions |
|---|-----|-------|------------|
| 1 | `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO-2.webp` | Main left-side hero image | `width="458"` |
| 2 | `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO-_1_.webp` | Decorative badge (absolute positioned, rotated on reveal) | `width="610" height="110"` (CSS: 110px on desktop, 74px mobile) |
| 3 | `https://ecociclo.es/wp-content/uploads/2026/03/ECOCICLO.webp` | Leaf icon next to "Nuestra Filosofía" | `width="28" height="1080"` (CSS: 28px wide, auto height) |

**All `alt` attributes:**
- Main image: `"Soluciones integrales de limpieza técnica Gestión de residuos en Barcelona."`
- Badge image: `""` (empty)
- Leaf icon: `""` (empty)

**All `loading` attributes:** All three images use `loading="lazy"`.

**Image format:** All images are `.webp`.

---

## 4. CSS Properties & Variables Summary

### 4.1 Greenshift-Specific CSS Variables

| Variable | Default Value | Used In |
|----------|--------------|---------|
| `--gs-row-column-padding` | `15px min(3vw, 20px)` | All column padding |
| `--gs-root-animation-easing` | `cubic-bezier(0.42, 0, 0.58, 1)` | Most animation transitions |
| `--gs-root-animation-opacity` | `0` | Initial opacity (hidden) for all animated elements |
| `--gs-root-animation-transform` | varies per element | Initial transform (hidden state) |
| `--gs-root-animation-delay` | varies per element | Staggered delay on reveal |

### 4.2 Theme CSS Variables

| Variable | Default Fallback | Used In |
|----------|-----------------|---------|
| `--theme-container-width` | `1200px` | Row content width |
| `--theme-normal-container-max-width` | `1200px` | Row content max-width |
| `--theme-link-initial-color` | `currentColor` | Icon fill |
| `--theme-palette-color-1` | `#36611C` | (not in this section directly) |
| `--theme-palette-color-2` | `#45891E` | Button hover bg |
| `--theme-palette-color-3` | `#65C132` (green) | Overhead text, button bg, decorative elements |
| `--theme-palette-color-4` | `#192a3d` | (dark blue, used in adjacent sections) |
| `--theme-palette-color-5` | `#EAFDE7` | (light green, used in hover states of slider cards) |
| `--theme-palette-color-6` | `#f2f5f7` | (light gray, not in this section) |
| `--theme-palette-color-7` | `#00312D` (dark green) | Headings, text color |
| `--theme-palette-color-8` | `#ffffff` | (white, used in slider cards section) |

### 4.3 WordPress Preset Variables (via `var(--wp--preset--color--palette-color-N, ...)`)

The Greenshift blocks reference WordPress palette colors through the theme bridge:
- `var(--wp--preset--color--palette-color-3, var(--theme-palette-color-3, #65C132))` — primary green
- `var(--wp--preset--color--palette-color-7, var(--theme-palette-color-7, #00312D))` — dark green (text)
- `var(--wp--preset--color--palette-color-2, var(--theme-palette-color-2, #45891E))` — darker green (button hover)
- `var(--wp--preset--color--palette-color-8, var(--theme-palette-color-8, #ffffff))` — white

### 4.4 Hardcoded Colors

| Color | Usage |
|-------|-------|
| `#ffffff` | Button text, button text on hover |
| `#565D66` | SVG icon fill (checkmark path) |
| `#1a1a1a` | Button border color (border-width: 0 anyway) |
| `#00000005` | Button box-shadow |
| `#00000040` | Button hover/focus box-shadow |
| `#65c23257` | Slider nav button background (not in Filosofía section) |

---

## 5. Animation Patterns (AOS + Greenshift)

### 5.1 How Greenshift Animations Work

All animated elements follow this pattern:

1. **Hidden state:** `opacity: var(--gs-root-animation-opacity, 0)` + `transform: var(--gs-root-animation-transform, ...)`
2. **Visible state (triggered by AOS):** When `.aos-animate` or `[data-gs-aos]` is added, `opacity: 1` and `transform: translateZ(0)` or similar reset.
3. **Transition:** `transition-duration: 0.8s` with a specific easing curve.

### 5.2 AOS Data Attributes Used

All elements use `data-aos-duration="800"`. The easing and animation type vary:

| Element | AOS Animation | Easing | Delay |
|---------|--------------|--------|-------|
| Main image | `fade` | `ease` | — |
| Badge image | `fade-up-left` | `ease` | — |
| Leaf icon | `zoom-in` | `ease-in-back` | — |
| "Nuestra Filosofía" span | `fade-left` | `ease-out-cubic` | — |
| "Residuo Cero" | `fade-left` | `ease` | `100` |
| "Garantía Legal Certificada" | `fade-left` | `ease` | `300` |
| "Acción en 24/48h" | `fade-left` | `ease` | `200` |
| "Recuperación de Activos" | `fade-left` | `ease` | `400` |
| Checkmark icons (×4) | `zoom-in` | `ease` | 0, 100, 200, 300 |
| CTA Button | `fade-up` | `ease` | — |

### 5.3 Easing Functions Used

| Type | Cubic Bezier | Where |
|------|-------------|-------|
| Default GS | `cubic-bezier(0.42, 0, 0.58, 1)` | Most elements via `--gs-root-animation-easing` |
| Leaf icon | `cubic-bezier(0.6, -0.28, 0.735, 0.045)` | `#gspb_image-id-gsbp-1e88121` — aggressive back-ease-in |
| Overhead text | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | `.gsbp-73d4613` |

### 5.4 Staggered Reveal Timing (Grid Feature List)

The four feature items use staggered `data-aos-delay`:
- Item 1: `0.1s`
- Item 2: `0.3s`
- Item 3: `0.2s`
- Item 4: `0.4s`

Wait — that's odd ordering. Let me re-check: the grid items are in this order in the DOM:

| Grid Position | Item | Delay |
|--------------|------|-------|
| col 1, row 1 | Residuo Cero | 100ms |
| col 2, row 1 | Garantía Legal Certificada | 300ms |
| col 1, row 2 | Acción en 24/48h | 200ms |
| col 2, row 2 | Recuperación de Activos | 400ms |

The timing seems meant to create a diagonal reveal: top-left (100ms), bottom-left (200ms), top-right (300ms), bottom-right (400ms).

### 5.5 Special Animation: Rotating Badge

The decorative badge (`#gspb_image-id-gsbp-f03f6e2`) has a unique reveal animation:
```css
/* Hidden state */
transform: translate3d(calc(max(50px, 15%)), calc(max(50px, 15%)), 0);

/* Visible state */
transform: translateX(0px) translateY(0px) rotateZ(30deg);
transition: all 0.5s cubic-bezier(0.42, 0, 0.58, 1);
```
It slides in from bottom-right and settles at a 30° rotation.

---

## 6. Responsive Breakpoints

| Breakpoint | Media Query | Effect on Filosofía Section |
|------------|-------------|----------------------------|
| Desktop (≥1000px) | `@media (min-width: 1000px)` | Columns become 55%/45% split |
| Tablet (<1000px) | default | Columns revert to 50%/50% base |
| Mobile (<690px) | `@media (max-width: 689.98px)` | Stack to 100% width, reduced padding (10px top, 20px bottom), font-size 14px on overhead, grid becomes single column, badge 74px height |

---

## 7. Greenshift Block Types Used

| Block Type | CSS Class Pattern | Count in Section |
|------------|------------------|------------------|
| Row | `gspb_row gspb_row-id-gsbp-*` | 2 (`d281619`, `425d88c`) |
| Row Column | `gspb_row__col--N gspb_col-id-gsbp-*` | 3 (`f135a48`, `028184b`, `deba916`) |
| Image | `gspb_image gspb_image-id-gsbp-*` | 3 (`7c27e75`, `f03f6e2`, `1e88121`) |
| Heading | `gspb_heading gspb_heading-id-gsbp-*` | 6 (`4656fc2`, `b69d217`, `5a4bed0`, `4f30e34`, `23f04f0`, `7092ff2`) |
| Text | `gspb_text gspb_text-id-gsbp-*` | 1 (`2f34b6c`) |
| Container | `gspb_container gspb_container-gsbp-*` | 7 (`f10e825`, `7780c7d`, `814ade3`, `7059d69`, `6b71524`, `f9e8fa9`, plus nested variants) |
| IconBox | `gspb_iconBox gspb_iconBox-id-gsbp-*` | 4 (`f098b3f`, `afd9a98`, `a7a55a1`, `6d54635`) |
| Custom class span | `.gsbp-*` | 2 (`73d4613`, `8bce4f6`) |

### 7.1 Naming Convention

GS block IDs follow the pattern `gsbp-` + 7-character hash:
- `d281619`, `f135a48`, `425d88c`, `028184b`, `7c27e75`, `deba916`, `f03f6e2`, `1e88121`, `73d4613`, `4656fc2`, `2f34b6c`, `f10e825`, `7780c7d`, `f098b3f`, `b69d217`, `814ade3`, `afd9a98`, `5a4bed0`, `7059d69`, `a7a55a1`, `4f30e34`, `6b71524`, `6d54635`, `23f04f0`, `f9e8fa9`, `8bce4f6`

### 7.2 Custom CSS Classes

| Class | Type | Purpose |
|-------|------|---------|
| `.gsbp-73d4613` | Custom span class | "Nuestra Filosofía" overhead label — green color, fade-left animation |
| `.gsbp-8bce4f6` | Custom button class | CTA button with hover lift effect, green background |
| `.overhead-span` | Utility class | Shared class (also used in other sections like `.gsbp-b9ee22d`) |

---

## 8. Structural Observations

1. **Every Greenshift element has its own `<style>` block** injected directly before the element in the HTML. This is Greenshift's inline-styles approach — styles are NOT in a global stylesheet but in `<style>` tags within the post content.

2. **`div[id^=gspb_col-id]` selectors** are duplicated in every style block. This means `box-sizing: border-box`, `position: relative`, and padding are re-declared for every row's column styles.

3. **Double `<strong>` nesting**: Line 689 has `<strong><strong>...</strong></strong>` — likely a WordPress editor artifact.

4. **Duplicate `loading="lazy"` attributes**: Some `<img>` tags have `loading="lazy"` twice (e.g., the badge image and the leaf icon).

5. **Hardcoded heights**: The badge uses `height:custom` in one rule and `height:110px` in another — the `110px` rule takes precedence on desktop.

6. **No `data-src` usage**: All images have `data-src=""` (empty), meaning Greenshift's lazy-loading attribute is configured but the actual `src` is used directly.

7. **Section has NO background**: Unlike many other sections on the page (which use `gspb_backgroundOverlay`), the Filosofía section has a plain background.

8. **CSS Grid for feature list**: The 2×2 grid of feature items (Residuo Cero, Garantía Legal, Acción 24/48h, Recuperación de Activos) uses CSS Grid with explicit `grid-column-start/end` and `grid-row-start/end` positioning, switching to single-column on mobile.

9. **Container approach**: The section uses a row-inside-row pattern — the outer row (`d281619`) provides full-width with constrained content, the inner row (`425d88c`) provides the actual two-column layout.

---

## 9. Key Dimensions & Spacing

| Property | Desktop | Mobile (<690px) |
|----------|---------|-----------------|
| Section padding-top | 50px | 10px |
| Section padding-bottom | 40px | 20px |
| Left column width | 55% | 100% |
| Right column width | 45% | 100% |
| Right column padding-top | 50px | (default) |
| Left column padding-right | 20px | 0 |
| Decorative badge height | 110px | 74px |
| Main image width | 458px | (responsive) |
| Leaf icon width | 28px | 28px |
| Grid column gap | 35px | (single column) |
| Grid row gap | 20px | 20px |
| CTA button top-margin | 20px padding-top on container | same |
| Checkmark icon size | 30×30px | 30×30px |
| Overhead text font-size | (default) | 14px |

---

## 10. SVG Icons

All four checkmark icons use the same SVG path — a circled checkmark from a 1024×1024 viewBox, filled with `#565D66`. The path data:

```
M1008 512c0 273.934-222.066 496-496 496s-496-222.066-496-496 222.066-496 496-496 496 222.066 496 496z
M454.628 774.628l368-368c12.496-12.496 12.496-32.758 0-45.254l-45.254-45.254c-12.496-12.498-32.758-12.498-45.256 0l-300.118 300.116-140.118-140.118c-12.496-12.496-32.758-12.496-45.256 0l-45.254 45.254c-12.496 12.496-12.496 32.758 0 45.254l208 208c12.498 12.498 32.758 12.498 45.256 0.002z
```

---

## 11. CTA Button Link

- **URL:** `https://ecociclo.es/quienes-somos/`
- **Text:** "Conoce más sobre nosotros"
- **`data-type`:** `button-component`
- **Classes:** `gs-parent-hover gs_button gsbp-8bce4f6`

---

**End of analysis.**
