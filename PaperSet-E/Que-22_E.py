import cx_Oracle

con = cx_Oracle.connect('system/Vivek_2003')

cursor = con.cursor()

cursor.close()
