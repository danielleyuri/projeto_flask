from mysql.connector import connection

def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from unico")
    cursor.execute(query)
    response = []
    for (unico_id, unico_name) in cursor:
        response.append({
            'unico_id':unico_id,
            'unico_name':unico_name

        })

    return response


if __name__=='__main__':
    from sql_connection import get_sql_connection
 
    connect = get_sql_connection()
    print(get_uoms(connection))  