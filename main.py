import psycopg2

connection = psycopg2.connect(database="pdb", user="puser",
                              password="12345", host="151.248.113.116", port=5432)

with connection:
    with connection.cursor() as cur:
        try:
            cur.execute("DELETE FROM users")
            cur.execute()
            cur.execute()
            cur.execute()
        except:
            connection.rollback()

cursor = connection.cursor()

# cursor.execute("INSERT INTO users (login, password, name) VALUES (%s, %s, %s)",
#                ("user2", "user2", "user2"))
# connection.commit()

cursor.execute("SELECT * FROM users")

for currentUser in cursor:
    print(currentUser)

cursor.close()
connection.close()
