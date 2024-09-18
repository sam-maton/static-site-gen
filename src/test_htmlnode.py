import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()