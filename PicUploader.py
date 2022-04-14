#!/usr/bin/env python3
#Author:Rexoen

import requests
import os
import re
import sys

# ============= 请在这里修改配置 =============

URL='https://example.com/images' #这里填你 OneIndex 图床服务的地址

# =========================================

if len(sys.argv) <= 1:
        print("Please append a picture file path to the command!")
        sys.exit(1)

filelist = sys.argv[1:]

for filepath in filelist:
        filename=os.path.basename(filepath)
        filestream = open(filepath,'rb')
        r = requests.post(URL,files=dict(file=(filename,filestream)))
        filestream.close()
        pic_link = re.search(f'{URL}.+?\.png',r.text)
        print(pic_link.group(0))
