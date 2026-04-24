name: cinematic-hero-builder
description: "End-to-end premium website builder — from business URL to cinematic $15k-looking site. Researches the business, creates branding/typography/layout, generates hero imagery via Nano Banana 2, creates scroll animations with GSAP, and deploys. Trigger for: build a website, landing page, hero section, premium site, homepage redesign, scroll animation, website imagery, cinematic web page, hero image, exploding product, floating items, product animation, or any request combining AI image generation with web design. Full pipeline: research → design → image gen → build."

---

# Cinematic Hero Builder

Build websites that look like they cost $15k — for any business, any product. This skill orchestrates a complete pipeline: research the business, design branding and layout, generate product-specific hero imagery with AI, and build cinematic HTML pages with scroll animations.

The magic is in the product-specific hero concept. A coffee company gets an exploding coffee bean shower on scroll. A van removal company gets items floating dramatically out the back of a van. A tech startup gets a holographic product reveal. Every business gets a hero that tells their story through motion.

## When to use this skill

Trigger this skill for any website build request, landing page design, hero section creation, or homepage redesign — especially when the user wants something that feels premium, cinematic, or visually striking. This is the go-to skill when combining AI-generated imagery with animated web design.

Before writing any code, ALWAYS read the relevant reference files from this skill's `references/` directory. They contain prompt templates, business-type mappings, and design patterns that have been tested and refined.

## Dependencies

This skill works alongside `cinematic-site-components` for animation patterns. Read relevant component references from that skill when building the animation layer.

External tools used in the pipeline:
- **Nano Banana 2 CLI** (`nano-banana` command) — AI image generation via Gemini API. If installed, call directly from the terminal. Supports transparent backgrounds (`-t` flag), reference images (`-r`), and 4K output. Install: `bun install -g nano-banana-2-skill` (requires Gemini API key). See: github.com/kingbootoshi/nano-banana-2-skill
- **Google Flow** (flow.google) — Image-to-video for scroll video backgrounds and animated transitions (uses Veo 3.1)
- **Kling 3.0** (alternative to Flow) — AI video generation that creates smooth transitions between two images. Useful for the frame animation pipeline.
- **FFMPEG** — Frame extraction from generated videos (for scroll-driven frame animations)
- **Web scraping / research tools** — For analysing existing business sites

## Core Technique: Scroll-Driven Frame Animation

This is the signature technique that makes these sites look like $15k builds. Read `references/frame-animation.md` for the full technical implementation.

**How it works (the digital flipbook):**

Instead of CSS/JS animations, the hero plays back actual AI-generated video frames synced to scroll position. Each scroll increment advances one frame, creating buttery smooth, photorealistic animation that no CSS could replicate.

**The pipeline:**

1. **Generate start frame** — Use Nano Banana 2 to create the hero's initial state (e.g., a complete coffee cup on dark background)
2. **Generate end frame** — Use Nano Banana 2 to create the hero's final state (e.g., exploded coffee beans scattered outward)
3. **Generate transition video** — Feed both frames into Google Flow or Kling 3.0, which AI-interpolates a smooth cinematic transition between them (4-6 seconds)
4. **Extract frames** — Use FFMPEG to extract every frame from the video at the target framerate:
   ```bash
   ffmpeg -i transition.mp4 -vf "fps=30,scale=1920:-1" frames/frame_%04d.webp
   ```
5. **Build the scroll player** — Load all frames into an HTML canvas, use ScrollTrigger to map scroll position to frame index:
   ```javascript
   const frameCount = 120; // 4 seconds × 30fps
   const canvas = document.querySelector('#hero-canvas');
   const ctx = canvas.getContext('2d');
   const images = [];

   // Preload all frames
   for (let i = 0; i < frameCount; i++) {
     const img = new Image();
     img.src = `frames/frame_${String(i).padStart(4, '0')}.webp`;
     images.push(img);
   }

   // Sync to scroll
   gsap.to({ frame: 0 }, {
     frame: frameCount - 1,
     snap: 'frame',
     ease: 'none',
     scrollTrigger: {
       trigger: '#hero-section',
       start: 'top top',
       end: '+=300%',
       scrub: 0.5,
       pin: true
     },
     onUpdate: function() {
       const index = Math.round(this.targets()[0].frame);
       ctx.clearRect(0, 0, canvas.width, canvas.height);
       if (images[index]?.complete) {
         ctx.drawImage(images[index], 0, 0, canvas.width, canvas.height);
       }
     }
   });
   ```

