import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):
    try:
        result = reader.readtext(image_path)

        if not result:
            return "No text detected"

        text = ""

        for item in result:
            text += item[1] + " "

        return text.strip()

    except Exception as e:
        return f"OCR Error: {e}"