# import csv

# def is_identity_number_present(file_path, identity_number, column_index):
#     try:
#         with open(file_path, 'r') as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader:
#                 if len(row) > column_index and identity_number in row[column_index]:
#                     return True
#         return False
#     except Exception as e:
#         print(f"Error: {e}")
#         return False

# # Take user input for file path, identity number, and column index
# file_path = input("Enter the path to your CSV file: ")
# identity_number = input("Enter the identity number to check: ")
# column_index = int(input("Enter the column index to check (0-based index): "))

# result = is_identity_number_present(file_path, identity_number, column_index)

# if result:
#     print(f"The identity number '{identity_number}' is present in column {column_index} of the CSV file.")
# else:
#     print(f"The identity number '{identity_number}' is not present in column {column_index} of the CSV file.")


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

def is_identity_number_present(file_path, identity_number, column_index):
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > column_index and identity_number in row[column_index]:
                    return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_identity_number():
    file_path = file_entry.get()
    identity_number = identity_entry.get()
    try:
        column_index = int(column_entry.get())
        result = is_identity_number_present(file_path, identity_number, column_index)
        if result:
            messagebox.showinfo("Result", f"The identity number '{identity_number}' is present in column {column_index} of the CSV file.")
        else:
            messagebox.showinfo("Result", f"The identity number '{identity_number}' is not present in column {column_index} of the CSV file.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the column index.")

# Tkinter GUI
root = tk.Tk()
root.title("Identity Number Checker")

# File Path Entry
file_label = ttk.Label(root, text="Enter CSV File Path:")
file_label.pack()
file_entry = ttk.Entry(root, width=50)
file_entry.pack()

# Identity Number Entry
identity_label = ttk.Label(root, text="Enter Identity Number:")
identity_label.pack()
identity_entry = ttk.Entry(root, width=20)
identity_entry.pack()

# Column Index Entry
column_label = ttk.Label(root, text="Enter Column Index (0-based):")
column_label.pack()
column_entry = ttk.Entry(root, width=5)
column_entry.pack()

# Check Button
check_button = ttk.Button(root, text="Check Identity Number", command=check_identity_number)
check_button.pack()

root.mainloop()
