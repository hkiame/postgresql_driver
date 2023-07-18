import psycopg2
import json

class PostgreSQLDriver:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL:", error)

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    def get_data(self, table_name):
        try:
            query = f"SELECT user_id, name, age, phone FROM {table_name} ORDER BY user_id ASC"
            self.cur.execute(query)
            rows = self.cur.fetchall()

            data = []
            for row in rows:
                user_id, name, age, phone = row
                # Exclude phone if it is NULL
                if phone is not None:
                    data.append({
                        'user_id': user_id,
                        'name': name,
                        'age': age,
                        'phone': phone
                    })
                else:
                    data.append({
                        'user_id': user_id,
                        'name': name,
                        'age': age
                    })

            return data
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while retrieving data from PostgreSQL:", error)
            return []

    def get_data_as_json(self, table_name):
        data = self.get_data(table_name)

        result = {
            'status_code': 200,
            'data': data
        }

        json_data = json.dumps(result)
        return json_data
