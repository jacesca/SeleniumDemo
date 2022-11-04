import inspect

def whoami():
    return inspect.stack()[1][3]

def whosdady():
    return inspect.stack()[2][3]

def foo():
    print(f"Hello, I'm {whoami()}, my daddy is {whosdady()}")
    bar()

def bar():
    print(f"Hello, I'm {whoami()}, my daddy is {whosdady()}")

johny = bar

# Call them all!
print('Calling foo()')
foo()
print('Calling bar()')
bar()
print('Calling johny()')
johny()
