# Design System — Coding Interview Questions

Last updated: 2026-08-10

## Product Context

- **What this is:** A problem-first LeetCode solution library presented as a connected learning curriculum.
- **Who it's for:** Developers studying algorithms, data structures, and reusable interview patterns.
- **Space:** Technical education and reference documentation.
- **Project type:** Editorial documentation site with interactive curriculum and knowledge-graph views.

## Aesthetic Direction

- **Direction:** Compact editorial.
- **Decoration level:** Minimal. Typography, spacing, and hierarchy do the work.
- **Mood:** Calm, precise, and serious without feeling dense. Solution content and learning relationships remain visually dominant over metadata.

## Typography

- **Display and headings:** The VitePress heading stack, used with restrained sizes and weight.
- **Body and UI:** The VitePress body stack. No new font asset is introduced in the initial pass.
- **Code:** The VitePress monospace stack to remain consistent with syntax highlighting.
- **Scale:** 12px metadata, 13px section labels, 14–16px supporting text, and the existing VitePress document-heading scale.
- **Labels:** Uppercase, 0.04–0.08em tracking, and 600 weight. Labels must remain quieter than linked content.

## Color

- **Approach:** Restrained. Reuse VitePress semantic tokens for theme compatibility.
- **Accent:** `var(--vp-c-brand-1)` for links, difficulty, focus, and hover states only.
- **Primary text:** `var(--vp-c-text-1)`.
- **Secondary text:** `var(--vp-c-text-2)`.
- **Dividers:** `var(--vp-c-divider)`.
- **Dark mode:** Preserve VitePress surface colors; hierarchy comes from text contrast rather than additional panels.

## Spacing

- **Base unit:** 4px.
- **Density:** Compact-comfortable.
- **Scale:** 4px, 6px, 8px, 10px, 12px, 16px, 22px, 32px.
- Metadata sections should use less vertical space than solution sections.

## Layout

- **Approach:** Grid-disciplined document layout with single-column metadata.
- **Content width:** Inherit VitePress's readable document width.
- **Relationship rows:** Stack the relation label above the linked problem. Do not reserve a fixed label column.
- **Topic links:** Flat underlined text tags rather than outlined pills.
- **Border radius:** Use only where interaction or grouping requires it; metadata does not need containers.

## Motion

- **Approach:** Minimal-functional.
- Use only existing VitePress link, focus, navigation, and color transitions.
- Do not animate document metadata or relationship rows.

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-08-10 | Adopt compact editorial metadata | The previous fixed-width labels competed with related problem titles and wasted horizontal space. |
| 2026-08-10 | Replace topic pills with flat text tags | Topics are navigation metadata, not primary actions. |
| 2026-08-10 | Keep the existing font assets | This pass improves hierarchy without introducing a new runtime dependency. |
