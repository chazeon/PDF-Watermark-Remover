from PyPDF2 import PdfFileReader, PdfFileWriter

def removeWatermark(input_fname: str, output_fname: str):

    with open(input_fname, "rb") as inputFile, open(output_fname, "wb") as outputFile:

        reader = PdfFileReader(inputFile)
        writer = PdfFileWriter()

        for n in range(reader.numPages):

            page = reader.getPage(n)
            del page["/Contents"][-1]

            writer.addPage(page)

        writer.write(outputFile)

if __name__ == "__main__":

    import sys

    if len(sys.argv) != 3:
        raise RuntimeError("Arguments not correct!")

    removeWatermark(sys.argv[1], sys.argv[2])

