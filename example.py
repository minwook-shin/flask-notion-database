from flasgger import Swagger
from flask import Flask

from flask_notion_database import NotionDatabaseExtension

nde = NotionDatabaseExtension()

app = Flask(__name__)
nde.init_app(app)

Swagger(app)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
