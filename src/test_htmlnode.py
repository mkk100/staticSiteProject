import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), node2.__repr__())
    
    def test_not_eq(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "targets": "_blank"})
        node2 = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node.__repr__(), node2.__repr__())
    
    def printTheValues(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "targets": "_blank"})
        print(node.__repr__())
        
    def propTesting(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "targets": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()