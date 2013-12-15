from xmlrpc.decorators import xmlrpc_func


@xmlrpc_func(context="payment", returns='string', args=['string'])
def make_payment(text):
    """Simply returns the args passed to it as a string"""
    return "Made Payment! %s" % str(text)