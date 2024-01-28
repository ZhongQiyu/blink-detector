import os
import subprocess
from PIL import Image
import pytesseract

class FileOperator:
    def __init__(self, tess_path):
        # 获取所有非魔术方法名称
        self.ops = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
        self.tess_path = tess_path
        pytesseract.pytesseract.tesseract_cmd = self.tess_path

    def detect_text(self, img_path):
        # 打开图像
        img = Image.open(img_path)

        # 使用 Tesseract 识别图像中的文本
        text = pytesseract.image_to_string(img)

        # 输出识别后的文本
        print(text)
        return text

    def merge_python_files(self, src_files, dest_file):
        with open(dest_file, 'w') as outfile:
            for file_path in src_files:
                if os.path.exists(file_path):
                    with open(file_path) as infile:
                        # 读取每个文件的内容并写入输出文件
                        outfile.write(infile.read())
                        # 在每个文件内容后添加换行，确保文件之间有分隔
                        outfile.write('\n')
                else:
                    print(f"File not found: {file_path}")

    def lint_files(self, files):
        for file in files:
            subprocess.run(["pylint", file])
            subprocess.run(["flake8", file])

# 使用示例
tess_path = r'<full_path_to_your_tesseract_executable>'  # 替换为你的 Tesseract 路径
img_path = 'word2vec_1.png'  # 替换为你的图像文件路径
fop = FileOperator(tess_path)
fop.detect_text(img_path)

src = 'qt'
src_files = [os.path.join(src, f) for f in ['allansystem.py', 'main.py', 'NEW System.py']]  # 将这些替换为你的文件名
dest_file = 'merged2.py'  # 合并后的文件名
fop.merge_python_files(src_files, dest_file)

# files = src_files  # 如果你想对这些文件运行 Lint
# fop.lint_files(files)
