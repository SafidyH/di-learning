import psycopg2

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="your_host",
                port="your_port"
            )
            cursor = connection.cursor()
            query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);"
            cursor.execute(query, (self.item_name, self.item_price))
            connection.commit()
            cursor.close()
            connection.close()
            print("Item was added successfully.")
        except Exception as e:
            print("Error: ", e)

    def delete(self):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="your_host",
                port="your_port"
            )
            cursor = connection.cursor()
            query = "DELETE FROM Menu_Items WHERE item_name = %s;"
            cursor.execute(query, (self.item_name,))
            connection.commit()
            cursor.close()
            connection.close()
            print("Item was deleted successfully.")
        except Exception as e:
            print("Error: ", e)

    def update(self, new_name, new_price):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="your_host",
                port="your_port"
            )
            cursor = connection.cursor()
            query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;"
            cursor.execute(query, (new_name, new_price, self.item_name))
            connection.commit()
            cursor.close()
            connection.close()
            print("Item was updated successfully.")
        except Exception as e:
            print("Error: ", e)
