# Exact input data required
scores = [72, 45, 90, 61, 38]

# Track metrics
passes = 0
failures = 0
total_score = 0

print("Individual Grades & Status:")
print("-" * 30)

# Loop through scores and apply specific grading scale
for score in scores:
    total_score += score
    
    # Grading scale:
    # 80 and above: A
    # 70 to 79: B
    # 50 to 69: C
    # Below 50: F
    if score >= 80:
        grade = "A"
        passes += 1
    elif score >= 70:
        grade = "B"
        passes += 1
    elif score >= 50:
        grade = "C"
        passes += 1
    else:
        grade = "F"
        failures += 1
        
    print(f"Score: {score} -> Grade: {grade}")

# Calculate average rounded to 1 decimal place
average = round(total_score / len(scores), 1)

print("\nSummary Metrics:")
print("-" * 30)
print(f"Passes: {passes}")
print(f"Failures: {failures}")
print(f"Average: {average}")