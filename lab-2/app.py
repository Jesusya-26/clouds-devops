from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'I\'m alive'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 500))
    app.run(debug=True, host='0.0.0.0', port=port)

