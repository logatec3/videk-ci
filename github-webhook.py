import sys
import json
import subprocess
from flask import Flask, request

github_token = sys.argv[1]

app = Flask(__name__)

@app.route('/pyload', methods=['POST'])
def webhook():
	data = json.loads(request.data)
	if 'hook_id' not in data:
		tag_name = data['release']['tag_name']
		upload_url = data['release']['upload_url'].replace("{?name,label}", "")
		repository_name = data['repository']['name']
		repository_url = data['repository']['clone_url']
		subprocess.Popen(["./releasebuilder", tag_name, upload_url, repository_name, repository_url, github_token])
	return "OK"

if __name__ == '__main__':
	app.run(host="localhost", port=8000)
