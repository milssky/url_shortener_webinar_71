import random
import string


def get_short_slug(
    slug_length = 8,
    alphabet = string.ascii_lowercase + string.digits
):
    return "".join(
        [random.choice(alphabet) for _ in range(slug_length)]
    )

# print(get_short_slug())

# def foo3():
#     try:
#         foo()
#     except Exception:
#         raise ...

# try:
    
# except ...:
#     foo3()