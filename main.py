from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from utils import Feed, add_feed_to_db,get_all_feeds


app = FastAPI()

template_dir = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return {"Hello": "RSS Manager"}


@app.get("/addfeed")
async def add_feed_page(request: Request):
    return template_dir.TemplateResponse("add_feed.html", {"request": request})


@app.post("/addfeed")
async def add_feed_submit(url: str = Form(...), tag: str = Form(...)):
    feed = Feed(url)
    add_feed_to_db(url=url, title=feed.title, tag=tag,link=feed.link)
    return {"message": "add successfully"}


@app.get("/feeds_list")
async def get_rss_feeds(request:Request):
    feeds = get_all_feeds()
    return template_dir.TemplateResponse("feeds_list.html",{"request":request,"feeds":feeds})
