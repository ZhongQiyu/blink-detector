from PIL import Image
import pytesseract

# 设置你的 Tesseract 路径，如果 Tesseract 不在你的 PATH 中，你需要直接指向它
pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

# 打开图像
img = Image.open('word2vec_1.png')

# 使用 Tesseract 识别图像中的文本
text = pytesseract.image_to_string(img)

# 输出识别后的文本
print(text)
