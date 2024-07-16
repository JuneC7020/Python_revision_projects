def swap_case(txt):
    result = ''

    for c in txt:
        if c.islower():
            result += c.upper()
        else:
            result += c.lower()

    return result

if __name__ == '__main__':
    input_txt = input('Enter string: ')
    output = swap_case(input_txt)
    print('Swapped result: '+output)