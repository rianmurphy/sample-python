class Course(ModelBase):
    "A named course"

    collectionName = 'courses'
    _c = db[collectionName]

    def __init__(self, name='name not set'):
        self.name = name

    def __str__(self):
        return 'Course ' + self.name

Course.modelBaseSetup()
