import http.server
from .controllers.pokemon_controllers import getPokemons

class routeHandler(http.server.BaseHTTPRequestHandler):
    base_path = "/api_v1"
    
    def do_GET(self):
        path = self.path if self.path[-1] != "/" else self.path[:-1] 

        if path == self.base_path + "/pokemons":
            print("GET Pokemons")
            getPokemons(self, path)
        
    def do_POST(self):
        print("POST")

def main():

    PORT = 6666

    handler = http.server.HTTPServer(("", PORT), routeHandler)
    print(f"Server is running on port {PORT}...")
    handler.serve_forever()

if __name__ == "__main__":
    main()