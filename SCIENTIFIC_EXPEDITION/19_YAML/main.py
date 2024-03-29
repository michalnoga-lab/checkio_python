def yaml(a):
    groups = a.splitlines()
    output = {}

    for group in sorted(list(groups)):
        try:
            key, value = str(group).split(':')
            output[f'{key.replace(" ", "")}'] = int(value) if value.replace(' ', '').isdigit() else value.lstrip(' ')
        except ValueError:
            pass
    return output


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
    age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
    age: 12""") == {'age': 12, 'name': 'Alex'}
assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
print("Coding complete? Click 'Check' to earn cool rewards!")
