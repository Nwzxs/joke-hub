import os
from datetime import datetime, timedelta

# 配置参数
base_dirs = [
    r"D:\tqsa\shijiazhuang\hikpic\1",
    r"D:\tqsa\shijiazhuang\hikpic\2",
    r"D:\tqsa\shijiazhuang\hikpic\3",
    r"D:\tqsa\shijiazhuang\hikpic\4"
]  # 需要创建日期文件夹的基础目录列表
days_to_create = 40  # 创建过去40天的文件夹

# 生成过去40天的日期列表（从昨天开始倒推）
today = datetime.today()
date_list = [today - timedelta(days=i) for i in range(1, days_to_create + 1)]

# 遍历所有基础目录并创建文件夹
for base_dir in base_dirs:
    # 确保基础目录存在
    os.makedirs(base_dir, exist_ok=True)
    print(f"\n🔧 正在处理目录: {base_dir}")

    created_count = 0
    skipped_count = 0

    # 为每个日期创建文件夹
    for date_obj in date_list:
        folder_name = date_obj.strftime("%Y-%m-%d")  # 格式化为 yyyy_mm_dd
        folder_path = os.path.join(base_dir, folder_name)

        # 创建文件夹（跳过已存在的）
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"✅ 创建成功: {folder_path}")
            
            # 创建10个测试txt文件
            for i in range(1, 11):
                test_file_path = os.path.join(folder_path, f"test_{i}.txt")
                with open(test_file_path, 'w') as f:
                    f.write(f"测试文件 {i} 创建于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            created_count += 1
        else:
            print(f"⏩ 跳过已存在: {folder_path}")
            skipped_count += 1

    # 输出当前目录的统计信息
    print(f"📊 目录完成: 新建 {created_count} 个 | 跳过 {skipped_count} 个")

# 最终统计
total_dirs = len(base_dirs) * days_to_create
print(f"\n🎉 全部完成！共处理 {len(base_dirs)} 个目录，生成 {total_dirs} 个日期文件夹")