import yaml
import os
import json
import joblib
import numpy as np
from src.get_data import read_params

params_path = "params.yaml"
schema_path = os.path.join("research","schema_in.json")

class NotInRange(Exception):
    def __init__(self,message="value entered not in Range"):
        self.message = message
        super().__init__(self.message)


class NotInCols(Exception):
    def __init__(self,message="Not in Columns"):
        self.message = message
        super().__init__(self.message)\
        
def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]

    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected results"
    
def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(dict_req):
    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCols
    
    def _validate_values(col,val):
        schema = get_schema()
        if not (schema[col]["min"] <= float(dict_req[col]) and float(dict_req[col]) <= schema[col]["max"]):
            raise NotInRange

    for col,val in dict_req.items():
        _validate_cols(col)
        _validate_values(col,val)
    
    return True

def form_response(dict_request):
    try:
        if validate_input(dict_request):
            data = dict_request.values()
            data = [list(map(float,data))]
            response  = predict(data)
            return response
    except Exception as e:
        response = {"The_Expected_Range" : get_schema(),"response":str(e)}
        return response

def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.values())])
            response = predict(data)
            response = {"response": response}
            return response
    except NotInRange as e:
        response = {"The_Expected_Range" : get_schema(),"response":str(e)}
        return response
    except NotInCols as e:
        response = {"The_Expected_Cols" : get_schema().keys(),"response":str(e)}
        return response
    except Exception as e:
        response = {"response":str(e)}
        return response