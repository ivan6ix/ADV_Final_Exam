print("=== STUDENT ENROLLMENT SYSTEM ===")

full_name = input("Enter full name:")
address = input("Enter Address:")
age = input("Enter age:")

print("\nCourses Available:")
print("1. BSIT")
print("2. BSCS")
print("3. BSIS")

course_choice = input("Choose course (1-3):")

if course_choice == "1":
	course = "BSIT"
elif course_choice == "2":
	course = "BSCS"
else:
	course = "BSIS"

subjects = int(input("Enter number of subjects:"))
rate = 1500
total_payment = subjects * rate

print("\n==== ENROLLMENT SUMMARY ====")
print("Name:",full_name)
print("Address:", address)
print("Age:", age)
print("Course:", course)
print("Number of Subjects:", subjects)
print("Total Payment:P", total_payment)
