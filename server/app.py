from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False

# Set a secret key for session management
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    # Initialize session variables if they don't exist
    session["hello"] = session.get("hello", "World")
    session["goodnight"] = session.get("goodnight", "Moon")

    # Check if the requested key exists in the session
    session_value = session.get(key)
    if session_value is None:
        return jsonify({'error': f'Session key "{key}" does not exist'}), 404

    # Build response JSON
    response_data = {
        'session': {
            'session_key': key,
            'session_value': session_value,
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]} for cookie in request.cookies],
    }

    response = make_response(jsonify(response_data), 200)

    # Set a cookie named 'mouse' with a value of 'Cookie'
    response.set_cookie('mouse', 'Cookie', max_age=3600, secure=True, httponly=True)

    return response

if __name__ == '__main__':
    app.run(port=5555)
