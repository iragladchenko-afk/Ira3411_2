import colorama

print(type(colorama))
print(dir(colorama))

for name in dir(colorama):
    value = getattr(colorama, name)
    print(f'{name}->{type(value)}')