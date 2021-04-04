# Typora OneIndex upload script

## 介绍

自动上传图片到 OneIndex 服务的 Typora 脚本

## 使用

### 1. 下载

- 下载[本仓库](https://github.com/JeroGC/Typora-OneIndex-upload-script)中的`PicUploader.py`

### 2. 依赖包安装

`python3 -m pip install requests lxml requests_toolbelt`

### 3. OneIndex 配置

![image-20210402232055191](https://x.lod.pub:8085/images/2021/04/02/AMS2MgUPGl/image-20210402232055191.png)

### 4. 脚本配置

修改 `PicUploader.py` 中的图床地址

```python
# ============= 请在这里修改配置 =============

url = 'https://example.com/images' #这里填你 OneIndex 图床服务的地址

# =========================================

```



### 5. Typora 配置

#### 添加执行权限(Mac/Linux)

```shell
chmod u+x PicUploader.py
```

![image-20210402233013883](https://x.lod.pub:8085/images/2021/04/02/j0AzDBqfZJ/image-20210402233013883.png)



### 6. 测试

点击`验证图片上传选项`按钮进行测试

![image-20210402233347509](https://x.lod.pub:8085/images/2021/04/02/VjDunb4ijp/image-20210402233347509.png)



### 7. 使用

![image-20210402233611983](https://x.lod.pub:8085/images/2021/04/02/87QbrLdhOP/image-20210402233611983.png)

直接粘贴图片或者拖动到 Typora 编辑区域，图片将自动完成上传并且引用。
