---
name: explanatory-writing-style
description: Writing style for technical content that emphasizes why over what/how, with interview-focused reasoning
tags: [writing, documentation, technical-content]
---

# Explanatory Writing Style for Technical Content

This skill defines the preferred writing style for technical chapters and explanations in this repository.

## Core Principles

### 1. Lead with "Why" Before "What" and "How"

Always establish **why the topic matters** and **what it tests** before diving into implementation details.

**Bad (what/how first):**
> Binary search is an algorithm that finds elements in sorted arrays with O(log n) complexity. Here's how to implement it...

**Good (why first):**
> Binary search appears in nearly every technical interview not because it's complicated, but because it's deceptively simple. The algorithm itself fits in a few lines, yet implementing it correctly requires careful reasoning about boundaries, loop invariants, and edge cases. This gap between conceptual simplicity and implementation precision makes it an ideal test of engineering fundamentals.

### 2. Frame Technical Choices as Evaluation Criteria

When comparing approaches, explain how each choice reveals different qualities in a candidate's thinking.

**Bad (neutral comparison):**
> Template A uses closed intervals. Template B uses open intervals. Both work.

**Good (evaluation-focused):**
> The `l <= r` template rewards candidates who establish a clear invariant and trust it to handle all cases uniformly. The `l + 1 < r` template forces candidates to enumerate cases and handle each explicitly. Neither is wrong, but one is easier to get right under pressure. When the interviewer adds a twist—"Now find the last occurrence instead of the first"—the candidate with a stable invariant adjusts confidently. The candidate with case-by-case logic revisits every branch, wondering which one needs updating.

### 3. Use Concrete Examples to Illustrate Edge Cases

Never say "handles edge cases well" without showing the actual edge case and how it's handled.

**Bad (abstract claim):**
> This approach handles boundary cases correctly.

**Good (concrete demonstration):**
> Consider searching for `target = 0` or `target = 5` in `nums = [1, 3]`:
>
> With `l <= r`, when `target = 0`, the loop moves `r` leftward until `l = 0` and `r = -1`, then exits with `l = 0`—the correct insertion point at the array's start. When `target = 5`, the loop moves `l` rightward until `l = 2` and `r = 1`, then exits with `l = 2`—the correct insertion point beyond the array's end. No special handling needed.

### 4. Explain What Interviewers Notice

Make explicit what signals different coding choices send to an interviewer.

**Good examples:**
- "This detail—overflow handling—is precisely the kind of thing interviewers watch for. It doesn't change the algorithm's correctness in Python, but knowing why you'd write it differently in C++ demonstrates awareness of how abstractions leak."
- "State your invariant explicitly when coding in an interview. 'I'm maintaining that everything before `l` is less than target' is a single sentence that makes your reasoning transparent."
- "In an interview, this difference shows. A candidate using `l <= r` can explain: 'I maintain the invariant that everything before `l` fails my condition.' A candidate using `l + 1 < r` must explain: 'I keep `l` and `r` as boundaries. When they're adjacent, I check both...'"

### 5. Connect Details to Broader Skills

Link implementation choices to the underlying engineering skill being tested.

**Bad (just the fact):**
> Use `mid = l + (r - l) // 2` to avoid overflow.

**Good (fact + skill being tested):**
> Always calculate the midpoint as `mid = l + (r - l) // 2` rather than `mid = (l + r) // 2`. In languages like C++ and Java, the sum `l + r` can overflow when both values are large. This detail demonstrates awareness of how abstractions leak—a candidate who mentions overflow prevention unprompted signals that they've debugged production code, not just solved toy problems.

### 6. Describe Variants as Progressive Tests

When covering problem variants, explain what additional reasoning skill each one tests.

**Good pattern:**
- "**Rotated arrays** — Can you decompose complex conditions into simpler checks?"
- "**2D matrices** — Can you abstract away irrelevant details (coordinate transformation)?"
- "**Circular arrays** — Can you handle 'not found' as a defined behavior (wrap-around) rather than an error?"
- "**Peaks and valleys** — Do you understand binary search works on any monotonic property, not just target comparison?"

## Paragraph Structure

### Use Explanatory Paragraphs, Not Bullet Points

Technical content should read like thoughtful prose, not slide decks.

**Bad (bullet points for prose):**
```markdown
### Why This Matters
- Tests attention to detail
- Tests boundary reasoning
- Tests systematic thinking
```

**Good (explanatory paragraph):**
```markdown
Binary search tests your ability to think through details systematically. The algorithm's simplicity is deceptive—getting it right requires clear reasoning about boundaries, loop invariants, and edge cases. Each variation probes whether you reason systematically or patch bugs reactively.
```

### Reserve Bullets for True Lists

Use bullets only for:
- Enumerating distinct items (conditions, requirements, steps)
- Listing examples or variants
- Quick reference material

Not for explanations that deserve paragraph treatment.

## Language and Tone

### Be Direct and Confident

**Bad (hedging):**
> You might want to consider using the `l <= r` template because it could be easier in some cases.

**Good (confident):**
> The `l <= r` template is superior. It handles edge cases uniformly, extends cleanly to variants, and reveals systematic thinking under pressure.

### Write in English for Technical Content

All technical chapters, comparisons, and implementation guidance should be in English, even if the repository serves a bilingual audience. Keep Chinese for problem metadata or specific requirements documents only.

### Use Active Voice

**Bad (passive):**
> The search space is divided in half by the algorithm.

**Good (active):**
> The algorithm divides the search space in half.

## Structure for Technical Chapters

1. **Why It Matters** (2-3 paragraphs establishing interview/engineering value)
2. **Core Concept** (brief, clear explanation of the fundamental idea)
3. **Approaches/Templates** (side-by-side comparison with explanations)
4. **Deep Comparison** (why one approach is superior, with concrete examples)
5. **Implementation Details** (practical guidance on overflow, invariants, return semantics)
6. **Variants and Extensions** (each framed as testing a specific skill)
7. **Classic Problems** (with code transclusion)

## Example Application

See `book/binary-search.md` (last updated 2026-08-23) for a complete example of this style applied to a technical chapter.

## When to Use This Style

Apply this style to:
- ✓ Technical chapter content (`book/*.md`)
- ✓ Deep-dive explanations of algorithms and data structures
- ✓ Comparison of different approaches or templates
- ✓ Implementation guidance and best practices

Do not apply to:
- ✗ Problem metadata (YAML frontmatter)
- ✗ Code comments (keep those concise and direct)
- ✗ README files (unless they contain substantial technical teaching)
- ✗ Build/deployment documentation (stay factual and imperative)
