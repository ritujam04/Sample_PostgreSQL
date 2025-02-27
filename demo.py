import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "heckpost@888", port = 5432) 

cur = conn.cursor()

#Create Table 
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS Stud(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    roll INT);
    """
)

#Insert Data
'''
cur.execute("""
            INSERT INTO Stud (id,name, roll) VALUES
            (2,'PQR',65);
            """)
'''

#Display Data
cur.execute("""
            SELECT * FROM Stud;
            """)

#print(cur.fetchone())
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()