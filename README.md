# PostgreSQL Driver

The PostgreSQL Driver is a Python class that simplifies interaction with a PostgreSQL database table. It is designed to work with a table that has the following columns: `user_id`, `name`, `age`, and `phone`. The driver allows you to retrieve data from the table and return it as JSON. If the `phone` column has a null value, it won't be included in the generated JSON output.

## Prerequisites

Before using the driver, ensure that you have the following:

- Python 3 installed on your system
- `psycopg2` package installed. You can install it using `pip install psycopg2`.
- Make sure the postgresql_driver.py file is located in the same directory as your script or module, or provide the correct path when importing the driver class.

## Usage

1. Import the `PostgreSQLDriver` class into your Python script or module:

   ```python
   from postgresql_driver import PostgreSQLDriver
   ```

2. Create an instance of the PostgreSQLDriver class, providing the required database connection details:

   ```python
   driver = PostgreSQLDriver(
      host="your_host",
      database="your_database",
      user="your_username",
      password="your_password"
   )
   ```

- Replace "your_host", "your_database", "your_username", and "your_password" with the actual values for your PostgreSQL database connection.

3. Connect to the PostgreSQL database:

   ```python
   driver.connect()
   ```

4. Retrieve data from a table and print it as JSON:

   ```python
   table_name = "your_table"
   json_result = driver.get_data_as_json(table_name)
   print(json_result)
   ```

- Replace "your_table" with the name of the table from which you want to retrieve data.

5. Disconnent from the database:

   ```python
   driver.disconnect()
   ```

## Example

```python
from postgresql_driver import PostgreSQLDriver

# Create an instance of the PostgreSQLDriver
driver = PostgreSQLDriver(
   host="your_host",
   database="your_database",
   user="your_username",
   password="your_password"
)

# Connect to the PostgreSQL database
driver.connect()

# Retrieve data from the table and print as JSON
table_name = "your_table"
json_result = driver.get_data_as_json(table_name)
print(json_result)

# Disconnect from the database
driver.disconnect()
```
