from flask_notion_database.routes.database import DatabaseRoutes
from flasgger import swag_from

from flask_notion_database.routes.page import PageRoutes


def define_routes(app):
    db_routes = DatabaseRoutes()
    @app.route('/notion/database/search', methods=['POST'])
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
    def search_database():
        return db_routes.search()

    @app.route('/notion/database/retrieve', methods=['POST'])
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
                "name": "database_id",
                "in": "formData",
                "type": "string",
                "required": True
            },
            {
                "name": "get_properties",
                "in": "formData",
                "type": "boolean",
                "required": False
            }
        ]
    })
    def retrieve_database():
        return db_routes.retrieve()

    page_routes = PageRoutes()
    @app.route('/notion/page/search', methods=['POST'])
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
            },
            {
                "name": "page_size",
                "in": "formData",
                "type": "integer",
                "required": False
            },
            {
                "name": "start_cursor",
                "in": "formData",
                "type": "string",
                "required": False
            }
        ]
    })
    def search_page():
        return page_routes.search()


class NotionDatabaseExtension:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    @classmethod
    def init_app(cls, app):
        define_routes(app)
