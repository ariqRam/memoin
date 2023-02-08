from fastapi import FastAPI
import motor.motor_asyncio

app = FastAPI()
db_client = motor.motor_asyncio.AsyncIOMotorClient()
db = db_client['memoin']

@app.get("/")
async def home():
    result = await db.user.find_one({"username": "azhar"})
    username = result['username'] if result else "Username not found"
    return f"Hello, {username}"