from . import criteria_check_api_blueprint
from .. import create_app

app = create_app()

@criteria_check_api_blueprint.route('/')
def index():
    return {
            'message':'Initial commit of criteria check application'
            }
