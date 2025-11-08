def get_quiz_score():
    return float(input("Quiz score: "))


def get_exam_score():
    return float(input("Exam score: "))


def compute_average(quiz, exam):
    return (quiz * 0.4) + (exam * 0.6)


def check_pass(average):
    if average >= 60:
        return "Pass!"
    return "Fail!"


quiz_score = get_quiz_score()
exam_score = get_exam_score()
average_score = compute_average(quiz_score, exam_score)
print("Status:", check_pass(average_score))
