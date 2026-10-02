import dotenv
import os
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.middleware.cors import CORSMiddleware
import jwt

dotenv.load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:8080", "http://127.0.0.1:8080", "https://decentralized-voting-system-one.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/login")
async def login(request: Request, voter_id: str, password: str):
    role = "admin" if voter_id == "admin" else "voter"
    token = jwt.encode({'password': password, 'voter_id': voter_id, 'role': role}, os.environ.get('SECRET_KEY', 'default_secret'), algorithm='HS256')
    return {'token': token, 'role': role}

@app.get("/verify")
async def verify(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization token")
    try:
        token = auth_header.split(" ")[1]
        payload = jwt.decode(token, os.environ.get('SECRET_KEY', 'default_secret'), algorithms=['HS256'])
        return {"status": "valid", "data": payload}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid authorization token")