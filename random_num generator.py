import random
import string


def generate(kwargs):
    num = kwargs.get('num', 1)  
    struct = kwargs.get('struct', {}) 

    for _ in range(num):
        root = list()
        for k, v in struct.items():  
            if k == 'tuple':
                tuple_data = []
                for key, value in v.items():
                    if key == 'str':
                        datarange, length = value['datarange'], value['len']
                        tmp = ''.join(random.SystemRandom().choice(datarange) for _ in range(length))
                        tuple_data.append(tmp)
                root.append(tuple(tuple_data))
            elif k == 'list':
                list_data = []
                for key, value in v.items():
                    if key == 'int':
                        it = iter(value['datarange'])
                        list_data.append(random.randint(next(it), next(it)))
                    elif key == 'float':
                        it = iter(value['datarange'])
                        list_data.append(random.uniform(next(it), next(it)))
                root.append(list_data)
            elif k == 'dict':
                dict_data = {}
                for key, value in v.items():
                    if key == 'str':
                        datarange, length = value['datarange'], value['len']
                        tmp = ''.join(random.SystemRandom().choice(datarange) for _ in range(length))
                        dict_data[random.randint(0, 10)] = tmp
                root.append(dict_data)
            elif k == 'int':
                it = iter(v['datarange'])
                root.append(random.randint(next(it), next(it)))
        yield root


def apply():
    struct = {
        'num': 100000000,  
        'struct': {
            'tuple': {
                'str': {'datarange': string.ascii_uppercase, 'len': 50}
            },
            'list': {
                'int': {'datarange': (0, 10)},
                'float': {'datarange': (0, 1.0)}
            },
            'dict': {
                'str': {'datarange': string.ascii_lowercase, 'len': 10}
            },
            'int': {'datarange': (0, 10)}
        }
    }

    count = 0  
    for data in generate(struct):
        print(data)  
        count += 1
        if count > 100000000: 
            break
        
        
apply()
        
