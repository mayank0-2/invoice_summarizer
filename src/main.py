from pypdf import PdfReader


def main():
    reader = PdfReader("test.pdf")
    page = reader.pages[0]
    text = page.extract_text()
    index = text.find("Total")
    temp = text[index:]
    indexnew = temp.find("\n")
    print(temp[:indexnew])



if __name__ == "__main__":
    main()
