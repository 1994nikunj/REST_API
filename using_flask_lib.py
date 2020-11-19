from flask import Flask

app = Flask(__name__)
REST_GET_URL = 'https://reqres.in/api/users/1'


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.request_class()
