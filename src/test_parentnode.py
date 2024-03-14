import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_leaf_children(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        res = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), res)

    def test_nesting(self):
        node: ParentNode = ParentNode(
            tag="head",
            children=[
                ParentNode(
                    tag="body",
                    children=[
                        ParentNode(
                            tag="p",
                            children=[
                                LeafNode(tag="b", value="Bold text1"),
                                LeafNode(tag=None, value="Normal text1"),
                                LeafNode(tag="i", value="italic text1"),
                                LeafNode(tag=None, value="Normal text1"),
                            ],
                        ),
                        ParentNode(
                            tag="p",
                            children=[
                                LeafNode(tag="b", value="Bold text2"),
                                LeafNode(tag=None, value="Normal text2"),
                                LeafNode(tag="i", value="italic text2"),
                                LeafNode(tag=None, value="Normal text2"),
                            ],
                        )
                    ],
                )
            ],
        )
        res = ('<head><body><p><b>Bold text1</b>Normal text1<i>italic text1</i>Normal text1</p><p><b>Bold '
               'text2</b>Normal text2<i>italic text2</i>Normal text2</p></body></head>')
        self.assertEqual(node.to_html(), res)


if __name__ == "__main__":
    unittest.main()
