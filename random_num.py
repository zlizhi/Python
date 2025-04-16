import random
import string


def generate_data(data_type, data_range, length=None):
    """
    根据数据类型生成随机数据
    """
    if data_type == "int":
        return random.randint(data_range[0], data_range[1])
    elif data_type == "float":
        return random.uniform(data_range[0], data_range[1])
    elif data_type == "str":
        return ''.join(random.choice(data_range) for _ in range(length))
    else:
        raise ValueError(f"Unsupported data type: {data_type}")


def parse_struct(struct):
    """
    递归解析结构并生成数据
    """
    if isinstance(struct, dict):
        result = {}
        for key, value in struct.items():
            if key in ["int", "float", "str"]:  # 基础数据类型
                result[key] = generate_data(key, value["datarange"], value.get("len"))
            elif key in ["tuple", "list", "dict"]:  # 容器类型
                result[key] = parse_struct(value)
            else:
                result[key] = parse_struct(value)
        return result
    elif isinstance(struct, list):
        result = []
        for item in struct:
            result.append(parse_struct(item))
        return result
    elif isinstance(struct, tuple):
        result = []
        for item in struct:
            result.append(parse_struct(item))
        return tuple(result)
    else:
        return struct


def structDataSampling(**kwargs):
    """
    根据结构生成数据
    :param kwargs: 包含结构定义的字典
    :return: 生成的数据列表
    """
    num = kwargs.get("num", 1)
    struct = kwargs.get("struct", {})
    result = []

    for _ in range(num):
        data = parse_struct(struct)
        result.append(data)

    return result


def apply():
    struct = {
        "num": 100,
        "struct": {
            "tuple": {
                "str": {"datarange": string.ascii_uppercase, "len": 50}
            },
            "list": {
                "int": {"datarange": (0, 10)},
                "float": {"datarange": (0, 1.0)}
            },
            "dict": {
                "str": {"datarange": string.ascii_lowercase, "len": 10}
            },
            "int": {"datarange": (0, 10)},
        }
    }

    result = structDataSampling(**struct)
    for item in result:
        print(item)


apply()
# import random
# import string
#
# def generate_data(data_type, data_range, length=None):
#     """
#     根据数据类型生成随机数据
#     """
#     if data_type == "int":
#         return random.randint(data_range[0], data_range[1])
#     elif data_type == "float":
#         return random.uniform(data_range[0], data_range[1])
#     elif data_type == "str":
#         return ''.join(random.choice(data_range) for _ in range(length))
#     else:
#         raise ValueError(f"Unsupported data type: {data_type}")
#
# def parse_struct(struct):
#     """
#     递归解析结构并生成数据
#     """
#     if isinstance(struct, dict):
#         result = {}
#         for key, value in struct.items():
#             if key in ["int", "float", "str"]:  # 基础数据类型
#                 result = generate_data(key, value["datarange"], value.get("len"))
#             elif key in ["tuple", "list", "dict"]:  # 容器类型
#                 result[key] = parse_struct(value)
#             else:
#                 result[key] = parse_struct(value)
#         return result
#     elif isinstance(struct, list):
#         result = []
#         for item in struct:
#             if isinstance(item, dict):
#                 result.append(parse_struct(item))
#             else:
#                 result.append(item)
#         return result
#     elif isinstance(struct, tuple):
#         result = []
#         for item in struct:
#             if isinstance(item, dict):
#                 result.append(parse_struct(item))
#             else:
#                 result.append(item)
#         return tuple(result)
#     else:
#         return struct
#
#
# def structDataSampling(**kwargs):
#     """
#     根据结构生成数据
#     :param kwargs: 包含结构定义的字典
#     :return: 生成的数据列表
#     """
#     num = kwargs.get("num", 1)
#     struct = kwargs.get("struct", {})
#     result = []
#
#     for _ in range(num):
#         data = parse_struct(struct)
#         result.append(data)
#
#     return result
#
#
# def apply():
#     struct = {
#         "num": 100,
#         "struct": {
#             "tuple": {
#                 "str": {"datarange": string.ascii_uppercase, "len": 50}
#             },
#             "list": {
#                 "int": {"datarange": (0, 10)},
#                 "float": {"datarange": (0, 1.0) }
#             },
#             "dict": {"str": {"datarange": string.ascii_lowercase, "len": 10}},
#             # "int":{"datarange": (0, 10)}
#
#         }
#     }
#     result = structDataSampling(**struct)
#     for item in result:
#             print(item)
# apply()

