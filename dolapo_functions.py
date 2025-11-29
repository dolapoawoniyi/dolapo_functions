# This is an update for pull request
# Task 1: Simple Greeting Function

def greet_user():
    print("Welcome to Python programming!")

# Calling the function
greet_user()


# Task 2: Function with Parameters

def display_full_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}, nice to meet you!")

# Calling the function
display_full_name("Dolapo", "Awoniyi")


# Task 3: Function that Returns a Value

def add_numbers(a, b):
    return a + b

# Calling the function and print the result
result = add_numbers(10, 15)
print("The sum is:", result)



# Task 4: Function That Uses a Global Variable

school_name = "Obafemi Awolowo University"   # Global variable

def print_school_name():
    print("The name of my school is", school_name)  # Using global variable

    vice_chancellor = "Mr. Awoniyi"   # Local variable
    print("Our Vice chancellor is", vice_chancellor)

# Calling the function
print_school_name()
