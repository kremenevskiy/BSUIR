class FieldsFromFileMeta(type):
    file_path = ''

    def __new__(cls, class_name, bases, attrs):
        import json
        # super().__init__(*args, **kwargs)
        with open(cls.file_path, 'r') as f:
            res_attrs = dict(json.load(f))

        for name, value in res_attrs.items():
            try:
                res_attrs[name] = eval(value)
            except (NameError, TypeError):
                res_attrs[name] = value
        return type(class_name, bases, res_attrs)

    pass


# file_path = input('Enter source file path: ')
file_path = 'task29_file.json'
FieldsFromFileMeta.file_path = file_path


class MyClass(metaclass=FieldsFromFileMeta):
    pass


print(MyClass.x)
MyClass.fn(5)
print(MyClass.s)

# or like that
class FieldsFromFileMeta(type):
    file_path = ''

    def __init__(cls, *args, **kwargs):
        import json
        super().__init__(*args, **kwargs)
        with open(cls.file_path, 'r') as f:
            res_attrs = dict(json.load(f))

        for name, value in res_attrs.items():
            try:
                setattr(cls, name, eval(value))
            except (NameError, TypeError):
                setattr(cls, name, value)

    pass



