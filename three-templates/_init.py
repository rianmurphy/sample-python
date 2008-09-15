import re

# create a dictionary for our application data.
# right now this cannot just be a scalar: see:
# http://www.10gen.com/wiki/appserver.lifecycle
data = {};
data['count'] = 0

def mapUrlToJxpFile (uri, request, response):
    """
    Maps a uri to a controller.

    Here we just map every url to single controller.
    """

    # allow any request for a static asset to be just handled
    # by the appserver
    if re.compile("^/assets/").match(uri):
         return None

    # otherwise, just always return our "controller", which is
    # ./controller.* (in this case controller.py)
    return "controller"
