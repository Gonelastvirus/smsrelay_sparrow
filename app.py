from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SPARROW_TOKEN = 'v2_3NbaPLXQ9Arh2kMSlQj89MExZ7i.0yRc'
FROM = 'Demo'
TO = '9845141603'

@app.route('/send_sms', methods=['GET', 'POST'])
def send_sms():
    msg = request.args.get('msg') if request.method == 'GET' else request.form.get('msg')

    if not msg:
        return jsonify({'status': 'error', 'message': 'Missing msg parameter'}), 400

    payload = {
        'token': SPARROW_TOKEN,
        'from': FROM,
        'to': TO,
        'text': msg
    }

    response = requests.post('https://api.sparrowsms.com/v2/sms/', data=payload)

    try:
        response_json = response.json()
    except:
        return jsonify({'status': 'error', 'message': 'Invalid response from SparrowSMS', 'raw': response.text}), 500

    return jsonify({'status': 'success', 'response': response_json}), response.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

