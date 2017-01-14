#!/bin/bash
# Very simple push-to-deploy script to be installed in the remote crontab
# with an entry like:
# * * * * * (cd /home/devbot/devbrobot && ./update.sh)

git fetch origin
current=$(git log --pretty=%H)
remote=$(git log origin/master --pretty=%H)

if ! [ "$current" = "$remote" ]; then
    git pull origin master
    echo "Restarting nerdbot."
    sudo service nerdbot restart
fi
