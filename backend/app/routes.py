from fastapi.responses import JSONResponse
from . import server


@server.get('/')
def index():
    return JSONResponse({'success': 'OK'})
