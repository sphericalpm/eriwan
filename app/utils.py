from functools import wraps

from flask import request, redirect, url_for, flash
from flask_login import current_user


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if not current_user.is_admin:
                flash("Для доступа нужно обладать правами администратора")
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return redirect(url_for('login'))
    return decorated_function
