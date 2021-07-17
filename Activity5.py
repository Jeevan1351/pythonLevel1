def get_cs():
    return input()


def cs_to_dict(string):
    string = string.split(';')
    d = {}
    for item in string:
        l = item.split('=')
        d[l[0]] = l[1]
    return d


def dict_to_cs(d):
    s = ""
    for item in d:
        s += item + "=" + d[item] + ";"
    return s


def main():
    cs = get_cs()
    d = cs_to_dict(cs)
    print(d)
    cs = dict_to_cs(d)
    print(cs)


main()
