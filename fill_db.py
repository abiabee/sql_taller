import pandas as pd
import sqlite3

print("Llenando base de datos...")

# ======================================
# Conectar DB
# ======================================

con = sqlite3.connect("university.db")
cursor = con.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# ======================================
# Leer Excel
# ======================================

xls = pd.ExcelFile("university.xlsx")

# ======================================
# Department
# ======================================

df = pd.read_excel(xls, sheet_name="department")
# Para que quepan en el UNIQUE
df = df.drop_duplicates(subset=["dept_name"])

df.to_sql(
    "department",
    con,
    if_exists="append",
    index=False
)

print("department OK")

# ======================================
# Instructor
# ======================================

df = pd.read_excel(xls, sheet_name="instructor")

df.to_sql(
    "instructor",
    con,
    if_exists="append",
    index=False
)

print("instructor OK")

# ======================================
# Course
# ======================================

df = pd.read_excel(xls, sheet_name="course")

df.to_sql(
    "course",
    con,
    if_exists="append",
    index=False
)

print("course OK")

# ======================================
# Classroom
# ======================================

df = pd.read_excel(xls, sheet_name="classroom")

df.to_sql(
    "classroom",
    con,
    if_exists="append",
    index=False
)

print("classroom OK")

# ======================================
# Section
# ======================================

df = pd.read_excel(xls, sheet_name="section")

# Foreign key, como el excel no tiene este ID
if "id" not in df.columns:
    df.insert(0, "id", range(1, len(df) + 1))

df.to_sql(
    "section",
    con,
    if_exists="append",
    index=False
)

print("section OK")

# ======================================
# Student
# ======================================

df = pd.read_excel(xls, sheet_name="student")

df.to_sql(
    "student",
    con,
    if_exists="append",
    index=False
)

print("student OK")

# ======================================
# Advisor
# ======================================

df = pd.read_excel(xls, sheet_name="advisor")

# Nombres del excel
df = df.rename(columns={
    "s_ID": "student_id",
    "i_ID": "instructor_id"
})

df.to_sql(
    "advisor",
    con,
    if_exists="append",
    index=False
)

print("advisor OK")

# ======================================
# Prereq
# ======================================

df = pd.read_excel(xls, sheet_name="prereq")

df.to_sql(
    "prereq",
    con,
    if_exists="append",
    index=False
)

print("prereq OK")

# ======================================
# Time Slot
# ======================================

df = pd.read_excel(xls, sheet_name="time_slot")

# Si el ID no viene en el excel
if "id" not in df.columns:
    df.insert(0, "id", range(1, len(df) + 1))

df.to_sql(
    "time_slot",
    con,
    if_exists="append",
    index=False
)

print("time_slot OK")

# ======================================
# Teaches
# ======================================

df = pd.read_excel(xls, sheet_name="teaches")

df.to_sql(
    "teaches",
    con,
    if_exists="append",
    index=False
)

print("teaches OK")

# ======================================
# Takes
# ======================================

df = pd.read_excel(xls, sheet_name="takes")

df.to_sql(
    "takes",
    con,
    if_exists="append",
    index=False
)

print("takes OK")

# ======================================
# Finalizar
# ======================================

con.commit()
con.close()

print("\nBase de datos llenada exitosamente.")