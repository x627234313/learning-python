#!/usr/bin/env python
# encoding: utf-8

import json
import pickle

data = {'a' : 1, 'b' : 2, 'c' : 3}

# json
json_str = json.dumps(data)
print(json_str)

data = json.loads(json_str)
print(data)

with open('C:\\Users\\chail\\Desktop\\data.json', 'w') as f:
	json.dump(data, f)

with open(r'C:\Users\chail\Desktop\data.json', 'r') as f:
	data = json.load(f)

# pickle
s = pickle.dumps(data)
print(s)

data = pickle.loads(s)
print(data)

f= open('datafile', 'wb')
pickle.dump(data, f)
f.close()

f= open('datafile', 'rb')
data = pickle.load(f)
f.close()

