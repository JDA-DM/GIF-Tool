import json
import csv
import os
import sys
import pandas as pd

args = sys.argv
files = args[1:]

for file in files:

    df = pd.read_csv(file, header=0, index_col=0)
    json_fields = df.to_json(orient='table', force_ascii=False)
    file_name = os.path.splitext(os.path.basename(file))[0]
    json_data = json.loads(json_fields)
    result = {}
    result['name'] = file_name
    result['items'] = json_data['data']
    file_path = './' + file_name + '.json'

    with open(file_path, 'w') as f:
        json.dump(result, f,  indent=2, ensure_ascii=False)
