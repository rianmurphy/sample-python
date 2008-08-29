
// install some libraries

core.content.forms();

local.models.ModelBase();
local.models.utils();
local.models.course();
local.models.student();

core.core.routes();

// setup routing

routes = new Routes();

routes.student = "student";
routes.add( "students" , "student" , { extra : { action : "list" } } );

routes.add( "courses" , "course" , { extra : { action : "list" } } );

//core.modules.forum.setup();
//routes.forum = Forum.routes;
//assert( routes.forum );
