student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

# Print the student scores and names
for name, score in zip(student_names, student_scores):
    print(f"Student: {name} scored {score} in the exam")
