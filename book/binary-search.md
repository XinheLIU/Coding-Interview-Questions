---
chapter: binary-search
---

# Binary Search

Last updated: 2026-08-23

## Why Binary Search Matters in Interviews

Binary search appears in nearly every technical interview not because it's complicated, but because it's deceptively simple. The algorithm itself—halve the search space repeatedly—fits in a few lines. Yet implementing it correctly requires careful reasoning about boundaries, loop invariants, and edge cases. This gap between conceptual simplicity and implementation precision makes it an ideal test of engineering fundamentals.

Interviewers use binary search to evaluate how candidates think about details. When does the loop terminate? What happens when the array has one element? Two elements? When the target is smaller than everything? Larger than everything? Each variation probes whether you reason systematically or patch bugs reactively. A candidate who writes `l <= r` and immediately knows `l` holds the insertion point demonstrates clearer thinking than one who switches to `l < r`, realizes it breaks on single-element arrays, then tries `l + 1 < r` with manual post-loop checks.

The algorithm scales into variations that test progressively deeper reasoning: rotated arrays force you to identify which half is sorted before deciding direction; 2D matrices require mapping one-dimensional indices to two-dimensional coordinates; circular arrays need modular arithmetic to handle wrap-around. Each builds on the same foundation—divide the space, move a boundary—but punishes sloppy assumptions about what "middle" means and where "left" and "right" should go next.

Binary search isn't about memorizing a template. It's about demonstrating that you can take a well-defined problem, establish clear invariants, handle every possible input without special-casing, and confidently state why your code is correct. That's why it remains a cornerstone of technical assessment.

## Core Concept

Binary search is an efficient algorithm for finding elements in sorted arrays. The fundamental idea is elegant: repeatedly halve the search space until you locate the target or exhaust all possibilities. Each comparison eliminates half of the remaining candidates, achieving **O(log n)** time complexity with **O(1)** space.

The algorithm works because sorted arrays have a critical property: if the middle element is too large, you know the target must be in the left half; if too small, it must be in the right half. This decision point, repeated recursively, transforms a linear scan into a logarithmic search.

Binary search requires three conditions to work correctly. First, the data structure must support random access—arrays work perfectly, but linked lists cannot efficiently reach the middle element. Second, the data must be sorted (or monotonic in some measurable way). Third, the search space must be bounded with clear endpoints.

In modern software engineering, binary search's real value extends beyond exact-match lookups. The most common applications involve **boundary finding**: locating the first or last element satisfying a condition (often called `lower_bound` and `upper_bound`). This pattern appears everywhere—finding version ranges in release manifests, identifying timestamp windows in logs, matching IP address blocks in routing tables, and detecting peaks or valleys in rotated or mountain arrays.

## Two Binary Search Templates

Binary search implementations typically follow one of two patterns. The choice matters because it affects how you reason about edge cases, how easily the code extends to variants, and how many places bugs can hide.

### Template One: `l <= r` (Closed Interval)

```python
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2  # avoid overflow
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1  # discard mid and everything to the right
        else:
            l = mid + 1  # discard mid and everything to the left
    return -1  # not found
```

This template treats the search space as a **closed interval `[l, r]`**, where both endpoints are valid candidates. Each iteration examines the middle element and then **excludes it** from the remaining search space by moving the boundary past it (`mid ± 1`). The loop continues while there are still elements to check (`l <= r`), and exits when the interval becomes empty (`l > r`).

The key advantage appears when you need the insertion point: after the loop exits, `l` points directly to where the target would belong if it's not present. This makes implementing `lower_bound` trivial—just return `l` without any additional logic.

### Template Two: `l + 1 < r` (Adjacent Exit)

```python
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid  # keep r as a ">= target" boundary
        else:
            l = mid  # keep l as a "< target" boundary
    # when loop exits, only l and r remain—check both
    if nums[l] == target: return l
    if nums[r] == target: return r
    return -1
```

This template maintains `l` and `r` as known boundaries of an **open interval `(l, r)`**, where elements between them remain unexplored. The `mid` calculation never equals `l` or `r` themselves. The loop exits when `l` and `r` become adjacent (`l + 1 == r`), leaving exactly two candidates that must be checked explicitly.

The trade-off is clear: you avoid thinking about `±1` adjustments during the loop, but you must write additional branches after the loop to handle the two remaining elements. For boundary-finding variants, this post-loop logic becomes more complex because you need to determine which of the two candidates (or neither, or the position beyond them) is the correct answer.

## Comparing the Two Approaches

Understanding the differences between these templates helps you choose the right tool and avoid subtle bugs. Here's how they compare across six critical dimensions:

