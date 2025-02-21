from metafind.client import Client
from metafind.models import Document, Metadata

from pathlib import Path
import exiftool


TAGS_TO_SKIP = {"SourceFile", "ExifTool:ExifToolVersion", "ExifTool:Warning"}


class ExifToolClient(Client):
    """
    ExifToolClient is a wrapper built around the `exiftool.ExifToolHelper` class.
    """

    def __init__(self, path: str):
        self.client = exiftool.ExifToolHelper()
        self.path = path

    def get_metadata(self):
        result = self.client.get_metadata(self.path)
        return self.parse_get_metadata_result(result)

    def parse_get_metadata_result(self, result) -> list[Document]:
        """
        parse_result parses the result of get_metadata.
        """
        documents: list[Document] = []
        # iterate through all the individual document results
        for data in result:
            name = Path(data["SourceFile"]).name
            new_doc = Document(name)
            # iterate through all the discovered tags
            for tag, value in data.items():
                if tag not in TAGS_TO_SKIP:
                    clean_tag = tag.split(":")[1]
                    new_metadata = Metadata(parent=name, tag=clean_tag, value=value)
                    new_doc.add_metadata(new_metadata)
            # add the new document to the list
            documents.append(new_doc)
        return documents

    def scrub_metadata():
        pass

    def get_unique(self):
        result = self.client.get_metadata(self.path)
        return self.parse_get_unique_result(result)

    def parse_get_unique_result(self, result) -> list[Metadata]:
        unique_tags: list[str] = []
        for data in result:
            for tag, _ in data.items():
                if tag not in TAGS_TO_SKIP and tag not in unique_tags:
                    clean_tag = tag.split(":")[1]
                    unique_tags.append(clean_tag)
        return sorted(unique_tags)
