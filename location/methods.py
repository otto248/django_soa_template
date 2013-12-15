from xmlrpc.decorators import xmlrpc_func


@xmlrpc_func(context="location", returns='string', args=['string'])
def move_to(text):
    """Simply returns the args passed to it as a string"""
    return "Moved to! %s" % str(text)