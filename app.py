from flask import Flask, render_template,jsonify
import pyjokes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/get_joke', methods=['GET'])
def get_joke():
    joke= pyjokes.get_joke()
    return jsonify({"joke": joke})



if __name__ == '__main__':
    app.run(debug=True,)