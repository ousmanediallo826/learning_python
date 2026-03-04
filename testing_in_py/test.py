import unittest
import main


class Test(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = main.do_sum( num )

        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = "shsjjehbe"
        result = main.do_sum( test_param )
        self.assertIsInstance(result, ValueError)
    def test_do_stuff3(self):
        test_param = None
        result = main.do_sum( test_param )
        self.assertEqual(result, "Please enter a number")
    def test_do_stuff4(self):
        test_param = ''
        result = main.do_sum( test_param )
        self.assertEqual(result, "Please enter a number")



if __name__ == '__main__':
    unittest.main()