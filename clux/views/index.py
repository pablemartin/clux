from flask import Blueprint, redirect, render_template, abort, url_for
from flask_security import login_required
index_bp = Blueprint('view_index', __name__)


@index_bp.route('/')
@login_required
def index():
    return render_template('index.html')