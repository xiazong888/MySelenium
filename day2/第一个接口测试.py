import requests

url = 'http://apis.juhe.cn/ip/ipNew'
para = {"cityname":"北京","key":"221ec2c9d854d2859310ea808cb760fd"}
# 发送请求
r = requests.get(url,params=para)
print(r.json())