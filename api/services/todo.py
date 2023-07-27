from flask import request, jsonify
import api.models.todo as modelTodo

def listTodo():
    list = modelTodo.listTodo({ "id": request.args.get("id") })
    
    return jsonify({
        "status": "true",
        "data": list[0] if request.args.get("id") else list
    })

def addTodo():
    add = modelTodo.saveTodo(request.json)

    return jsonify({
        "status": "true",
        "data": add
    })

def updateTodo():
    edit = modelTodo.updateTodo({ **request.json, "id": request.args.get("id") })

    return jsonify({
        "status": "true",
        "data": edit
    })

def removeTodo():
    remove = modelTodo.deleteTodo(request.args.get("id"))

    return jsonify({
        "status": "true",
        "data": remove
    })