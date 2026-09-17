# Week 3: Grade Reporter & Bug Hunt

This repository contains solution scripts for PLP Python Week 3 exercises focused on control flow (loops and conditions).

## Files Overview
* `grade_reporter.py`: Iterates through student numerical scores, assigns letter grades using conditional statements, and outputs class statistics.
* `bug_hunt.py`: Features a fixed `while` loop that correctly calculates cumulative sums with annotated bug comments.

## Reflection Questions

The hardest bug to isolate in Part B was the variable scope error where `total_sum` was reset inside the loop body. Because Python raised no syntax or runtime exceptions, the script executed smoothly but produced inaccurate values. I detected the anomaly by comparing the actual printed output against the expected math result of 15 and manually tracing state changes line by line.
