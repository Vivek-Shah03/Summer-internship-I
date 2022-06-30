import cx_Oracle
con = cx_Oracle.connect('system/Vivek_2003')
cursor = con.cursor()
cursor.execute("select * from  task20")
rows = cursor.fetchall()
print(rows)
cursor.close()
con.close()