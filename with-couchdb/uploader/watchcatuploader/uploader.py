# -*- coding: utf-8 -*-
import couchdb


class CouchDB(object):
    def __init__(self, dbname, host, port='5984',
                 username=None, password=None):
        if username is None and password is None:
            uri = ('http://' + host + ':' + port)
        else:
            uri = ('http://' + username + ':' + password + '@'
                   + host + ':' + port)
        self.server = couchdb.Server(uri)
        self.db = self.server[dbname]

    def list_docs(self):
        for doc_id in self.db:
            print doc_id

    def get_stat(self):
        return self.server.stats()

    def get_db_info(self):
        return self.db.info()
