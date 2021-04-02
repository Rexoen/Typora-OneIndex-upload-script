#!/usr/bin/python3
import os, random, sys, requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from lxml import etree

# ============= 请在这里修改配置 =============

url = 'https://example.com/images' #这里填你 OneIndex 图床服务的地址

# =========================================

def upload(imgfile):
    boundary='-----------------------------' + str(random.randint(11819682032731101902815316090, 91819682032731124902815316090 - 1))
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/87.0',
    'Referer': url,
    'Content-Type' : 'multipart/form-data;boundary={}'.format(boundary)
    }
    
    multipart_encoder = MultipartEncoder(
    fields={
        'file': (os.path.basename(imgfile) , open(imgfile, 'rb'), 'application/octet-stream')
        #file为路径
        },
        boundary=boundary
    )
    
    headers['Content-Type'] = multipart_encoder.content_type
    #请求头必须包含一个特殊的头信息，类似于Content-Type: multipart/form-data; boundary=${bound}
    
    r = requests.post(url, data=multipart_encoder, headers=headers)
    #print(r.text)
    with open('debug.html','w') as f:
        f.write(r.text)
    selector = etree.HTML(r.text)
    external_link = selector.xpath("/html/body/div/div/div[1]/input/@value")[0]
    print(external_link)
    
if __name__ == "__main__":
    argvstr = sys.argv[1:]
    for imgfile in argvstr:
        upload(imgfile)
