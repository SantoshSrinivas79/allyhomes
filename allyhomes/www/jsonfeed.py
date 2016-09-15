import json

data = {
   'title' : 'ammmittthhhhhhhhaaaaaaa',
   'start' : '2016-09-11'
}

json_str = json.dumps(data)
data = json.loads(json_str)
