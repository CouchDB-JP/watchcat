#!/bin/sh

PHOTODIR="/path/to/motion"
SCRIPTPATH="with-couchdb/uploader/bulkphotos.py"
USER="user"
PASS="password"
HOSTNAME="example.org"
PORT=5984
DB="dbname"

cd $PHOTODIR

curl -X POST -H 'Content-Type:application/json' -d "`$SCRIPTPATH`" \
    http://${USER}:${PASS}@${HOSTNAME}:${PORT}/${DB}/_bulk_docs
