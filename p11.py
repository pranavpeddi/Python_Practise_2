from builtins import Exception


class MyError(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self):
        return (repr(self.value))

try:
    raise (MyError(3*2))

except MyError as error:
    print('a new exception is occured',error.value)