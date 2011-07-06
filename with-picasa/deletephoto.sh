#!/bin/bash

USER=GoogleAccount

google -u $USER picasa delete --query="`date --date '8 hour ago' +\"%Y%m%d%H\"`" --yes
