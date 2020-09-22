#Install git-remote-hg to your PATH and run this script
#Mac: sudo port install git-remote-hg
#git-remote-hg: https://github.com/felipec/git-remote-hg
#Obviously git and mercurial both are needed 
import subprocess
import glob
import pathlib
import argparse
class HG2Git:
    """
    Install git-remote-hg to your PATH and run this script
    Mac: sudo port install git-remote-hg
    git-remote-hg: https://github.com/felipec/git-remote-hg
    Obviously git and mercurial both are needed
    """
    def __init__(self,repo_path:str):
        self.repo_path=pathlib.Path(repo_path)
        self.hg_repo_ls=self.repo_path.iterdir()
    def convert_hg_repo(self):
        fout = open('HG2Git_stdout.txt','w')
        ferr = open('HG2Git_stderr.txt','w')
        for repo_dir in self.hg_repo_ls:
            print(repo_dir)
            if repo_dir.is_dir():
                s=str(repo_dir)
                s='hg::'+s
                subprocess.run(['git','clone',s],
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
    hg2git = HG2Git(args.f)
    hg2git.convert_hg_repo()
                                    
                                     

