#!/bin/bash -x

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

eval "$(ssh-agent -s)"
chmod 600 key
ssh-add key

# Travis clones with https, so change to ssh
git remote set-url origin git@github.com:rmcentyre/janet-slack.git

git push --force origin origin/dev:master
