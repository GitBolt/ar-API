from fastapi import FastAPI
from newspaper import Article      # Modules for parsing an article

app = FastAPI()


@app.get('/')
async def index():
    return {"Hello": "World!"}


@app.get('/parse')
async def ParseText(url: str = ""):
    """ Parses a given article and splits it into pieces. """

    # Download and Parse Articles
    article = Article(url, language="en")
    article.download()
    article.parse()

    # return the json values
    value = {
        "title": article.title,
        "article": article.text,
        "images": article.images,
        "summary": article.summary,
        "top_image": article.top_image

    }

    return value
