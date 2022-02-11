from datetime import datetime

from sql_connection import get_sql_connection


def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO orders"
             "(cliente_name, total, datetime)"
             "VALUES(%s,%s,%s)")
             
    order_data = (order['cliente_name'],order['total_geral'],datetime.now())

    cursor.execute(order_query, order_data)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'cliente_name':'SHINY',
        'total_geral' : 200,

        'order_details':[
            {
            'product_id':3,
            'qty':2,
            'total_price':80

            },
            
            {
            'product_id':5,
            'qty':7,
            'total_price':30

            },


        ]
    }))