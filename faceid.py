# -*- coding: utf-8 -*-

from aip import AipFace

APP_ID = 'your APP ID'
API_KEY = 'your Api Key'
SECRET_KEY = 'your Secret Key'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

def face_register(image, group_id, user_id, image_type = 'BASE64',options = None):
    # 注册
    # image = image_to_base64(image)
    res = client.addUser(image, image_type, group_id, user_id, options)
    print(res)
    if res['error_msg'] != 'SUCCESS':
        return False
    return True

# 验证
"""
TODO：
活体验证
"""
def face_valid(image,group_id_list, imageType = 'BASE64',options=None):

    res = client.search(image, imageType, group_id_list, options)
    try:
        if [item[key] for item in res['result']['user_list'] for key in item][-1] > 80: # score>80
            return {'result': True, 'info': res['result']['user_list']}
    except Exception as e:
        print(e)
    return {'result': False, 'info': '检测失败！'}


if __name__ == '__main__':

    image_type = "BASE64"
    group_id = "group11"
    user_id = "user11"

    res = client.addUser(image, image_type, group_id, user_id, options=None)
    print (res)
