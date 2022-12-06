import file_formats
from file_formats import the_arrow, white, blue, red, escape

with open("2022\\datastream.txt") as file:
    datatream: str = file.readline()

def get_index(data: str, length: int) -> int:
    index: int = 0
    for alpha in range(0, len(data) - 1):
        items = data[alpha:alpha + length]
        if len(set(items)) == len(items) == length:
            index = alpha + length
            break
    return index

def start_of_package():
    return get_index(datatream, 4)

def start_of_message():
    return get_index(datatream, 14)

print(
    f"{the_arrow}{white} Therefore, the number of characters to be processed {blue}before the start of the first start-of-package marker is detected{white} is: {red}{start_of_package()}{escape}[0m")
print(
    f"{the_arrow}{white} Therefore, the number of characters to be processed {blue}before the start of the first start-of-message marker is detected{white} is: {red}{start_of_message()}{escape}[0m")
