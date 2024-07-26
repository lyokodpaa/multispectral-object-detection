import os

# 获取包含子文件夹的文件夹路径
folder_path = r"E:\work\data\dayyolo\val"

# 遍历所有子文件夹
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        # 检查文件名是否包含“thermal”
        if "rgb" in file_name:
            # 构建新文件名
            new_file_name = file_name.replace("rgb", "thermal")
            # 构建完整路径
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)
            # 重命名文件
            os.rename(old_file_path, new_file_path)