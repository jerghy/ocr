from paddleocr import PaddleOCR
import json

# 初始化OCR实例
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="ch",
    use_gpu=False  # GitHub Actions环境只能用CPU
)

# 执行OCR识别
result = ocr.ocr('input.png', cls=True)

# 格式化输出结果
output = []
for line in result:
    if line:
        output.append({
            "coordinates": line[0],
            "text": line[1][0],
            "confidence": float(line[1][1])
        })

# 保存结果到JSON文件
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("OCR完成，结果已保存至output.json")
