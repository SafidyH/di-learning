import requests
import random
import psycopg2

# REST Countries API endpoint
REST_COUNTRIES_API = "https://restcountries.com/v3.1/all"

# Create a database connection
def create_connection():
    return psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )

# Create the countries table
def create_countries_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = """CREATE TABLE IF NOT EXISTS countries (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    capital VARCHAR(100),
                    flag TEXT,
                    subregion VARCHAR(100),
                    population INT
                );"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error creating table: ", e)

# Insert a new country into the countries table
def insert_country(name, capital, flag, subregion, population):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (name, capital, flag, subregion, population))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error inserting country: ", e)

# Fetch 10 random countries from the API
def fetch_random_countries():
    try:
        response = requests.get(REST_COUNTRIES_API)
        if response.status_code == 200:
            countries_data = response.json()
            random_countries = random.sample(countries_data, 10)
            return random_countries
        else:
            print("Failed to fetch data from the API.")
            return []
    except Exception as e:
        print("Error fetching data from the API: ", e)
        return []

def main():
    create_countries_table()
    random_countries = fetch_random_countries()
    
    for country in random_countries:
        name = country.get("name").get("common")
        capital = country.get("capital")[0] if country.get("capital") else None
        flag = country.get("flags").get("png") if country.get("flags") else None
        subregion = country.get("subregion")
        population = country.get("population")

        insert_country(name, capital, flag, subregion, population)
        print(f"Country '{name}' inserted into the database.")

if __name__ == "__main__":
    main()
