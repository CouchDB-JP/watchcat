#!/bin/sh

LOG=~/log/picasa-upload.log
PHOTODIR=/path/to/motion/photos/dir
USER=GoogleAccount
TITLE=PicasaAlbumTitle

cd $PHOTODIR
google -u $USER picasa post --title=$TITLE --tags=$(date +%Y%m%d-%H) [0-9]*-??????????????-??*.jpg [0-9]*-??????????????-snapshot*.jpg > $LOG 2>&1

for i in $(awk '/Loading file/ {print $3}' $LOG)
do
	test -f $i && rm -f $i
done

rm -f *.swf
