import unittest

class Test1(unittest.TestCase):

    def setUp(self) -> None:
        print('hello')

    def tearDown(self) -> None:
        print('end')

    def test_01(self):

        print('001')

    def test_02(self):

        print('002')

    def test_03(self):

        print('003')

if __name__ == '__main__':
   # unittest.main()
   # 创建测试套件
   suite = unittest.TestSuite()
   list_test = ['test_01','test_02','test_03']
   for case in list_test:
       suite.addTest(Test1(case))

   s = unittest.TextTestRunner(verbosity=3)
   s.run(suite)



