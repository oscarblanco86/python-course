import sqlite3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class GradeDatabase:
    def __init__(self, db_name="grades.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY,
                period1 INTEGER,
                period2 INTEGER,
                period3 INTEGER,
                period4 INTEGER
            )
        """)
        self.conn.commit()

    def add_grades(self, period1, period2, period3, period4):
        self.cursor.execute("INSERT INTO grades (period1, period2, period3, period4) VALUES (?, ?, ?, ?)",
                            (period1, period2, period3, period4))
        self.conn.commit()

    def get_grades(self):
        self.cursor.execute("SELECT * FROM grades")
        return self.cursor.fetchall()



# Initialize database
db = GradeDatabase()

st.title("📊 Student Grade Tracker")

# Input grades for four periods
period1 = st.number_input("Enter Period 1 grade", min_value=0, max_value=100)
period2 = st.number_input("Enter Period 2 grade", min_value=0, max_value=100)
period3 = st.number_input("Enter Period 3 grade", min_value=0, max_value=100)
period4 = st.number_input("Enter Period 4 grade", min_value=0, max_value=100)

if st.button("Save Grades"):
    db.add_grades(period1, period2, period3, period4)
    st.success("Grades saved successfully!")

# Fetch stored grades
grades = db.get_grades()

if grades:
    # Convert grades to DataFrame
    df = pd.DataFrame(grades, columns=["ID", "Period 1", "Period 2", "Period 3", "Period 4"])
    
    # Calculate averages
    df["Average"] = df.iloc[:, 1:].mean(axis=1)
    
    # Display table
    st.subheader("📋 Grades Overview")
    st.dataframe(df)

    # Visualization - Line Chart
    st.subheader("📈 Grade Trends")
    fig, ax = plt.subplots()
    for index, row in df.iterrows():
        ax.plot(["Period 1", "Period 2", "Period 3", "Period 4"], row[1:5], marker='o', label=f"Student {row['ID']}")
    
    ax.set_xlabel("Periods")
    ax.set_ylabel("Grades")
    ax.set_title("Grade Performance Over Time")
    ax.legend()
    st.pyplot(fig)
