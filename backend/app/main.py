from fastapi import FastAPI

app = FastAPI(
    title="Atlas API",
    version="0.1.0",
    description="API inicial do projeto Atlas."
)


@app.get("/")
def root():
    return {
        "message": "Atlas conectado"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/version")
def version():
    return {
        "name": "Atlas API",
        "version": "0.1.0"
    }