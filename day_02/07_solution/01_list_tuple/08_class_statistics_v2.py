student_scores = [98, 75, 100, 86, 100, 3]

# Print the average score
average_score = sum(student_scores) / len(student_scores)
print(average_score)

# Print the rankings, highest to lowest
print(sorted(student_scores, reverse=True))
