import uvicorn
from notes import main
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    uvicorn.run("notes.main:app",host=os.getenv('HOST'),reload=True,port=int(os.getenv('PORT')))