| Aspect | `l <= r` | `l + 1 < r` |
|--------|----------|-------------|
| **Loop exit condition** | `l > r` | `l + 1 == r` |
| **Remaining elements at exit** | 0 | 2 |
| **Answer retrieval** | Direct `return l` | Requires branching logic |
| **Boundary case handling** | Unified through `l` | Needs 3 branches for edge cases |
| **Mid assignment** | `mid ± 1` | `mid` |
| **Code length** | 6-7 lines | 10-12 lines |
| **Infinite loop risk** | Very low with correct implementation | Very low by design |
| **Extension to variants** | Easy, `l` semantics remain stable | Difficult, exit logic needs rederivation |

## Why `l <= r` Is Superior

The closed-interval template (`l <= r`) offers several compelling advantages that become more pronounced as problems grow complex. More importantly, it encourages the kind of systematic thinking that distinguishes strong candidates from those who patch bugs reactively.

### Clearer Interval Semantics

The `l <= r` template maintains a closed interval `[l, r]` where every element is a potential candidate. Each iteration examines the middle element and then excludes it by moving the boundary past it (`mid ± 1`). The interval shrinks monotonically until it becomes empty, at which point `l > r` and the search terminates.

The `l + 1 < r` template, by contrast, maintains `l` and `r` as known boundary values that define an open interval `(l, r)`. The middle element is always between them, never equal to them. This means you're tracking relationships between pointers rather than reasoning about the interval itself. When the loop exits, you're left with two adjacent positions that both need explicit checking.

This difference matters when handling edge cases. With closed intervals, you reason: "The search space contains these elements. I've checked `mid`. Now the search space contains everything except `mid`." With open intervals, you reason: "I know `l` is too small and `r` is too large. The answer is between them. Now I know `mid` is too small/large, so I update a boundary." The former is a statement about the data; the latter is a statement about the pointers.

When an interviewer asks "Why do you return `l` here?", the closed-interval answer is immediate: "Because when the loop exits, all elements before `l` are smaller than target, and `l` is the first position that could hold target or something larger." The open-interval answer requires explaining why the post-loop checks work and why you chose to return one value over another in each branch.

### Consistent Mid-Update Strategy

With `l <= r`, you always use `mid ± 1` because `mid` has already been examined and must be excluded from further consideration. This consistency means you never question whether to add or subtract one—if you checked `mid`, it's out of bounds for the next iteration.

With `l + 1 < r`, you assign `r = mid` or `l = mid` without adjustment because `mid` lives inside the open interval `(l, r)`. Moving a boundary to `mid` naturally shrinks the interval without manual arithmetic. While this sounds convenient, it creates a decision point: "Do I include `mid` in the next iteration or exclude it?" Different problems give different answers, and the post-loop checks change accordingly.

The consistency of `mid ± 1` reduces cognitive load. You're not switching mental gears between "exclude this time" and "include that time"—you always exclude. This uniformity extends to variants: finding the first occurrence, the last occurrence, or an insertion point all use the same update rule. The comparison changes, but the pointer arithmetic doesn't.

### Unified Boundary Handling

Edge cases expose the difference between the two templates. Consider searching for `target = 0` or `target = 5` in `nums = [1, 3]`:

With `l <= r`, both edge cases resolve automatically. When `target = 0`, the loop moves `r` leftward until `l = 0` and `r = -1`, then exits with `l = 0`—the correct insertion point at the array's start. When `target = 5`, the loop moves `l` rightward until `l = 2` and `r = 1`, then exits with `l = 2` (which equals `len(nums)`)—the correct insertion point beyond the array's end. No special handling needed. The empty interval (`l > r`) encodes "not found," and `l` encodes "where it belongs."

With `l + 1 < r`, the initial state is `l = 0, r = 1`, so `l + 1 < r` becomes `1 < 1`, which is false. The loop never executes. Now you face a decision tree: if `target <= nums[l]`, return `l`; else if `target <= nums[r]`, return `r`; else return `len(nums)`. Three branches, each with its own comparison direction. Get the operators backward—`<` vs `<=`—and you return the wrong answer for exact matches. Forget the third branch and you crash on out-of-bounds cases.

This isn't about memorizing edge cases. It's about choosing a representation where edges are handled by the same logic as the common case. The closed interval does this. The open interval doesn't.

### Simpler Mental Model

The `l <= r` template asks you to think about the interval itself—it starts full and empties progressively. The `l + 1 < r` template asks you to think about two pointers converging until they're adjacent. The former aligns with the name "binary search" (divide the space), while the latter feels more like a pincer movement.

