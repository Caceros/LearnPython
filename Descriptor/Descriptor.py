# -*- coding:utf-8 -*-


class PersonDescriptor:
    def __set_name__(self, owner, name):
        # 当你需要知道描述符在哪个类被创建，或者变量名时什么的时候
        print(owner)
        self.public_name = name
        self.private_name = '_%s' % name
    
    def __get__(self, obj, owner):
        value = getattr(obj, self.private_name)
        return value
    
    def __set__(self, obj, value):
        setattr(obj, self.private_name, value)

class Person:
    name = PersonDescriptor()
    age = PersonDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person('David', 25)
print(vars(a))
print(vars(vars(Person)['name']))


class LazyProperty(object):
    """
    实现惰性求值(访问时才计算，并将值缓存)
    利用了 obj.__dict__ 优先级高于 non-data descriptor 的特性
    第一次调用 __get__ 以同名属性存于实例字典中，之后就不再调用 __get__
    """
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.fun(instance)
        setattr(instance, self.fun.__name__, value)
        return value


class ReadonlyNumber(object):
    """
    实现只读属性(实例属性初始化后无法被修改)
    利用了 data descriptor 优先级高于 obj.__dict__ 的特性
    当试图对属性赋值时，总会先调用 __set__ 方法从而抛出异常
    """
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError(
            "'%s' is not modifiable" % self.value
         )


class Circle(object):

    pi = ReadonlyNumber(3.14)

    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return self.pi * self.radius ** 2
