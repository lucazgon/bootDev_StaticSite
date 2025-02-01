import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        a = LeafNode("p", "This is a paragraph of text.")
        b = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        print(a.to_html())
        print(b.to_html())

        #self.assertEqual(a,'<p>This is a paragraph of text.</p>')
        #self.assertEqual(b,'<a href="https://www.google.com">Click me!</a>')
        '''
        <p>This is a paragraph of text.</p>
        <a href="https://www.google.com">Click me!</a>
        '''
        pass

if __name__ == "__main__":
    unittest.main()