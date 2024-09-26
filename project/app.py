import requests
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['n']
    pfp = request.form['p']
    nn = request.form['nn']
    w = request.form['w']
    data = {
        "avatar_url": pfp,
        "content": name,
        "username": nn
    }
    response = requests.post(w, json=data)
    print(data)
    
        
    return render_template('pass.html', n=name, r=response, d=data)


   
   



if __name__ == '__main__':
    app.run(debug=True)