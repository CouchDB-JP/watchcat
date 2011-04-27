#!/bin/bash

USER=GoogleAccount

google -u $USER picasa delete --query "`date --date '1 day ago' +\"%Y%m%d\"`" --yes
