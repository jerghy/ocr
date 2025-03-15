import requests
from requests.auth import HTTPBasicAuth
from tqdm import tqdm


name="高中必刷题数学人教A版必修1.pdf"
# url = "https://chogo.teracloud.jp/dav/documents/output.mp3"
url = "https://chogo.teracloud.jp/dav/shuati/"+name
auth = HTTPBasicAuth("ThomasXie", "43rKo29cev5Uzbyp")

response = requests.get(url, auth=auth, stream=True)

if response.status_code == 200:
    total_size = int(response.headers.get('content-length', 0))
    with open(name, "wb") as f:
        for data in tqdm(response.iter_content(1024), total=total_size // 1024, unit='KB'):
            f.write(data)
    print("下载成功")
else:
    print(f"下载失败，状态码：{response.status_code}")


import fitz  # PyMuPDF
import os

def pdf_to_images(pdf_path, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    
    # 遍历每一页并保存为图片
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        pix.save(f'{output_folder}/page_{page_num+1}.png')

# 使用示例
pdf_name = '高中必刷题数学人教A版必修1.pdf'
current_file_path = os.path.abspath(__file__)
pdf_path = os.path.join(os.path.dirname(current_file_path), pdf_name)
print(pdf_path)
output_folder = f'output_{pdf_name.split(".")[0]}'

pdf_to_images(pdf_path, output_folder)



from imgocr import ImgOcr
# import cv2
import json
# 初始化OCR模型
ocr = ImgOcr()

# 读取图片并进行OCR识别
image_path = "input2.png"
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
