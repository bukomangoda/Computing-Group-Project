def openCv():
    import cv2
    from PIL import Image

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 32:
            # SPACE 
            cv2.imwrite('./static/img/camimg.jpg', frame)
            break

    cam.release()

    cv2.destroyAllWindows()


    import easyocr
    reader = easyocr.Reader(['en'], gpu = False) # need to run only once to load model into memory
    results = reader.readtext('./static/img/camimg.jpg', detail = 0)
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