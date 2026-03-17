int = None
str = None
def set_globals(int_value, str_value):
    global int
    global str
    int = int_value
    str = str_value
def get_globals():
    return int, str
