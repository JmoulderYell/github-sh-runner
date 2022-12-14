import sys
import subprocess
import json
import argparse

parser = argparse.ArgumentParser(
    description=("Python script to run when starting Github Actions Self-Hosted Runner container, this will obtain the Runner Config, and start the service"),
    epilog='''Let's get these security reports!''')
args = parser.parse_args()


ghasrunnerconfig = subprocess.Popen(["/gh-actions-runner/config.sh --unattended --url https://github.com/YellEngineering --token $(cat /tmp/runnertoken.txt) --name ghas-$(echo $RANDOM | md5sum | head -c 20) --runnergroup security --labels security,ghas-runner,self-hosted,poc"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(ghasrunnerconfig)
ghasrunnerstart = subprocess.Popen(["/gh-actions-runner/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
