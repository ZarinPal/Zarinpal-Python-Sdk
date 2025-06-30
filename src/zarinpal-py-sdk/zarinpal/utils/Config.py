from typing import Optional


class Config:
    def __init__(self, sandbox: Optional[bool] = None, merchant_id: Optional[str] = None, access_token: Optional[str] = None):
        self.sandbox = sandbox
        self.merchant_id = merchant_id
        self.access_token = access_token