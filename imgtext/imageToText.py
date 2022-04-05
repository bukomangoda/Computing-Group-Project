from imgtext.models import Image as ig
def text1():
    imgdbpath = ig.objects.order_by('id')
    impath = str(imgdbpath.latest('image'))
    # = str(ig.objects.last('image'))
    #print(imgdbpath)
    #imgdbpath = imgdb.image[-1]

    import easyocr
    reader = easyocr.Reader(['en'], gpu = False) # need to run only once to load model into memory
    results = reader.readtext('./media/'+ impath, detail = 0)
    text = ''
    for result in results:
        text += result + ''

    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, text)
    pdf.output('./static/files/01.pdf', 'F')

    print(text)
    return text

