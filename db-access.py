#   https://www.python.org/dev/peps/pep-0249/
import db.h2

def log(cur):
   print('inserted', cur.rowcount, 'number of rows')

INSERT_PARTS = 'INSERT INTO PARTS (PART_ID, PART_NAME) VALUES(%(part_id)s, %(part_name)s)' 
INSERT_VENDORS = 'INSERT INTO VENDORS (VENDOR_NAME) VALUES (%(vendor_name)s)'  # VENDOR_ID is an autoincrement column
#INSERT INTO VENDORS (VENDOR_NAME) VALUES (%(vendor_name)s) RETURNING VENDOR_ID
conn = db.h2.connect()
cur = conn.cursor()
cur.execute('''INSERT INTO PARTS (PART_ID, PART_NAME) VALUES (1, 'Carburetor')''')
log(cur)
cur.execute(INSERT_PARTS, {'part_name': 'Bush', 'part_id': 2})
log(cur)
cur.execute(INSERT_PARTS, {'part_name': 'Chain drive', 'part_id': 3})
log(cur)
cur.execute('SELECT * FROM PARTS')

#row = cur.fetchone()   # returns a sequence / tuple
print('selecting using cur.fetchone(). cur.rowcount:', cur.rowcount)
#while row is not None:  # INFO: We don't have to do this. and assignemnt expression will be sufficient
while row := cur.fetchone():
   print(row)
else:
   print('DONE printing with cur.fetchone()')

cur.execute('SELECT * FROM PARTS')
#fetch_many = cur.fetchmany(size=2)   # by default size is cur.arraysize
print('selecting using cur.fetchmany(). cur.rowcount:', cur.rowcount)
#while fetch_many:
while fetch_many := cur.fetchmany(size=2): 
   for row in fetch_many:
      print(row, 'cur.rownumber', cur.rownumber)
else:
   print('DONE printing with cur.fetchmany()')

cur.execute('SELECT * FROM PARTS')
#fetch_all = cur.fetchall()
print('selecting using cur.fetchall(). cur.rowcount:', cur.rowcount)
for row in cur.fetchall():
   print(row)
else:
   print('DONE printinh with cur.fetchall()')

# BATCH execution
cur.executemany(INSERT_PARTS, [
                              {'part_name': 'Gear', 'part_id': 4},
                              {'part_name': 'Wiper', 'part_id': 5},
                              {'part_name': 'Steering wheel', 'part_id': 6},
                              {'part_name': 'Wind shield', 'part_id': 7},
                              {'part_name': 'Brake', 'part_id': 8},
                              {'part_name': 'Clutch', 'part_id': 9}])
cur.execute('SELECT * FROM PARTS')
# The cur.description is like the ResultsetMetadata in Java
print('cur.description', type(cur.description), cur.description)  # cur.description <class 'tuple'> (Column(name='part_id', type_code=23), Column(name='part_name', type_code=1043))
for desc in cur.description:
   print(type(desc), desc, desc.name, desc.type_code)  # <class 'psycopg2.extensions.Column'> Column(name='part_id', type_code=23) part_id 23

#fetch_all = cur.fetchall()
print('selecting using cur.fetchall(). cur.rowcount:', cur.rowcount)
#for row in fetch_all    # INFO: This is not needed
for row in cur.fetchall():
   print(row)

cur.execute(INSERT_VENDORS, {'vendor_name': 'Damn Inc'})
#vendor_id = cur.fetchone()[0]
#print('new vendor id', vendor_id)

cur.close()
conn.commit()
conn.close()

