# Step 15 (Continued): Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
cursor.execute("SELECT * FROM students WHERE birth_date >= '2000-01-01';")
birth_dates_after_2000 = cursor.fetchall()
print("Students with birth_date after 1/01/2000:")
print(birth_dates_after_2000)

# Step 16: Fetch the first four students. You have to order the four students alphabetically by last_name.
cursor.execute("SELECT * FROM students ORDER BY last_name LIMIT 4;")
first_four_students = cursor.fetchall()
print("First four students ordered by last_name:")
print(first_four_students)

# Step 17: Fetch the details of the youngest student.
cursor.execute("SELECT * FROM students ORDER BY birth_date DESC LIMIT 1;")
youngest_student = cursor.fetchone()
print("Youngest student:")
print(youngest_student)

# Step 18: Fetch three students skipping the first two students.
cursor.execute("SELECT * FROM students OFFSET 2 LIMIT 3;")
three_students_skip_first_two = cursor.fetchall()
print("Three students skipping the first two:")
print(three_students_skip_first_two)

# Close the cursor and connection
cursor.close()
conn.close()
