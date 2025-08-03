import json

# 输入JSON文件路径（替换为实际路径）
input_file = "response.txt"
# 输出结果文件路径
output_file = "int_ids.txt"

try:
    # 1. 读取并解析JSON文件
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2. 提取root数组中的所有int_id
    int_ids = []
    for item in data.get("root", []):  # 确保root字段存在，避免KeyError
        int_id = item.get("int_id")  # 确保int_id字段存在，不存在则为None
        if int_id is not None:
            int_ids.append(str(int_id))  # 转换为字符串，避免写入时格式问题

    # 3. 按行写入输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(int_ids))

    print(f"成功提取 {len(int_ids)} 个int_id，已保存至 {output_file}")

except FileNotFoundError:
    print(f"错误：未找到输入文件 {input_file}")
except json.JSONDecodeError:
    print(f"错误：输入文件 {input_file} 不是有效的JSON格式")
except Exception as e:
    print(f"处理出错：{str(e)}")