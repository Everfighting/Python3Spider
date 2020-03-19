# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         Baidu_ocr
# Author:       Negoowen
# Date:         2020/3/19
__Author__ = 'Negoo_wen'


#-------------------------------------------------------------------------------
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '18'
API_KEY = 'bpW'
SECRET_KEY = 'Nol'


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def main():
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 识别参数
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "false"

    # 本地图片识别
    image = get_file_content('jingo.png')
    result = client.basicGeneral(image, options)

    # 网络图片识别
    url = "http://www.xxxxxx.com/download.jpg"
    #result = client.basicGeneralUrl(url, options)
    print(result['words_result'])

if __name__ == '__main__':
    main()