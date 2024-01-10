import json

def export_to_json(file_path):
    with open(file_path) as f:
        json_data = json.load(f)
        print (json_data)
    data_list = []
    for item in json_data['datas']:
        Id = item['id']
        Priority = item['priority']['name']
        Site = item['site']['name']
        Status = item['status']['name']
        Time = item['created_time']['display_value']
        data_list.append([Id,Time,Priority,Site,Status])

