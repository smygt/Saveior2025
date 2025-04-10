from fastapi import FastAPI
from routers import folders, links, tags
from database import engine
import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Saveior API")

# Include routers
app.include_router(folders.router)
app.include_router(links.router)
app.include_router(tags.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Saveior API"} 