Both models work, but the interval-shrinking model scales better to variants. When you switch from exact search to `lower_bound`, you change one comparison operator but keep the same `return l` at the end. The loop invariant—elements before `l` are less than target, elements after `r` are greater—remains easy to reason about. You're not re-deriving exit conditions; you're tweaking what "greater" means.

In an interview, this difference shows. A candidate using `l <= r` can explain: "I maintain the invariant that everything before `l` fails my condition. When the loop exits, `l` is the first position that might pass." A candidate using `l + 1 < r` must explain: "I keep `l` and `r` as boundaries. When they're adjacent, I check both. For this variant, I return whichever one passes first. Or maybe I return the one after both if neither passes. Let me think..."

The first explanation is algorithmic. The second is case-by-case reasoning. Interviewers notice the difference.

### Code Length and Extensibility

For exact search, the `l <= r` template averages 6-8 lines. For `lower_bound`, `upper_bound`, rotated arrays, or peak finding, the core structure stays the same: loop until `l > r`, then `return l`. The return statement never changes. The comparison operator might flip, or the condition for moving `l` vs `r` might involve additional logic (like checking which half of a rotated array is sorted), but the exit logic is constant.

The `l + 1 < r` template requires 10-15 lines depending on the variant. Every time you adapt it—finding the first occurrence instead of any occurrence, or handling a rotated array—you must rethink the post-loop branching logic. What if `l` holds the answer? What if `r` does? What if neither does, and you need the position beyond both? Each variant forces you to re-derive this logic from scratch.

This compounding complexity makes `l + 1 < r` harder to maintain and extend. Each new problem is a fresh derivation rather than a mechanical application of a stable pattern. In an interview, this translates to visible hesitation: "Wait, for this problem, which one do I check first?" The `l <= r` candidate writes the loop, writes `return l`, and moves to testing.

### Testing Attention to Detail

Ultimately, the choice between templates reveals how a candidate approaches correctness. The `l <= r` template rewards candidates who establish a clear invariant and trust it to handle all cases uniformly. The `l + 1 < r` template forces candidates to enumerate cases and handle each explicitly.

Neither is wrong, but one is easier to get right under pressure. When the interviewer adds a twist—"Now find the last occurrence instead of the first" or "What if the array is empty?"—the candidate with a stable invariant adjusts confidently. The candidate with case-by-case logic revisits every branch, wondering which one needs updating.

Binary search tests your ability to think through details systematically. The `l <= r` template is the tool that makes systematic thinking easier.

## Implementation Details

### Preventing Integer Overflow

Always calculate the midpoint as `mid = l + (r - l) // 2` rather than `mid = (l + r) // 2`. In languages like C++ and Java, the sum `l + r` can overflow when both values are large, producing incorrect results or undefined behavior. Subtracting first (`r - l`) keeps the intermediate value bounded.

Python handles arbitrary-precision integers natively, so overflow isn't a concern. For performance, you can use the bitwise right-shift operator: `mid = (l + r) >> 1`. Shifting right by one bit is equivalent to integer division by two, but faster because it's a single CPU instruction.

This detail—overflow handling—is precisely the kind of thing interviewers watch for. It doesn't change the algorithm's correctness in Python, but knowing why you'd write it differently in C++ demonstrates awareness of how abstractions leak. A candidate who mentions overflow prevention unprompted signals that they've debugged production code, not just solved toy problems.

### Loop Invariants

A loop invariant is a property that remains true before and after each iteration. Maintaining clear invariants makes your code easier to verify and debug. More importantly, it's how you prove to an interviewer that your code handles every case correctly without testing all of them.

For the `l <= r` template, the invariant is: all elements in `[0, l)` are less than the target, and all elements in `(r, n)` are greater than the target. The search space `[l, r]` contains the only remaining candidates. When the loop exits (`l > r`), the invariant tells you that `l` is the first position where an element greater than or equal to the target would belong.

For the `l + 1 < r` template, the invariant is: `l` is the last known position less than the target, and `r` is the first known position greater than or equal to the target. The elements at positions `l` and `r` themselves are the boundaries. When the loop exits (`l + 1 == r`), you must check both positions to determine the answer.

State your invariant explicitly when coding in an interview. "I'm maintaining that everything before `l` is less than target" is a single sentence that makes your reasoning transparent. Without it, the interviewer has to reverse-engineer your logic from the pointer updates, wondering whether you know why it works or just memorized a template.

### Return Value Semantics

Binary search variants differ in what they return when the target isn't found, and this is where attention to detail matters most:

