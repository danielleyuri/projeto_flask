from flask import Flask, request, jsonify 
from flask.wrappers import Response
from mysql.connector import connection
import product_dao
from sql_connection import get_sql_connection
import uom_dao
import json


app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProdutos', methods=['GET'])
def getProdutos():
    produtos = product_dao.get_all_produtos(connection)
    Response = jsonify(produtos)
    Response.headers.add('Access-Control-Allow-Origin','*')
    return Response

@app.route('/deletarProdutos', methods=['POST'])
def deletarProdutos():
    return_id = product_dao.delete.produtos(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProdutos', methods=['GET'])
def insertProdutos():
    request_payload = json.loads(request.form['data'])
    product_id = product_dao.insert_produtos(connection,request_payload)
    response = jsonify ({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__=='__main__':
    print("começando o web site em Flask")

    app.run(port=5000)