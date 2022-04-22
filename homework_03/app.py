from fastapi import FastAPI
from view import router_ping

app = FastAPI()
app.include_router(router_ping)

@app.get('/')
def root_path():
    return {'message' : 'all is okay'}