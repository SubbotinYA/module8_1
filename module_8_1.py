def add_everything_up(a,b):
    try:
       x=a+b
    except:
       return f'{a}{b}'
    else:
        return f"x={a}+{b}, {x=}"
    finally:
        print('Как тебе такое Илон Маск?')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
