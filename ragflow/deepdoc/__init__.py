from beartype.claw import beartype_this_package

from .parser.pdf_parser import PDFParser


class DeepDoc:
    def __init__(self):
        self.parsers = {
            "pdf": PDFParser(),
            # Add other parsers (e.g., docx, txt) here
        }

    def process_document(self, file_path, file_type):
        """Process a document based on its type"""
        if file_type in self.parsers:
            return self.parsers[file_type].parse(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")


beartype_this_package()
