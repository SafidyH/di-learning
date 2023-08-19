import psycopg2

# Step 1: Create a database called bootcamp
conn = psycopg2.connect(
    dbname="postgres",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute("CREATE DATABASE bootcamp;")

cursor.close()
conn.close()

# Step 2: Connect to the bootcamp database
conn = psycopg2.connect(
    dbname="bootcamp",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Step 3: Create the students table
cursor.execute("""
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        birth_date DATE NOT NULL
    );
""")

# Step 4: Insert data into the students table
students_data = [
    (1, 'Marc', 'Benichou', '1998-11-02'),
    (2, 'Yoan', 'Cohen', '2010-12-03'),
    (3, 'Lea', 'Benichou', '1987-07-27'),
    (4, 'Amelia', 'Dux', '1996-04-07'),
    (5, 'David', 'Grez', '2003-06-14'),
    (6, 'Omer', 'Simpson', '1980-10-03'),
]

cursor.executemany("INSERT INTO students (id, first_name, last_name, birth_date) VALUES (%s, %s, %s, %s);", students_data)

# Step 5: Fetch all of the data from the table
cursor.execute("SELECT * FROM students;")
all_data = cursor.fetchall()
print("All data:")
print(all_data)

# Step 6: Fetch all of the students' first_names and last_names
cursor.execute("SELECT first_name, last_name FROM students;")
names_data = cursor.fetchall()
print("First names and last names:")
print(names_data)

# Step 7: Fetch the student whose id is equal to 2
cursor.execute("SELECT * FROM students WHERE id = 2;")
student_id_2 = cursor.fetchone()
print("Student with id = 2:")
print(student_id_2)

# Step 8: Fetch the student whose last_name is Benichou AND first_name is Marc
cursor.execute("SELECT * FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';")
benichou_marc = cursor.fetchone()
print("Student with last_name = 'Benichou' AND first_name = 'Marc':")
print(benichou_marc)

# Step 9: Fetch the students whose last_names are Benichou OR first_names are Marc
cursor.execute("SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';")
benichou_or_marc = cursor.fetchall()
print("Students with last_name = 'Benichou' OR first_name = 'Marc':")
print(benichou_or_marc)

# Step 10: Fetch the students whose first_names contain the letter a
cursor.execute("SELECT * FROM students WHERE first_name LIKE '%a%';")
names_with_a = cursor.fetchall()
print("Students with first_name containing 'a':")
print(names_with_a)

# Step 11: Fetch the students whose first_names start with the letter a
cursor.execute("SELECT * FROM students WHERE first_name LIKE 'a%';")
names_start_with_a = cursor.fetchall()
print("Students with first_name starting with 'a':")
print(names_start_with_a)

# Step 12: Fetch the students whose first_names end with the letter a
cursor.execute("SELECT * FROM students WHERE first_name LIKE '%a';")
names_end_with_a = cursor.fetchall()
print("Students with first_name ending with 'a':")
print(names_end_with_a)

# Step 13: Fetch the students whose second to last letter of their first_names are a
cursor.execute("SELECT * FROM students WHERE first_name LIKE '%a_';")
second_last_a = cursor.fetchall()
print("Students with first_name containing 'a' as the second last letter:")
print(second_last_a)

# Step 14: Fetch the students whose id's are equal to 1 AND 3
cursor.execute("SELECT * FROM students WHERE id IN (1, 3);")
ids_1_and_3 = cursor.fetchall()
print("Students with id = 1 OR id = 3:")
print(ids_1_and_3)

# Step 15: Fetch the students whose birth_dates are equal to or come after 
