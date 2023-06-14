import fillpdf
from fillpdf import fillpdfs

if __name__ == "__main__":
    filename = "volform.pdf"
    filenamenew = "written.pdf"
    fillpdfs.print_form_fields(filename)

