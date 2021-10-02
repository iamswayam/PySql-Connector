import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="7668",
    database="sway-db"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute(
#     "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# mycursor.executemany(sql, val)

val = [
    ("John", "Highway 21"), ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

sql = "DELETE FROM customers WHERE name = 'John'"

sql = "UPDATE customers SET name = 'Amway' WHERE name = 'Amy'"

mycursor.execute(sql)


mydb.commit()
# print(mycursor.rowcount, "record inserted.")
