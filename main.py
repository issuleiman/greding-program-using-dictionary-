student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}


#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
  if   student_scores[name]>=100:
    student_grades[name]="Outstanding"
  elif student_scores[name]>=90:
    student_grades[name]="Exceeds Expectations"
  elif student_scores[name]>=80:
    student_grades[name]="Acceptable"
  elif student_scores[name]<=65:
    student_grades[name]="fail"
