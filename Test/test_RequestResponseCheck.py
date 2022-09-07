import unittest

import requests
from PythonProjectNASA.src import configfile
import json
import pytest
import unittest
#import sys
# This code is for the tests
class myTest(unittest.TestCase):
    def test_get_data(self):
        api=r"https://api.publicapis.org/entries"
        response = requests.get(f"{api}")
        assert response.status_code, 200


# class myDefinedError(Exception):
#     def __init__(self):
#         #text=" This is self defined error "
#         super().__init__(" This is self defined error ")
#
#
#
# class MakeApiCall:
#
#     def test_get_data(self, api):
#         response = requests.get(f"{api}")
#         assert response.status_code == 200
#         print(type(response.json()))
#         print("sucessfully fetched the data")
#         info = response.json()
#         self.formatted_print(info)
#
#
#
#
#
#
#
#         with open("4forces.json","w") as f:
#             json.dump(info, f)
#             #print(info)
#
#         with open("4forces.json","r") as f:
#             data=f.read()
#
#         info=json.loads(data)
#         #print(info)
#
#
#     def test_get_user_data(self, api, parameters):
#         response = requests.get(f"{api}", params=parameters)
#         assert response.status_code == 200
#         print("sucessfully fetched the data with parameters provided")
#         # self.formatted_print(response.json())
#         print(response.json())
#         # print(tfile)
#
#     def formatted_print(self, info):
#         yahoo_APIs = {}
#         ctr = 0
#         for det in info['entries']:
#             API = det['API']
#             Description = det['Description']
#             Auth = det['Auth']
#             Category = det['Category']
#             yahoo_APIs['API' + str(ctr)] = API
#             yahoo_APIs['Description' + str(ctr)] = Description
#             yahoo_APIs['Auth' + str(ctr)] = Auth
#             yahoo_APIs['Category' + str(ctr)] = Category
#             ctr = ctr + 1
#
#
#         # for animal in yahoo_APIs
#         for k, v in yahoo_APIs.items():
#             print(k, '->', v)

        # #for animal in yahoo_APIs
        # for k,v in yahoo_APIs.items():
        #     print(k, '->', v)
        # cat=[cat for cat in yahoo_APIs['category']]
        # if yahoo_APIs[k]==Category:
        # print(yahoo_APIs[k],'->',yahoo_APIs[v])
        # with open('./Users/hp/tk.json','w') as file:
        # with open("4forces.json","w") as f:
        # json.dump(obj, f)
        #pass
        # json.dump(obj, open("out.json","w"))
        # text = json.dumps(obj, sort_keys=True, indent=4)
        # print(type(text))
        # print(text)
        # DictOutput=eval(text)
        # print(DictOutput)
        # for key, value in DictOutput.items():
        #    print(key, '->', value)
        # for content in text():
        #    print(content)

    # def __init__(self, api):
    #     self.test_get_data(api)
    #     parameters = {
    #         "username": "kedark"
    #     }
    #     self.test_get_user_data(api, parameters)






# if __name__ == "__main__":
#     try:
#         #api_call = MakeApiCall("https://api.nasa.gov/planetary/apod?api_key=Od1LG4sqbZxyWTN5mNYlD7raAbFZbnWSGX5XUevQ")
#         #Calling the configfile.ini file for the input parameters
#         param = configfile.readconfigini()
#         api_call = MakeApiCall(param)

#
#
#
#         #r = http.request('GET', 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
#         #print(r.status)
#         #if r.status==403:
#             #raise myDefinedError
#     except ValueError:
#         print ("Please make sure the API has proper Values")
#     except Exception  as e:
#         print(e.args)
#     except myDefinedError:
#         print("This is after MyDefonedError Function has been called")
#     except HTTPError as e:
#         if e.code==403:
#             print("You are accessing the unauthorsied files")
#     except Exception as e:
#         print("oops",e.__class__,"occured")
#     finally:
#         print ("Mission Succesful")