from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

hostname = 'localhost'
user = 'macromedia'
password = 'macromedia'
mydatabase = 'JuggerTube'


def execute_query(query):
    conn = mysql.connector.connect(
        host=hostname,
        user=user,
        password=password,
        database=mydatabase
    )
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        conn.commit()
        return result, columns
    except Error as e:
        conn.rollback()
        return {'error': str(e)}, 400
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


@app.route('/query', methods=['GET'])
def query():
    sql_query = request.args.get('query')
    if not sql_query:
        return jsonify({'error': 'No SQL query provided'}), 400

    results, columns = execute_query(sql_query)
    if isinstance(results, tuple) and 'error' in results[0]:
        return jsonify({'error': results[0]['error']}), results[1]
    return jsonify({'results': results, 'columns': columns})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
