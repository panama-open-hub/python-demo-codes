import sqlite3
from sqlite3 import Error
import json
from dummyJsonData import dummyJsonData

filename = 'labAccess.sqlite'    # name of the sqlite database file
#c.execute('''INSERT INTO membersTb(MemberId, FirstName, LastName, Phone, Email, CreatedDate_Tx, CreatedDate_Ticks, Country, City, UserName, Deleted)VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(1, "Pablo", "Gonzalez", 66865816, "p.gonzalez7027@gmail.com","17/10/2019 15:30:16",637069230160000000,"Panama","Chitre","pangoro24", 0))
#c.execute("INSERT INTO {tn}({cn1}, {cn2}, {cn3}) VALUES ('sensor2', 'on',48)".format(tn=table_name, cn1=col1,cn2=col2,cn3=col3))
#c.execute('''INSERT INTO sensors_table(name, status, value)VALUES(:name,:status, :value)''',{'name':name1, 'status':status1, 'value':value1})
#c.execute('''INSERT INTO sensors_table(name, status, value)VALUES(?,?,?)''',(name1, status1, value1))

# Connecting to the database file
data  = dummyJsonData()


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
"""
c.execute('''CREATE TABLE membersTb(
    MemberId INTEGER PRIMARY KEY NOT NULL,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL, 
    Phone INTEGER,
    Email TEXT,
    Created_at TEXT,
    Updated_at TEXT,
    Country TEXT,
    City TEXT,
    UserName TEXT NOT NULL,
    Password TEXT NOT NULL,
    Deleted INTEGER
    )''')
print("Tabla de members creada")

c.execute('''CREATE TABLE cardsTb(
    CardId INTEGER PRIMARY KEY NOT NULL,
    Tag INTEGER NOT NULL,
    Texto TEXT,
    MemberId INTEGER,
    FOREIGN KEY (MemberId) REFERENCES members (MemberId)
    )''')
print("Tabla de cards creada")


c.execute('''CREATE TABLE recordsTb(
    RecordId INTEGER PRIMARY KEY NOT NULL,
    DeviceId INTEGER NOT NULL,
    GetIn TEXT NOT NULL,
    Leave TEXT NOT NULL,
    MemberId INTEGER NOT NULL,
    FOREIGN KEY (MemberId) REFERENCES members (MemberId)
    FOREIGN KEY (DeviceId) REFERENCES devices (DeviceId) 
    )''')
print("Tabla de records creada")

c.execute('''CREATE TABLE devicesTb(
    DeviceId INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Status TEXT,
    Location TEXT,
    Version REAL NOT NULL,
    Created_at TEXT, 
    Updated_at TEXT
    )''')
print("Tabla de devices creada")

c.execute('''CREATE TABLE ioTb(
    SensorId INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Status TEXT,
    DeviceId INTEGER NOT NULL,
    FOREIGN KEY (DeviceId) REFERENCES devices (DeviceId) 
    )''')
print("Tabla de io creada")

c.execute('''CREATE TABLE readingsTb(
    ReadingId INTEGER PRIMARY KEY NOT NULL,
    SensorId INTEGER NOT NULL, 
    Value1 REAL,
    Value2 REAL,
    Value3 REAL,
    Reading_at TEXT,
    FOREIGN KEY (SensorId) REFERENCES sensors (SensorId)
    )''')
print("Tabla de readings creada")
conn.commit()
print("Comando SQL comiteado")
"""

