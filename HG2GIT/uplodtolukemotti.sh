#!/bin/sh

dirnames=`ls`
for dirname in $dirnames
do
    echo $dirname
    pushd $dirname
    git remote rename origin master
    repository=lukemotti/$dirname
    echo $repository
    gh repo create $repository --private --confirm
    git push origin master
    popd
    #exit
done
