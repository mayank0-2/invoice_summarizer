#!/bin/bash
echo "Commiting to repo"

echo $(date +"%Y-%M-%d") > last-updated.txt
git add .
git commit -m "chore: update last activity date"
git push origin main
