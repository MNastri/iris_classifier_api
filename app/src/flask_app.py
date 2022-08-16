import flask

from predict_species import predict_species_from

app = flask.Flask(__name__)

app_route = "/predict_iris"
allowed_methods = ["POST"]
force_input_as_json = True


@app.route(app_route, methods=allowed_methods)
def predict_iris():
    """
    Predicts the iris species for the received parameters of a single sample.
    :return: Dict[str]. The prediction.
    """
    request_data = flask.request.get_json(force=force_input_as_json)
    iris_species = predict_species_from(request_data)
    return flask.jsonify(iris_species)
