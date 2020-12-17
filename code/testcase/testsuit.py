import unittest
from testcase.TestCase import testcase
from Commonlib.HTMLTestRunner import HTMLTestRunner

class SuitTest(unittest.TestCase):
    def testcase(self):
        case_list = ['test_001','test_002','test_003','test_004']
        # 创建测试套件
        suit = unittest.TestSuite()

        # 循环将测试用例放到测试套件中
        for case in case_list:
            suit.addTest(testcase(case))
        with open('report.html','wb') as f:
            HTMLTestRunner(
                stream=f,  # 相当于f.write(报告)
                title='第一个测试报告',
                description='第一个测试报告a',
                verbosity=2  # 为每个测试用例生成测试报告
            ).run(suit)

if __name__ == '__main__':
    unittest.main()