import sys
import json
import subprocess
from flask import Flask, request

github_token = sys.argv[1]

app = Flask(__name__)

@app.route('/pyload', methods=['POST'])
def webhook():
	data = json.loads(request.data)
	merged_status = data['pull_request']['merged']
	if merged_status == True:
		sha = data['pull_request']['merge_commit_sha']
		status_url = data['repository']['statuses_url'].replace("{sha}", sha)
		repository_url = data['repository']['clone_url']
		subprocess.Popen(["./experimentrunner", sha, status_url, repository_url, github_token])
	return "OK"

if __name__ == '__main__':
	app.run(host="0.0.0.0", port="8000")
