# Interview Guide

Last updated: 2026-08-02

## Practice principles

- Build knowledge structures instead of memorizing isolated answers.
- Repeat each problem until the invariant and tradeoffs are recallable without prompts.
- Use feedback to correct reasoning, explanation, and implementation.
- Review by technique and by prerequisite chain.

## Seven-step interview workflow

1. **Clarify:** confirm inputs, outputs, constraints, and ambiguous behavior.
2. **Choose examples:** use representative cases rather than only trivial or exceptional inputs.
3. **Establish a baseline:** state a correct direct solution before optimizing it.
4. **Optimize:** identify the bottleneck, enumerate alternatives, and improve one constraint at a time.
5. **Walk through:** prove the key invariant and state time and space complexity.
6. **Implement:** use precise names, explicit control flow, and small cohesive functions.
7. **Test:** start with a small normal case, then cover boundaries and large inputs.

## Coding standards

- Match the language's established naming and formatting conventions.
- Comment the invariant or non-obvious move, not the syntax.
- Add type annotations where the language supports them.
- Handle invalid inputs only when the problem contract permits them.
- Test normal, boundary, and negative cases where applicable.

Language references:

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)

[Back to the repository overview](../ReadMe.md)
