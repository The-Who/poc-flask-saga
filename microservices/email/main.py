from flask import Flask

app = Flask(__name__)


@app.route('/emails')
def get_info():
    return 'API: Emails'
