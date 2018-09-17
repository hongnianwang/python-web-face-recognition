# -*- coding: utf-8 -*-

from tornado import web, ioloop, httpserver, locale
from model.models import UserModel
import base64
from faceid import face_register, face_valid
import datetime

#
class MainPageHandler(web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        # self.render('week2.html')
        self.redirect('/login')

# 首页
class HomePageHandler(web.RequestHandler):
    def get(self):
        self.render('week2.html')

# 照片墙
class PhotoPageHandler(web.RequestHandler):
    def get(self):
        self.render('week3.html')

# 注册
class RegisterHandler(web.RequestHandler):
    def get(self):
        self.render('register.html')
    def post(self):
        global list
        username = self.get_argument('username')
        groupname = self.get_argument('groupname')
        img = self.get_argument('face')
        img = str(img[22:])
        # 人脸注册
        res = face_register(img, groupname, username)
        if res:
            # 添加数据库
            mode1 = UserModel()
            user_id = mode1.add_user(username=username, groupname=groupname)
            if user_id != None:
                self.write("注册成功！")
                list = list + ',' + groupname
                print(list)
                # group_name = list(groupname)
                # group_id_list.append(group_name)
                print(res)
                self.render('login.html')
                return
            print(res)

        self.write("注册失败!")

# 登入
class LoginPageHandler(web.RequestHandler):
    def get(self):
        # self.write("Hello, world")
        self.render('login.html')
    def post(self):

        img = self.get_argument('face')
        img = str(img[22:])
        res = face_valid(img, list)

        if res['result']:
            # 获取数据
            username = [item[key] for item in res['info'] for key in item][1]
            groupname = [item[key] for item in res['info'] for key in item][0]
            # 添加数据库
            mode1 = UserModel()
            all_id = mode1.add_user_login(username=username, groupname=groupname)
            id = mode1.get_id_by_name(username)
            print(id)
            all_id = str(all_id)
            id_n = str(id['count'])
            print(id_n)
            times = str(datetime.datetime.now())
            self.write([item[key] for item in res['info'] for key in item][0]+','
                       +[item[key] for item in res['info'] for key in item][1]+','+
                       times[:19]+"\n 登入成功！")
            self.write(" 您一共访问"+id_n+"次! 您是第"+all_id+"位访客!")
            self.render('week2.html')
            # time.sleep(5)
            # self.redirect('/')
            print(res)
            return
        print(res)
        self.write("登入失败,请多试一次!")

settings = {
    # 模板的路径
    'template_path' : 'baiduai/templates',
    # 静态资源的路径
    'static_path' : 'baiduai/static',
}
application = web.Application([
            (r"/", MainPageHandler),
            (r"/register", RegisterHandler),
            (r"/login", LoginPageHandler),
            (r"/week2", HomePageHandler),
            (r"/week3", PhotoPageHandler)], **settings)

if __name__ == "__main__":
    global list
    # init
    list = 'cs'
    http_server = httpserver.HTTPServer(application)
    http_server.listen(80)
    ioloop.IOLoop.current().start()
