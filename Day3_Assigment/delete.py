import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user = "sunbeam",
    password ="sunbeam",
    database ="empdb"
)
def delete_employe(emid):
    #conn = mysql.connector.get_connection()
    query= f"delete from emply where emid=%s;"
    #query= f"update from emply where emid=%s;"
    val=(emid,)
    
    cursor = conn.cursor()  
    cursor.execute(query,val)
    
    conn.commit()
    
    cursor.close()
    conn.close()
    
delete_employe(123)

