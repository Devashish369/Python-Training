import psycopg2

connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Devashish@123",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()
print("Database connected successfully")

insert_query = """
INSERT INTO employees (name, department, salary)
VALUES (%s, %s, %s)
"""

# cursor.execute(insert_query, ("Rahul", "Finance", 45000))
# connection.commit()

print("Record inserted successfully")

select_query = "SELECT * FROM employees"
cursor.execute(select_query)

records = cursor.fetchall()

for row in records:
    print(row)

update_query = """
UPDATE employees
SET salary = %s
WHERE name = %s
"""

cursor.execute(update_query, (55000, "Rahul"))
connection.commit()

print("Record updated successfully")

# delete_query = """
# DELETE FROM employees
# WHERE name = %s
# """

# cursor.execute(delete_query, ("Amit",))
# connection.commit()

print("Record deleted successfully")

select_query = "SELECT * FROM employees"
cursor.execute(select_query)

records = cursor.fetchall()

for row in records:
    print(row)
    
cursor.close()
connection.close()
print("Database connection closed")