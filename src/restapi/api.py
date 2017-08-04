import method


def API(func):
    # Decorator
    def decorated_func(*args, **kwargs):
        print "API '" + func.__name__ + "' was called"
        api_info = func(*args, **kwargs)
        return _api_call(args[0].url, api_info)
    return decorated_func


def _api_call(url, api_info):
    if not isinstance(api_info, dict):
        raise TypeError('API infomation should be dictionary type')
    url = url + api_info['path']
    headers = api_info['headers']
    api_method = api_info['method']

    print "API info {}".format(str(api_info))
    if api_method == "Get":
        return method.get(url, headers)
    elif api_method == "Post":
        data = api_info['data'] if 'data' in api_info else None
        json = api_info['json'] if 'json' in api_info else None
        return method.post(url, headers, data, json)
    elif api_method == "Put":
        data = api_info['data'] if 'data' in api_info else None
        json = api_info['json'] if 'json' in api_info else None
        return method.put(url, headers, data, json)
    elif api_method == "Delete":
        return method.delete(url, headers)
    else:
        raise ValueError("Undefined API method '{}'".format(api_method))


class BaseAPIs:

    def __init__(self, url):
        self.url = url

#     @API
#     def api_1(self, a):
#         return {'path': '/v1/banners/ja_android_tabs_unlimited/banner',
#                 'headers': {'X-Device-ID': '263b6570-0d13-0def-37ff-'},
#                 'method': 'Get',
#                 'data': a}
#
#

