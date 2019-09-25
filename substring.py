"""Count same substrings in string """
from sys import stdin

def read_str():
    """read strig"""
    main_str = []
    while True:
        try:
            buf_symb = stdin.read(1)
            if ord(buf_symb) is ord('\n'):
                break
            main_str.append(buf_symb)
        except EOFError:
            break
    main_string = "".join(main_str)
    return main_string

def main_f():
    """main_f"""
    flg_err = False
    counter_s = 0
    main_string = read_str()
    sub_str = main_string[counter_s]
    while counter_s is not len(main_string):
        count_sub = main_string.count(sub_str)
        i = count_sub*len(sub_str)
        if i is len(main_string):
            flg_err = True
            break
        counter_s += 1
        sub_str += main_string[counter_s]
    if (flg_err is True)&(count_sub > 1):
        print(str(main_string.count(sub_str)))
    else:
        print('Incorrect string')

main_f()
