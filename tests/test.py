import sys, getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    print(sys.argv)
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('输入的文件为-', inputfile)
    print('输出的文件为-', outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])

    {"list": {"2017-11-01": {"ppap": {"300001": {"3000|1": {"t": 0, "e": 83023, "b": 99628, "l": 0, "m": 0}}},
                             "clt": {"300001": {"3000|1": {"t": 0, "e": 10516, "b": 12619, "l": 0, "m": 0}}}}},
     "total": {"2017-11-01": {"t": 0, "e": 93000, "b": 111000, "l": 0, "m": 0}}}
