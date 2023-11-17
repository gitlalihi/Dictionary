#Program to create grade calculator in Python

def calculate_grade(average_score):
    if 90 <= average_score <= 100:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'

def main():
   
    num_subjects = int(input("Enter the number of subjects: "))
    subjects = {}
    for _ in range(num_subjects):
        subject_name = input("Enter the subject name: ")
        subject_score = float(input(f"Enter the score for {subject_name}: "))
        subjects[subject_name] = subject_score
    average_score = sum(subjects.values()) / num_subjects
    grade = calculate_grade(average_score)
    print(f"\nAverage Score: {average_score}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
