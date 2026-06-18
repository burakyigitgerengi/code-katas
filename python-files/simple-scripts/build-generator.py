def gen_values():
    yield 1
    yield 2
    yield 3


print(next(gen_values()))  # returns 1
print(next(gen_values()))  # still returns 1
gen_values_obj = gen_values()
# next is like the lever you pull to make yields return
print(next(gen_values_obj))  # returns 1

for _ in gen_values_obj:
    print(_)  # prints 2 & 3, you don't need to type next()
    # exits the loop automatically
