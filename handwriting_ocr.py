#!/usr/local/bin/python3
import sys


def detect_handwritten_ocr(path):
    """Detects handwritten characters in a local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision_v1p3beta1 as vision
    client = vision.ImageAnnotatorClient()

#    with io.open(path, 'rb') as image_file:
#        content = image_file.read()
    content = open(path, 'rb').read()

    image = vision.types.Image(content=content)

    # Language hint codes for handwritten OCR:
    # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
    # Note: Use only one language hint code per request for handwritten OCR.
    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])

    response = client.document_text_detection(image=image,
                                              image_context=image_context)

    res = response.full_text_annotation.text
    res_txt = res.encode('ascii', 'ignore').decode('ascii')
#    print('Full Text: {}'.format(res_txt))
    print('{}'.format(res_txt))
#    for page in response.full_text_annotation.pages:
#        for block in page.blocks:
#            print('\nBlock confidence: {}\n'.format(block.confidence))

#            for paragraph in block.paragraphs:
#                print('Paragraph confidence: {}'.format(
#                    paragraph.confidence))

#                for word in paragraph.words:
#                    word_text = ''.join([
#                        symbol.text for symbol in word.symbols
#                    ])
#                    print('Word text: {} (confidence: {})'.format(
#                        word_text, word.confidence))

#                    for symbol in word.symbols:
#                        print('\tSymbol: {} (confidence: {})'.format(
#                            symbol.text, symbol.confidence))


if __name__ == "__main__":
    p = sys.argv[1]
    detect_handwritten_ocr(p)
