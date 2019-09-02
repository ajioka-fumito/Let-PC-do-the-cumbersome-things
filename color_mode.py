from PIL import Image
import numpy as np
"""
１CHの画像に対してパレットを差し込むことでカラーモード画像を作成することが可能
"""
# image の読み込み　この時点でカラーマップ画像
image = Image.open("./test.png")
# palette の取得
palette = image.getpalette()
# image の array化
image = np.array(image)
# array から image へ
# このときmode="P"を指定しておくことによりカラーマップとして取り扱うことができる
image = Image.fromarray(np.uint8(image),mode="P")
# パレットの挿入
image.putpalette(palette)

image.show()



