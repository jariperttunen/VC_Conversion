#https://osric.com/chris/accidental-developer/2018/03/converting-cvs-to-git-repository/
#cvs2svn project includes cvs2git
#Commands to convert cvs repository to git, example is lignum core-model. 
mkdir cvsrepo
mkdir gitrepo

cd cvsrepo
#For core-model <project> is (one at a time): CVSROOT,c++adt,stl-lignum,Firmament,stl-voxelspace,XMLTree,LEngine,Pine,qt-workbench,Graphics
rsync -av jarip@redmine.ns.luke.fi:/home/cvs/<project> .

cvs2git --blobfile=../gitrepo/git-blob.dat --dumpfile=../gitrepo/git-dump.dat --retain-conflicting-attic-files  --username=jarip --fallback-encoding=ascii . >> coremodel.log
#Create empty main (root) repository
cd ../gitrepo/
git init --bare lignum-core.git
cd lignum-core.git
#import git files created by cvs2git
cat ../git-blob.dat ../git-dump.dat | git fast-import
git gc --prune=now
cd ..
#Clone the main repository and add it to GitHub
git clone lignum-core.git
cd lignum-core
#To GitHub
git remote add origin https://github.com/jariperttunen/lignum-core.git
git add --all
git commit -m "Conversion from CVS to Git"
git push -u origin master
git remote -v