try:
    members = json.loads(json.dumps(data.addmembersJson()))
    for var in members:
        c.execute('''INSERT INTO membersTb(FirstName, LastName, Phone, Email, Created_at, Updated_at, Country, City, UserName, Deleted, Password)VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(var["FirstName"],var["LastName"],var["Phone"],var["Email"],var["Created_at"],var["Updated_at"],var["Country"],var["City"],var["UserName"],var["Deleted"],var["Password"]))
        print(var["FirstName"],'. Nuevo colaborador ha sido agregado.')
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    cards = json.loads(json.dumps(data.addcardsJson()))
    for var in cards:
        print(var)
        c.execute('''INSERT INTO cardsTb(Tag, Texto, MemberId)VALUES(?,?,?)''',(var["Tag"],var["Texto"],var["MemberId"]))
        print("Nueva tarjeta asociada a ",var["Texto"]," ha sido agregada.")
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    records = json.loads(json.dumps(data.addrecordsJson()))
    for var in records:
        print(var)
        c.execute('''INSERT INTO recordsTb(DeviceId, GetIn, Leave, MemberId)VALUES(?,?,?,?)''',(var["DeviceId"],var["GetIn"],var["Leave"],var["MemberId"]))
        print("Nuevo Record ha sido registrado el ",var["GetIn"])
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    devices = json.loads(json.dumps(data.adddevicesJson()))
    for var in devices:
        print(var)
        c.execute('''INSERT INTO devicesTb(Name, Status, Location, Version, Created_at, Updated_at)VALUES(?,?,?,?,?,?)''',(var["Name"],var["Status"],var["Location"],var["Version"],var["Created_at"],var["Updated_at"]))
        print("Device ",var["Name"]," agregado.")
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    readings = json.loads(json.dumps(data.addreadingsJson()))
    for var in readings:
        print(var)
        c.execute('''INSERT INTO readingsTb(SensorId, Value1, Value2, Value3, Reading_at)VALUES(?,?,?,?,?)''',(var["SensorId"],var["Value1"],var["Value2"],var["Value3"],var["Reading_at"]))
        print("Nuevo reading el: ",var["Reading_at"]," completado")
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    io = json.loads(json.dumps(data.addioJson()))
    for var in io:
        print(var)
        c.execute('''INSERT INTO ioTb(Name, Status, DeviceId)VALUES(?,?,?)''',(var["Name"],var["Status"],var["DeviceId"]))
        print("Nuevo io: ",var["Name"]," ha sido agregado")
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))




"""
# Inserts an ID with a specific value in a second column
try:
    c.execute('''INSERT INTO membersTb(MemberId, FirstName, LastName, Phone, Email, CreatedDate_Tx, CreatedDate_Ticks, Country, City, UserName, Deleted, Password)VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',(1, "Pablo", "Gonzalez", 66865816, "p.gonzalez7027@gmail.com","17/10/2019 15:30:16",637069230160000000,"Panama","Chitre","pangoro24", 0,"123456"))
    print('New members added')
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    c.execute('''INSERT INTO cardsTb(CardId, Password, MemberId)VALUES(?,?,?)''',(1,"abc",1))
    print('New cards added')
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    c.execute('''INSERT INTO devices(DeviceId, Name, Status, Location, Version, CreatedDate_Tx, CreatedDate_Ticks, VersionModifiedDate_Tx, VersionModifiedDate_Ticks)VALUES(?,?,?,?,?,?,?,?,?)''',(1, "CheckStation1", 1, "Puerta trasera", 1.1, "17/10/2019 15:04:00", 637069218200000000, "17/10/2019 15:04:00", 637069218200000000))
    print('New devices added')
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
   c.execute('''INSERT INTO records(RecordsId, DeviceId, GetIn_Tx, GetIn_Ticks, Leave_Tx, Leave_ticks, MemberId)VALUES(?,?,?,?,?,?,?)''',(1, 1, "17/10/2019 12:00:55", 637069176550000000, "17/10/2019 12:00:55", 637069284550000000, 1))
   print('New records added')
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))


try:
    c.execute('''INSERT INTO sensors(SensorId,Name, STATUS, DeviceId)VALUES(?,?,?,?)''',(1, "Humedad", 1, 1))
    print('New sensors added')
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))

try:
    c.execute('''INSERT INTO readings(ReadingId, SensorId, Value1, Value2, Value3, LastSensorsReading_Tx, LastSensorsReading_Ticks)VALUES(?,?,?,?,?,?,?)''',(1,1,35.2,95,0.0,"17/10/2019 12:00:55", 637069176550000000))
    print('New readings added')
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(0))
"""
conn.commit()
print("Comando SQL comiteado")
conn.close()