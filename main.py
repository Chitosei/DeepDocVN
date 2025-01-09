# This is a sample Python script.
import os
import shutil
from PIL import Image
import pytesseract
import cv2
import numpy as np
from utilities import *
import camelot
from pdf2image import convert_from_path
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import openai

app = FastAPI()

pdf_path = 'pdf_uploaded/test.pdf'


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise JSONResponse(content="File is not '.pdf'. Please upload a valid file.", status_code=400)

    # Save uploaded file
    temp_file_path = f"pdf_uploaded/temp_{file.filename}"
    with open(temp_file_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)

    try:
        # Process PDF result
        result = extract_text(temp_file_path)

        # Clarify some potential error:
        for page in result["pages"]:
            original_text = page['text']
            corrected_text = correct_text([original_text])  # We expect a list for batch processing
            page['corrected_text'] = corrected_text[0]

        json_result = jsonable_encoder(result)
        print(json_result)
        return JSONResponse(content=json_result)

    except Exception as e:
        return JSONResponse(content={"error": f"An error occurred while processing the PDF: {str(e)}"}, status_code=500)

    finally:
        os.remove(temp_file_path)


#Debug
# texts = [
#     "côn viec kin doanh thì rất kho khan nên toi quyết dinh chuyển sang nghề khac  ",
#     "toi dang là sinh diên nam hai ở truong đạ hoc khoa jọc tự nhiên , trogn năm ke tiep toi sẽ chọn chuyen nganh về trí tue nhana tạo",
#     "Tôi  đang học AI ở trun tam AI viet nam  ",
#     "Nhưng sức huỷ divt của cơn bão mitch vẫn chưa thấm vào đâu lsovớithảm hoạ tại Bangladesh ăm 1970 ",
#     "Lần này anh Phươngqyết xếp hàng mua bằng được 1 chiếc",
#     "một số chuyen gia tài chính ngâSn hànG của Việt Nam cũng chung quan điểmnày",
#     "Cac so liệu cho thay ngươi dân viet nam đang sống trong 1 cuôc sóng không duojc nhu mong đọi",
#     "Nefn kinh té thé giới đang đúng trươc nguyen co của mọt cuoc suy thoai",
#     "Khong phai tất ca nhưng gi chung ta thấy dideu là sụ that",
#     "chinh phủ luôn cố găng het suc để naggna cao chat luong nền giáo duc =cua nuoc nhà",
#     "nèn kinh te thé giới đang đứng trươc nguy co của mọt cuoc suy thoai",
#     "kinh tế viet nam dang dứng truoc 1 thoi ky đổi mơi chưa tung có tienf lệ trong lịch sử"
# ]
#
# corrected_text = correct_text(texts)
# print(f"Original: {texts}")
# print(f"Corrected: {corrected_text}")
# # Gray image
# img = cv2.imread('input/test_text_vn.png', 0)
# # # Gaussian Blur
# # blurred = cv2.GaussianBlur(img, (5, 5), 0)
#
# # Apply adaptive threshold
#
# sharpened = unsharp_mask(img, sigma=3.0, strength=9.0)
#
# # thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#
# cv2.imwrite('preprocessed_image.jpg', sharpened)
#
# extracted_text = pytesseract.image_to_string(sharpened, lang='vie')
#
# print(extracted_text)
