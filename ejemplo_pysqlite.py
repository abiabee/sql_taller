# ======================================
# Ejemplo SQLite en Python
# ======================================

import sqlite3

try:
    # Conectar a la base de datos
    # Si no existe, se crea automáticamente
    con = sqlite3.connect("ejemplo_pysqlite.db")

    # Crear cursor
    cursor = con.cursor()

    # -----------------------------
    # Crear tabla Departamentos
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departamentos(
        Departamento_ID INTEGER PRIMARY KEY,
        Departamento_Nombre TEXT NOT NULL
    )
    """)

    # Insertar datos
    cursor.executemany(
        """
    INSERT OR REPLACE INTO Departamentos
    VALUES (?,?)
    """,
        [(101, "RRHH"), (102, "TI")],
    )

    # -----------------------------
    # Crear tabla Empleados
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Empleados(
        Empleado_ID INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Cargo TEXT NOT NULL,
        Departamento_ID INTEGER,

        FOREIGN KEY (Departamento_ID)
        REFERENCES Departamentos(Departamento_ID)
    )
    """)

    # Insertar empleados
    cursor.executemany(
        """
    INSERT OR REPLACE INTO Empleados
    VALUES (?,?,?,?)
    """,
        [
            (1, "Alicia", "Gerente", 101),
            (2, "Roberto", "Desarrollador", 102),
            (3, "Carlos", "Diseñador", 101),
        ],
    )

    # Guardar cambios
    con.commit()

    # -----------------------------
    # Consulta JOIN
    # -----------------------------
    consulta = """
    SELECT
        E.Empleado_ID,
        E.Nombre,
        E.Cargo,
        D.Departamento_Nombre

    FROM Empleados E

    JOIN Departamentos D
    ON E.Departamento_ID=D.Departamento_ID
    """

    cursor.execute(consulta)

    resultados = cursor.fetchall()

    print("\nResultado del JOIN:\n")

    for fila in resultados:
        print(fila)


except sqlite3.Error as error:
    print("Error SQLite:", error)


finally:
    if con:
        con.close()
        print("\nConexión cerrada")
