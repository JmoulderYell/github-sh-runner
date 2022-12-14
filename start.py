import sys
import subprocess
import requests
import json
import argparse

parser = argparse.ArgumentParser(
    description=("Python script to run when starting Github Actions Self-Hosted Runner container, this will obtain the Runner Config, and start the service"),
    epilog='''Let's get these security reports!''')
args = parser.parse_args()

url = 'https://api.github.com/orgs/yellengineering/actions/runners/registration-token'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer <GITHUB TOKEN>',
    'X-GitHub-Api-Version': '2022-11-28'
    }

response = requests.post(url, headers=headers)
response_json = response.json()
token = json.dumps(response_json['token'])
print(token)
f = open("/tmp/runnertoken.txt", "w")
f.write(token)
f.close()

ghasrunnerconfig = subprocess.Popen(["/gh-actions-runner/config.sh --unattended --url https://github.com/YellEngineering --token {token} --name ghas-$(echo $RANDOM | md5sum | head -c 20) --runnergroup security --labels security,ghas-runner,self-hosted,poc"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(ghasrunnerconfig)
ghasrunnerstart = subprocess.Popen(["/gh-actions-runner/run.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
