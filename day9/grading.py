student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

def selectGrade(score):
    if score >= 91 and score <= 100:
        return "Outstanding"
    elif score >= 81 and score <= 90:
        return "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        return "Acceptable"
    else:
        return "Fail"

for student, score in student_scores.items():
    student_grades[student] = selectGrade(score)

print(student_grades)