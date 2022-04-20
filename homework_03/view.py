from fastapi import APIRouter

router_ping = APIRouter()

@router_ping.get('/ping/')
def ping():
    return {'message' : 'pong'}