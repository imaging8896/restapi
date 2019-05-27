import requests


def get(api_path, headers):
    try:
        resp = requests.get(api_path, headers=headers)
    except requests.ConnectionError as e:
        print(e)  # should I also sys.exit(1) after this?
        resp = None
    return resp


def post(api_path, headers, data=None, json=None, files=None):
    resp = None
    try:
        if files:
            resp = requests.post(api_path, data=data, json=json, headers=headers, files=files)
        else:
            resp = requests.post(api_path, data=data, json=json, headers=headers)
    except requests.ConnectionError as e:
        print(e)  # should I also sys.exit(1) after this?
    return resp


def put(api_path, headers, data=None, json=None):
    try:
        resp = requests.put(api_path, data=data, json=json, headers=headers)
    except requests.ConnectionError as e:
        print(e)  # should I also sys.exit(1) after this?
        resp = None
    return resp


def delete(api_path, headers):
    try:
        resp = requests.delete(api_path, headers=headers)
    except requests.ConnectionError as e:
        print(e)  # should I also sys.exit(1) after this?
        resp = None
    return resp
