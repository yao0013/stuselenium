import unittest2

class Test(unittest2.TestCases):

    def setUp(self):
        number = input("number")
        self.number = int(number)

    def test_case(self):
        self.assertEqual(self.number,10,msg="you input is not 10")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest2.mian()
