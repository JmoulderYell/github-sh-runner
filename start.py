import random
import string
import subprocess
import requests
import json
import argparse
from time import sleep

parser = argparse.ArgumentParser(
    description=("Python script to run when starting Github Actions Self-Hosted Runner container, this will obtain the Runner Config, and start the service"),
    epilog='''Let's get these security reports!''')
args = parser.parse_args()

url = 'https://api.github.com/orgs/yellengineering/actions/runners/registration-token'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer <PAT TOKEN>',
    'X-GitHub-Api-Version': '2022-11-28'
    }

response = requests.post(url, headers=headers)

response_json = response.json()
token = json.dumps(response_json['token'])
print(token)
f = open("/tmp/runnertoken.txt", "w")
f.write(token)
f.close()

get_str = string.ascii_letters + string.digits
result_str = "".join((random.choice(get_str) for i in range(10)))
print(result_str)

ghasrunnerconfig = subprocess.Popen([f"/gh-actions-runner/config.sh --unattended --url https://github.com/YellEngineering --token {token} --name ghas-{result_str} --runnergroup security --labels security"], shell=True, stdout=subprocess.PIPE)
sleep(5)
ghasrunnerstart = subprocess.Popen(["/gh-actions-runner/run.sh"], shell=True, close_fds=True, stdout=subprocess.PIPE)
