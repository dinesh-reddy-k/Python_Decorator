#Log _message Decorator
def log_message(fun):
    def wrapper(*a):
        b=fun(*a)
        with open('/tmp/decorator_logs.txt','a') as f:
            f.write(b+'\n')
        f.close()
        return b
    return wrapper

@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"

a_function_that_returns_a_string()
a_function_that_returns_a_string_with_newline('Dinesh')
a_function_that_returns_another_string('reddy')