def get_sum(a, b):
    return a + b

def get_product(a, b):
    return a * b

def print_name():
    print("__name__ in Sample:", __name__)

print(get_product(50,10))

if __name__ == "__main__":
    print(get_sum(10,20))
    print_name()
    print("I am in sample file!")