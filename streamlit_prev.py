import psycopg2
import streamlit as st

conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "heckpost@888", port = 5432) 



cur = conn.cursor()

st.title("PostgreSQL APP")

st.write("Enter Your Information:")
stud_id = st.number_input("ID: ")
stud_name = st.text_input("Name: ")
stud_roll = st.number_input("Roll No.: ")
bt = st.button("Save")

if bt:
    cur.execute("""
            INSERT INTO Stud (id,name,roll) VALUES 
            (%s,%s,%s);
            """,
            (stud_id,stud_name,stud_roll)
            )

    st.write("Data Saved Successfully!")

conn.commit()

cur.close()
conn.close()

