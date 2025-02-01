import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test___repr__(self):
        node = HTMLNode()
        print(repr(node))
        pass

if __name__ == "__main__":
    unittest.main()