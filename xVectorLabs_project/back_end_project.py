from flask import Flask, jsonify, request
from mysql.connector import connection
import matplotlib.pyplot as plt
import json


app = Flask(__name__)


@app.route('/dataset', methods=['GET'])
def get_records():
    conn = connection.MySQLConnection(user='saigopi',
                                      password='sai3121@',
                                      host='localhost',
                                      database='employees_new')
    cursor = conn.cursor()

    cursor.execute('SELECT * from employee')
    res = list(cursor)
    cursor.close()
    conn.close()

    return jsonify(res)


@app.route('/dataset', methods=['POST'])
def write_record():
    conn = connection.MySQLConnection(user='saigopi',
                                      password='sai3121@',
                                      host='localhost',
                                      database='employees_new')

    rec = json.loads(request.data)
    rec1 = tuple([rec[i] for i in rec])
    cursor = conn.cursor()

    cursor.execute('insert into employee (eid, salary, age) values ' + str(rec1))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'successfully added'})


@app.route('/dataset/<col_name>/<operation>', methods=['POST'])
def filtered_value(col_name, operation):
    conn = connection.MySQLConnection(user='saigopi',
                                      password='sai3121@',
                                      host='localhost',
                                      database='employees_new')

    cursor = conn.cursor()
    cursor.execute('SELECT ' + operation + '(' + col_name + ')' + ' from employee')
    res = list(cursor)
    cursor.close()
    conn.close()

    return jsonify({'data': res})


@app.route('/dataset/<col_1>/<col_2>', methods=['GET'])
def _plotting(col_1, col_2):
    conn = connection.MySQLConnection(user='saigopi',
                                      password='sai3121@',
                                      host='localhost',
                                      database='employees_new')
    cursor = conn.cursor()
    query1 = 'SELECT ' + col_1 + ' from employee limit 20'
    query2 = 'SELECT ' + col_2 + ' from employee limit 20'

    cursor.execute(query1)
    x_axis = list(cursor)

    cursor.execute(query2)
    y_axis = list(cursor)

    plt.plot(x_axis, y_axis)

    try:
        plt.show()
    except UserWarning:
        ...

    cursor.close()
    conn.close()

    return jsonify({'message': 'output directed to other thread/process'})


if __name__ == "__main__":
    app.run()
