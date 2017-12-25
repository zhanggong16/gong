import sys, os
import subprocess

def create_venv(path):
    virtualenv_path = subprocess.check_output(['which', 'virtualenv']).strip()
    if not virtualenv_path:
        print "Not found virtualenv, do 'yum install virtualenv -y'" 
        sys.exit(0)
    
    venv_path = "%s/venv" % path
    if os.path.isdir(venv_path):
        pass
    else:
        virtualenv_create_cmd = "%s venv" % virtualenv_path
        os.chdir(path)
        os.system(virtualenv_create_cmd)
