import urllib.request
import ssl
import suds.transport.http

class UnverifiedHttpsTransport(suds.transport.http.HttpTransport):
    """
    Used with the suds client to bypass SSL certificate validation
    """
    
    def __init__(self, *args, **kwargs):
        super(UnverifiedHttpsTransport, self).__init__(*args, **kwargs)

    def u2handlers(self):
        handlers = super(UnverifiedHttpsTransport, self).u2handlers()
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        handlers.append(urllib.request.HTTPSHandler(context=context))
        return handlers