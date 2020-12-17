# 登录成功
success_data = {
    'user': 'admin',
    'pwd': 'test123'
}

# 登录失败

fail_data = [{'user': 'ad', 'pwd': 'test', 'check': '帐号不存在或者已被禁用，请重试'},
             {'user': '', 'pwd': 'test123', 'check': '帐号不能为空，请输入帐号'},
             {'user': 'admin', 'pwd': '', 'check': '密码不能为空，请输入密码'}]
