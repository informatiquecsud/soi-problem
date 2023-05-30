#!/bin/sh

while true
do
    git add . && git commit -m "sauvegarde automatique" && git push
    sleep 2m
done
