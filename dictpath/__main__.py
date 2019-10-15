from dictpath import dictpath
import sys, json

if __name__ == '__main__':
    d = json.loads(sys.stdin.read())
    print(json.dumps(dictpath(d).explore()))