**When to use frame animation vs GSAP animation:**
- **Frame animation** — For photorealistic product transformations (exploding, disassembling, morphing). This is the premium technique. Use whenever the hero concept involves a physical product changing state.
- **GSAP animation** — For UI element movements, text reveals, layout transitions. Use for the supporting sections and simpler hero concepts.
- **Combine both** — Frame animation for the hero "wow moment", GSAP for everything else on the page.

**For single-file delivery:** When the user needs a single HTML file (no external frame files), base64-encode the frames directly into the HTML as a JavaScript array. This makes larger files but keeps everything self-contained. Alternatively, use a sprite sheet approach where all frames are stitched into one large image.

## The 6-Phase Pipeline

Every build follows this pipeline. Each phase has an approval gate — never skip ahead without user sign-off.

### Phase 1: Business Research & Analysis

Before designing anything, deeply understand the business. This phase determines everything that follows.

**If the business has an existing website:**
1. Scrape and analyse the current site (use Apify, Claude in Chrome, or web fetch)
2. Extract: brand colours (hex values), fonts, logo, tagline, tone of voice, products/services, target audience
3. Screenshot key pages for reference
4. Note what works and what doesn't about the current design

**If starting from scratch:**
1. Ask the user about: business name, industry, products/services, target audience, competitors, brand personality (modern/traditional/playful/serious)
2. Research 3-5 competitor sites in the same industry for design inspiration
3. Identify industry design conventions and opportunities to stand out

**Output of Phase 1:** A business brief document containing:
- Business name, industry, core offering
- Target audience profile
- Brand personality keywords (e.g., "premium, artisan, warm" for a coffee company)
- Existing brand assets (colours, fonts, logo) or recommendations
- 3 competitor references with notes
- Initial hero concept idea (the "wow" moment)

Present the brief to the user for approval before proceeding.

### Phase 2: Design System Creation

Build a complete design system that matches the brand. This is what makes a site look like it had a real designer.

**Typography:**
- Select a primary heading font (display/hero use) and body font (readability)
- Use Google Fonts — read `references/typography-pairings.md` for tested combinations
- Define a type scale using `clamp()` for responsive sizing:
  - Hero headline: `clamp(3rem, 8vw, 7rem)`
  - Section heading: `clamp(2rem, 4vw, 3.5rem)`
  - Subheading: `clamp(1.2rem, 2vw, 1.5rem)`
  - Body: `clamp(1rem, 1.2vw, 1.1rem)`

**Colour Palette:**
- Primary brand colour (from existing brand or derived from industry)
- Secondary accent
- Background (dark or light depending on brand personality)
- Text colour (high contrast with background)
- Muted/subtle colour for secondary text
- Define as CSS custom properties in `:root`

**Layout Framework:**
- Section structure (what sections the page needs)
- Grid system (12-column, max-width, gutters)
- Spacing scale (consistent vertical rhythm)
- Card/component border-radius, shadows, glass effects

**Output of Phase 2:** A design system document with:
- Font selections with Google Fonts import URLs
- Full colour palette with hex values and CSS custom properties
- Type scale with responsive `clamp()` values
- Layout structure and spacing rules
- Mood/style reference (which cinematic components fit this brand)

Present the design system to the user for approval. This is the most important approval gate — everything builds on these foundations.

### Phase 3: Hero Concept & Scroll Animation Design

This is where the magic happens. Design a product-specific hero that tells the business's story through motion.

**Read `references/hero-concepts.md`** for a library of proven concepts mapped to business types.

The hero concept has three parts:

**1. The Static Hero (above the fold)**
- What the user sees before any scrolling
- Typically: hero image/video + headline + CTA
- The image should feature the business's actual product in a cinematic setting

**2. The Scroll Trigger (the "wow" moment)**
- What happens when the user starts scrolling
- This is the money shot — the exploding coffee, the floating van items, the disassembling product
- Must feel physical, dramatic, and directly related to the product

**3. The Transition (into the rest of the page)**
- How the hero animation resolves into the next section
- Should feel intentional, not jarring — the animation tells a story that leads to the content

**Hero concept examples by business type:**

| Business Type | Hero Concept | Scroll Animation | Cinematic Components |
|---|---|---|---|
| Coffee shop | Steaming cup on dark background | Coffee beans explode outward on scroll, cup rises | `zoom-parallax` + `particle-button` patterns |
| Removals company | Van with back doors opening | Items float out dramatically, each revealing a service | `sticky-stack` + `horizontal-scroll` patterns |
| Tech startup | Product on podium with glow | Product disassembles into features on scroll | `sticky-cards` + `curtain-reveal` patterns |
| Restaurant | Hero dish, steam rising | Ingredients fly in from edges, assembling the dish | `split-scroll` + `image-trail` patterns |
| Fitness | Athlete mid-motion | Motion blur splits into training scenes | `horizontal-scroll` + `text-mask` patterns |
| Real estate | Property exterior, golden hour | Door opens, camera pushes through rooms | `curtain-reveal` + `zoom-parallax` patterns |
| Fashion | Model in hero garment | Fabric ripples and transforms between looks | `accordion-slider` + `color-shift` patterns |
| SaaS / App | Dashboard screenshot, floating | UI elements separate and showcase features | `sticky-stack` + `spotlight-border` patterns |

