from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
# from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

import os.path
import markdown
import settings

load_dotenv()

app = Flask(__name__)
auth = HTTPBasicAuth()

ACTIVE_PROBLEM="1_roman_numerals"

def load_markdown(path):
    if not os.path.exists(path):
        return ("Markdown file not found", 404)

    # Read the content of the file
    with open(path, 'r') as md_file:
        md_content = md_file.read()

    return markdown.markdown(md_content, extensions=['fenced_code'])

@app.route("/")
def index():
    return show_problem(ACTIVE_PROBLEM)

def _list_problems():
    return os.listdir("problems")

@app.route("/problems/list")
def list_problems():
    template_vars = {
        "problem_list": _list_problems()
    }
    return render_template('problem/list.html', **template_vars)

@app.route("/problems/<name>")
def show_problem(name):
    return _show_problem(name)

def _show_problem(name, challenge_number=1):
    challenge_number = 1
    problem_statement = load_markdown(f"problems/{name}/problem.md")
    challenge_input = load_markdown(f"problems/{name}/input_{challenge_number}.md")
    template_vars = {
        "title": "Welcome",
        "problem_statement": problem_statement,
        "challenge_input": challenge_input,
        "challenge_number": challenge_number,
        "problem_name": name,
    }
    return render_template('problem/show.html', **template_vars)


@app.route("/problems/<problem_name>/challenges/<int:challenge_number>/validate/", methods=["POST"])
def validate(problem_name, challenge_number):

    if problem_name not in _list_problems():
        return "Invalid problem name", 400

    if challenge_number not in range(1,4):
        return "Invalid challenge number", 400

    answer_file = f"problems/{problem_name}/answer_{challenge_number}.txt"
    with open(answer_file, 'r') as f:
        answer_string = f.read()

    if answer_string == request.json["data"]:
        return "success", 200

    return "Invalid submission", 400


if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
