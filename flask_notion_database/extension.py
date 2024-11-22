import json

from flasgger import swag_from
from flask import request, jsonify
from notion_database import NotionDatabase
from notion_database.const.query import Direction, Timestamp


def define_routes(app):
    @app.route('/notion-db/search', methods=['POST'])
    @swag_from({
        'responses': {200: {}},
        'parameters': [
            {
                "name": "integrations_token",
                "in": "formData",
                "type": "string",
                "required": True
            },
            {
                "name": "query",
                "in": "formData",
                "type": "string",
                "required": False
            }
        ]
    })
    def search_db():
        integrations_token = request.form.get('integrations_token')
        query = request.form.get('query', "")
        # sort = request.form.get('sort')
        sort = {"direction": Direction.ascending, "timestamp": Timestamp.last_edited_time}

        result = NotionDatabase.search_database(integrations_token, sort, query)
        return jsonify(result)


class NotionDatabaseExtension:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    @classmethod
    def init_app(cls, app):
        define_routes(app)