**Output of Phase 3:** A hero concept document with:
- Written description of the hero animation (what happens at each scroll point)
- Which cinematic-site-components modules to use as the animation foundation
- Image generation brief (what images need to be created — see Phase 4)
- Video generation brief if applicable (what Flow videos are needed — see Phase 5)
- Rough storyboard (can be text-based: "At 0% scroll: X. At 25%: Y. At 50%: Z...")

Present for approval. The user should be able to visualise the end result from this description.

### Phase 4: AI Image Generation (Nano Banana 2)

Generate the hero imagery using Google's Nano Banana 2 model. The goal is photorealistic, cinematic product imagery that looks like it was shot by a professional photographer.

**Read `references/image-prompts.md`** for the prompt template library.

**How to generate images:**

**Option A — nano-banana CLI (preferred if installed):**

If the `nano-banana` CLI tool is available, generate images directly from the terminal:

```bash
# Hero image (4K, 16:9)
nano-banana "Cinematic product photography..." -s 4k -a 16:9 -o hero-main

# Element with transparent background (for compositing into animations)
nano-banana "Single coffee bean floating..." -s 2k -a 1:1 -t -o coffee-bean

# Using reference image for style consistency
nano-banana "Same style, different angle..." -r hero-main.png -o hero-alt
```

The `-t` flag generates on green screen and auto-removes background via FFMPEG — perfect for individual elements that need to float/explode in the animation.

**Option B — Gemini web UI:**

If the CLI isn't installed, generate optimised prompts for the user to paste into Gemini (gemini.google.com).

**Prompt structure for hero images:**

```
[STYLE]: Cinematic product photography, [LIGHTING], [MOOD]
[SUBJECT]: [Product] in [setting/context], [pose/arrangement]
[DETAILS]: [Textures, materials, specific visual details]
[COMPOSITION]: [Camera angle, depth of field, focal length equivalent]
[TECHNICAL]: 4K resolution, photorealistic, no text overlays, clean background for compositing
```

**Example prompts by business type:**

Coffee company hero:
```
Cinematic product photography, dramatic rim lighting with warm amber tones, luxurious and inviting mood. A single artisan ceramic cup of freshly brewed coffee centered on a dark slate surface, steam rising in elegant curls caught by backlight. Rich crema visible on the coffee surface, scattered whole coffee beans on the slate. Shot from slightly above at 35mm equivalent, shallow depth of field with bokeh background of warm blurred lights. 4K resolution, photorealistic, clean dark background suitable for web compositing.
```

Removals company hero:
```
Cinematic commercial photography, bright natural daylight, professional and trustworthy mood. A modern white removal van with rear doors wide open, shot from a 3/4 rear angle. Interior is warmly lit showing neatly stacked furniture and boxes. Clean suburban street background with soft bokeh. Shot at 24mm equivalent for slight wide-angle drama, full depth of field. 4K resolution, photorealistic, clean composition with space for text overlay on the left third.
```

**For the scroll animation, generate additional "element" images:**
- Individual product items on transparent/clean backgrounds (for floating/exploding effects)
- Before/after states (for the scroll transition)
- Background textures or environments

Generate 3-5 prompt variations for each key image to give the user options.

**Output of Phase 4:** A complete set of Nano Banana 2 prompts, organised by:
- Hero image (the main above-fold shot)
- Element images (individual items for animation)
- Background/texture images
- Any lifestyle/context shots for other sections

Present the prompts to the user. They can generate images in Gemini, or these prompts can feed into an n8n automation workflow.

### Phase 5: Video Generation & Frame Extraction

This phase creates the transition video between the start and end hero states, then extracts frames for the scroll-driven animation. This is what makes the site feel like a $15k build.

**Read `references/frame-animation.md`** for the full technical implementation.

**Step 1: Generate the transition video**

Use EITHER Google Flow or Kling 3.0 to create a smooth AI-interpolated video between the two hero states from Phase 4:

**Google Flow** (flow.google):
- Upload the start frame image and end frame image
- Flow uses Veo 3.1 to interpolate between them
- Set duration to 4-6 seconds
- Add camera movement if appropriate (subtle zoom, pan)
- Download the resulting MP4

**Kling 3.0** (alternative):
- Image-to-video with start and end frame
- Often produces more dramatic physical transitions (good for product explosions, disassembly)
- 4-6 second duration target

