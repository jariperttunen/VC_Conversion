## Converting CVS repository to Git repository

The example is for *lignum-core* CVS projects. Adjust workflow for each specific case.
See also detailed original [instructions](https://osric.com/chris/accidental-developer/2018/03/converting-cvs-to-git-repository/).
The cvs2svn MacPorts port includes the required cvs2git.

### Step by step commands to convert CVS repository to Git. 
First, create two directories, one for CVS and one for the Git.
+ mkdir cvsrepo
+ mkdir gitrepo
+ cd cvsrepo

For each lignum core-model `<project>` rsync from the original cvs repository */home/cvs/*:
+ rsync -av \<user\>@\<server\>:/home/cvs/\<project\> .

where `<project>` is (one at a time): CVSROOT,c++adt,stl-lignum,Firmament,stl-voxelspace,XMLTree,LEngine,Pine,qt-workbench,Graphics.
The server part is optional if you have direct access to repository.

Then do the conversion. The \<user\> denotes the user name, owner, of the repository files:
+ cvs2git --blobfile=../gitrepo/git-blob.dat --dumpfile=../gitrepo/git-dump.dat --retain-conflicting-attic-files  --username=\<user\> --fallback-encoding=ascii . >> coremodel.log

Note that CVSROOT is mandatory. `cvs2git` needs it in conversion. For example for the project 
FineRoots in CVS both CVSROOT and FineRoots both must appear after rsync. CVSROOT can be deleted 
from the Git repository after conversion. 

Create empty main (root) repository:
+ cd ../gitrepo/
+ git init --bare lignum-core.git
+ cd lignum-core.git

Import Git files created by cvs2git:
+ cat ../git-blob.dat ../git-dump.dat | git fast-import
+ git gc --prune=now

The so called *bare* Git repository shows only adminstrative files. To use the lignum-core.git this bare 
repository must be cloned to working repository, lignum-core:
+ cd ..
+ git clone lignum-core.git
+ cd lignum-core

The project files are now visible in lignum-core. Note that CVS lignum-core projects became a directories in Git.
In CVS *lignum-core* alias name could check them out at once, in Git lignum-core is a single repository. 

#### Optional: Push local repository to GitHub
+ Create empty *lignum-core* repository in GitHub

Still in lignum-core directory
+ git remote add origin https://github.com/<githubuser\>/lignum-core.git
+ git add --all
+ git commit -m "Conversion from CVS to Git"
+ git push -u origin master
+ Check the remote repositories
  + git remote -v

The name *origin* may already exist. Change it for example to *main* in `git remote add` and `git push`.  
