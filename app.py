from aiohttp import web
import json

# Responses
async def status(request):
  response_obj = { 'status': 'alive'}
  return web.Response(text=json.dumps(response_obj))

async def new_user(request):
    try:
        user = request.query['name']
        email = request.query['email']
        print("Created new user %s with email %s " % (user, email) )

        response_obj = { 'status' : 'success' }
        return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }
        return web.Response(text=json.dumps(response_obj), status=500)

# Routers
app = web.Application()
app.router.add_get('/status', status)
app.router.add_post('/user', new_user)

web.run_app(app)