from flask import Flask, render_template
from flask_bootstrap import Bootstrap
appFlask = Flask(__name__)
Bootstrap(appFlask)
@appFlask.route('/')
def index():
return render_template('index.html')
if __name__ == '__main__':
appFlask.run(debug=True)