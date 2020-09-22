#Clone all Hg projects in the given Hg directory
#MottiFor contains Fortran in several files.
import subprocess
import glob
import pathlib
import argparse

class HgClone:
    """
    Clone all Hg projects in the given Hg directory
    MottiFor contains Fortran in several files.
    """
    def __init__(self,repo_path:str):
        self.repo_path=pathlib.Path(repo_path)
        self.repo_ls=self.repo_path.iterdir()
    def clone_hg_repo(self):
        fout = open('HgClone_stdout.txt','w')
        ferr = open('HgClone_stderr.txt','w')
        for repo_dir in self.repo_ls:
            print(repo_dir)
            subprocess.run(['hg','clone',str(repo_dir)],
                            stdout=fout,stderr=ferr)
        fout.close()
        ferr.close()
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',type=str,dest='f',help='Hg repo directory')
    args = parser.parse_args()
    if args.f == None:
        print("No Hg repo directory")
        quit()
    hgclone = HgClone(args.f)
    hgclone.clone_hg_repo()

