from . import criteria_check_api_blueprint
from .. import create_app
from flask import request
from .api.CriterInfo import CriteriaInfoClient
import jsonify

app = create_app()

@criteria_check_api_blueprint.route('/check',methods=['GET'])
def index():
    name = request.args.get('name')
    criteria_info = CriteriaInfoClient.get_info(name)
    response_json = CriteriaInfoClient.check_criterias(criteria_info)
    return jsonify(response_json)
