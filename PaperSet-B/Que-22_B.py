import cx_Oracle

con = cx_Oracle.connect('system/Vivek_2003')

cursor = con.cursor()
cursor.execute('select * from employee')
rows = cursor.fetchall()
print(rows)

cursor.execute("update employee set emp_name='Anand' where emp_no=101")

cursor.execute('select * from employee')
rows = cursor.fetchall()
print(rows)
