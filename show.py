from PIL import Image
import os

# 原始图片文件夹路径
img_folder_path = r"E:\work\yolov5\runs\detect\day"

# 包含rgb和ir图片的文件夹路径
rgb_ir_folder_path = r"E:\work\multispectral-object-detection\runs\detect\day"

# 生成的新图片保存路径
new_img_folder_path = r"E:\work\dete"

# 遍历原始图片文件夹中的所有图片
for filename in os.listdir(img_folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(img_folder_path, filename)
        img = Image.open(img_path)

        # 查找与当前图片名称相同的rgb和ir图片
        rgb_ir_filename = filename.split('.')[0]
        rgb_ir_path = os.path.join(rgb_ir_folder_path, rgb_ir_filename)

        rgb_path = rgb_ir_path + '_rgb.jpg'
        ir_path = rgb_ir_path + '_ir.jpg'

        if os.path.exists(rgb_path) and os.path.exists(ir_path):
            # 打开rgb和ir图片
            rgb_img = Image.open(rgb_path)
            ir_img = Image.open(ir_path)

            # 将三张图片水平拼接在一起
            new_img = Image.new('RGB', (img.width * 3, img.height))
            new_img.paste(img, (0, 0))
            new_img.paste(rgb_img, (img.width, 0))
            new_img.paste(ir_img, (img.width * 2, 0))

            # 保存新图片
            new_img_path = os.path.join(new_img_folder_path, filename)
            new_img.save(new_img_path)