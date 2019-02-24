#!/bin/bash -x

eval "$(ssh-agent -s)"
chmod 600 key
ssh-add key

case $1 in
    staging) scp_dest="/slack-qa/";;
    release) scp_dest="/slack/";;
esac

scp -P 15010 -o StrictHostKeyChecking=no -r app.py janet.wsgi ./common ./resources Pipf* travis@slack.rmcentyre.com:${scp_dest}

ssh -T -P 15010 -o StrictHostKeyChecking=no travis@slack.rmcentyre.com << EOF
    cd ${scp_dest}
    pipenv sync
EOF
