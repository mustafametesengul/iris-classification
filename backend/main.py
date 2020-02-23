from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

import tensorflow as tf
import numpy as np


app = Flask(__name__)
CORS(app)
api = Api(app)

sess = tf.Session()
graph = tf.get_default_graph()
tf.keras.backend.set_session(sess)

model = tf.keras.models.load_model("model.h5")

parser = reqparse.RequestParser()
parser.add_argument("sepal_length")
parser.add_argument("sepal_width")
parser.add_argument("petal_length")
parser.add_argument("petal_width")


class Predict(Resource):

    @staticmethod
    def post():
        global sess
        global graph
        global model

        iris = ["Setosa", "Versicolor", "Virginica"]

        args = parser.parse_args()
        x = np.array(
            [
              args["sepal_length"],
              args["sepal_width"],
              args["petal_length"],
              args["petal_width"]
            ]
          ).astype(np.float).reshape(1, 4)

        with graph.as_default():
            tf.keras.backend.set_session(sess)
            y = model.predict(x)[0]
            return {'class': str(iris[int(np.argmax(y))])}


api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
