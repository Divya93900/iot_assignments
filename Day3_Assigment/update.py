import mysql.connector
def get_connection():
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user = "sunbeam",
    password ="sunbeam",
    database ="empdb"
)
def update_employe(salary,emid):
    conn=get_connection()
    query1=f"update emply SET salary=%s where emid=%s;"
    val=(emid,salary)
    cursor=conn.cursor()
    cursor.execute(query1,val)
    conn.commit()
    cursor.close()
    conn.close()
#emid=int(input("enter the emid"))

#salary=int(input("enter the salary"))

update_employe(345,50000) 
update_employe(456,30000)   