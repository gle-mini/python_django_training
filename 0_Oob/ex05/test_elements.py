import unittest
from elements import Elem, Text, Html, Head, Body, Title, Img

class TestHtmlElements(unittest.TestCase):
    def test_html_element(self):
        """Test the basic structure of an HTML element."""
        html = Html([Head(Title("My Website")), Body("Hello, world!")])
        self.assertIn('<html>', str(html))
        self.assertIn('</html>', str(html))

    def test_head_and_title(self):
        """Test the HEAD element with a TITLE."""
        head = Head([Title("My Website")])
        self.assertIn('<head>', str(head))
        self.assertIn('<title>', str(head))
        self.assertIn('My Website', str(head))
        self.assertIn('</title>', str(head))
        self.assertIn('</head>', str(head))

    def test_body_element(self):
        """Test the BODY element with content."""
        body = Body(Text("Hello, world!"))
        self.assertIn('<body>', str(body))
        self.assertIn('Hello, world!', str(body))
        self.assertIn('</body>', str(body))

    def test_img_element(self):
        """Test the IMG element with attributes."""
        img = Img(attr={'src': 'image.png', 'alt': 'An image'})
        self.assertIn('<img alt="An image" src="image.png" />', str(img))

    def test_empty_attributes(self):
        """Test elements with no attributes should not include empty attribute strings."""
        div = Elem(tag='div')
        self.assertEqual('<div></div>', str(div))

if __name__ == '__main__':
    unittest.main()

