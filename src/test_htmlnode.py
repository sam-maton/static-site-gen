import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')

    def test_multiple_props_to_html(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_repr(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.boot.dev"})
        self.assertEqual(repr(node), "HTMLNode: a, link, None, {'href': 'https://www.boot.dev'}")

    def test_repr_no_arguments(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "HTMLNode: None, None, None, None")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
    
    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me!</a>')


if __name__ == "__main__":
    unittest.main()