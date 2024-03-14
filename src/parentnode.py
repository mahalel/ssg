from typing import Dict, List, Any
from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, children: List['HTMLNode'], tag: str = None, props: Dict[str, Any] = None) -> None:
        super().__init__(children=children, tag=tag, props=props)

    def to_html(self) -> str:
        if len(self.tag) == 0:
            raise ValueError('All parent nodes require a tag')
        if len(self.children) == 0:
            raise ValueError(' This parent is not a parent')

        result: list[str] = []
        for child in self.children:
            result.append(child.to_html())

        return f'<{self.tag}>{"".join(result)}</{self.tag}>'
