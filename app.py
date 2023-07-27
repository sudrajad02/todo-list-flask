from flask import Flask
from dotenv import load_dotenv

from api.routes.todo import todo

app = Flask(__name__)

app.register_blueprint(todo)

load_dotenv()

if __name__ == "__main__":
    app.run(debug=True)