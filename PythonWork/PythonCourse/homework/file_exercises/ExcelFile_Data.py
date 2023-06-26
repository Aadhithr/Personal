import xlsxwriter
import xlrd

Book = xlsxwriter.Workbook("c:\\work\\programming club\\homework\\Data_Sheet.xlsx")
Sheet = Book.add_worksheet()

Names = []
Elective_Grades = []
English_Grades = []
Science_Grades = []
History_Grades = []
PhysEd_Grades = []
Math_Grades = []

students = int(input("How many students are you entering"))

for i in range(0,students):
    # This loop is just to make sure to get an unique name. 
    # If not unique, it retries for 10 time before it gives-up.
    for j in range(10, 0):
        name = input("Enter the students name: ")
        if name in Names:
           print("This name exists, you may try %d more times" %(j))
           continue
        else:
            elective = int(input("Enter the students elective grade: "))
            english = int(input("Enter the students english grade: "))
            science = int(input("Enter the students science grade: "))
            history = int(input("Enter the students history grade: "))
            PhysEd = int(input("Enter the students P.E. grade: "))
            math = int(input("Enter the students math grade: "))
            Names.append(name)
            Elective_Grades.append(elective)
            English_Grades.append(english)
            Science_Grades.append(science)
            History_Grades.append(history)
            PhysEd_Grades.append(PhysEd)
            Math_Grades.append(math)
            break

Sheet.write("A1", "Names")
Sheet.write("B1", "Elective")
Sheet.write("C1", "English")
Sheet.write("D1", "Science")
Sheet.write("E1", "History")
Sheet.write("F1", "PhysEd")
Sheet.write("G1", "Math")

for n in range(len(Names)):
    Sheet.write(n+1, 0, Names[n])
    Sheet.write(n+1, 1, Elective_Grades[n])
    Sheet.write(n+1, 2, English_Grades[n])
    Sheet.write(n+1, 3, Science_Grades[n])
    Sheet.write(n+1, 4, History_Grades[n])
    Sheet.write(n+1, 5, PhysEd_Grades[n])
    Sheet.write(n+1, 6, Math_Grades[n])
    

Book.close()



workbook = xlrd.open_workbook("c:\\work\\programming club\\homework\\Data_Sheet.xlsx")
worksheet = workbook.sheet_by_index(0)

students = []
record = []
Student = {}


for x in range(1,worksheet.nrows):
    for y in range(worksheet.ncols):
        record.append(worksheet.cell(x,y).value)
    students.append(record)
    record = []
    x +=1

for m in range(len(students)):
    Student[students[m][0]] =  students[m][1:7]
    
score = input("Enter the students name to see their scores in the order of [Elective, English, Science, History, PhysEd, Math]  : ")
print(Student[score])

    
    
    