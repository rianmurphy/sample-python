class ModelBase(object):
    @classmethod
    def find(cls, key=None, fields=None):
        return cls._c.find(key, fields)
    def save(self):
        return self._c.save(self)
    @classmethod
    def findOne(cls, key="", create=False):
        if key == "" or key == None:
            if create:
                return cls()
            return None
        if isinstance(key, str):
            key = ObjectId(key)
        
        o = cls._c.findOne(key);
        if create and o == None:
            o = cls()
        return o
    def remove(self, key=None):
        if key == None:
            key = {}
            if not self._id:
                return
            key['_id'] = self._id
        return self._c.remove(key)
    
    # TODO This shouldn't be necessary. But when a template goes to print a course
    # It looks for toString and for some reason the bridge doesn't translate that
    # to __str__
    def toString(self):
        return self.__str__()

    @classmethod
    def modelBaseSetup(cls):
        cls._c.setConstructor(cls)