def its_me_decorator(func):
    return lambda : f"{func()}, it's me!"

def u_decorator(func):
    return lambda : f"<u> {func()} </u>"


@u_decorator
@its_me_decorator
def say_hi():
    return 'Hi'

print(say_hi())
