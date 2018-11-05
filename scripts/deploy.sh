#!/bin/bash

eval "$(ssh-agent -s)"
chmod 600 key
ssh-add key

case $1 in
    staging) scp_dest="/slack-qa/"
    release) scp_dest="/slack/"
esac

scp -P 15010 ./janet.* travis@rmcentyre.com:$scp_dest

