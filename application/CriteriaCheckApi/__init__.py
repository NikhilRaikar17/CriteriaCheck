from flask import Blueprint

criteria_check_api_blueprint = Blueprint('criteria_check', __name__)

from . import routes
