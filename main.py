
from click import File
from fastapi import FastAPI,Request,Depends,Form, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import jwt
import shutil
from typing import Optional
import uuid
from sqlalchemy import func
from sqlalchemy.orm import Session
#from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates 
from starlette.middleware.sessions import SessionMiddleware
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse,RedirectResponse
from database import *
import modals
import utils
from jose import JWTError, jwt
import random
from utils import BaseConfig

from utils import create_access_token


app = FastAPI()

current_datetime = datetime.utcnow()
templates = Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
app.add_middleware(

    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key="e8Lj5R$Zv@n8!sWm3P#q")
# app.mount("/templates", StaticFiles(directory="templates"), name="templates")
# templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request:Request):
    return {"hello": "Medially"}

@app.get("/signin")
def login_page(request:Request):   
    return templates.TemplateResponse('signin.html', context={'request': request})

@app.get("/signup")
def login_page(request:Request):   
    return templates.TemplateResponse('signup.html', context={'request': request})

@app.get('/circle')
def get_home(request: Request, page: int = 1, db: Session = Depends(get_db)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            per_page = 12
            start_index = (page - 1) * per_page
            end_index = start_index + per_page

            circles = db.query(modals.Circle).filter(modals.Circle.circle_status == "Active").offset(start_index).limit(per_page).all()
            user_data=db.query(modals.User).filter(modals.User.Username==username,modals.User.Status=="Active").first()
            print(circles)
            total_circles = db.query(modals.Circle).filter(modals.Circle.circle_status == "Active").count()

            total_pages = (total_circles + per_page - 1) // per_page

            return templates.TemplateResponse("circle2.html", context={"request": request, "circles": circles, "page": page, "total_pages": total_pages,"user_datas":user_data})
    except JWTError:
         raise HTTPException(status_code=401,detail="Unauthorized")

@app.get("/profilepost")        
def login_page(request:Request,db:Session = Depends(get_db)): 
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            #login_status=1
            user_datas=db.query(modals.User).filter(modals.User.Username==username,modals.User.Status=="Active").first()
            posts=db.query(modals.Posts).filter(modals.Posts.Status=="Active").all()
            postimg=db.query(modals.Posts).filter(modals.Posts.Username==modals.User.Username,modals.Posts.Status=="Active").all()
            user_posts=db.query(modals.Posts).filter(modals.Posts.Username==username,modals.User.Status=="Active").all()
            menus=db.query(modals.Menus).filter(modals.Menus.Status=="Active").all()
            infectious=db.query(modals.Infectious).filter(modals.Infectious.Status=='active').all()
            research=db.query(modals.Research).filter(modals.Research.Status=="Active").all()
            random.shuffle(posts)
            c=0
            for i in user_posts:
                c+=1
            count=len(posts)
            other_user = db.query(modals.User).filter(modals.User.Username != username).all()
            for i in posts:
                i.comment=db.query(modals.Comments).all()
                # Query the database to count comments associated with the current post
                comment_count = db.query(func.count()).filter(modals.Comments.Postid == i.Postid).scalar()
                # Assign the comment count to the post object
                i.comment_count = comment_count
            

            
            #print(other_user)
            active_ads = db.query(modals.Advertisement).filter(modals.Advertisement.Status == "Active").all()
            ad = random.choice(active_ads)
            return templates.TemplateResponse('profilepost.html', context={'request': request,"user_datas":user_datas,"posts":posts,"ad":ad,"otheruser":other_user,"count":count,"c":c,"menus":menus,"infect":infectious,"postimg":postimg,"research":research}) 
    except JWTError:
         raise HTTPException(status_code=401,detail="Unauthorized")

@app.get("/profileabout")
def profile_about(request:Request,db:Session = Depends(get_db)):   
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            #login_status=1
            user_data=db.query(modals.User).filter(modals.User.Username==username,modals.User.Status=="Active").first()
            non_null_count = 0
            total_fields = 0
            
            # Iterate over the attributes of the user_data object
            for attribute, value in user_data.__dict__.items():
                # Exclude private attributes (starting with '_')
                if not attribute.startswith('_'):
                    total_fields += 1
                    if value is not None and value != "":
                        non_null_count += 1
            c=total_fields-non_null_count
            d=0
            user_posts=db.query(modals.Posts).filter(modals.Posts.Username==username,modals.User.Status=="Active").all()

            for i in user_posts:
                d+=1
            infectious=db.query(modals.Infectious).filter(modals.Infectious.Status=='active').all()

            research=db.query(modals.Research).filter(modals.Research.Status=="Active").all()

            return templates.TemplateResponse('profileabout.html', context={'request': request,"user_data":user_data,"total":total_fields,"complete":non_null_count,"c":c,"research":research,"infect":infectious,"d":d}) 
    except:
        raise HTTPException(status_code=401,detail="Unauthorized")
    

@app.get("/details")
def login_page(request:Request):   
    return templates.TemplateResponse('details.html', context={'request': request})


@app.post("/signup1")
def logcheck(request:Request,db:Session=Depends(get_db),username:str=Form(...),email:str=Form(...),password:str=Form(...)):
    find=db.query(modals.User).filter(modals.User.Emailid==email,modals.User.Status=="Active").first()
    find1=db.query(modals.User).filter(modals.User.Username==username,modals.User.Status=="Active").first()
    if find is None and find1 is None:
        
        new_user=modals.User(Username=username,Emailid=email,Password=password,Status="Active",Created_at=current_datetime,Name=" ",Occupation=" ",Dob="",Location=" ",City=" ",Cover_IMG=" ",Thumb_IMG=" ",Website=" ",Aboutus=" ",Interest=" ")
        db.add(new_user)
        db.commit()
        error="Valid Creditional"
        access_token_expires = timedelta(minutes=BaseConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"user_name": username},expires_delta=access_token_expires)
        sessid = access_token
        request.session["user"] = sessid
        print(sessid)
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
        
    else:
        if find is not None:
            error= "This EmailID already exists"   
        elif find1 is not None:
            error= "This User already exists" 
        else:
            error= "This EmailID and username already exists" 

        
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)

