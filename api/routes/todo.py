from flask import Blueprint
import api.services.todo as todoServices

todo = Blueprint("todo", __name__, url_prefix="/api/todo")

@todo.get('/')
def list():
    list = todoServices.listTodo()
    return list

@todo.post('/')
def addTodo():
    save = todoServices.addTodo()
    return save

@todo.put('/')
def editTodo():
    edit = todoServices.updateTodo()
    return edit

@todo.delete('/')
def removeTodo():
    edit = todoServices.removeTodo()
    return edit