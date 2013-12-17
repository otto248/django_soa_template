
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/xmlrpc',)

    def __init__(self, a, b, c):
        SimpleXMLRPCRequestHandler.__init__(self, a, b, c)

    def do_GET(self):
        splitted = self.path.split("/")[1:]
        valid = splitted[0] == "xmlrpc"
        assert valid

        again_splitted = splitted[1].split("?")
        method = again_splitted[0]
        try:
            params = again_splitted[1].split("&")
            params = [p.split("=") for p in params]

            correct_params = False not in [len(p) == 2 for p in params]
            assert correct_params

            new_params = []

            for p in params:
                new_params.append(p[1])
        except:
            new_params = []


        # In previous versions of SimpleXMLRPCServer, _dispatch
        # could be overridden in this class, instead of in
        # SimpleXMLRPCDispatcher. To maintain backwards compatibility,
        # check to see if a subclass implements _dispatch and dispatch
        # using that method if present.
        response = self.server._dispatch(method, new_params)


        data = "<div>Method:%s</div>" % method
        data += "<div>Params:%s</div>" % new_params
        data += "<div>response:%s</div>" % response

        self.send_response(200)
        self.send_header("Content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)



class ServiceXMLRPCServer(SimpleXMLRPCServer):


    def __init__(self, socket_data, requestHandler):
        SimpleXMLRPCServer.__init__(self, socket_data, requestHandler=requestHandler)
        self.register_introspection_functions()
        self.register_function(self.ping, "ping")

    def ping(self, msg):
        return msg



# Create server
server = ServiceXMLRPCServer(("localhost", 8099), requestHandler=RequestHandler)


import sqlite3



# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
class ServiceMethods(object):

    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.c = self.conn.cursor()

    def register_user(self, name, password):
        try:
            self.c.execute("INSERT INTO users VALUES ('?','?')", (name, password, ))
            self.conn.commit()
            return True
        except Exception as e:
            print e
            return False

    def view_users(self, username):
        print username
        command = "SELECT username, password FROM users WHERE username=?"
        self.c.execute(command, (username, ))
        result = self.c.fetchall()
        return result


    def get_page(self, *args, **kwargs):
        return """

         <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>

         <script>
            $(document).ready(function(){
                $("#button").bind("click", function(){
                    make();
                });
            });

            function make(){
                $.ajax({
                    url: 'http://localhost:8099/xmlrpc/view_users?username=testuser',
                    method: "GET",
                    success: function(data) { alert(data);}
                });
            }
        </script>

         <input id="button" type="button" value="make">
        """

server.register_instance(ServiceMethods())


# Run the server's main loop
server.serve_forever()


