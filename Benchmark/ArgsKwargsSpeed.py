import time

def add_fixed(a, b):
    return a + b

def add_args(*args):
    return sum(args)

def add_kwargs(**kwargs):
    return sum(kwargs.values())

# Benchmark fixed arguments
start_time = time.time()
for _ in range(1000000):
    add_fixed(3, 5)
fixed_time = time.time() - start_time

# Benchmark *args
start_time = time.time()
for _ in range(1000000):
    add_args(3, 5)
args_time = time.time() - start_time

# Benchmark **kwargs
start_time = time.time()
for _ in range(1000000):
    add_kwargs(a=3, b=5)
kwargs_time = time.time() - start_time



print(f"Fixed arguments time: {fixed_time:.6f} seconds")
print(f"*args time: {args_time:.6f} seconds")
print(f"**kwargs time: {kwargs_time:.6f} seconds")