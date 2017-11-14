import method
import urllib
import logging
import sys
try:
    from http.client import HTTPConnection  # py3
except ImportError:
    from httplib import HTTPConnection  # py2


def API(func):
    HTTPConnection.debuglevel = 0
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.INFO)
    requests_log.propagate = True

    # Decorator
    def decorated_func(*args, **kwargs):
        log_file = open("restapi.log", "a+")
        sys.stdout = log_file
        print "API '" + func.__name__ + "' was called"
        api_info = func(*args, **kwargs)
        apis_obj = args[0]
        is_status_check = apis_obj.is_status_check
        url = apis_obj.url
        r = _api_call(url, api_info)
        print "API URL {}".format(url)
        print "API response object {}".format(r)
        sys.stdout = sys.__stdout__
        log_file.close()
        if is_status_check:
            if r.status_code != 200:
                raise Exception("Fail to call API the status code is not 200 but {}".format(r.status_code))
        return r
    return decorated_func


def _api_call(url, api_info):
    if not isinstance(api_info, dict):
        raise TypeError('API infomation should be dictionary type')
    url = url + api_info['path']
    headers = api_info['headers']
    query_strings = api_info['query_strings'] if 'query_strings' in api_info else None
    api_method = api_info['method']

    if query_strings:
        if not isinstance(query_strings, dict):
            raise ValueError("'query_strings' should be type of dictionary")
        else:
            url += "?" + urllib.urlencode(query_strings)

    p_info = dict(api_info)
    if "files" in p_info:
        p_info["files"] = "Truncated"
    print "API info {}".format(str(p_info))

    if api_method == "Get":
        return method.get(url, headers)
    elif api_method == "Post":
        data = api_info['data'] if 'data' in api_info else None
        json = api_info['json'] if 'json' in api_info else None
        files = api_info['files'] if 'files' in api_info else None
        return method.post(url, headers, data, json, files)
    elif api_method == "Put":
        data = api_info['data'] if 'data' in api_info else None
        json = api_info['json'] if 'json' in api_info else None
        return method.put(url, headers, data, json)
    elif api_method == "Delete":
        return method.delete(url, headers)
    else:
        raise ValueError("Undefined API method '{}'".format(api_method))


class BaseAPIs:

    def __init__(self, url, is_status_check=False):
        self.url = url
        self.is_status_check = is_status_check


class DirectAPIs:

    def __init__(self, headers, is_status_check=False):
        self.url = ""
        self.headers = headers
        self.is_status_check = is_status_check

    @API
    def api_call(self, api_method, url, data=None, json=None, files=None):
        api_info = {
            "method": api_method,
            "path": url,
            "headers": self.headers
        }
        if data:
            api_info["data"] = data
        if json:
            api_info["json"] = json
        if files:
            api_info["files"] = files
        return api_info

