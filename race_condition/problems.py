import os.path
import markdown
from flask import Blueprint, render_template, request, jsonify, current_app

# from race_condition import settings
from race_condition.auth import login_required

from race_condition.db import get_db

bp = Blueprint("problems", __name__, url_prefix="/")


def set_active_problem(problem_name):
    db = get_db()
    db.execute(
        'UPDATE properties SET value = ? WHERE name = "active_problem"', (problem_name,)
    )
    db.commit()


def get_active_problem():
    db = get_db()
    cursor = db.execute(
        'SELECT name, value FROM properties WHERE name == "active_problem"'
    )
    result = cursor.fetchone()

    if result:
        # If the 'active_problem' property exists, fetch its value
        active_problem_value = result["value"]
        print(active_problem_value)
        return active_problem_value
    else:
        # If the 'active_problem' property does not exist, insert it with a default value
        default_value = _list_problems()[0]  # Define your default value
        print(f"Inserting {default_value} as default active_problem")
        db.execute(
            "INSERT INTO properties (name, value) VALUES (?, ?)",
            ("active_problem", default_value),
        )
        db.commit()
        return default_value


def load_markdown(path):
    full_path = os.path.join(current_app.root_path, path)
    if not os.path.isfile(full_path):
        return "Markdown file not found", 404

    with current_app.open_resource(path, "r") as md_file:
        md_content = md_file.read()

    return markdown.markdown(md_content, extensions=["fenced_code"])


def _list_problems():
    full_path = os.path.join(current_app.root_path, "problems")
    return os.listdir(full_path)


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
    return render_template("problem/show.html", **template_vars)


def _show_challenge(problem_name, challenge_number):
    # Try return next challenge if one exists
    next_challenge_candidate = f"problems/{problem_name}/input_{challenge_number}.md"
    full_path = os.path.join(current_app.root_path, next_challenge_candidate)

    if os.path.exists(full_path):
        template_vars = {
            "problem_name": problem_name,
            "challenge_input": load_markdown(
                f"problems/{problem_name}/input_{challenge_number}.md"
            ),
            "challenge_number": challenge_number,
        }
        next_challenge = render_template("problem/_challenge.html", **template_vars)
        return next_challenge


def validate_challenge_submission(problem_name, challenge_number, submission):
    answer_file = f"problems/{problem_name}/answer_{challenge_number}.txt"

    with current_app.open_resource(answer_file, "r") as f:
        answer_string = f.read()

    if str(answer_string).strip() == str(submission).strip():
        return True

    return False


@bp.route("/")
def index():
    active_problem = get_active_problem()
    return _show_problem(active_problem)


@bp.route("/problems/")
@login_required
def list_problems():
    template_vars = {"problem_list": _list_problems()}
    return render_template("problem/list.html", **template_vars)


@bp.route("/problems/<name>")
@login_required
def show_problem(name):
    return _show_problem(name)


@bp.route(
    "/problems/<name>/activate",
    methods=["POST"],
)
@login_required
def activate(name):
    # TODO
    set_active_problem(name)
    # g.active_problem=name
    return "ok", 200


@bp.route(
    "/problems/<problem_name>/challenges/<int:challenge_number>/validate/",
    methods=["POST"],
)
def validate(problem_name, challenge_number):

    # No path traversal
    if problem_name not in _list_problems():
        return "Invalid problem name", 400

    if isinstance(challenge_number, int):
        return "Invalid challenge number", 400

    submission_is_valid = validate_challenge_submission(
        problem_name, challenge_number, request.json["data"]
    )

    if not submission_is_valid:
        return "Incorrect submission", 400

    next_challenge = _show_challenge(problem_name, challenge_number + 1)

    if next_challenge is None:
        next_challenge = "<h1 class='success'>Problem Complete</h1>"

    return jsonify(
        {
            "challenge_response": next_challenge,
        }
    )
