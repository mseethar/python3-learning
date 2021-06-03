sqls = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)

reset_sqls = ('DROP TABLE vendor_parts', 'DROP TABLE part_drawings', 'DROP TABLE parts', 'DROP TABLE vendors')
import os.path
# Searching the config file in the module's directory
def load_config(path=os.path.dirname(__file__), filename='database.ini', section='h2'):
   from configparser import ConfigParser
   parser = ConfigParser()
   parser.read(f'{path}/{filename}')
   db_config = {}
   if parser.has_section(section):
      params = parser.items(section)
      for key, value in params:
         db_config[key] = value
   else:
      raise Exception(f'Section {section} is not found in file {filename}')
   return db_config

def execute_sql(conn, sql):
   cur = conn.cursor()
   cur.execute(sql)
   print(sql, 'cur.rowcount', cur.rowcount)
   #res = cur.fetchone()   # psycopg2.ProgrammingError: no results to fetch
   #print(res)
   cur.close()
   print('DONE - execute SQL')

def connect():
   return psycopg2.connect(**conn_params)

def clear_db(conn):
   for sql in reset_sqls:
      execute_sql(conn, sql)

def init_db(conn):
   for sql in sqls:
      execute_sql(conn, sql)

import psycopg2

conn_params = load_config()
try:
   conn = connect() 
   print('Connecting to the DB')
   cur = conn.cursor()
   cur.execute('SELECT version()')
   db_version = cur.fetchone()
   print(f'db version is {db_version}')
   cur.close()
   clear_db(conn)
   init_db(conn)
except psycopg2.OperationalError as ex:
   # psycopg2.OperationalError: server closed the connection unexpectedly
   # This probably means the server terminated abnormally
   # before or while processing the request.
   print(ex)
   raise RuntimeError() from ex
except (Exception, psycopg2.DatabaseError) as error:
   print(error)
   raise RuntimeError() from error
finally:
   if conn is not None:
      conn.close()
      print('Closed the db connection')

print('psycopg2.apilevel', psycopg2.apilevel)
print('paycopg2.threadsafety', psycopg2.threadsafety)
print('psycopg2.paramstyle', psycopg2.paramstyle)

