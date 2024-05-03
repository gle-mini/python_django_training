import unittest
from elements import Html, Head, Body, Title, Img, Div, H1, H2, P, Span, Meta, Table, Tr, Th, Td, Ul, Ol, Li, Elem, Text
from Page import Page

class TestPage(unittest.TestCase):
    def test_tables(self):
        """Test tables with valid and invalid configurations."""
        # Table should be valid empty or with TR children only
        self.assertTrue(Page(Table()).is_valid())
        self.assertTrue(Page(Table([Tr()])).is_valid())
        
        # Table with non-TR children should be invalid
        self.assertFalse(Page(Table([H1(Text("Hello World!"))])).is_valid())

    def test_table_rows(self):
        """Test table rows with TH and TD children."""
        # TR with TH children only should be valid
        self.assertTrue(Page(Tr([Th(Text("title")) for _ in range(5)])).is_valid())

        # TR with TD children only should be valid
        self.assertTrue(Page(Tr([Td(Text("content")) for _ in range(6)])).is_valid())

        # Mixing TH and TD should be invalid
        self.assertFalse(Page(Tr([Th(Text("title")), Td(Text("content"))])).is_valid())

    def test_lists(self):
        """Test ordered and unordered lists with valid and invalid children."""
        # Empty lists should be invalid
        self.assertFalse(Page(Ul()).is_valid())
        self.assertFalse(Page(Ol()).is_valid())

        # Lists with only Li children should be valid
        self.assertTrue(Page(Ul([Li(Text("test"))])).is_valid())
        self.assertTrue(Page(Ol([Li(Text("test"))])).is_valid())
        self.assertTrue(Page(Ul([Li(Text("test")), Li(Text("test"))])).is_valid())

        # Lists with non-Li children should be invalid
        self.assertFalse(Page(Ul([Li(Text("test")), H1(Text("test"))])).is_valid())

    def test_spans(self):
        """Test spans with valid and invalid configurations."""
        # Span with no children or with Text and P children should be valid
        self.assertTrue(Page(Span()).is_valid())
        self.assertTrue(Page(Span([Text("Hello?"), P(Text("World!"))])).is_valid())

        # Span with invalid children like H1 should be invalid
        self.assertFalse(Page(Span([H1(Text("World!"))])).is_valid())

    def test_paragraphs(self):
        """Test paragraphs with valid and invalid configurations."""
        # Paragraph with no children or Text should be valid
        self.assertTrue(Page(P()).is_valid())
        self.assertTrue(Page(P([Text("Hello?")])).is_valid())

        # Paragraph with invalid children like H1 should be invalid
        self.assertFalse(Page(P([H1(Text("World!"))])).is_valid())

    def test_headers_titles_li_th_td(self):
        """Test H1, H2, Li, Th, Td for valid and invalid text content configurations."""
        for Element in [H1, H2, Li, Th, Td]:
            with self.subTest(Element=Element):
                # Valid with single Text child
                self.assertTrue(Page(Element([Text("Hello?")])).is_valid())

                # Invalid with non-Text children or multiple Text children
                self.assertFalse(Page(Element([H1(Text("World!"))])).is_valid())
                self.assertFalse(Page(Element([Text("Hello?"), Text("Hello?")])).is_valid())

    def test_body_div(self):
        """Test Body and Div with various valid and invalid children."""
        for Element in [Body, Div]:
            with self.subTest(Element=Element):
                # Valid configurations
                self.assertTrue(Page(Element()).is_valid())
                self.assertTrue(Page(Element([Text("Hello?")])).is_valid())
                self.assertTrue(Page(Element([H1(Text("World!"))])).is_valid())
                self.assertTrue(Page(Element([Span()])).is_valid())

                # Invalid configuration with non-body/div elements like Html
                self.assertFalse(Page(Element([Html()])).is_valid())

    def test_titles(self):
        """Test Title for correct text content handling."""
        # Invalid with no children
        self.assertFalse(Page(Title()).is_valid())

        # Valid with single Text child
        self.assertTrue(Page(Title([Text("Hello?")])).is_valid())

        # Invalid with multiple Text children
        self.assertFalse(Page(Title([Text("Hello?"), Text("Hello?")])).is_valid())

    def test_html_structure(self):
        """Test HTML structure with correct head and body."""
        # Valid HTML structure
        self.assertTrue(Page(Html([Head([Title(Text("Hello?"))]), Body([H1(Text("Hello?"))])])).is_valid())

        # Invalid HTML with non-head/body elements
        self.assertFalse(Page(Html([Div()])).is_valid())

if __name__ == '__main__':
    unittest.main()
