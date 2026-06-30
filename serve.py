import os, functools
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Serve this project's directory. Pass `directory` explicitly so the handler
# never calls os.getcwd() (some sandboxed environments block it). Honour PORT
# if provided, else default to 8080.
DIR = os.path.dirname(os.path.abspath(__file__))
Handler = functools.partial(SimpleHTTPRequestHandler, directory=DIR)
port = int(os.environ.get('PORT', '8080'))
print(f'Serving Negative Space on http://localhost:{port}')
HTTPServer(('', port), Handler).serve_forever()
