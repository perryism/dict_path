from dictpath import dictpath
import sys, json
import pprint

if __name__ == '__main__':
    d = json.loads(sys.stdin.read())
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(dictpath(d).explore())

