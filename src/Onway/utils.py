import random
import string


def random_string_generator(size=6,chars= string.ascii_letters + string.digits):

    l = ""
    for i in range(size):
        l += random.choice(chars)
    return l

def random_shortcode_generator(instance):

    size = random.randint(10,15)

    shortcode =  random_string_generator(size=size)

    Klass = instance.__class__
    qs = Klass.objects.filter(shortcode=shortcode)
    if qs.exists():
        shortcode = random_string_generator(size=size)
    return shortcode