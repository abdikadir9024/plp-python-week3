# Fixed version of bug_hunt.py with required # BUG: annotations

# BUG: Bug 1 - Logic/Off-by-one Error
# The original condition (count < 5) stopped the loop before adding 5, leading to an incorrect total of 10.
# Fix: Changed condition to count <= 5 or updated increment/condition flow.

# BUG: Bug 2 - Infinite Loop / Incorrect Variable Update
# The loop variable wasn't updating properly toward the exit condition inside the iteration block.
# Fix: Ensured `count += 1` executes reliably within the loop body.

# BUG: Bug 3 - Variable Scope / Incorrect Accumulation
# The total sum variable was re-initialized to 0 inside the loop body, resetting the sum on every iteration.
# Fix: Moved initialization of `total_sum = 0` outside the loop block.

total_sum = 0
count = 1

while count <= 5:
    total_sum += count
    count += 1

print(f"Sum of 1 to 5 is: {total_sum}")