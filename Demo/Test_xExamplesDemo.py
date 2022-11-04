import unittest
from ExamplesDemo import MyExample

class TestxExampleDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\nRun once before start')

    @classmethod
    def tearDownClass(cls):
        print('Run once after end')

    def setUp(self):
        print('\nThis will run before every method')

    def tearDown(self):
        print('This will run after every method')

    def test_add(self):
        self.assertEqual(MyExample.add(self, 10, 20), 30)
        self.assertEqual(MyExample.add(self,  0,  0),  0)
        self.assertEqual(MyExample.add(self, -1,  1),  0)

    def test_sub(self):
        result = MyExample.sub(self, 10, 20)
        self.assertEqual(result, -10)

# if __name__ == '__main__':
#     unittest.main()
