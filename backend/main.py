from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import tensorflow as tf
import numpy as np


class Model:

    def __init__(self, directory):
        self.classes = ["Setosa", "Versicolor", "Virginica"]

        self.session = tf.compat.v1.Session()
        self.graph = tf.compat.v1.get_default_graph()

        with self.graph.as_default():
            with self.session.as_default():
                self.model = tf.keras.models.load_model(directory)
                
    def predict(self, x):
        with self.graph.as_default():
            with self.session.as_default():
                y = self.model.predict(x.astype(np.float).reshape(1, 4))[0]
        return str(self.classes[int(np.argmax(y))])


app = Flask(__name__)
CORS(app)
api = Api(app)

model = Model("./model.h5")

parser = reqparse.RequestParser()
parser.add_argument("sepal_length")
parser.add_argument("sepal_width")
parser.add_argument("petal_length")
parser.add_argument("petal_width")


class Predict(Resource):

    @staticmethod
    def post():
      global model, parser

      args = parser.parse_args()
      x = np.array(
        [
          args["sepal_length"],
          args["sepal_width"],
          args["petal_length"],
          args["petal_width"]
        ]
      )

      result = model.predict(x)
      return {'class': result}


api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
