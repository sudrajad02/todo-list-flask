import api.utils.db as db
conn = db.connection()
cursor = conn.cursor()

def listTodo(data = {}):
    sql = ("SELECT * FROM todos WHERE 1")
    params = ()

    if data["id"]:
        sql += (" AND todo_id = %s")
        params = (data["id"],)

    cursor.execute(sql, params)

    #Get Column
    column_name = [i[0] for i in cursor.description]

    data = []

    for row in cursor.fetchall():
        data.append(dict(zip(column_name, row)))

    return data

def saveTodo(data):
    sql = "INSERT INTO todos(activity_group_id, title, priority, is_active) VALUES (%s, %s, %s, %s)"
    params = (data["activity_group_id"], data["title"], data["priority"], data["is_active"])
    
    cursor.execute(sql, params)

    conn.commit()
    lastId = cursor.lastrowid

    return lastId

def updateTodo(data):
    sql = "UPDATE todos SET activity_group_id = %s, title = %s, priority = %s, is_active = %s WHERE todo_id = %s"
    params = (
        data["activity_group_id"],
        data["title"],
        data["priority"],
        data["is_active"],
        data["id"]
    )

    cursor.execute(sql, params)

    conn.commit()
    id = data["id"]

    return id

def deleteTodo(id):
    sql = "DELETE FROM todos WHERE todo_id = %s"
    params = (id,)

    cursor.execute(sql, params)

    conn.commit()

    return id