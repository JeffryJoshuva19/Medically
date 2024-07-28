from fastapi import APIRouter, Depends, HTTPException, FastAPI, Request, Form
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse
from sqlalchemy.orm import Session
from config.base_config import BaseConfig
from fastapi.staticfiles import StaticFiles
from datetime import  datetime,date, timedelta
from models import get_db,modals
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from resources.utils import create_access_token
from starlette.middleware.sessions import SessionMiddleware
#from jose import jwt, JWTError
current_datetime = datetime.utcnow()
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

@app.get("/signin")
def login_page(request:Request):   
    return templates.TemplateResponse('signin.html', context={'request': request})


@app.post("/signup")
def logcheck(request:Request,db:Session=Depends(get_db),susername:str=Form(...),semail:str=Form(...),smobile:str=Form(...),spassword:str=Form(...)):
    find=db.query(modals.User).filter(modals.User.Emailid==semail,modals.User.Status=="Active").first()
    if find is None:
        new_user=modals.User(Username=susername,Emailid=semail,Phonenumber=smobile,Password=spassword,Status="Active",Created_at=current_datetime)
        db.add(new_user)
        db.commit()
        error="Valid Creditional"
        access_token_expires = timedelta(minutes=BaseConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"user_name": susername,"user_email": semail},expires_delta=access_token_expires)
        sessid = access_token
        request.session["user"] = sessid
        print(sessid)
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
        
    else:
        error= "This EmailID already exists"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
        

@app.post("/login")
def logcheck(request:Request,db:Session=Depends(get_db),lemail:str=Form(...),lpassword:str=Form(...)):
    find=db.query(modals.User).filter(modals.User.Emailid==lemail,modals.User.Password==lpassword,modals.User.Status=="Active").first()
    if find is not None:
        error="Valid Creditional"
        access_token_expires = timedelta(minutes=BaseConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"user_name": find.Username,"user_email": find.Emailid},expires_delta=access_token_expires)
        sessid = access_token
        request.session["user"] = sessid
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
        
    else:
        error= "Invalid password or emailid"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)

@app.get("/logout")
def logout(request:Request):
    request.session.clear()
    return RedirectResponse("/locationSelection", status_code=303)