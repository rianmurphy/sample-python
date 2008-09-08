import models.course as course
import _10gen

data = {}

data['cs'] = course.Course.find().limit( 100 ).sort( { 'name' : 1 } )
template = local.views.courses



if request.c__id:
    data['c'] = course.Course.findOne( request.c__id )

if request.action == "list":
    # already setup
    pass
elif data.has_key('c') and request.action == "Delete":
    data['c'].remove()
    del data['c']
elif data.has_key('c') and request.action == "Edit":
    pass
elif request.action == "Save":
    data['c'] = data.get('c', course.Course())
    Forms.fillInObject("c_", data['c'], request)
    data['c'].save()
    del data['c']

elif request.action == "New":
    data['c'] = course.Course()

if data.has_key('c'):
    data['c']._form = Forms.Form(data['c'], "c_")
    template = local.views.course

template(data)
