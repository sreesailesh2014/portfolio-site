from tabulate import tabulate

print("==============STUDENT MANAGEMENT SYSTEM==============")
student_name = input("Enter student name:")
student_id = str(input("Enter student ID:"))
age = int(input("Enter age:")) 
maths = int(input("Enter maths mark:"))
science = int(input("Enter science mark:"))
english = int(input("Enter english mark:"))
computer = int(input("Enter computer mark:"))
social = int(input("Enter social mark:"))

if(maths<0 or maths>100 or science<0 or science>100 or english<0 or english>100 or social < 0 or social > 100 or computer < 0 or computer > 100):
    print("Invalid marks entered! Marks should be between 0 and 100.")
else:
    total = maths + science + english + computer + social
    average = total / 5
    if(maths <35 or science <35 or english<35 or computer <35 or social <35 or average <35):
        promotion = "Fail"
        passtype = "No classification"
    else:
        promotion = "Pass"
        if (35 <= average <50):
            passtype = "Just Pass"
        elif (50 <= average <60):
            passtype = "Average"
        elif (60 <= average <75):
            passtype = "First Class"
        elif (75 <= average <90):
            passtype = "Distinction"
        elif (90 <= average <=100):
            passtype = "Distinction with Gold Medal"

    # Table data
    table = [
        ["Name", student_name],
        ["ID", student_id],
        ["Age", age],
        ["Maths", maths],
        ["Science", science],
        ["English", english],
        ["Computer", computer],
        ["Social", social],
        ["Total", total],
        ["Average", average],
        ["Promotion", promotion],
        ["Passtype", passtype]
    ]

    print("\n----------STUDENT DETAILS----------")
    print(tabulate(table, headers=["Field", "Value"], tablefmt="grid"))