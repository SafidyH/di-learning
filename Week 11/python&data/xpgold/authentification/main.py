import psycopg2
import bcrypt

# Create a database connection
def create_connection():
    return psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )

# Create the users table
def create_users_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(100) NOT NULL
                );"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error creating table: ", e)

# Insert a new user into the users table
def insert_user(username, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        query = "INSERT INTO users (username, password) VALUES (%s, %s);"
        cursor.execute(query, (username, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error inserting user: ", e)

# Get user details from the users table
def get_user(username):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "SELECT username, password FROM users WHERE username = %s;"
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        return user_data
    except Exception as e:
        print("Error getting user: ", e)
        return None

def main():
    create_users_table()

    while True:
        action = input("Enter 'login' or 'exit': ")
        if action == 'exit':
            break
        elif action == 'login':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            user_data = get_user(username)
            if user_data:
                if bcrypt.checkpw(password.encode('utf-8'), user_data[1].encode('utf-8')):
                    print("You are now logged in.")
                else:
                    print("Invalid password.")
            else:
                signup = input("User does not exist. Do you want to sign up? (Y/N): ").upper()
                if signup == 'Y':
                    password_confirm = input("Enter your password again: ")
                    if password == password_confirm:
                        insert_user(username, password)
                        print("You are now signed up and logged in.")
                    else:
                        print("Password mismatch.")
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main()
