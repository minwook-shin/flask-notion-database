from flask import request, jsonify
from notion_database import NotionDatabase
from notion_database.const.query import Direction, Timestamp


class DatabaseRoutes:
    def __init__(self):
        self.common_sort = {"direction": Direction.ascending, "timestamp": Timestamp.last_edited_time}


    def search(self):
        integrations_token = request.form.get('integrations_token')
        query = request.form.get('query', "")
        # sort = request.form.get('sort')
        sort = self.common_sort

        result = NotionDatabase.search_database(integrations_token, sort, query)
        return jsonify(result)
