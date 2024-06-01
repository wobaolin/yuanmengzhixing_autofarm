import easyocr

# 创建一个OCR reader，这里以英文和简体中文为例
reader = easyocr.Reader(['en', 'ch_sim'])

# 读取图片并进行OCR
results = reader.readtext('./restart/touxiang_xxt.png')

# 输出识别结果及其坐标
for result in results:
    location = result[0]  # 文字区域的四个角点坐标
    text = result[1]      # 识别出的文字
    confidence = result[2] # 识别的置信度

    print(f"Detected text: {text} (confidence: {confidence:.2f})")
    print(f"Location: {location}")
    print("---")
