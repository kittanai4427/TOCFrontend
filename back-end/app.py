from flask import Flask, jsonify,render_template
import WebReader as wr
app = Flask(__name__)

data = wr.getJSON()
@app.route('/')
def index():
    data = wr.getJSON()
    return render_template('index.html',data=data)

@app.route("/database", methods=['GET'])
def get():

    # return jsonify({'database' : database})
    return render_template('index.html',database=data)

@app.route("/database/<int:id>", methods=['GET'])
def get_name(id):
    return jsonify({'database' : data[id]})   


if __name__ == '__main__':
    app.run(debug=True)