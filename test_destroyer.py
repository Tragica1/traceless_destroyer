import unittest
from traceless_destroyer import Destroyer


class TestDestroyer(unittest.TestCase):
    def setUp(self) -> None:
        self.destroyer = Destroyer()

    def test_fill(self):
        self.assertEqual(self.destroyer.fill('test.txt', '$', 5), '$$$$$')

    def test_destroyer(self):
        self.assertEqual(self.destroyer.destroy('test.txt'), 'File has been destroyed!')
