from flask import Flask,Response
global search
import requests as req
from flask import Flask, Response
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
api_key = os.environ.get("GITHUB_API_KEY", "")
owner = os.environ.get("REPO_OWNER", "")
repo = os.environ.get("REPO_NAME", "")

@app.route("/commits")
def commit():
    def streamer():
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/vnd.github.v3+json",
        }
        res = req.get(f'https://api.github.com/repos/{owner}/{repo}/commits', headers=headers)
        data = res.json()
        for i in data:
            commit = {"author": i['commit']['author']['name'], "message": i['commit']['message'], "date": i['commit']['author']['date']}
            yield str(f"{commit}\n")
    return Response(streamer())

@app.route("/issuesAndPR")
def issueandpr():
    def streamer():
        headers = {"Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"}
        res = req.get(f'https://api.github.com/repos/{owner}/{repo}/issues', headers=headers)
        data = res.json()
        for i in data:
            if ("pull_request" in i):
                issues = {"title": i['title'], "login": i['user']['login'], "date": i['created_at'],"body" : i["body"],"isPr" : True}
            else:
                issues = {"title": i['title'], "login": i['user']['login'], "date": i['created_at'],"body" : i["body"],"isPr" : False}
            yield str(f"{issues}\n")

    return Response(streamer())
    
if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=4000)