import unittest
import traceless_destroyer


class TestDestroyer(unittest.TestCase):
    def test_fill(self):
        self.assertEqual(traceless_destroyer.fill('$', 5), '$$$$$')
