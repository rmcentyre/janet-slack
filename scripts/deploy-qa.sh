#!/bin/bash

eval "$(ssh-agent -s)"
chmod 600 key
ssh-add key

scp ./janet.* travis@rmcentyre.com:/slack-qa/
