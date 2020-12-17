def decorator(func):
    def func_wrapper(*args, **kwargs):
        for _ in range(args[0]):
            func(args[1])
    return func_wrapper

@decorator
def repeat_func(greet):
    print(greet)

repeat_func(5, "hi")