# Dependencies
from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np
import spacy
import string
from dataCleaning import dataCleaning
import json
import sys
from flask_cors import CORS,cross_origin



# Your API definition
app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/',methods=['POST','GET','OPTIONS'])

def predict():
    if mp:
        try:
            json_ = request.json
            print(json_)
            
            prediction=[]
            for x in json_:
               key = x.keys()
            #    print(key)
               value = x.values()
               for v in value:
                #  print(v)
                 prediction.append(mp.predict([v]))
                

            # query = json.dumps(json_)

            # print(query)
            # query=query[7:-3]
            # print(query)

            # prediction = (mp.predict([query]))
            # print(prediction)
            output=[]
            cnt_neg=0
            for pred in prediction:
                if pred[0]==0:
                    output.append("Negative")
                else:
                    output.append("Positive")
                # print(pred)
            
            # print(output)

            return jsonify({'prediction': str(output)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    mp = joblib.load("model.pkl") # Load "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')
    

    
    app.run(port=port,debug=True)