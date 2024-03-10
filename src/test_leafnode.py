import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode(value="Click me!", tag="a", props={"href": "https://www.google.com"})
        res = "LeafNode(Click me!, a, {'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), res)

    def test_props_to_html(self):
        node = LeafNode(value="Click me!", tag="a", props={"href": "https://www.google.com"})
        res = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), res)


if __name__ == "__main__":
    unittest.main()