@app.post("/login")
def logcheck(request:Request,db:Session=Depends(get_db),username:str=Form(...),password:str=Form(...)):
    find=db.query(modals.User).filter(modals.User.Username==username,modals.User.Password==password,modals.User.Status=="Active").first()
    if find is not None:
        error="Valid Creditional"
        access_token_expires = timedelta(minutes=BaseConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"user_name": find.Username},expires_delta=access_token_expires)
        sessid = access_token
        request.session["user"] = sessid
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
        
    else:
        error= "Invalid password or emailid"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    
@app.post("/details")
def update_data(request:Request,db:Session=Depends(get_db),name:str=Form(...),category:str=Form(...),certificate:UploadFile=File(...)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            
            
            if category.lower() == "doctor":
                file_type=certificate.content_type
                exit=file_type.split('/')[-1]
                image4=str(uuid.uuid4())+ '.' + str(exit)
                file_loc=f"templates/static/UploadFiles/{image4}"
                with open(file_loc,"wb+") as file_view:
                    shutil.copyfileobj(certificate.file,file_view)
                db.query(modals.User).filter(modals.User.Username == username).update({"Name": name, "Occupation": category, "Certificates": image4})
            else:
                db.query(modals.User).filter(modals.User.Username == username).update({"Name": name, "Occupation": category})            
            db.commit()
            error = "Done"
            json_compatible_item_data = jsonable_encoder(error)
            return JSONResponse(content=json_compatible_item_data)
    except JWTError:
        raise HTTPException(status_code=401,detail="Unauthorized")

@app.post("/comments")
def comments_data(request:Request,db:Session=Depends(get_db),postid:str=Form(...),inputcomment:str=Form(...)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            db_name=modals.Comments(Postid=postid,Comments=inputcomment,Username=username,Created_at=current_datetime)
            db.add(db_name)
            db.commit()
            error = "Done"
            json_compatible_item_data = jsonable_encoder(error)
            return JSONResponse(content=json_compatible_item_data)
    except JWTError:
        raise HTTPException(status_code=401,detail="Unauthorized")
    

@app.post("/details1")
def update_data(request:Request,db:Session=Depends(get_db),dob:str=Form(...),location:str=Form(...),coverimage:UploadFile=File(...),profile:UploadFile=File(...),city:str=Form(...),aboutme:str=Form(...),interests:str=Form(...),currentposition:str=Form(...),website:str=Form(...)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            find=db.query(modals.User).filter(modals.User.Username==username,modals.User.Occupation=="Doctor",modals.User.Status=="Active").first()
            file_type=coverimage.content_type
            exit=file_type.split('/')[-1]
            image4=str(uuid.uuid4())+ '.' + str(exit)
            file_loc=f"templates/static/UploadFiles/{image4}"
            with open(file_loc,"wb+") as file_view:
                shutil.copyfileobj(coverimage.file,file_view)

            file_type=profile.content_type
            exit=file_type.split('/')[-1]
            image3=str(uuid.uuid4())+ '.' + str(exit)
            file_loc=f"templates/static/UploadFiles/{image3}"
            with open(file_loc,"wb+") as file_view:
                shutil.copyfileobj(profile.file,file_view)
            verify="Not Verified"
            if find is not None:
                db.query(modals.User).filter(modals.User.Username == username).update({"Dob": dob, "Location": location, "City": city,"Cover_IMG":image4,"Thumb_IMG":image3,"Aboutus":aboutme,"Interest":interests,"Website":website,"Position":currentposition,"verify":verify})
            else:
                db.query(modals.User).filter(modals.User.Username == username).update({"Dob": dob, "Location": location, "City": city,"Cover_IMG":image4,"Thumb_IMG":image3,"Aboutus":aboutme,"Interest":interests})            
            db.commit()
            error = "Done"
            json_compatible_item_data = jsonable_encoder(error)
            return JSONResponse(content=json_compatible_item_data)
    except JWTError:
        raise HTTPException(status_code=401,detail="Unauthorized")
    
@app.post("/circle")
def comments_data(request:Request,db:Session=Depends(get_db),imageInput:UploadFile=File(...),name1:str=Form(...)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:
            file_type=imageInput.content_type
            exit=file_type.split('/')[-1]
            image4=str(uuid.uuid4())+ '.' + str(exit)
            file_loc=f"templates/static/UploadFiles/{image4}"
            with open(file_loc,"wb+") as file_view:
                shutil.copyfileobj(imageInput.file,file_view)
            db_name=modals.Circle(image=image4,name=name1,circle_status="Active",Created_at=current_datetime)
            db.add(db_name)
            db.commit()
            error = "Done"
            json_compatible_item_data = jsonable_encoder(error)
            return JSONResponse(content=json_compatible_item_data)
    except JWTError:
        raise HTTPException(status_code=401,detail="Unauthorized")
    



@app.put('/circle1/{id}')
def get_form(id:int,request:Request,db:Session = Depends(get_db)):
    try:
        token = request.session["user"]
        payload = jwt.decode(token, BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGORITHM] )
        username: str= payload.get("user_name")
        print(username)
        if username is None:
            raise HTTPException(status_code=401,detail="Unauthorized")
        else:

            db.query(modals.Circle).filter(modals.Circle.id==id).update({"circle_status": "Following"})    
            db.commit()
            error = "Done"
            json_compatible_item_data = jsonable_encoder(error)
            return JSONResponse(content=error)
    except JWTError:
        raise HTTPException(status_code=401,detail="Unauthorized")
'''admin pannel code comes here'''


