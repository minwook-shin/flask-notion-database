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

        result = NotionDatabase.search_database(integrations_token=integrations_token, sort=sort, query=query)
        return jsonify(result)

    def retrieve(self):
        integrations_token = request.form.get('integrations_token')
        database_id = request.form.get('database_id')
        get_properties = request.form.get('get_properties', True)
        result = NotionDatabase.retrieve_database(integrations_token=integrations_token, database_id=database_id,
                                                  get_properties=get_properties)
        return jsonify(result)