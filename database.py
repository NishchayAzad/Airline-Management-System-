import mysql.connector as c

def get_connection():
    con = c.connect(host="localhost", user="root", passwd="galactika", database="travel")
    return con, con.cursor()
