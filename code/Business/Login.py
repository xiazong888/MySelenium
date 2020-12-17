# 导入selenium封装类
from Commonlib.Commonlib import Commonshare

class Login(Commonshare):
    def login(self,user,pwd):
        self.open_url('http://www.yhd.com/')
        self.click('class', 'hd_login_link')
        self.input_data('id', 'un', user)
        self.input_data('id', 'pwd', pwd)
        self.click('id', 'login_button')

if __name__ == '__main__':
    log = Login()
    log.login('diguo168', 'abcd1234')