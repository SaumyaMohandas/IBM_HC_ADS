import numpy as np
from flask import Flask, render_template,request
app = Flask(__name__)
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "DdE__V_DMNe7ctXwJkqRyGhft1PNG9gESB2XHusKRx63"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

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

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [[int(s),int(p),int(q),int(r)]], "values": t}]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/06a80b61-68ab-4b0f-92e5-7039d71f8a6e/predictions?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print(response_scoring)
    predictions =response_scoring.json() 
    output = predictions['predictions'][0]['values'][0][0]
    print("Final prediction :",output)

    print(output)
    return render_template('index.html', y= "The prediction by ibm watson is: "+str(np.round(output)))
if __name__ == '__main__':
    app.run()

