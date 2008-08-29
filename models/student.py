class Student(ModelBase):
    "A student. Can be enrolled in multiple courses."

    collectionName = 'students'
    _c = db[collectionName]

    def __init__(self, name='name not set'):
        self.name = name
        self.email = "no email set"
        self.address = Address()
        self.scores = []
        # This is how we'd do it in JS. See below for how we do it here.
        # self.scores._dbCons = Score

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

    def summary(self):
        s = self.name + '\n' + self.address + '\n'
        def addScore(score):
            s += score + '\n'
        map(addScore, self.scores)
        return s
    
    def addScore(self, course, grade):
        self.scores.append(Score(course, grade))
        
    _transientFields = ["gpa", "_form", "_new"]

Student.modelBaseSetup()