# import random
# import string
#
#
# def generate_data(data_type, data_range, length=None):
#     """
#     根据数据类型生成随机数据
#     """
#     if data_type == "int":
#         return random.randint(data_range[0], data_range[1])
#     elif data_type == "float":
#         return random.uniform(data_range[0], data_range[1])
#     elif data_type == "str":
#         return ''.join(random.choice(data_range) for _ in range(length))
#     else:
#         raise ValueError(f"Unsupported data type: {data_type}")
#
#
# def parse_struct(struct):
#     """
#     递归解析结构并生成数据
#     """
#     if isinstance(struct, dict):
#         result = {}
#         for key, value in struct.items():
#             if key in ["int", "float", "str"]:  # 基础数据类型
#                 result = generate_data(key, value["datarange"], value.get("len"))
#             elif key in ["tuple", "list", "dict"]:  # 容器类型
#                 result[key] = parse_struct(value)
#             else:
#                 result[key] = parse_struct(value)
#         return result
#     elif isinstance(struct, list):
#         result = []
#         for item in struct:
#             result.append(parse_struct(item))
#         return result
#     elif isinstance(struct, tuple):
#         result = []
#         for item in struct:
#             result.append(parse_struct(item))
#         return tuple(result)
#     else:
#         return struct
#
#
# def structDataSampling(**kwargs):
#     """
#     根据结构生成数据
#     :param kwargs: 包含结构定义的字典
#     :return: 生成的数据列表
#     """
#     num = kwargs.get("num", 1)
#     struct = kwargs.get("struct", {})
#     result = []
#
#     for _ in range(num):
#         data = parse_struct(struct)
#         result.append(data)
#
#     return result
#
#
# def apply():
#     struct = {
#         "num": 100,
#         "struct": {
#             "tuple": {
#                 "str": {"datarange": string.ascii_uppercase, "len": 50}
#             },
#             "list": {
#                 "int": {"datarange": (0, 10)},
#                 "float": {"datarange": (0, 1.0) }
#             },
#             "dict": {}
#         }
#     }
#
#     result = structDataSampling(**struct)
#     for item in result:
#         print(item)
# apply()
# import random
# import string
#
# def generate(kwargs):
#     result = list()
#     num = kwargs.get('num', 1)
#     for _ in range(num):
#         res = list()
#         for k, v in kwargs.items():
#             if k == 'num':
#                 continue
#             elif k == 'int':
#                 it = iter(v['datarange'])
#                 res.append(random.randint(next(it), next(it)))
#             elif k == 'float':
#                 it = iter(v['datarange'])
#                 res.append(random.uniform(next(it), next(it)))
#             elif k == 'str':
#                 datarange, length = v['datarange'], v['len']
#                 tmp = ''.join(random.SystemRandom().choice(datarange) for _ in range(length))
#                 res.append(tmp)
#             elif k == 'dict':
#                 elem = dict()
#                 elem[random.randint(0, 10)] = random.randint(0, 10)
#                 res.append(elem)
#             elif k == 'list':
#                 res.append(generate(v))
#             elif k == 'tuple':
#                 res.append(tuple(generate(v)))
#             else:
#                 continue
#         result.append(res)
#     return result
#
# def main():
#     struct = {
#         'num': 2,
#         'tuple': {
#             'str': {"datarange": string.ascii_uppercase, "len": 50},
#             'list': {
#                 'int': {"datarange": (0, 10)},
#                 'float': {"datarange": (0, 1.0)}
#             },
#             'dict': {}
#         },
#         "int": {"datarange": (0, 10)}
#     }
#     print(generate(struct))
#
# if __name__ == "__main__":
#     main()
