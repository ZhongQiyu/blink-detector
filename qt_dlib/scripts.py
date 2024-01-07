import os
import subprocess
from PIL import Image

import pytesseract

class FileOperator:

	def __init__(self, ops):
		self.ops = ops

	def detect(self, tess_path, img):
		# 设置你的 Tesseract 路径，如果 Tesseract 不在你的 PATH 中，你需要直接指向它
		pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

		# 打开图像
		img = Image.open('word2vec_1.png')

		# 使用 Tesseract 识别图像中的文本
		text = pytesseract.image_to_string(img)

		# 输出识别后的文本
		print(text)

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

	def lint(self, files):
		for file in files:
		    subprocess.run(["pylint", file])
		    subprocess.run(["flake8", file])

	# 文件名列表

# 使用示例
fop = FileOperator(["detect", "merge_python_files", "lint"])  # *改为自动获取函数名

src = 'qt'
src_files = [os.path.join(src, f) for f in ['allansystem.py', 'main .py', 'NEW System.py']]  # 将这些替换为你的文件名
dest_file = 'merged2.py'  # 合并后的文件名
fop.merge_python_files(src_files, dest_file)

# fop.lint(files)
