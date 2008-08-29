#TODO make this extend from ModelBase
class Student(object):
    "A student. Can be enrolled in multiple courses."

    # MB
    collectionName = 'students'
    _c = db[collectionName]
    
    # Since we _dbCons doesn't work on lists we do some magic here
    def __setattr__(self, name, value):
        if name == 'scores':
            def objToScore(obj):
                c = Course()
                c.name = obj.for_course.name
                c._id = obj.for_course._id
                s = Score(c, obj.grade)
                return s
            map(objToScore, value)
        super(Student, self).__setattr__(name, value)

    def __init__(self, name='name not set'):
        self.name = name
        self.email = "no email set"
        self.address = Address()
        self.scores = []
        # TODO FIX THIS
        #self.scores._dbCons = Score

    def summary(self):
        s = self.name + '\n' + self.address.toString() + '\n'
        def addScore(score):
            s += score.toString() + '\n'
        map(addScore, self.scores)
        return s
    
    def addScore(self, course, grade):
        self.scores.append(Score(course, grade))
        
    _transientFields = ["gpa", "_form", "_new"];
    
    #MB
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
    def toString(self):
        return self.__str__()
#MB
Student._c.setConstructor(Student)
