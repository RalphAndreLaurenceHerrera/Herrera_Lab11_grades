'''
Input 5 student grade and identify the following:

Average Grade:
Number of students with passing grade:
Passing percentage:

**display the grades that have been inputted
**Passing grade is 75 and above
**Grade input must be between 40-100
'''
SumOfAllGrade = 0
StudentGradeList = []
loopcounter = 0
StudentGradePassers = 0
SOrNot = ""
while loopcounter < 5:
    
    if loopcounter == 0:
        rank = "1st"
    elif loopcounter == 1:
        rank = "2nd"
    elif loopcounter == 2:
        rank = "3rd"
    elif loopcounter == 3:
        rank = "4th"
    elif loopcounter == 4:
        rank = "5th"
        
    StudentGrade = float(input(f"Enter {rank} student's grade: "))
    
    if 40 <= StudentGrade <= 100:
        loopcounter += 1
        SumOfAllGrade += StudentGrade
        StudentGradeList.append(StudentGrade)
        if StudentGrade >= 75:
            StudentGradePassers +=1
    else:
        print("Please try again. Grade must be only be between or equal to 40 and 100.")

AverageStudentGrade = SumOfAllGrade / len(StudentGradeList)
StudentGradePassersPercentage = StudentGradePassers / len(StudentGradeList) * 100

if StudentGradePassers >= 2 :
    SOrNot = "s"
    
print(f"Grades: {StudentGradeList}")
print(f"Average Grade: {AverageStudentGrade}")
print("Number of students with passing grade:", StudentGradePassers, "Student" + SOrNot)
print(f"Passing Percentage: {StudentGradePassersPercentage}%")