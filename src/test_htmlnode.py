import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        node1 = HTMLNode(tag="s", value="t")
        node2 = HTMLNode(tag="p", value='test', children=[node, node1])
        res = ("HTMLNode(p, test, [HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'}), "
               "HTMLNode(s, t, None, None)], None)")
        self.assertEqual(repr(node2), res)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        res = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), res)


if __name__ == "__main__":
    unittest.main()
