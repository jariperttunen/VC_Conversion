## Converting CVS repository to Git repository

The example is for *lignum-core* CVS projects. Adjust workflow for each specific case.
See also detailed original [instructions](https://osric.com/chris/accidental-developer/2018/03/converting-cvs-to-git-repository/). MacPorts has required software:

+ cvs
+ cvs2svn, includes cvs2git.


### Step by step commands to convert CVS repository to Git. 
First, create two directories, one for CVS and one for the Git.
+ mkdir cvsrepo
+ mkdir gitrepo
+ cd cvsrepo

For each lignum core-model `<project>` rsync from the original cvs repository */home/cvs/*:
+ rsync -av \<user\>@\<server\>:/home/cvs/\<project\> .

where `<project>` is (one at a time): CVSROOT, c++adt, stl-lignum, Firmament, stl-voxelspace, XMLTree, LEngine, Pine, qt-workbench, Graphics. The dot (`.`) at the end denotes the current directory. The user and server part for remote connection are not needed if you have direct access to the repository. The CVSROOT is always mandatory. `cvs2git` needs it in conversion. For example for the project FineRoots in CVS both CVSROOT *and* FineRoots both must appear after rsync. 
CVSROOT can be deleted from the Git repository after conversion. 

Next, do the conversion. The \<user\> denotes the user name, owner, of the repository files to appear in Git:
+ cvs2git --blobfile=../gitrepo/git-blob.dat --dumpfile=../gitrepo/git-dump.dat --retain-conflicting-attic-files  --username=\<user\> --fallback-encoding=ascii . >> coremodel.log

Change to gitrepo and create empty *bare* Git repository:
+ cd ../gitrepo/
+ git init --bare lignum-core.git
+ cd lignum-core.git

Import Git files created by cvs2git:
+ cat ../git-blob.dat ../git-dump.dat | git fast-import
+ git gc --prune=now

So called bare Git repositories show only adminstrative files. To use the lignum-core.git this bare 
repository must be cloned to create working repository lignum-core:
+ cd ..
+ git clone lignum-core.git
+ cd lignum-core

The project files are now visible in `lignum-core`. Note that CVS lignum-core projects became directories in Git.
In CVS lignum-core *alias name* could check them out at once, in Git lignum-core is a single repository. 

#### Push local repository to GitHub

See also GitHub instructions to [add existing project to GitHub](https://docs.github.com/en/github/importing-your-projects-to-github/importing-source-code-to-github/adding-an-existing-project-to-github-using-the-command-line)

+ Create new repository (e.g. *lignum-core*) in GitHub

Following the example still in lignum-core directory
+ git remote add origin https://github.com/<githubuser\>/lignum-core.git
+ Check the remote repositories
  + git remote -v
+ git add --all
+ git commit -m "Conversion from CVS to Git"
+ git push -u origin main

GitHub should show your project.
