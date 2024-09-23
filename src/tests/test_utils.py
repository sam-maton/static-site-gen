import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from utils import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_with_one_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        extracted = extract_markdown_images(text)
        self.assertListEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif')], extracted)

    def test_with_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_images(text)
        self.assertListEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], extracted)
    
    def test_with_no_images(self):
        text = "this is text with no images."
        extracted = extract_markdown_images(text)
        self.assertListEqual([], extracted)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_with_one_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        extracted = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], extracted)
    
    def test_with_two_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], extracted)
    
    def test_with_no_links(self):
        text = "this is text with no links."
        extracted = extract_markdown_links(text)
        self.assertListEqual([], extracted)