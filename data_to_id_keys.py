import os, json
from pprint_db import pprint

json_url = os.path.join("data", "full_data.json")
data = json.load(open(json_url))
print(data.keys())

new_data = {}
for k in data:
    print(data[k])
    new_data[data[k]['0']['model_info'][0]['id']] = data[k]

out_p = os.path.join('data', 'id_data.json')
with open(out_p, 'w') as out_f:
    json.dump(new_data, out_f)

with open(out_p, 'r') as out_f:
    pprint(out_f)
