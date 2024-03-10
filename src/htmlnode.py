from typing import List, Dict, Any


class HTMLNode:
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: List['HTMLNode'] = None,
                 props: Dict[str, Any] = None
                 ) -> None:
        self.tag = tag  # String
        self.value = value  # String
        self.children = children  # List of HTMLNode obj
        self.props = props  # Dict

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        props_list = []
        if self.props is not None:
            for i in self.props:
                props_list.append(f' {i}="{self.props[i]}"')
            return "".join(props_list)
        return ""

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
