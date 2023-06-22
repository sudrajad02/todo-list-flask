import os

from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = os.environ.get("host")
app.config['MYSQL_DATABASE_USER'] = os.environ.get("user")
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get("password")
app.config['MYSQL_DATABASE_DB'] = os.environ.get("db")
mysql.init_app(app)

conn = mysql.connect()

@app.route('/')
def root():
    return "Selamat Datang!"

@app.route('/person')
def person():
    return jsonify({
        "name": "anggi",
        "address": "yogya"
    })

@app.route('/todo', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def todo():
    if request.method == 'GET':
        cursor = mysql.get_db().cursor()
        sql = "SELECT * FROM todos WHERE 1"
        params = []

        if 'id' in request.args:
            sql += " AND todo_id = %s"
            params.append(request.args['id'])

        cursor.execute(sql, params)

        #Get Column
        column_name = [i[0] for i in cursor.description]

        #Fetch Data
        data = []

        for row in cursor.fetchall():
            data.append(dict(zip(column_name, row)))

        return jsonify(data)

        cursor.close()
    
    elif request.method == "POST":
        cursor = mysql.get_db().cursor()
        sql = "INSERT INTO todos(activity_group_id, title, priority, is_active) VALUES (%s, %s, %s, %s)"
        params = (request.json['activity_group_id'], request.json['title'], request.json['priority'], request.json['is_active'])
        cursor.execute(sql, params)

        mysql.get_db().commit()

        return jsonify({
            "message": "Data berhasil ditambahkan!"
        })
        cursor.close()

    elif request.method == "DELETE":
        cursor = mysql.get_db().cursor()
        sql = "DELETE FROM todos WHERE todo_id = %s"
        params = (request.args['id'])
        cursor.execute(sql, params)

        mysql.get_db().commit()

        return jsonify({
            "message": "Data berhasil dihapus!"
        })
        cursor.close()

    elif request.method == "PATCH":
        cursor = mysql.get_db().cursor()
        sql = "UPDATE todos SET activity_group_id = %s, title = %s, priority = %s, is_active = %s WHERE todo_id = %s"
        params = (
            request.json['activity_group_id'],
            request.json['title'],
            request.json['priority'],
            request.json['is_active'],
            request.args['id']
        )

        cursor.execute(sql, params)

        mysql.get_db().commit()

        return jsonify({
            "message": "Data berhasil diubah!"
        })
        cursor.close()

if __name__ == "__main__":
    app.run(debug=True)