- **Exact search**: Return the index if found, otherwise return `-1`.
- **Lower bound** (`lower_bound`): Return the first position where an element is greater than or equal to the target. If all elements are smaller, return `len(nums)`. With the `l <= r` template, this is simply `return l` at the end—the invariant guarantees it's correct.
- **Upper bound** (`upper_bound`): Return the first position where an element is strictly greater than the target. Change the comparison to `nums[mid] <= target` to move `l = mid + 1`, then `return l`.

The beauty of the `l <= r` template is that these three variants differ only in the comparison operator inside the loop. The return statement stays `return l` for all boundary-finding problems. You're not asking "Which variable holds the answer now?"—you're asking "What does 'less than' mean for this variant?"

This is the test of systematic thinking. A candidate who understands the invariant can handle "find the last occurrence" by flipping one inequality and explaining why the invariant still holds. A candidate who memorized case logic has to re-derive everything.

## Variants and Extensions

Binary search's power lies in its adaptability. The core idea—halve the search space by comparing against a middle element—extends far beyond sorted arrays. Each variant tests a different aspect of your reasoning.

### Searching in Rotated Arrays

A rotated sorted array like `[4, 5, 6, 7, 0, 1, 2]` is really two sorted subarrays joined at a rotation point. You can't assume `mid` divides the array into two sorted halves, but you can always determine which half is sorted by comparing `nums[l]` to `nums[mid]`. Once you know one half is sorted, you can decide whether the target falls in that half using standard comparisons.

This variant tests whether you can decompose a complex condition into simpler checks. Candidates who try to find the rotation point first, then do two separate searches, miss the elegance: you can search and handle rotation simultaneously in a single pass. The boundary updates follow the same `l = mid + 1` / `r = mid - 1` pattern—only the decision logic changes.

### Searching in 2D Matrices

When a matrix is sorted row-wise and column-wise such that you can treat it as a flattened sorted array, the challenge is mapping one-dimensional indices to two-dimensional coordinates. For a matrix with `n` columns, `row = mid // n` and `col = mid % n` convert the 1D midpoint into 2D coordinates.

This tests whether you can abstract away irrelevant details. The matrix isn't really 2D for search purposes—it's a 1D array with a coordinate transformation. Candidates who recognize this apply the standard template unchanged. Candidates who try to search row-by-row or use a "staircase" walk from a corner write more code and miss the O(log(m×n)) optimization.

### Circular Arrays

Finding the smallest letter greater than a target in a circular sorted array introduces wrap-around: if no letter is greater than the target, you return the first letter. The solution uses modular arithmetic on the final index: `return letters[l % len(letters)]`. The loop itself is unchanged.

This tests boundary thinking. The "not found" case isn't an error—it has a defined meaning (wrap to the start). Candidates who try to special-case this with an `if` statement after the loop are fighting the algorithm. Candidates who recognize that `% len` encodes the wrap-around in one operator demonstrate cleaner abstractions.

### Finding Peaks and Valleys

Mountain arrays or rotated arrays ask you to find a local maximum or minimum rather than a target value. Here, you're not comparing against a target—you're comparing `nums[mid]` to its neighbors to decide which direction slopes upward. The template is the same; the comparison is different.

This tests whether you've internalized that binary search is about eliminating half the space based on any monotonic property, not just "less than / greater than a target." Candidates who can switch from value comparison to slope comparison without rewriting the loop structure demonstrate deeper understanding.

## Classic Problems

The following problems demonstrate binary search in different contexts. Each solution uses the `l <= r` template for consistency and clarity.

### 35. Search Insert Position

Find the target value's insertion position in a sorted array. This is the canonical lower bound problem: return the first index where the element is greater than or equal to the target.

<<< @/problems/35-search-insert-position/solution.py

---

### 34. Find First and Last Position of Element in Sorted Array

Find the first and last occurrence of the target in a sorted array. This requires two binary searches: one for lower bound (first occurrence) and one for upper bound (last occurrence).

<<< @/problems/34-find-first-and-last-position-of-element-in-sorted-array/solution.py

---

### 69. Sqrt(x)

Compute the integer square root of a non-negative integer. Binary search finds the largest value where `mid * mid <= x`.

<<< @/problems/69-sqrt-x/solution.py

---

### 33. Search in Rotated Sorted Array

Search for a target in a rotated sorted array. The key insight is determining which half of the array is properly sorted, then deciding whether the target lies in that half.

<<< @/problems/33-search-in-rotated-sorted-array/solution.py

---

### 744. Find Smallest Letter Greater Than Target

Find the smallest character in a sorted circular array that is strictly greater than the target. Use modular arithmetic to handle the wrap-around.

<<< @/problems/744-find-smallest-letter-greater-than-target/solution.py

---

<ChapterGraph chapter="binary-search" />

<ChapterIndex chapter="binary-search" />
