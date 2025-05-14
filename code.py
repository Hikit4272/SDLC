def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0  
    return wrapper


def print_stats():
    print(f"Функція була викликана {my_function.call_count} разів")


@count_calls
def my_function():
    print("Функція працює")

my_function()
my_function()
my_function()
my_function()
my_function()

print_stats()
