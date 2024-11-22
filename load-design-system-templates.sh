#!/bin/sh

set -e

TMPFILE=`mktemp ./templates.XXXXXXXXXX`

wget https://github.com/ONSdigital/design-system/releases/download/70.0.4/templates.zip -O $TMPFILE
rm -rf onsApp/templates/components
rm -rf onsApp/templates/layout

unzip -d ./onsApp $TMPFILE
rm $TMPFILE
