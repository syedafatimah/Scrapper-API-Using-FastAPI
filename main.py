import string
from typing import Optional
from fastapi import FastAPI
from scrape import Scrapper
from pydantic import BaseModel # For post method

# Initialize app
app = FastAPI()
quotes = Scrapper()

#make class for all the data you want in return of post method
class Item(BaseModel):
    text : str
    author: str
    about: Optional[str] = None

# Create endpoint
@app.get("/get-item/{tag}")
async def read_item(tag: str):
    return quotes.scrapedata(tag)

# Create endpoint for post
@app.post("/create-item")
def create_item(item: Item):
    return{}
# Here we can add function to add more data through post method

#PUt method is used for update 
