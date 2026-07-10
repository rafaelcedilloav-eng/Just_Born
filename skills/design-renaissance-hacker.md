# Skill: The Renaissance Hacker — diseño con historia del arte

*(ES) Diseño de interfaces fundamentado en historia del arte: Renacimiento, Barroco, Bauhaus y Surrealismo como sistema de decisión, no como decoración. Nació de un loop de feedback exigente: cada belleza tuvo que justificarse con una referencia histórica.*

**Use when:** designing or redesigning any interface (landing, dashboard, product UI) that must evoke emotion and authority — not just display information.

---

## Origin (why this skill exists)

This skill was born from a demanding feedback loop between a human and their AI assistant. The first outputs were efficient and cold. The human rejected them — not with specs, but with standards: *"this has no soul."* The rule that emerged: **every aesthetic choice must be justified by a historical reference.** Code is not the goal; it is the brush. What follows is the art history that survived that filter.

## The four foundations (the actual art history)

### 1. Renaissance — the mathematics of the human gaze
The Renaissance discovered that beauty is computable: linear perspective (Brunelleschi), the golden ratio in composition, the grid as harmony. Da Vinci and Alberti treated the canvas as a mathematical space where the eye is *guided*, never forced.
**Applied:** layout grids with intentional proportions (not just 12 columns because the framework says so); whitespace as a designed element with the same weight as content; one clear focal point per view — the eye should travel a planned path. If you can't draw the path the eye takes, the layout isn't finished.

### 2. Baroque — chiaroscuro, or hierarchy through light
Caravaggio didn't illuminate scenes evenly: he carved them out of darkness. Light in the Baroque is *dramatic argument* — what matters is lit, what supports recedes. Depth and emotion come from the contrast, not from the objects.
**Applied (Chiaroscuro 2.0):** define an invisible light source for the page and keep it consistent — every shadow, glow, and elevation derives from it. Dark backgrounds are not "dark mode": they are the stage that makes the lit element theatrical. If an element floats, decide what shadow it casts. Hierarchy through luminance contrast beats hierarchy through size.

### 3. Bauhaus — form follows function, ornament is crime
The Bauhaus (Gropius, Moholy-Nagy) rejected decoration that doesn't work. Every element earns its place by doing something. Typography is information architecture; color is signal.
**Applied:** every effect must have a functional purpose — particles that communicate state, gradients that direct attention, motion that explains causality. If removing it changes nothing about comprehension, remove it. **The scarcity principle:** the accent color is not for decorating — it *declares*. Maximum 2-3 accent uses per viewport; things that matter must appear rarely for their appearance to count.

### 4. Surrealism — the calculated rupture
Magritte and Dalí worked because everything around the impossible object was rendered with academic precision. Subversion only lands on a stable base.
**Applied (the WOW factor):** ONE broken expectation per experience — a navigation that behaves like space, a transition that shouldn't be possible, a layout that floats. Earn it with rigor everywhere else. Two ruptures compete; three are noise.

## The creative engine (4 phases, in order)

1. **Abstraction:** name the core emotion of the content (wellness → peace; finance → sovereignty; developer tool → precision). One word. Everything derives from it.
2. **Visual metaphor:** choose the historical style or physical object that embodies that emotion. This decision, made early, resolves a hundred later micro-decisions.
3. **Chiaroscuro mapping:** place the invisible light source; define material properties (what reflects, what blurs, what absorbs).
4. **Kinetic momentum:** give the UI physics — inertia, gravity, resistance (lerp-based easing). A page that *breathes* (ambient motion), *reacts* (magnetism to presence) and *resists* (weight in transitions) feels inhabited rather than rendered.

## Architectural mandates

- **No blinding white voids.** Backgrounds are alive: texture, cinematic noise, or mesh gradients — subtle, functional (Bauhaus test applies).
- **The scroll is a journey.** If the journey bores, the destination doesn't matter. Design transitions as movement through a space, not as a document sliding.
- **Typography is emotional.** Tracking, leading and weight communicate authority, calm or urgency before a word is read. Negative letter-spacing on display sizes; generous leading on reading text.
- **Elegance is simplified complexity, not absence.** Minimalism misread as emptiness was this skill's founding error — don't repeat it.
- **Data fidelity is non-negotiable.** Art is not an excuse for disorder: every piece of real content is a brick in the cathedral. Beautiful and wrong is worse than plain and right.

## Quality bar

Before shipping, answer with historical references, not taste: *Which movement justifies this composition? Where is the light source? What does each effect DO? Where is the single rupture, and did the rest earn it?* If any answer is "it looks nice" — it goes back.
