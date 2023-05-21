### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/test')
def index():
    render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

