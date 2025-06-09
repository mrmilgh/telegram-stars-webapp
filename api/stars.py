from fastapi import APIRouter, Request
from pydantic import BaseModel
from datetime import datetime, timedelta
from utils.security import verify_stars_init_data
#from utils.redis import get_redis_client
#from utils.hashing import hash_telegram_id_for_lookup

router = APIRouter()

class StarsPurchaseRequest(BaseModel):
    user_id: int
    credits: int
    init_data: str

@router.post("/stars/buy")
async def stars_buy(data: StarsPurchaseRequest):
    # تایید صحت امضای init_data
    if not verify_stars_init_data(data.init_data):
        return {"success": False, "error": "توکن امنیتی نامعتبر است."}

    return {
        "success": True,
        "message": f"درخواست خرید {data.credits} امتیاز با موفقیت ثبت شد."
    }
