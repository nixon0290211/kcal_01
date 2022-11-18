from PIL import Image
import pyocr
import pyocr.builders
import datetime


# import datetime

tools = pyocr.get_available_tools()

# 推奨している順で読み込むので、配列の最初に推奨順の1つ目がはいる
tool = tools[0]


def gazoushori():
    chinko = 0
    for i in range(1, 6):
        image = Image.open("image/0" + str(i) + ".png")  # OCRする画像
        txt = tool.image_to_string(
            image,
            lang="jpn",  # 学習済み言語データ
            builder=pyocr.builders.DigitBuilder(tesseract_layout=6),  # 期待される出力のタイプを指定
        )
        chinko += int(txt)  # カロリーの合計を求めている
    return chinko


# 画像を保存の処理
def hozon(txts):
    with open("txts.txt", "w") as f:
        f.write(str(txts))


def main():
    today_data = datetime.date.today()
    f = open("txts.txt", "r", encoding="UTF-8")
    txts = f.read()
    print(
        str(today_data.year)
        + "/"
        + str(today_data.month)
        + "/"
        + str(today_data.day)
        + "の摂取カロリーは"
        + str(txts)
        + "kcalです。"
    )


# with open("text.txt", "w") as f:
#     f.writelines(txt)
if __name__ == "__main__":
    takashi = gazoushori()
    hozon(takashi)
    main()
