def my_func(param1="default"):
    """
        This is the doc string.

         :param1 parameter
    """
    print("my first function! {}".format(param1))


my_func("Hello")


mylist = [1, 2, 3, 4, 5, 6, 7, 8]


def even_bool(num):
    return num % 2 == 0


evens = filter(even_bool, mylist)
# evens is an object -> need to translate it to a list
print(list(evens))


# Doing the same with LAMBDA EXPRESSIONS
evens_with_lambda = filter(lambda num: num % 2 == 0, mylist)
print(list(evens_with_lambda))
