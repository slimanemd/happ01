from flask import Flask

app =  Flask(__name__)


@app.route('/')
def index():
    return 'Hello Heroku World 2020'


if __name__ == '__main__':
    app.run()

