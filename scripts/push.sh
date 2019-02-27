#!/bin/bash -x

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"

eval "$(ssh-agent -s)"
chmod 600 key
ssh-add key

git push --force origin origin/dev:master
