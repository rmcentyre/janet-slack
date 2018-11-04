#!/bin/bash

eval "$(ssh-agent -s)"
chmod 600 key
ssh-add key

scp -P 15010 ./janet.* travis@rmcentyre.com:/slack/
