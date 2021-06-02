from reverse import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(reverse_sentence("Hello I am Kelton"), "Kelton am I Hello")

    def test_single(self):
        self.assertEqual(reverse_sentence("Hello"), "Hello")

    def test_fail(self):
        self.assertEqual(reverse_sentence("I am a dog"), "god a ma I")


if __name__ == "__main__":
    unittest.main()

