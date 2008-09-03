
core.content.forms()

local.models.ModelBase()
local.models.utils()
local.models.course()
local.models.student()

core.core.routes()

routes = Routes()

routes.student = "student"
routes.add( "students" , "student" , { "extra" : { "action" : "list" } } )

routes.add( "courses" , "course" , { "extra": { "action" : "list" } } )

