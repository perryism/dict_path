class jsonpath:
    def __init__(self, js):
        self.js = js

    def query(self, path):
        self._query(path, self.js)

    def _query(self, path, js):
        found = []
        if type(js) == list:
            for i in js:
                #flatten
                found.append(self._query(path, i))
        elif type(js) == dict:
            for k, v in js.items():
                if key == path:
                    found.append(v)
                else:
                    pass
        return filter(lambda x: x is not None, found)

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
        return dict(map(lambda m: [m[0], self._path(m[1], self.d)], mapper.iteritems()))

    def _path(self, mapper, js):
        try:
            if callable(mapper):
                return mapper(js)

            parts = mapper.split('/')
            if len(parts) > 1:
               return self._path('/'.join(parts[1:]), js[parts[0]])
            else:
               return js[parts[0]]
        except:
            return None

    def query(self, q):
        pass

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
                        t = type(json[key][0])
                else:
                    t = type(json[key])
                h[k].append(t)

            elif type(json[key]) == dict:
                h[k] = {}
                self._explore(json[key], h[k], k, key_gen)
            else:
                h[k] = type(json[key])
        return h
