# module_11_3.py
# 15.12.2024 Домашнее задание по теме "Интроспекция"

def introspection_info(obj):
    return {
        'type': type(obj),
        'attributes': [attributes for attributes in dir(obj) if not callable(getattr(obj, attributes))],
        'methods': [methods for methods in dir(obj) if callable(getattr(obj, methods))],
        'module': obj.__class__.__module__}


number_info = introspection_info(42)
print(number_info)


# type - возвращает тип объекта
# attributes - генератор списка, который перебирает и возвращает атрибуты объекта
# methods - аналогичный генератор списка, который перебирает и возвращает методы объекта
# module - возвращает имя модуля, в котором определён класс объекта
