grades = []
while True:
    print("\n1. Add Grade\n2. View Average\n3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        subject = input("Subject: ")
        score = float(input("Score: "))
        grades.append({"subject": subject, "score": score})
        print("Grade added!")
    elif choice == "2":
        if grades:
            total = sum(g["score"] for g in grades) / len(grades)
            print("Grades:")
            for g in grades:
                print(f"- {g['subject']}: {g['score']}")
            print(f"Average = {total:.2f}")
        else:
            print("No grades yet.")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
