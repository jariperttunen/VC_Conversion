#!/bin/sh

dirnames=`ls`
for dirname in $dirnames
do
    echo $dirname
    pushd $dirname
    #Assuming cloned repository is origin 
    git remote rename origin clonedorigin
    repository=lukemotti/$dirname
    echo $repository
    gh repo create $repository --private --confirm
    #GitHub is origin by default, assuming the branch name is master
    git push origin master
    popd
    #exit
done
