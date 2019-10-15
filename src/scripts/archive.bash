#!/bin/sh

# Script to archive a supplied branch name

# Parameters
#
#	Branch name
#
# Note : Credit to Aaron West for http://www.aaronwest.net/blog/index.cfm/2011/6/7/Git-Workflows-Archiving-Old-Branches
# 

BRANCH=$1
echo "Archiving branch $BRANCH"

git tag archive/$BRANCH $BRANCH 

echo "Branch tagged as archive/$BRANCH"

git branch -d $BRANCH

echo "Deleted the local branch"

git push origin :$BRANCH
git push --tags

echo "Pushed the deletion to the server"

echo "$BRANCH archived"


