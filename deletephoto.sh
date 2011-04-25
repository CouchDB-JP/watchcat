#!/bin/bash

USER=GoogleAccount

google -u $USER picasa delete --query "`date --date '12 hour ago' +\"%Y%m%d-%H\"`" --yes
