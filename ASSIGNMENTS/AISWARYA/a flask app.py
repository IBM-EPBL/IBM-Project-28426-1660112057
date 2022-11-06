from flask import Flask

app = Flask(__name__)


#@app.route('/')
#def hello():
 #   return render_template("C:\Users\HP\Desktop\IBM Naliya Thiran\john.html")
#if __name__ == "__main__"
@app.route('/')
def hello():
    return 'Hello, World!'
app.run()