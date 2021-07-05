import http.server
import json
import time
import asyncio
from urllib import request

def _set_response(self):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Content-type', 'application/json')
    self.end_headers()

# API without async.

# def getPokemons(self, path):

#     time_at_start = time.time()
#     pokemon_list = []
#     base_poke_api = "https://pokeapi.co/api/v2/pokemon/"

#     for num in range(1, 5):
#         # Setup headers otherwise it will think you are spider crawler.
#         r = request.Request(base_poke_api + str(num), headers={'User-Agent': 'Mozilla/5.0'})
#         data = request.urlopen(r).read()
        
#         print(type(data))
#         # Byte type need to convert to str.
#         pokemon_list.append(data.decode())

#     j = json.dumps(pokemon_list)
#     _set_response(self)
    
#     time_sum = time.time() - time_at_start
#     print(f"Total seconds: {time_sum:.2f}")
#     # Encoding back into bytes for Python response.
#     self.wfile.write(j.encode())


# API with async.

async def fetchPokemon(base_path, num):
    r = await request.Request(base_path + str(num), headers={'User-Agent': 'Mozilla/5.0'})
    data = request.urlopen(r).read()
    print(type(data))
    return data.decode()

def getPokemons(self, path):

    time_at_start = time.time()
    pokemon_list = []
    base_poke_api = "https://pokeapi.co/api/v2/pokemon/"
    
    for num in range(1, 5):
        data = fetchPokemon(base_poke_api, num)
        print(type(data))
        # Byte type need to convert to str.
        pokemon_list.append(data)

    j = json.dumps(pokemon_list)
    _set_response(self)
    
    time_sum = time.time() - time_at_start
    print(f"Total seconds: {time_sum:.2f}")
    # Encoding back into bytes for Python response.
    self.wfile.write(j.encode())
