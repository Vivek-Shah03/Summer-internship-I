import cx_Oracle

con = cx_Oracle.connect('system/Vivek_2003')
print(con.version)

cursor = con.cursor()

# cursor.execute("create table task20(empid integer primary key, my_name varchar2(20))")
# cursor.execute("insert into task20 values(101,\'Vivek\')")
# con.commit()
cursor.execute("select * from  task20")
rows = cursor.fetchall()
print(rows)

cursor.close()
con.close()