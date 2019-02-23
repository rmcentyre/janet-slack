#!/bin/bash -x

eval "$(ssh-agent -s)"
chmod 600 key
ssh-add key

case $1 in
    staging) scp_dest="/slack-qa/";;
    release) scp_dest="/slack/";;
esac

scp -P 15010 -o StrictHostKeyChecking=no -r app.py janet.wsgi ./common ./resources travis@slack.rmcentyre.com:$scp_dest

ssh -P 15010 -o StrictHostKeyChecking-no travis@slack.rmcentyre.com << 'EOF'
    export PIPENV_VENV_IN_PROJECT=true
    pipenv install
EOF
