import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999. is my office.'

phones = re.compile(r'\d{3}.\d{3}.\d{4}')

matches = phones.finditer(message)

for match in matches:
    print(match.group(0))


if __name__ == '__main__':
    pass