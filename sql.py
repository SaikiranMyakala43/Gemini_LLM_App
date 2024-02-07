import sqlite3

#conect to sqlite
connection=sqlite3.connect("student2.db")

#create a cursor object to insert record, create table, retrive
cursor=connection.cursor()

#create the table
table_info="""
create table STUDENT2(NAME VARCHAR (25), CLASS VARCHAR(25),
SEACTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#inerst some records
cursor.execute("""Insert Into Student2 values('Kiran','Data science','A','90')""")
cursor.execute("""Insert Into Student2 values('Nagesh','Lokopilot','B','75')""")
cursor.execute("""Insert Into Student2 values('Santhu','Data Analysis','A','95')""")
cursor.execute("""Insert Into Student2 values('Balayya','Java','A','93')""")
cursor.execute("""Insert Into Student2 values('Uppi','HR','B','85')""")

#display all the records
print("the inserted records are")

data =cursor.execute('''select * from STUDENT2''')

for row in data:
    print(row)
    
#close the connection
connection.commit()
connection.close()

