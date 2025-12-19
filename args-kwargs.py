def display(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display(1, 2, 3, name="Alice", age=25)
display(14,  name="Hello", age=35)