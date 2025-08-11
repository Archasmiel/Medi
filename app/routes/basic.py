from flask import Blueprint, render_template
from app.models.user import User
from app.services.database import db

bp = Blueprint('basic', __name__)


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@bp.route('/users/add/<name>')
def add_user(name):
    new_user = User(name=name)
    db.session.add(new_user)
    db.session.commit()
    return render_template('user_add.html', name=name)
