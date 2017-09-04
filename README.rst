A beautiful Rest API list to be called
=======================

Install
=======================
pip install git+https://github.com/imaging8896/restapi.git

Usage
=======================
Support 'Get', 'Post', 'Put', 'Delete'
Support 'data' and 'json' parameters for 'Post', 'Put' (optional)
Support 'query_strings' (optional)

.. code-block:: python

  from restapi.api import BaseAPIs, API

  class Abc(BaseAPIs):

    def __init__(self):
        BaseAPIs.__init__(self, "http://XXXX")
        self.headers = {'X-Device-ID': 'YA'}

    @API
    def aa(self):
        return {
            'path': '/v1/A/C/X',
            'headers': self.headers,
            'method': 'Get',
            'query_strings': {
                'first_str': 'val space, yee',
                'second_str': 123
            }
            'json': {
                'a': 123,
                'b': ['123', '234']
            }
        }
 

  r = Abc().aa() # Return for requests Response object

  if r.status_code != 200:
     raise Exception("Fail to call API")
  r_json = r.json()
