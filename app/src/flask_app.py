import logging

import flask

from predict_species import predict_species_from

app = flask.Flask(__name__)

app_route = "/predict_iris"
allowed_methods = ["POST"]
force_input_as_json = True
log_format = "%(levelname)-7s: %(asctime)s %(message)s"

logging.basicConfig(level=logging.DEBUG, format=log_format)


def _log_request(rr):
    message_to_log = " ".join([app_route, "received", str(rr)])
    logging.info(message_to_log)


def _log_prediction(pp):
    message_to_log = " ".join([app_route, "returned", str(pp)])
    logging.info(message_to_log)


@app.route(app_route, methods=allowed_methods)
def predict_iris():
    """
    Predicts the iris species for the received parameters of a single sample.
    :return: Dict[str]. The prediction.
    """
    request_data = flask.request.get_json(force=force_input_as_json)
    _log_request(request_data)
    iris_species = predict_species_from(request_data)
    _log_prediction(iris_species)
    return flask.jsonify(iris_species)
