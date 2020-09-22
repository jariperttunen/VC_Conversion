#Clone all Git projects in the given Git directory
#MottiFor contains Fortran in several files.
import subprocess
import glob
import pathlib
import argparse

class GitClone:
    """
    Clone all Git projects in the given Git directory
    MottiFor contains Fortran in several files.
    """
    def __init__(self,repo_path:str):
        self.repo_path=pathlib.Path(repo_path)
        self.repo_ls=self.repo_path.iterdir()
    def clone_git_repo(self):
        fout = open('GitClone_stdout.txt','w')
        ferr = open('GitClone_stderr.txt','w')
        for repo_dir in self.repo_ls:
            print(repo_dir)
            subprocess.run(['git','clone',str(repo_dir)],
                            stdout=fout,stderr=ferr)
        fout.close()
        ferr.close()
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',type=str,dest='f',help='Git repo directory')
    args = parser.parse_args()
    if args.f == None:
        print("No Git repo directory")
        quit()
    gitclone = GitClone(args.f)
    gitclone.clone_git_repo()

