# 🟢 1. map(function, iterable)

nav_for_map = [
    {"name": "Home", "state": True, "url": "google.com"},
    {"name": "About", "state": True, "url": "googl/about.com"},
    {"name": "Sign up", "state": True, "url": "googl/signup.com"},
    {"name": "Login", "state": True, "url": "googl/login.com"},
    {"name": "Log Out", "state": False, "url": "googl/logout.com"}
]
def check_state(navitem):
    if navitem["state"]:
        print(f"name: {navitem['name']} url: {navitem['url']}")

list(map(check_state, nav_for_map))

# 🟣 2. filter(function, iterable)


nav_for_fiter = [
    {"name": "Home", "state": True, "url": "google.com"},
    {"name": "About", "state": True, "url": "googl/about.com"},
    {"name": "Sign up", "state": True, "url": "googl/signup.com"},
    {"name": "Login", "state": True, "url": "googl/login.com"},
    {"name": "Log Out", "state": False, "url": "googl/logout.com"}
]
new_nav=list(filter(lambda navitem: navitem["state"],nav_for_fiter))
for navitem in new_nav:
    print(navitem["name"])


# 🔵 3. reduce(function, iterable)
'''
n reduce(lambda a, b: ..., iterable) —
👉 a is the accumulator (the running total or combined result so far)
👉 b is the current value (the next item from the list)
'''
from functools import reduce

arr=[1,2,3,4,5]
print(reduce(lambda acc,curr:acc+curr,arr))