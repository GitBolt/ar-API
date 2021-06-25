from fastapi import FastAPI

# Modules for parsing an article
from newspaper import Article
# Cors import
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# CORS Setup

# origins that are allowed
origins = [
    "https://ansh-test-api.herokuapp.com/",
    "http://127.0.0.1:8000",
    "http://localhost:8000",

]

# Adding origin links
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        "images": article.top_image,
        "summary": article.summary,
    }

    return value
