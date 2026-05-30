import fitz


class PDFService:

    @staticmethod
    def extract_text(pdf_path: str):

        document = fitz.open(pdf_path)

        pages = []

        for page in document:

            pages.append(
                page.get_text()
            )

        return "\n".join(pages)