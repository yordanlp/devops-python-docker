from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    name = "Hello"
    description = "Yordan"
    url = request.host_url

    data = {
        'name': name,
        'description': description,
        'url': url
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run()
