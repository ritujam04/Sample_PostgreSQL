from supabase import create_client
import psycopg2
import streamlit as st

# Supabase credentials (Replace with your actual credentials)
SUPABASE_URL = "https://xorqzrtiwnivgjtdospk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhvcnF6cnRpd25pdmdqdGRvc3BrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDA2NjI1MjUsImV4cCI6MjA1NjIzODUyNX0.ok-K_9ESDb9ncfjBDKcSb2Fl7g9Ur6Ee8MnFR4NXQFE"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
 
# PostgreSQL Connection
DATABASE_URL = "postgresql://postgres:heckpost@888.xyzcompany.supabase.co:5432/postgres"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

conn = get_db_connection()

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

