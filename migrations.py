from dotenv import load_dotenv
import psycopg2
import os

class DB:
    def __init__(self) -> None:
        load_dotenv()

    def connect(self):
        print("connecting to database")
        conn = psycopg2.connect(database= os.getenv('PGDATABASE'),
                                host=os.getenv("PGHOST"),
                                user=os.getenv("PGUSER"),
                                password=os.getenv("PGPASSWORD"),
                                port=os.getenv("PGPORT"))
        if(conn):
            print("connected")
            cursor= conn.cursor()
            arr= ["Siddharth","divyom","aryan p"]
            commands = ["""CREATE TABLE IF NOT EXISTS Student(
                        Roll int,
                        StudentName varchar(255)
            );""",
            *[f"""INSERT INTO Student (Roll, StudentName) VALUES ({i},'{arr[i]}');""" for i in range(len(arr))]]


            for command in commands:
                cursor.execute(command)
                conn.commit()
        else:
            print("not connected")


obj = DB()
obj.connect()