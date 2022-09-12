print('registration.py')

registry = []

def register(func):
    print('running register')
    registry.append(func)
    return func

@register
def f1():
    print('running f1')

if __name__ == '__main__':
    f1()
