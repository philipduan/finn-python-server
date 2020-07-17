from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from random import randrange
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

@app.route("/")
@cross_origin()
def voice():
  tone = ['Humorous', 'Ironic', 'Cynical']
  return jsonify(tone[randrange(3)])

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')