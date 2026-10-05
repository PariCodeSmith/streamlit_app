import streamlit as st
from sqlalchemy import text, create_engine
# import pymysql  # Ensure pymysql is installed
import urllib.parse

# Database connection setup
DB_HOST = "127.0.0.1" 
DB_PORT = "3306"
DB_NAME = "student_database"
DB_USER = "root"
DB_PASSWORD = urllib.parse.quote("Aditya@07")  # Encode special characters

# SQLAlchemy engine
db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# function to fetch data
def fetch_data():
    query = text("SELECT * FROM Student_Data")
    try:
        with engine.connect() as conn:
            result = conn.execute(query)
            columns = result.keys()
            data =[dict(zip(columns ,row)) for row in result]
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []
    
#Stremlit UI
st.title("View Student Data")

data = fetch_data()

if data:
    st.table(data)
else:
    st.info("No data found in the database")