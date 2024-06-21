import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), node2.__repr__())
    
    def test_not_eq(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "targets": "_blank"})
        node2 = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node.__repr__(), node2.__repr__())
    
    def test_value(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "targets": "_blank"})
        print(node.__repr__() + '\n')
        
    def test_prop(self):
        node = HTMLNode("b","yay",['b','c'],{"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
    
    def test_leaf(self):
        ln = LeafNode("p", "This is a paragraph of text.")
        ln2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        self.assertEqual(ln.to_html(),'<p>This is a paragraph of text.</p>')
        self.assertEqual(ln2.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_parent(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
    def test_parent_withProps(self):
                node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text", {"href": "https://www.google.com"}),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
                self.assertEqual(node.to_html(),'<p><b href="https://www.google.com">Bold text</b>Normal text<i>italic text</i>Normal text</p>')
    
if __name__ == "__main__":
    unittest.main()