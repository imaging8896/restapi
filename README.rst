A beautiful Rest API list to be called
=======================

Install
=======================
pip install git+https://github.com/imaging8896/restapi.git

Usage
=======================
Support 'Get', 'Post', 'Put', 'Delete', and support 'data' and 'json' parameters for 'Post', 'Put'

.. code-block:: python

  from restapi.api import BaseAPIs, API

  class Abc(BaseAPIs):

    def __init__(self):
        BaseAPIs.__init__(self, "http://XXXX")
        self.headers = {'X-Device-ID': 'YA'}

    @API
    def aa(self):
        return {'path': '/v1/A/C/X',
                'headers': self.headers,
                'method': 'Get'}
 

  r = Abc().aa() # Return for requests Response object

  if r.status_code != 200:
     raise Exception("Fail to call API")
  r_json = r.json()
