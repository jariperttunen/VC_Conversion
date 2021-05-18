## Converting cvs to git

The example is for lignum-core repository.
See detailed [instructions](https://osric.com/chris/accidental-developer/2018/03/converting-cvs-to-git-repository/).
The cvs2svn MacPorts port includes the required cvs2git.

### Commands to convert CVS repository to Git. 

+ mkdir cvsrepo
+ mkdir gitrepo
+ cd cvsrepo

For each lignum core-model `<project>` rsync from the original cvs repository:
+ rsync -av \<user\>@\<server\>:/home/cvs/\<project\> .

where `<project>` is (one at a time): CVSROOT,c++adt,stl-lignum,Firmament,stl-voxelspace,XMLTree,LEngine,Pine,qt-workbench,Graphics.
The server part is optional if you have direct access to repository.

+ cvs2git --blobfile=../gitrepo/git-blob.dat --dumpfile=../gitrepo/git-dump.dat --retain-conflicting-attic-files  --username=jarip --fallback-encoding=ascii . >> coremodel.log

Note that CVSROOT is mandatory if other projects need conversion to Git. cvs2git needs it in conversion. For example for project FineRoots both CVSROOT and FineRoots both must appear after rsync. CVSROOT can be deleted from Git repository after conversion. 

Create empty main (root) repository:
+ cd ../gitrepo/
+ git init --bare lignum-core.git
+ cd lignum-core.git

Import git files created by cvs2git:
+ cat ../git-blob.dat ../git-dump.dat | git fast-import
+ git gc --prune=now

Note that the `bare` Git repository shows only adminstrative files. To use the lignum-core the repository
must be cloned:
+ cd ..
+ git clone lignum-core.git
+ cd lignum-core

Optional: Push to GitHub
+ git remote add origin https://github.com/<githubuser\>/lignum-core.git
+ git add --all
+ git commit -m "Conversion from CVS to Git"
+ git push -u origin master
+ git remote -v
