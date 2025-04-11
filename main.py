from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import users_collection
from fastapi import status
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
@app.get("/signup", response_class=HTMLResponse)
async def signup_get(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
@app.post("/signup")
async def signup(
    fullname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    user = {
        "fullname": fullname,
        "email": email,
        "password": password
    }

    existing_user = users_collection.find_one({"email": email})
    if existing_user:
        print(f"User already exists: {email}")
        return RedirectResponse(url="/signup", status_code=status.HTTP_303_SEE_OTHER)

    users_collection.insert_one(user)
    print(f"New user saved: {fullname}, {email}")
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
@app.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login_post(
    email: str = Form(...),
    password: str = Form(...)
):
    user = users_collection.find_one({"email": email, "password": password})
    if user:
        print(f"User logged in: {email}")
        return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    else:
        print(f"Invalid credentials for: {email}")
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
@app.get("/compare_property", response_class=HTMLResponse)
async def compare_property(request: Request):
    return templates.TemplateResponse("compare_property.html", {"request": request})

@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})
