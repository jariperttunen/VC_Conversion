#!/bin/sh
#Assuming a set of cloned repositories in directory
#this command line framework creates GitHub repositoeries and 
#pushes current work there.  
dirnames=`ls`
for dirname in $dirnames
do
    echo $dirname
    pushd $dirname
    #Assuming cloned repository remote name is origin 
    git remote rename origin clonedorigin
    repository=lukemotti/$dirname
    echo $repository
    #gh is part of GitHub CLI (GitHub Command Line Interface)
    gh repo create $repository --private --confirm
    #GitHub repository remote name is origin by default, assuming the current *branch* name is master
    git push origin master
    popd
    #exit
done
