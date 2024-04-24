from flask_restplus import Namespace, Resource

api = Namespace('security', description='Security Endpoints')
logger = get_logger(__name__)