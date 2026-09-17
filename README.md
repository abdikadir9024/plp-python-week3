# Week 3: Grade Reporter & Bug Hunt

This repository contains solution scripts for PLP Python Week 3 exercises focused on control flow, list processing, conditional branching, and debugging.

## Files Overview
* `grade_reporter.py`: Iterates through the specified list of student scores (`[72, 45, 90, 61, 38]`), classifies them into four letter tiers (A, B, C, F), and outputs total passes, failures, and class average rounded to one decimal place.
* `bug_hunt.py`: Features a corrected `while` loop that outputs "Sum of 1 to 5 is: 15" with three `# BUG:` comments detailing the SyntaxError, LogicError, and TypeError in the original snippet.

## Reflection Questions

The hardest bug to diagnose in Part B was the off-by-one logic error (`count < 5`). Unlike the missing colon (SyntaxError) or string concatenation issue (TypeError) which immediately raised explicit Python exceptions, the boundary condition ran smoothly without crashing. I identified it by manually stepping through the loop counters and observing that the total accumulated to 10 instead of the expected 15.