import sqlite3

try:
    print("Reconstruyendo base de datos...")
    con = sqlite3.connect("university.db")
    cursor = con.cursor()

    # Hablitar foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")

    # -----------------------------
    # Department
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS department (
        dept_name TEXT PRIMARY KEY,
        building TEXT,
        budget REAL
    );
    """)

    # -----------------------------
    # Instructor
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS instructor (
        ID INTEGER PRIMARY KEY,
        name TEXT,
        dept_name TEXT,
        salary REAL,

        FOREIGN KEY (dept_name)
            REFERENCES department(dept_name)
    );
    """)

    # -----------------------------
    # Course
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS course (
        course_id TEXT PRIMARY KEY,
        title TEXT,
        dept_name TEXT,
        credits INTEGER,

        FOREIGN KEY (dept_name)
            REFERENCES department(dept_name)
    );
    """)

    # -----------------------------
    # Classroom
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classroom (
        room_number INTEGER,
        building TEXT,
        capacity INTEGER,

        PRIMARY KEY (room_number, building)
    );
    """)

    # -----------------------------
    # Section
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS section (
        id INTEGER PRIMARY KEY,
        sec_id INTEGER,
        course_id TEXT,
        room_number INTEGER,
        building TEXT,
        semester TEXT,
        year INTEGER,

        FOREIGN KEY (course_id)
            REFERENCES course(course_id),

        FOREIGN KEY (room_number, building)
            REFERENCES classroom(room_number, building)
    );
    """)

    # -----------------------------
    # Teaches
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teaches (
        ID INTEGER,
        course_id TEXT,
        sec_id INTEGER,
        semester TEXT,
        year INTEGER,

        PRIMARY KEY (ID, course_id, sec_id, semester, year),

        FOREIGN KEY (ID)
            REFERENCES instructor(ID),

        FOREIGN KEY (course_id)
            REFERENCES course(course_id),

        FOREIGN KEY (sec_id)
            REFERENCES section(id)
    );
    """)

    # -----------------------------
    # Advisor
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS advisor (
        student_id INTEGER PRIMARY KEY,
        instructor_id INTEGER,

        FOREIGN KEY (student_id)
            REFERENCES student(ID),

        FOREIGN KEY (instructor_id)
            REFERENCES instructor(ID)
    );
    """)

    # -----------------------------
    # Student
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        ID INTEGER PRIMARY KEY,
        name TEXT,
        dept_name TEXT,
        tot_cred INTEGER,

        FOREIGN KEY (dept_name)
            REFERENCES department(dept_name)
    );
    """)

    # -----------------------------
    # Prereq
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prereq (
        course_id TEXT,
        prereq_id TEXT,

        PRIMARY KEY (course_id, prereq_id),

        FOREIGN KEY (course_id)
            REFERENCES course(course_id)
    );
    """)

    # -----------------------------
    # Time Slot
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS time_slot (
        id INTEGER PRIMARY KEY,
        time_slot_id TEXT, 
        day TEXT,
        start_time TEXT,
        end_time TEXT
    );
    """)

    # -----------------------------
    # Takes
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS takes (
        ID INTEGER,
        course_id TEXT,
        sec_id INTEGER,
        semester TEXT,
        year INTEGER,
        grade TEXT,

        PRIMARY KEY (ID, course_id, sec_id, semester, year),

        FOREIGN KEY (ID)
            REFERENCES student(ID),

        FOREIGN KEY (sec_id)
            REFERENCES section(id)
    );
    """)

    con.commit()
    print("Database creada exitosamente.")

except sqlite3.Error as error:
    print("SQLite Error:", error)

finally:
    if con:
        con.close()
        print("Conexión cerrada :).")

