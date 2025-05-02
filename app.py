from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/relay_sms', methods=['POST'])
def relay_sms():
    required_fields = ['token', 'from', 'to', 'text']
    
    # Validate required fields
    if not all(field in request.form for field in required_fields):
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400

    # Forward to SparrowSMS
    response = requests.post('https://api.sparrowsms.com/v2/sms/', data=request.form)

    try:
        response_json = response.json()
    except:
        return jsonify({'status': 'error', 'message': 'Invalid response from SparrowSMS', 'raw': response.text}), 500

    return jsonify({'status': 'success', 'response': response_json}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
