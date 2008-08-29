#TODO make this extend from ModelBase
class Course(object):
    "A named course"

    # MB
    collectionName = 'courses'
    _c = db[collectionName]

    def __init__(self, name='name not set'):
        self.name = name

    def __str__(self):
        return 'Course ' + self.name
    
    #MB
    @classmethod
    def find(cls, key=None, fields=None):
        return cls._c.find(key, fields)
    def save(self):
        return self._c.save(self)
    @classmethod
    def findOne(cls, key="", create=False):
        if key == "":
            if create:
                return cls.cons()
            return None
        if isinstance(key, str):
            key = ObjectId(key)
        
        o = cls._c.findOne(key);
        if create and o == None:
            o = cls.cons()
        return o
    def remove(self, key=None):
        if key == None:
            key = {}
            if not self._id:
                return
            key['_id'] = self._id
        return self._c.remove(key)
    def toString(self):
        return self.__str__()
#MB
Course._c.setConstructor(Course)