from imgocr import ImgOcr
# import cv2
import json
# 初始化OCR模型
ocr = ImgOcr()

# 读取图片并进行OCR识别
image_path = "input.png"
result = ocr.ocr(image_path)

# 打印识别结果
for line in result:
    # box, text, score = line
    box=line["box"]
    text=line["text"]
    score=line["score"]
    # print(f"识别文本: {text}, 置信度: {score:.4f}")
    # print(f"识别文本: {text}, 置信度: ")
    print(f"位置：{box}，文字：“{text}”")
# 保存result到JSON文件
with open("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)


# 可选：在图片上绘制识别框并保存
# img = cv2.imread(image_path)
# # img_with_boxes = draw_ocr_boxes(img, result)
# img_with_boxes = draw_ocr_boxes(img, result).astype(np.uint8)
# cv2.imwrite("output.png", img_with_boxes)
