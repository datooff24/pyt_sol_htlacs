def grade(mark):
    if mark >= 75:
        final_grade = "First"
    elif (mark >= 70) and (mark < 75):
        final_grade = "Upper Second"
    elif (mark >= 60) and (mark < 70):
        final_grade = "Second"
    elif (mark >= 50) and (mark < 60):
        final_grade = "Third"
    elif (mark >= 45) and (mark < 50):
        final_grade = "F1 Supp"
    elif (mark >= 40) and (mark < 45):
        final_grade = "F2"
    elif (mark >= 0) and (mark < 40):
        final_grade = "F3"
    else:
        print("Enter a positive mark")
        return
    return final_grade


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for i in xs:
    print("Your exam mark is ", i, " so your final grade is ", grade(i))
