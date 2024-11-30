from flask_notion_database.routes.database import DatabaseRoutes
from flasgger import swag_from


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
    def search():
        return db_routes.search()


class NotionDatabaseExtension:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    @classmethod
    def init_app(cls, app):
        define_routes(app)
