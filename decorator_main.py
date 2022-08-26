def my_fun_decor(fun):
    def wrap(*args, **kwargs):
        fun(*args, **kwargs)

        return wrap


@my_fun_decor
def sample_fun(greet, emoji="0_0"):

    print(greet, emoji)


sample_fun('sidd')
