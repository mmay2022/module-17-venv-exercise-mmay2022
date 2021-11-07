import arrow
from parse import *
from joke_generator import generate

print(generate())
print(parse("Hello {}", "Hello World"))
utc = arrow.utcnow()
print(utc)