from dataclasses import dataclass, field


@dataclass(order=True)
class Metadata:
    """
    Metadata is a class used to encapsulate discovered metadata.

    :param parent: Identifies the parent file or resource from which the metadata was discovered.
    :type parent: str
    :param tag: The metadata tag (used for sorting).
    :type tag: str
    :param value: The value associated with the given tag.
    :type value: str
    """

    parent: str = field(compare=False)
    tag: str = field(compare=True)
    value: str = field(compare=False)


class Document:
    """
    Document is a class used to encapsulate file metadata.
    """

    def __init__(self, name: str):
        self.name = name
        self.metadata: list[Metadata] = []

    def add_metadata(self, new_metadata: Metadata):
        self.metadata.append(new_metadata)

    def __repr__(self) -> str:
        return f"{self.name}, {self.metadata}"
