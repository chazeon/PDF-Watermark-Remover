from PyPDF2 import PdfReader, PdfWriter

def removeWatermark(input_fname: str, output_fname: str):

    with open(input_fname, "rb") as input_file, open(output_fname, "wb") as output_file:

        reader = PdfReader(input_file)
        writer = PdfWriter()

        for n in range(len(reader.pages)):

            page = reader.pages[n]
            del page["/Contents"][-1]

            writer.add_page(page)

        writer.write(output_file)

if __name__ == "__main__":

    import sys

    if len(sys.argv) != 3:
        raise RuntimeError("Arguments not correct!")

    removeWatermark(sys.argv[1], sys.argv[2])

