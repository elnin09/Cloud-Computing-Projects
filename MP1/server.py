from flask import Flask, jsonify, request
import json

app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def index():
    global seed
    print(request.get_json())
    if(request.method == 'POST'):
        some_json = request.get_json()
        y=request.json
        seed = y["num"]
        return jsonify({"num": seed})
    elif(request.method == 'GET'):
        return str(seed)

if __name__ ==  '__main__':
    global seed
    seed = 0
    app.run(host='0.0.0.0',port = 5000)
    
        
            
        

    