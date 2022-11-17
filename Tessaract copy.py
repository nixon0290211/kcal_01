import pyocr
from PIL import Image
import datetime
import os

tools = pyocr.get_available_tools()
tool = tools[0]


def ocr():
    data_dir_path = "./images"
    file_list = os.listdir(r"./images")
    value = 0

    for file_name in file_list:
        root, ext = os.path.splitext(file_name)
        if ext == ".png" or ".jpg" or ".jpeg":
            abs_name = data_dir_path + "/" + file_name
            img = Image.open(abs_name)
            txt = tool.image_to_string(
                img, lang="jpn", builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
            )
            value += int(txt)
    return value


def save(text):
    with open("ex1.txt", "w") as f:
        f.write(str(text))


def display():
    value = ocr()
    save(value)
    f = open("ex1.txt", "r", encoding="UTF-8")
    out = f.read()

    now = datetime.datetime.now()
    print(
        str(now.year)
        + "/"
        + str(now.month)
        + "/"
        + str(now.day)
        + "の摂取カロリーは"
        + str(out)
        + "kcalです。"
    )


display()
