
# encoding:utf-8

import requests
import base64
import tkinter.filedialog
'''
人脸检测与属性分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
filename = tkinter.filedialog.askopenfilename()
print(filename)
f = open(filename,"rb")

img = str(base64.b64encode(f.read()),encoding="utf-8")
params = {"image":img,"image_type":"BASE64","face_field":"age,expression,face_shape,gender,glasses,eye_status,emotion,mask"}
access_token = '24.1c5dfbbf67cfb5aaf49e1326ace25c2b.2592000.1672304459.282335-27506930'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
