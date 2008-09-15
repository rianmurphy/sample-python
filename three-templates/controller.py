"""
This is our "controller" - right now, it doesn't do much but dispatch to the same templates.
A more advanced application could make decisions in here based on state to decide
what templates to use to render data for the user.
"""

# first, we increment out counter
data['count'] += 1

# now call our templates.  "local" means that the resource is coming from our
# application (all references relative to root), and that we're going to
# use a resource called  template1, template2 and template3, which are
# written using the 3 different templating options in 10gen.  We recommend
# using the djang10 templates, modeled after the Django template system
local.templates.template1({'theCount': data['count']})
local.templates.template2({'countThis': data['count']})
local.templates.template3({'countThat': data['count']})
