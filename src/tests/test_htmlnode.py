import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_only_leafs(self):
        child1 = LeafNode("p", "This is a first child")
        child2 = LeafNode("p", "This is a second child")
        child3 = LeafNode("p", "This is a third child")

        parent = ParentNode('div', [child1, child2, child3])

        self.assertEqual(parent.to_html(), '<div><p>This is a first child</p><p>This is a second child</p><p>This is a third child</p></div>')
    
    def test_to_html_nested_list(self):
        li1 = LeafNode("li", "First list item")
        li2 = LeafNode("li", "Second list item")
        li3 = LeafNode("li", "Third list item")

        ul = ParentNode('ul', [li1, li2, li3])

        div = ParentNode('div', [ul])

        self.assertEqual(div.to_html(), '<div><ul><li>First list item</li><li>Second list item</li><li>Third list item</li></ul></div>')
    
    def test_to_html_with_props(self):
        a = LeafNode('a', 'first link', {"href": "https://www.boot.dev", "target": "_blank"})
        li = ParentNode('li', [a])
        ul = ParentNode('ul', [li], {"class": "ul-class"})
        div = ParentNode('div', [ul])

        self.assertEqual(div.to_html(), '<div><ul class="ul-class"><li><a href="https://www.boot.dev" target="_blank">first link</a></li></ul></div>')



if __name__ == "__main__":
    unittest.main()