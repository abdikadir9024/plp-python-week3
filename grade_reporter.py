# List of numeric test grades
grades = [88, 92, 79, 64, 95, 81]

# Initialize variables to build up totals and counts
total_score = 0
letter_counts = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

print("Individual Grades & Letter Categories:")
print("-" * 38)

# Loop through each grade and apply conditional logic
for grade in grades:
    total_score += grade
    
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"
        
    letter_counts[letter] += 1
    print(f"Grade: {grade} -> Letter Grade: {letter}")

# Calculate average
average = total_score / len(grades)

print("\nSummary Report:")
print("-" * 38)
print(f"Total Students Processed: {len(grades)}")
print(f"Class Average: {average:.2f}")
print("Grade Distribution:")
for letter, count in letter_counts.items():
    print(f"  {letter}: {count}")