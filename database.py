from dotenv import load_dotenv
import psycopg2
import os
from datetime import datetime


class DB:
    conn = " "
    def __init__(self) -> None:

        load_dotenv()
        self.conn = psycopg2.connect(database= os.getenv('PGDATABASE'),
                                host=os.getenv("PGHOST"),
                                user=os.getenv("PGUSER"),
                                password=os.getenv("PGPASSWORD"),
                                port=os.getenv("PGPORT"))

    def connect(self):
        print("connecting to database")
        
        if(self.conn):
            print("connected")
            cursor= self.conn.cursor()
            cursor.execute()
            self.conn.commit()
        else:
            print("not connected")
        
    def mark_attendace(self,name):
        cursor= self.conn.cursor()
        cursor.execute(f"""ALTER TABLE Student
    ADD COLUMN IF NOT EXISTS "{datetime.today().date()}" int;""")
        
        print(name)
        cursor.execute(f"""UPDATE Student 
                        SET "{datetime.today().date()}"=1
                        WHERE StudentName='{name}'""")
        self.conn.commit()




