import sqlite3
from sqlite3 import Error

filename = 'labAccess.sqlite'    # name of the sqlite database file

# Connecting to the database file
def connectToDb():
    conn = None
    try:
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        print('Connected to db')
    except Error as e:
        print(e)
        if conn:
            conn.close()

    


#In SQLite, INTEGER PRIMARY KEY column is auto-incremented.
# Data types: INTEGER, TEXT, NULL, REAL, BLOB
#FOREIGN KEY (foreign_key_columns) REFERENCES parent_table(parent_key_columns)
def createTables():
    c.execute('''CREATE TABLE members(
        MemberId INTEGER PRIMARY KEY NOT NULL,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL, 
        Phone INTEGER,
        Email TEXT,
        CreatedData TEXT,
        Country TEXT,
        City TEXT,
        Deleted INTEGER,
        CardId INTEGER NOT NULL,
        Password TEXT NOT NULL,
        UserName TEXT NOT NULL
        )''')
    print("Tabla de members creada")

    c.execute('''CREATE TABLE records(
        RecordsId INTEGER PRIMARY KEY NOT NULL,
        DeviceId INTEGER NOT NULL,
        GetIn_Tx TEXT NOT NULL,
        GetIn_Ticks INTEGER NOT NULL,
        Leave_Tx TEXT NOT NULL,
        Leave_Ticks INTEGER NOT NULL,
        MemberId INTEGER NOT NULL,
        FOREIGN KEY (MemberId) REFERENCES members (MemberId)
        FOREIGN KEY (DeviceId) REFERENCES devices (DeviceId) 
        )''')
    print("Tabla de records creada")

    c.execute('''CREATE TABLE devices(
        DeviceId INTEGER PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        Status TEXT,
        Location TEXT,
        Version REAL NOT NULL,
        CreatedDate_Tx TEXT,
        CreatedDate_Ticks INTEGER, 
        VersionModifiedDate_Tx TEXT,
        VersionModifiedDate_Ticks INTEGER
        )''')
    print("Tabla de devices creada")

    c.execute('''CREATE TABLE sensors(
        SensorId INTEGER PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        STATUS TEXT,
        DeviceId INTEGER NOT NULL,
        FOREIGN KEY (DeviceId) REFERENCES devices (DeviceId) 
        )''')
    print("Tabla de sensors creada")

    c.execute('''CREATE TABLE readings(
        ReadingId INTEGER PRIMARY KEY NOT NULL,
        SensorId INTEGER NOT NULL, 
        Value1 REAL,
        Value2 REAL,
        Value3 REAL,
        LastSensorsReading_Tx TEXT,
        LastSensorsReading_Ticks INTEGER,
        FOREIGN KEY (SensorId) REFERENCES sensors (SensorId)
        )''')
    print("Tabla de readings creada")