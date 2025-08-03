import json


def load_and_fix_json(file_path):
    """加载并修复JSON文件，处理null值"""
    try:
        # 读取原始数据
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = f.read()

        # 修复非标准格式
        fixed_data = raw_data.replace('Null', 'null').replace('NULL', 'null')
        fixed_data = fixed_data.replace(',]', ']').replace(',}', '}')  # 处理多余逗号

        # 解析JSON
        json_data = json.loads(fixed_data)

        # 处理null值（转换为""）
        def process_nulls(obj):
            if isinstance(obj, dict):
                return {k: process_nulls(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [process_nulls(v) for v in obj]
            return obj if obj is not None else ""

        return process_nulls(json_data)

    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON格式错误：{e}，位置：{e.pos}")
        return None
    except Exception as e:
        print(f"处理错误：{e}")
        return None


# 使用示例
if __name__ == "__main__":
    data = load_and_fix_json("data.json")
    if data:
        print("处理后的数据：")
        print(data)
        # 后续可调用之前的json_to_payload函数生成payload
        # payload = json_to_payload(data)