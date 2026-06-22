# Core Analysis Script Shells

## Purpose
These files define the intended analysis workflow before a final implementation language is chosen. They are language-agnostic shells, not executable scripts yet.

## Planned workflow
1. `01_screening_shell.md`
   - build the main confirmatory sample from raw responses
2. `02_constructs_shell.md`
   - score retained constructs and document item handling
3. `03_main_results_shell.md`
   - generate the main manuscript tables and mechanism-path results
4. `04_robustness_shell.md`
   - run bounded sensitivity and supplemental checks only after the main results are fixed

## Rule
- When the final analysis language is chosen, each shell should be translated into one real script while preserving the same numbering and responsibility split.
