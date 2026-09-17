# BUG: 1. SyntaxError - Missing colon (:) at the end of the while loop statement header (`while count < 5`).
# BUG: 2. LogicError - Off-by-one loop boundary condition (`count < 5` stops at 4 instead of including 5).
# BUG: 3. TypeError - Invalid string concatenation attempting to add an integer (`total`) directly to a string without conversion (`str(total)` or f-string).

total = 0
count = 1

while count <= 5:
    total += count
    count += 1

print("Sum of 1 to 5 is: " + str(total))