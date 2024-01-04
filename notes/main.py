from fastapi import FastAPI
from .models import create_all_models,note_model,user_model
from .database import engine
from .routes import router as main_router



app = FastAPI()
create_all_models(engine)

app.include_router(main_router)  
