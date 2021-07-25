def get_cs():
    return "system=s;database=d;username=u;pas]sword=p"


def cs_to_dict(string):
    string = string.split(';')
    d = {x.split('=')[0]: x.split('=')[1] for x in string}
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
