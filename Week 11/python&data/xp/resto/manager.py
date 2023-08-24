import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="your_host",
                port="your_port"
            )
            cursor = connection.cursor()
            query = "SELECT * FROM Menu_Items WHERE item_name = %s;"
            cursor.execute(query, (item_name,))
            item_data = cursor.fetchone()
            cursor.close()
            connection.close()
            if item_data:
                return MenuItem(item_data[1], item_data[2])
            else:
                return None
        except Exception as e:
            print("Error: ", e)

    @classmethod
    def all_items(cls):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="your_host",
                port="your_port"
            )
            cursor = connection.cursor()
            query = "SELECT * FROM Menu_Items;"
            cursor.execute(query)
            items_data = cursor.fetchall()
            cursor.close()
            connection.close()
            items = []
            for item_data in items_data:
                items.append(MenuItem(item_data[1], item_data[2]))
            return items
        except Exception as e:
            print("Error: ", e)
            return []
