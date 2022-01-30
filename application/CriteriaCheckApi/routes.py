from . import criteria_check_api_blueprint
from .. import create_app
from flask import request, jsonify
from .api.CriterInfo import CriteriaInfoClient

app = create_app()

@criteria_check_api_blueprint.route('/check',methods=['GET'])
def index():
    city_name = request.args.get('city')
    criteria_info = CriteriaInfoClient.get_info(city_name)
    response_json = CriteriaInfoClient.check_criterias(criteria_info)
    return jsonify(response_json)