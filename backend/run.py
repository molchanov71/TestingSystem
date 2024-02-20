import uvicorn

if __name__ == '__main__':
    uvicorn.run('app:server', host='localhost', port=8080, reload=True)
