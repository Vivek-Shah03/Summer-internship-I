import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='password')