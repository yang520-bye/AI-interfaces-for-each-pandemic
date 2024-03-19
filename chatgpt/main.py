from flask import Flask, request, jsonify
from flask_cors import CORS
from chatgpt.api import make_new_conversation_id, sends

app = Flask(__name__)
CORS(app)


@app.route('/send', methods=['POST'])
def send():
    conversation_id = request.json.get('conversation_id')
    msg = request.json.get('msg')
    ws = sends(msg, conversation_id)
    return jsonify({'ws': ws})


@app.route('/createId',methods=['GET'])
def createId():
    conversation_id = make_new_conversation_id()
    return jsonify({'id': conversation_id})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
