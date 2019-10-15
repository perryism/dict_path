import sys
class dictpath:
    def __init__(self, d):
        self.d = d

    '''
    Return roughly the structure of a dictionary
    '''
    def explore(self, absolute_path=True):
        key_gen = self._keygen(absolute_path)
        return self._explore(self.d, {}, '', key_gen)

    '''
    Return the values according to the mapper
    eg
    {
        'a': 3
        'b': { 'c' : 3 }
    }
    To get 'c' in 'b',
    .path({'c': 'b/c' })
    '''
    def path(self, mapper):
        return dict(map(lambda m: [m[0], self._path(m[1], self.d)], mapper.items()))

    def _path(self, mapper, js):
        if type(js) == list:
            return map(lambda x: self._path(mapper, x), js)

        try:
            if callable(mapper):
                return mapper(js)

            parts = mapper.split('/')
            if len(parts) > 1:
                #print type(js[parts[0]])
                return self._path('/'.join(parts[1:]), js[parts[0]])
            else:
                return js[parts[0]]
        except:
            #print("Unexpected error:", sys.exc_info()[0])
            print(mapper, js)
            return None

    def query(self, q):
        return self.path({'q': q})['q']

    def _keygen(self, absolute_path):
        if absolute_path:
            return lambda parent, key: "%s%s"%(parent if len(parent)==0 else "%s/"%parent, key)
        else:
            return lambda parent, key: key

    def _explore(self, json, h, parent, key_gen):
        for key in json.keys():
            k = key_gen(parent, key)
            if type(json[key]) == list:
                k = "%s[]"%k
                h[k] = []
                if len(json[key]) > 0:
                    #only look at the first item
                    if type(json[key][0]) is dict:
                        t = self._explore(json[key][0], {}, k, key_gen)
                    else:
                        t = type(json[key][0]).__name__
                else:
                    t = type(json[key]).__name__
                h[k].append(t)

            elif type(json[key]) == dict:
                h[k] = {}
                self._explore(json[key], h[k], k, key_gen)
            else:
                h[k] = type(json[key]).__name__
        return h

