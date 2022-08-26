student_scores = {

    "sidd": 99,
    "par": 86,
    "prachi": 78,
    "pank": 56,
    "tillu": 25,
    "darco": 15,
    "luffy": 5
}
student_grades = {}
# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

for keys in student_scores:
    values = student_scores[keys]

    if values in range(91, 100):
        student_grades[keys] = "outsatnding"

    elif values in range(81, 90):
        student_grades[keys] = "exceeds expection"
    elif values in range(71, 80):
        student_grades[keys] = "acceprable"
    else:
        student_grades[keys] = "fail"


print(student_grades)