**Flow/Kling prompt template:**
```
Start frame: [Upload hero start image from Phase 4]
End frame: [Upload hero end image from Phase 4]
Motion: [Describe the physical transformation — e.g., "coffee beans gradually burst outward from the cup in all directions, the cup rises slowly, steam intensifies"]
Camera: [Pan left/right, zoom in/out, orbit, static]
Duration: 4-6 seconds
Style: Cinematic, smooth, 30fps minimum
```

**Step 2: Extract frames with FFMPEG**

Once the video is downloaded, extract individual frames:

```bash
# Create frames directory
mkdir -p frames

# Extract at 30fps, scale to 1920px wide, output as WebP (smaller than PNG)
ffmpeg -i transition.mp4 -vf "fps=30,scale=1920:-1" -quality 85 frames/frame_%04d.webp

# Check frame count
ls frames/ | wc -l
```

Target: 90-180 frames (3-6 seconds at 30fps). More frames = smoother animation but larger page size. For single-file delivery, consider 60 frames (2 seconds at 30fps) to keep file size manageable.

**Step 3: Optimise frames for web**

```bash
# Optional: reduce to 24fps for smaller payload
ffmpeg -i transition.mp4 -vf "fps=24,scale=1440:-1" -quality 80 frames/frame_%04d.webp

# Optional: create a sprite sheet (all frames in one image)
montage frames/frame_*.webp -tile 10x -geometry +0+0 spritesheet.webp
```

**Output of Phase 5:**
- Extracted frame images (WebP format) ready for the scroll animation
- Frame count and timing data for the scroll player configuration
- OR a sprite sheet for single-file delivery

If the user can't generate video (no Flow/Kling access), fall back to GSAP-only animation using the individual element images from Phase 4 — it won't be as premium but still looks great.

### Phase 6: Build the Cinematic Page

Now bring everything together into a production-ready HTML page.

**Before building, read the relevant reference files from `cinematic-site-components`:**
- Read the specific component `.html` files identified in Phase 3
- Extract the CSS patterns, GSAP animation code, and ScrollTrigger configurations
- Don't copy blindly — adapt to this business's design system

**Build approach:**

1. **Start with the design system as CSS custom properties**
   ```css
   :root {
     --bg: #0a0a0b;
     --text: #eae7e2;
     --accent: #c8a97e;
     --muted: #5a5a5e;
     --font-heading: 'Font Name', sans-serif;
     --font-body: 'Font Name', sans-serif;
   }
   ```

2. **Build the hero section first**
   - Place the AI-generated hero image (user will have generated this from Phase 4 prompts)
   - Use placeholder images initially with clear comments for where to swap in generated images
   - Wire up the scroll animation using GSAP + ScrollTrigger patterns from the cinematic components

3. **Add the scroll animation**
   - Implement the "wow moment" designed in Phase 3
   - Use `ScrollTrigger.create()` with `scrub: true` for scroll-linked animations
   - Layer multiple elements for depth (foreground items, midground product, background environment)

4. **Build remaining sections**
   - Features/services section
   - Social proof / testimonials
   - CTA section
   - Footer
   - Each section should have subtle scroll-triggered entrances (fade, slide, parallax)

5. **Add ambient effects**
   - Cursor interactions (from `cursor-reactive` component if appropriate)
   - Kinetic marquee strips between sections
   - Mesh gradient backgrounds for premium feel
   - Custom cursor if it suits the brand

6. **Optimise for performance**
   - Lazy load images below the fold
   - Use `will-change` and `transform` for GPU-accelerated animations
   - Preload hero image
   - Keep total JS under 200KB (GSAP CDN + custom code)

**Technical stack (consistent with cinematic-site-components):**
- Single-file HTML (HTML + CSS + JS)
- GSAP 3.12.5 via CDN
- ScrollTrigger via CDN
- Google Fonts
- No frameworks, no build step

**Output modes:**
- **Full landing page** — Complete single-file HTML with all sections
- **Hero section only** — Just the hero + scroll animation as a droppable component

**Output of Phase 6:** The built HTML file(s), saved to the outputs folder with a computer:// link for the user.

## Image Placeholder Strategy

Since AI images need to be generated externally (in Gemini or Flow), the built page uses a smart placeholder system:

```html
<!-- HERO IMAGE: Replace with Nano Banana 2 generated image -->
<!-- Prompt: [the exact prompt from Phase 4] -->
<div class="hero-image" style="background-image: url('placeholder.jpg')"></div>
```

Every image placeholder includes the exact Nano Banana 2 prompt as a comment, so the user (or an automation) can generate and swap images without any design knowledge.
