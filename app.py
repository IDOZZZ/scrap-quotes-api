from fastapi import FastAPI
from get import fetch_quotes # <- ini scraper kamu dari file uotes.py

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/quotes")
async def get_quotes():
    return {"quotes": fetch_quotes() # <- ini adalah import dari scraper kamu}
}

# at git bash: python -m venv venv    
# pip install pandas requests 
# pip install beautifulsoup4
# pip install "fastapi[standa]]