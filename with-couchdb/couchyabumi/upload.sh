#!/bin/sh

PHOTODIR="/path/to/motion"
SCRIPTPATH="/path/to/with-couchdb/uploader/bulkphotos.py"
USER="user"
PASS="password"
HOSTNAME="example.org"
PORT=5984
DB="dbname"
JSON=$(tempfile)

cd $PHOTODIR

$SCRIPTPATH > $JSON

case $PORT in
    80 )
	curl -X POST -H 'Content-Type:application/json' -d @${JSON} \
	    http://${USER}:${PASS}@${HOSTNAME}/${DB}/_bulk_docs
	;;
    443 )
	curl -X POST -H 'Content-Type:application/json' -d @${JSON} \
	    https://${USER}:${PASS}@${HOSTNAME}/${DB}/_bulk_docs
	;;
    6984 )
	curl -X POST -H 'Content-Type:application/json' -d @${JSON} \
	    https://${USER}:${PASS}@${HOSTNAME}:${PORT}/${DB}/_bulk_docs
	;;
    * )
	curl -X POST -H 'Content-Type:application/json' -d @${JSON} \
	    http://${USER}:${PASS}@${HOSTNAME}:${PORT}/${DB}/_bulk_docs
	;;
esac

rm -f $JSON *.jpg *.swf