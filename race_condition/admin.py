from flask import Blueprint, render_template
from race_condition.auth import login_required

bp = Blueprint("admin", __name__, url_prefix="/admin")

@bp.route("/")
@login_required
def index():
    template_vars = {}
    return render_template("admin/index.html", **template_vars)
