# Custom split function
def my_split(string, delimiter=','):
    segment = ''
    for char in string:
        if char == delimiter:
            yield segment.strip()  # Strip leading and trailing whitespace
            segment = ''
        else:
            segment += char
    yield segment.strip()  # Strip leading and trailing whitespace


# Custom strip function
def my_strip(string):
    start = 0
    end = len(string) - 1
    
    # Removing leading whitespace
    while start <= end and string[start].isspace():
        start += 1
    
    # Removing trailing whitespace
    while end >= start and string[end].isspace():
        end -= 1
    
    # Returning the stripped substring
    return string[start:end+1]
