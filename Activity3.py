def get_cs():
    return input("Input:\n")


def cs_to_lot(string):
    separated = string.split(';')
    listOt = []
    for i in separated:
        listOt.append(tuple(i.split('=')))
    return listOt


def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print("Output:")
    print(lot)


main()
