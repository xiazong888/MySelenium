import requests
import unittest

class tianqi(unittest.TestCase):
    def setUp(self) -> None:
        print("开始")
    def tearDown(self) -> None:
        print("结束")

    def test01(self):
        url=''
        para = {"": "", "": ""}
        r =  requests.get(url,params=para)
        s =r.json()
        self.assertEqual(s['reason'],'查询成功!')

if __name__ == '__main__':
    unittest.main()
