import hmac, hashlib, urllib.parse
from config import TELEGRAM_BOT_TOKEN

def verify_stars_init_data(init_data: str) -> bool:
    try:
        parsed = dict(urllib.parse.parse_qsl(init_data))
        hash_check = parsed.pop('hash', None)

        data_check_string = '\n'.join(f"{k}={v}" for k, v in sorted(parsed.items()))
        secret = hmac.new(b"WebAppData", TELEGRAM_BOT_TOKEN.encode(), hashlib.sha256).digest()
        calculated_hash = hmac.new(secret, data_check_string.encode(), hashlib.sha256).hexdigest()

        return calculated_hash == hash_check
    except:
        return False
