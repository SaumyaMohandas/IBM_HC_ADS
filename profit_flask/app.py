import numpy as np
from flask import Flask, render_template,request
app = Flask(__name__)
import pickle


model =pickle.load(open('profit.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template('index.html')

@app.route('/login',methods = ['POST'])
def login():
    p =request.form["ms"]
    q = request.form["as"]
    r = request.form["rd"]
    s = request.form["s"]
    if(s == "cal"):
        s=0
    elif (s== "flo"): 
        s=1
    else:
        s=2  
    t = [[int(s),int(p),int(q),int(r)]]
    output = model.predict(t) 
    print(output)
    return render_template('index.html', y= "The predicted profit is: "+str(np.round(output[0])))

if __name__ == '__main__':
    app.run()