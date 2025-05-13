import sqlite3

# Connect to SQLite database (creates one if it doesn't exist)
con = sqlite3.connect("students.db")
cursor = con.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    try:
        cursor.execute("INSERT INTO students (roll_no, name, age, course) VALUES (?, ?, ?, ?)",
                       (roll, name, age, course))
        con.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Roll number already exists.")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- All Students ---")
    for row in rows:
        print(f"Roll No: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

def search_student():
    roll = int(input("Enter Roll No to search: "))
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    row = cursor.fetchone()
    if row:
        print(f"Found: Roll No: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    else:
        print("Student not found.")

def update_student():
    roll = int(input("Enter Roll No to update: "))
    name = input("Enter new Name: ")
    age = int(input("Enter new Age: "))
    course = input("Enter new Course: ")
    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE roll_no=?",
                   (name, age, course, roll))
    con.commit()
    if cursor.rowcount:
        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    roll = int(input("Enter Roll No to delete: "))
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    con.commit()
    if cursor.rowcount:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    con.close()
    