
#require( "model" );

print( "name: <b>" + request["name"] + "</b><br>" )

key = { "name" : request["name"] }
val = None
val = db.things.findOne( key )

if val is None :
     val = { "name" : request.name , "counter" : 1 }
else :
    val["counter"] = val["counter"] + 1
    
db.things.save( val )

print( "name: <b>" + val["name"] + "</b><br>" )
print( "count: <b>" );
print( val["counter"] );
print( "</b><br>" )

