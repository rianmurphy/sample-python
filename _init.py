
core.content.forms()

core.core.routes()

routes = Routes()

routes.student = "student"
routes.add( "students" , "student" , { "extra" : { "action" : "list" } } )

routes.add( "courses" , "course" , { "extra": { "action" : "list" } } )

