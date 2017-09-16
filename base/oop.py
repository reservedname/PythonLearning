class A:
    ele = 2
    def __init__(self,ele):
        self.ele = ele

    def f1(self):
        # print(self.__class__)
        print(self.ele)

    def __del__(self):
        print('deleted')

# a = A(5)
# b = a
# del a
# b.f1()
# print('end')

# a.f1()
# print(hasattr(a,'ele'))
# print(hasattr(a,'abc'))
# print(getattr(a,'ele'))
