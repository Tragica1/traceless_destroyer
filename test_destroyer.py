import unittest
from traceless_destroyer import Destroyer


class TestDestroyer(unittest.TestCase):
    def setUp(self):
        self.destroyer = Destroyer()

    def test_01_fill(self):
        self.assertEqual(self.destroyer.fill('D:\\test_pr3\\test.txt', 't', 3), 'ttt')

    def test_02_destroyer(self):
        self.assertEqual(self.destroyer.destroy('D:\\test_pr3\\test.txt'), 'File/directory has been destroyed!')
        self.assertEqual(self.destroyer.destroy('D:\\test_pr3\\test_dir'), 'File/directory has been destroyed!')
        self.assertEqual(self.destroyer.destroy('pr.txt'), 'File does not exist!')


if __name__ == '__main__':
    unittest.main()
