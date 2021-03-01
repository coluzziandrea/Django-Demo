# s = "GLOBAL VAR"


# def func():
#     mylocal = 10
#     print(locals())
#     print(globals())
#     # global s
#     # s = 50
#     # print(s)


# func()
# print(s)


# def hello(name="Andrea"):

#     def greet():
#         return "Hello {}".format(name)

#     def welcome():
#         return "Welcome {}".format(name)

#     if name == "Andrea":
#         return greet
#     else:
#         return welcome


# x = hello()

# print(x())


def new_decorator(func):

    def wrap_func():
        print("Code here before exec")
        func()
        print("Func ahs been called")

    return wrap_func


# def func_needs_decorator():
#     print("This func is in need of a decorator")


# func_needs_decorator = new_decorator(func_needs_decorator)


# The following is the exactly same thing

@new_decorator
def func_needs_decorator():
    print("This func is in need of a decorator")


func_needs_decorator()
