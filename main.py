from fastapi import FastAPI
from scrape import Scrapper

# Initialize app
app = FastAPI()
quotes = Scrapper()

# Create endpoint
@app.get("/{tag}")
async def read_item(tag):
    return quotes.scrapedata(tag)