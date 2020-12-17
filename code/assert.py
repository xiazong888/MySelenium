import unittest

class two_test(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('start')
    #
    # def tearDown(self) -> None:
    #     print("end")

    def test01(self):
        self.assertEqual('1','1')
    def test02(self):
        self.assertEqual('1','0')

if __name__ == '__main__':
    unittest.main()