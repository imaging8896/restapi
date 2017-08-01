import requests


def get(api_path, headers):
    try:
        resp = requests.get(api_path, headers=headers)
    except requests.ConnectionError, e:
        print e  # should I also sys.exit(1) after this?
        resp = None
    return resp


def post(api_path, headers, data=None, json=None):
    try:
        resp = requests.post(api_path, data=data, json=json, headers=headers)
    except requests.ConnectionError, e:
        print e  # should I also sys.exit(1) after this?
        resp = None
    return resp


def delete(api_path, headers):
    try:
        resp = requests.delete(api_path, headers=headers)
    except requests.ConnectionError, e:
        print e  # should I also sys.exit(1) after this?
        resp = None
    return resp
