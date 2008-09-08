import models.modelbase as modelbase
import models.utils as utils

class Student(modelbase.ModelBase):
    "A student. Can be enrolled in multiple courses."

    collectionName = 'students'

    def __init__(self, name='name not set'):
        self.name = name
        self.email = "no email set"
        self.address = utils.Address()
        self.scores = []
        # This is how we'd do it in JS. See below for how we do it here.
        # self.scores._dbCons = utils.Score

    _dbCons = {'scores': utils.Score}

    def summary(self):
        s = self.name + '\n' + self.address + '\n'
        def addScore(score):
            s += score + '\n'
        map(addScore, self.scores)
        return s

    def addScore(self, course, grade):
        self.scores.append(utils.Score(course, grade))

    _transientFields = ["gpa", "_form", "_new"]

