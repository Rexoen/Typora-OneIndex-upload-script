#!/usr/bin/env bash
#Author:Rexoen

# ============= 请在这里修改配置 =============
URL='https://example.com/images' #这里填你 OneIndex 图床服务的地址
# ============================================

curl --silent  $URL -F "file=@$1" -D - | grep -oP 'location: \K.+\.(png|jpg|bmp|tiff)'
