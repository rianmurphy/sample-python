
def mapUrlToJxpFile( uri , req , res ):
    if uri.find( "." ) < 0:
        req["name"] = uri[1:]
        return "/controller.py"
