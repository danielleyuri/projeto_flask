from sql_connection import get_sql_connection
from mysql.connector import connection 

def get_all_produtos(connection):

    cursor = connection.cursor()

    query = ("SELECT produtos.product_id, produtos.name, produtos.unico_id, produtos.price_unit, unico.unico_nome from produtos inner join unico on produtos.unico_id=unico.unico_id") 

    cursor.execute(query)

    response = []

    for(product_id, name, unico_id, price_unit, unico_nome) in cursor:
        response.append({

            'product_id': product_id, 
            'name': name, 
            'unico_id': unico_id, 
            'price_unit': price_unit,
            'unico_nome': unico_nome

        })


    return response

def insert_produtos(connection, produtos):
    cursor = connection.cursor()
    query = ("INSERT INTO produtos"
             "(name, unico_id, price_unit)"
             "VALUES(%s,%s,%s)")
             
    data = (produtos['produtos_name'], produtos['unico_id'], produtos['price_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_produtos(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM produtos where product_id=" + str(product_id))
  
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_produtos(connection, 11))