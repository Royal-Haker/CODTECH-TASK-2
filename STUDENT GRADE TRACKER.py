import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class GradeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Tracker By Rehaan")
        root.wm_iconbitmap("2.ico")

        self.records = []
        self.current_grades = []

        # Labels and entry fields for student information
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.class_label = tk.Label(root, text="Class:")
        self.class_label.pack()
        self.class_entry = tk.Entry(root)
        self.class_entry.pack()

        self.roll_label = tk.Label(root, text="Roll Number:")
        self.roll_label.pack()
        self.roll_entry = tk.Entry(root)
        self.roll_entry.pack()

        # Labels and entry fields for subject and grades
        self.subject_label = tk.Label(root, text="Subject:")
        self.subject_label.pack()
        self.subject_entry = tk.Entry(root)
        self.subject_entry.pack()

        self.grade_label = tk.Label(root, text="Grade:")
        self.grade_label.pack()
        self.grade_entry = tk.Entry(root)
        self.grade_entry.pack()

        # Button to add subject and grade to current grades list
        self.add_grade_button = tk.Button(root, text="Add Grade", command=self.add_grade)
        self.add_grade_button.pack()

        # Button to save the student record
        self.save_button = tk.Button(root, text="SAVE", command=self.save_record)
        self.save_button.pack(pady=10)  # Added padding here

        # Treeview widget for displaying records
        self.tree = ttk.Treeview(root, columns=("Name", "Class", "Roll Number", "Subjects", "Grades", "Average", "Letter Grade"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Class", text="Class")
        self.tree.heading("Roll Number", text="Roll Number")
        self.tree.heading("Subjects", text="Subjects")
        self.tree.heading("Grades", text="Grades")
        self.tree.heading("Average", text="Average")
        self.tree.heading("Letter Grade", text="Letter Grade")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def add_grade(self):
        subject = self.subject_entry.get()
        grade_str = self.grade_entry.get()

        if not (subject and grade_str):
            messagebox.showerror("Input Error", "Please fill in both subject and grade fields.")
            return

        try:
            grade = float(grade_str)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid grade.")
            return

        self.current_grades.append((subject, grade))
        messagebox.showinfo("Grade Added", f"Grade for {subject} added successfully.")

        # Clear entry fields after adding grade
        self.subject_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)

    def save_record(self):
        name = self.name_entry.get()
        class_ = self.class_entry.get()
        roll_number = self.roll_entry.get()

        if not (name and class_ and roll_number and self.current_grades):
            messagebox.showerror("Input Error", "Please fill in all fields and add at least one grade.")
            return

        subjects = [subject for subject, grade in self.current_grades]
        grades = [grade for subject, grade in self.current_grades]
        average_grade = sum(grades) / len(grades)
        letter_grade = self.calculate_letter_grade(average_grade)

        record = {
            "name": name,
            "class": class_,
            "roll_number": roll_number,
            "subjects": subjects,
            "grades": grades,
            "average": average_grade,
            "letter_grade": letter_grade
        }
        self.records.append(record)
        messagebox.showinfo("Record Saved", f"Record for {name} saved successfully.")

        # Add record to the treeview
        self.tree.insert("", tk.END, values=(
            name, class_, roll_number,
            ', '.join(subjects),
            ', '.join(map(str, grades)),
            f"{average_grade:.2f}",
            letter_grade
        ))

        # Clear entry fields and current grades after saving record
        self.name_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.current_grades = []

    def calculate_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeTracker(root)
    root.mainloop()
