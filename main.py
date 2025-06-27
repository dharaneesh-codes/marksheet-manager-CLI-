import csv
import pandas as pd
filename="students.csv"
def init_file():
    try:
        with open(filename,'x',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID","Name","Physics","Math","Chemistry","Average","Grade"])
    except FileExistsError:
        pass
init_file()
def view_students():
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print('\t'.join(row))
def add_student():
    id =input("Enter Student ID: ")
    name =input("Enter Student Name: ")
    math =int(input("Enter Math Marks: "))
    physics =int(input("Enter Physics Marks: "))
    chem =int(input("Enter Chemistry Marks: "))
    avg =(math + physics + chem)/3
    if avg >= 95:
        avg >= '0'
    elif avg >= 90:
        grade ='A+'
    elif avg >= 80:
        grade ='A'
    elif avg >= 70:
        grade ='B+'
    elif avg >= 60:
        grade ='B'
    elif avg >= 50:
        grade ='C'
    else:
        grade ='D'
    with open(filename,'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, math, physics, chem, round(avg, 2), grade])
    print(" Student Added Successfully\n")
def search_student():
    key = input("Enter Student ID or Name to search: ").lower()
    found = False
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if key in row[0].lower() or key in row[1].lower():
                print('\t'.join(row))
                found = True
    if not found:
        print(" Student not found.")
def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    rows = []
    deleted = False
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != delete_id:
                rows.append(row)
            else:
                deleted = True
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    if deleted:
        print("Student deleted.")
    else:
        print("No matching student found.")
def top_scorer():
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        top_student = None
        top_score = -1
        for row in reader:
            try:
                avg = float(row[5])
                if avg>top_score:
                    top_score = avg
                    top_student = row
            except:
                continue
    if top_student:
        print("\n Top Scorer:")
        print(f"ID: {top_student[0]}")
        print(f"Name: {top_student[1]}")
        print(f"Average: {top_student[5]} | Grade: {top_student[6]}")
    else:
        print("No students found.")
def update_student():
    target_id = input("Enter Student ID to update: ")
    updated = False
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == target_id:
                print("Student found. Enter new marks:")
                try:
                    math = int(input("Enter new Math marks: "))
                    physics = int(input("Enter new Physics marks: "))
                    chem = int(input("Enter new Chemistry marks: "))
                    if not all(0 <= mark <= 100 for mark in [math, physics, chem]):
                        print("Marks must be between 0 and 100.")
                        return
                    avg = (math + physics + chem) / 3
                    if avg >= 90:
                        grade = 'A+'
                    elif avg >= 75:
                        grade = 'A'
                    elif avg >= 60:
                        grade = 'B'
                    elif avg >= 50:
                        grade = 'C'
                    else:
                        grade = 'D'
                    row = [row[0], row[1], math, physics, chem, round(avg, 2), grade]
                    updated = True
                except ValueError:
                    print("Invalid input enter numbers.")
                    return
            rows.append(row)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    if updated:
        print("Student record updated successfully.")
    else:
        print("Student not found.")
def export_to_excel():
    df=pd.read_csv(filename)
    df.to_excel(filename,index=False)
    print("Converted to Excel Sheet")
def main():
    while True:
        print("\n STUDENT MARKSHEET MANAGER")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Show Top Scorer")
        print("6. Update Student Details")
        print("7. Export as Excel sheet")
        print("8. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            top_scorer()
        elif choice == '6':
            update_student()
        elif choice == '7':
            export_to_excel
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
main()