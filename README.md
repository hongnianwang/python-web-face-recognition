# python-web：人脸注册登入
python+tornado+pymysql，搭建个人网站，实现人脸注册登入

#### 文件路径设置

将自己的html文件放在/templates路径下，css文件放在/static/css路径下，image文件放在/static/image 路径下，js文件放在/static/js 路径下即可。

#### 数据库配置

本系统采用Mysql作为数据库工具，使用python语言开发，连接数据库使用第三方包pymysql，只需要配置自己的数据库后调用pymysql.connect()即可，具体参考官方文档。配置字典格式如下：

```python
PY_MYSQL_CONN_DICT = {
     'host' : 'localhost',  # 本系统数据库与web同在一个服务器下
     'user' : 'user_name',
     'password' : 'password',
     'database' : 'db_name',
     'port' : port,
     'charset' : 'utf8'}
```

#### 人脸接口配置

因为这部分是调用的百度的API，所以需要新建一个AipFace，代码如下：

```python
from aip import AipFace

APP_ID = '你的 APP ID'
API_KEY = '你的 Api Key'
SECRET_KEY = '你的 Secret Key'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
```

在上面代码中，常量APP_ID在百度云控制台中创建，常量API_KEY与SECRET_KEY是在创建完毕应用后，系统分配给用户的，均为字符串，用于标识用户，为访问做签名验证，可在AI服务控制台中的应用列表中查看

#### 服务器部署

- 服务器系统：CentOS 6 x64
- 语言环境：Python3.6
- 数据库：Mysql-server 5.1.73
- 首先需要安装Mysql 和Python3.6，然后安装第三方包：tornado, pymysql, 使用{pip}安装命令：pip install {packagename}
- 最后直接运行# python {filename.py}即可，为了持续运行可以用screen命令或者nohup命令。



#### 效果图

注册

![](C:\Users\lenovo\Desktop\github.png)

登入

![](C:\Users\lenovo\Desktop\github2.png)

数据库

![](C:\Users\lenovo\Desktop\github3.png)

