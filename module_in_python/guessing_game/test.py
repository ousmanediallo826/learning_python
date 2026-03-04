import unittest
import main

class GuessingGame(unittest.TestCase):
    def user_input(self):
        test_param = ''
        result = main.guessing_game(test_param)
        self.assertEqual(result, "Please enter a positive integer")



if __name__ == '__main__':
    unittest.main()