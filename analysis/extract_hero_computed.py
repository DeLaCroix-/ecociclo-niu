"""Extract computed styles for HERO section from ecociclo.es using Playwright."""
import json
from playwright.sync_api import sync_playwright

URL = "https://ecociclo.es/"
HERO_ID = "gspb_row-id-gsbp-87fe861"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 900})
    page.goto(URL, wait_until='networkidle')
    page.wait_for_timeout(3000)  # Let animations/GSAP/AOS load

    result = page.evaluate('''(heroId) => {
        const hero = document.getElementById(heroId);
        if (!hero) return {error: "Hero not found"};

        const heroCS = window.getComputedStyle(hero);
        const heroRect = hero.getBoundingClientRect();

        const data = {
            hero: {
                tag: hero.tagName,
                classes: hero.className,
                id: hero.id,
                rect: { x: heroRect.x, y: heroRect.y, w: heroRect.width, h: heroRect.height },
                computed: {
                    backgroundColor: heroCS.backgroundColor,
                    backgroundImage: heroCS.backgroundImage,
                    backgroundSize: heroCS.backgroundSize,
                    backgroundPosition: heroCS.backgroundPosition,
                    backgroundAttachment: heroCS.backgroundAttachment,
                    backgroundRepeat: heroCS.backgroundRepeat,
                    minHeight: heroCS.minHeight,
                    display: heroCS.display,
                    justifyContent: heroCS.justifyContent,
                    flexWrap: heroCS.flexWrap,
                    padding: heroCS.padding,
                    margin: heroCS.margin,
                    position: heroCS.position,
                    overflow: heroCS.overflow,
                }
            },
            columns: [],
            heading: null,
            description: null,
            ctaButton: null,
            overlayImage: null,
            featureCards: [],
        };

        // Get all column divs inside hero
        const cols = hero.querySelectorAll('[id^="gspb_col-id"], [class*="gspb_row__col"]');
        cols.forEach((col, i) => {
            const cs = window.getComputedStyle(col);
            const rect = col.getBoundingClientRect();
            data.columns.push({
                index: i,
                id: col.id,
                classes: col.className,
                rect: { x: rect.x, y: rect.y, w: rect.width, h: rect.height },
                computed: {
                    width: cs.width,
                    display: cs.display,
                    flexDirection: cs.flexDirection,
                    justifyContent: cs.justifyContent,
                    alignItems: cs.alignItems,
                    padding: cs.padding,
                    margin: cs.margin,
                    gap: cs.gap || cs.rowGap,
                    backgroundColor: cs.backgroundColor,
                }
            });
        });

        // H1 heading
        const h1 = hero.querySelector('h1');
        if (h1) {
            const cs = window.getComputedStyle(h1);
            const rect = h1.getBoundingClientRect();
            data.heading = {
                text: h1.textContent.trim(),
                tag: h1.tagName,
                rect: { x: rect.x, y: rect.y, w: rect.width, h: rect.height },
                computed: {
                    fontSize: cs.fontSize,
                    fontWeight: cs.fontWeight,
                    fontFamily: cs.fontFamily,
                    color: cs.color,
                    textTransform: cs.textTransform,
                    lineHeight: cs.lineHeight,
                    margin: cs.margin,
                    padding: cs.padding,
                }
            };
        }

        // Description text
        const descEl = hero.querySelector('.gspb_text-id-gsbp-6c529be, [id*="gspb_text-id"]');
        if (descEl) {
            const cs = window.getComputedStyle(descEl);
            const rect = descEl.getBoundingClientRect();
            data.description = {
                html: descEl.innerHTML,
                text: descEl.textContent.trim().substring(0, 200),
                rect: { x: rect.x, y: rect.y, w: rect.width, h: rect.height },
                computed: {
                    fontSize: cs.fontSize,
                    fontWeight: cs.fontWeight,
                    fontFamily: cs.fontFamily,
                    color: cs.color,
                    lineHeight: cs.lineHeight,
                    margin: cs.margin,
                }
            };
        }

        // CTA Button
        const cta = hero.querySelector('.gsbp-b5caa74, a[data-type="button-component"]');
        if (cta) {
            const cs = window.getComputedStyle(cta);
            const rect = cta.getBoundingClientRect();
            data.ctaButton = {
                text: cta.textContent.trim(),
                href: cta.href,
                rect: { x: rect.x, y: rect.y, w: rect.width, h: rect.height },
                computed: {
                    fontSize: cs.fontSize,
                    fontWeight: cs.fontWeight,
                    fontFamily: cs.fontFamily,
                    color: cs.color,
                    backgroundColor: cs.backgroundColor,
                    borderRadius: cs.borderRadius,
                    padding: cs.padding,
                    boxShadow: cs.boxShadow,
                    borderWidth: cs.borderWidth,
                    borderColor: cs.borderColor,
                    display: cs.display,
                }
            };
        }

        // Overlay Image
        const overlayImg = hero.querySelector('.gspb_image-id-gsbp-83c61e6 img, [id*="gspb_image-id"] img');
        if (overlayImg) {
            const rect = overlayImg.getBoundingClientRect();
            data.overlayImage = {
                src: overlayImg.src,
                alt: overlayImg.alt,
                naturalWidth: overlayImg.naturalWidth,
                naturalHeight: overlayImg.naturalHeight,
                rect: { x: rect.x, y: rect.y, w: rect.width, h: rect.height },
            };
        }

        // Feature Cards — match by ID prefix (gspb_container-id-gsbp-deabda5, etc.)
        const featureContainers = hero.querySelectorAll('[id*="gspb_container-id-gsbp-"], .gspb_container[id*="gsbp-"]');
        // Filter to only top-level ones (not nested icon containers inside cards)
        const topLevelContainers = Array.from(featureContainers).filter(el => {
            // A top-level feature card has border-radius:10px and bg #EAFDE7
            const cs = window.getComputedStyle(el);
            return cs.borderRadius === '10px' && cs.backgroundColor === 'rgb(234, 253, 231)';
        });
        topLevelContainers.forEach((card, i) => {
            const cs = window.getComputedStyle(card);
            const rect = card.getBoundingClientRect();
            
            const cardData = {
                index: i,
                id: card.id,
                rect: { x: rect.x, y: rect.y, w: rect.width, h: rect.height },
                computed: {
                    backgroundColor: cs.backgroundColor,
                    borderRadius: cs.borderRadius,
                    padding: cs.padding,
                    margin: cs.margin,
                    display: cs.display,
                    flexDirection: cs.flexDirection,
                    gap: cs.gap,
                },
                icon: null,
                text: null,
            };

            // Icon SVG
            const svg = card.querySelector('svg');
            if (svg) {
                const svgCS = window.getComputedStyle(svg);
                cardData.icon = {
                    viewBox: svg.getAttribute('viewBox'),
                    width: svgCS.width,
                    height: svgCS.height,
                    fill: svgCS.fill,
                };
            }

            // Icon container — find by computed bg color (green #65C132 with border-radius 5px)
            const iconContainer = Array.from(card.querySelectorAll('[id*="gspb_container"]')).find(el => {
                const ics = window.getComputedStyle(el);
                return ics.backgroundColor === 'rgb(101, 193, 50)' && ics.borderRadius === '5px';
            });
            if (iconContainer) {
                const icCS = window.getComputedStyle(iconContainer);
                cardData.iconContainer = {
                    backgroundColor: icCS.backgroundColor,
                    borderRadius: icCS.borderRadius,
                    padding: icCS.padding,
                };
            }

            // Text
            const headingEl = card.querySelector('[id*="gspb_heading"]');
            if (headingEl) {
                const hCS = window.getComputedStyle(headingEl);
                cardData.text = {
                    content: headingEl.textContent.trim(),
                    fontSize: hCS.fontSize,
                    fontWeight: hCS.fontWeight,
                    fontFamily: hCS.fontFamily,
                    color: hCS.color,
                };
            }

            data.featureCards.push(cardData);
        });

        return data;
    }''', HERO_ID)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    browser.close()
