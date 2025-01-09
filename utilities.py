import json
import os
import shutil
import cv2
import camelot
import numpy as np
import pytesseract
from pdf2image import convert_from_path
import openai
from transformers import pipeline


def unsharp_mask(image, sigma=1.0, strength=1.5):
    blurred = cv2.GaussianBlur(image, (3, 3), sigma)
    sharpened = cv2.addWeighted(image, 1.0 + strength, blurred, -strength, 0)
    return sharpened


# def table_detection(pdf_file):
#     tables = camelot.read_pdf(pdf_file, pages='all', flavor='stream')
#     if len(tables) > 0:
#         for index, table in enumerate(tables):
#             table.to_csv(f'output/table{index + 1}.csv')
#             # Debug
#             print(f"Table {index + 1} saved as table_{index + 1}.csv")
#     else:
#         print("No tables found in the document.")
#     return tables


def preprocess_image(image):
    image_gray = image.convert('L')
    image_gray_array = np.array(image_gray)
    # Use adaptive thresholding to binarize the image
    thresh = cv2.adaptiveThreshold(image_gray_array, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)
    return image_gray_array


def convert_pdf_to_image(pdf_path, arg="No"):
    """
        Convert dpf to image and save it with format : page_{page number}:05
    """

    # os.makedirs(image_folder, exist_ok=True)
    # for i, page in enumerate(pages):
    #     page.save(f'input/page_{i + 1:05}.jpg', 'JPEG')  # Type PIL.PpmImagePlugin.PpmImageFile
    #
    # return len(pages) if arg == "Page Numbers" else pages

def resize_image(image, max_width=1024, max_height=768):
    # Maintain aspect ratio
    resized = cv2.resize(image,(1024,768))
    return resized

def extract_text(pdf_path):
    """

    :param pdf_path: Path of input pdf
    :return: Json file
    This function already contain convert pdf to image
    Put image input ok the folder ./input. Return json file have text extracted from image
    """
    pages = convert_from_path(pdf_path, 200)
    image_folder = "input"
    output_path = "output"
    os.makedirs(image_folder, exist_ok=True)
    os.makedirs(output_path, exist_ok=True)
    os.chmod(output_path, 0o777)
    document_name = os.path.basename(pdf_path)

    result = {
        "document file": document_name,
        "pages": [],

    }

    for page_num, page in enumerate(pages, start=1):
        image_path = os.path.join(image_folder, f"page_{page_num:05}.jpg")
        page.save(image_path, "JPEG")
        page = resize_image(page)
        sharpened = preprocess_image(page)
        extracted_text = pytesseract.image_to_string(sharpened, lang='vie')

        # Append output
        result['pages'].append({
            'page_number': page_num,
            'text': extracted_text.strip(),
        })

    # shutil.rmtree(image_folder) # Delete image

    # with open("output", 'w', encoding="utf-8") as json_file:
    #     json.dump(result, json_file, indent=4, ensure_ascii=False)

    print(f"Text extraction complete! Results saved in: ./output ")

    return result


def correct_text(input_text):
    corrector = pipeline("text2text-generation", model="bmd1905/vietnamese-correction-v2")

    predictions = corrector(input_text, max_length=1024)
    return [pred['generated_text'] for pred in predictions]