- Grading system using dict object
```
student_marks={
    "jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket":99,
    "Prem":34
}
for student in student_marks:
    if student_marks[student]>90:
        print(f"{student} got A+ grade.")
    if student_marks[student]>81 and student_marks[student]<90:
        print(f"{student} got A grade.")
    if student_marks[student]>71 and student_marks[student]<80:
        print(f"{student} got B+ grade.")
    if student_marks[student]>61 and student_marks[student]<70:
        print(f"{student} got B grade.")
    if student_marks[student]>51 and student_marks[student]<60:
        print(f"{student} got C grade.")
    if student_marks[student]>41 and student_marks[student]<50:
        print(f"{student} got D grade.")
    if student_marks[student]<40:
        print(f"{student} got F grade.")
```
