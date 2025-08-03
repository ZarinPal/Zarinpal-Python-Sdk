import re
from typing import List, Optional, Dict


class Validator:
    
    @staticmethod
    def validate_currency(currency: str | None) -> None:
        valid_currencies = ["IRR", "IRT"]
        if currency is not None and currency not in valid_currencies:
            raise ValueError('Invalid currency format. Allowed values are "IRR" or "IRT".')
        
    @staticmethod
    def validate_merchant_id(merchant_id: Optional[str]) -> None:
        if (
            merchant_id is None or
            not re.match(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$', merchant_id)
        ):
            raise ValueError('Invalid merchant_id format. It should be a valid UUID.')
   
    @staticmethod
    def validate_authority(authority: str) -> None:
        if not re.match(r'^[AS][0-9a-zA-Z]{35}$', authority):
            raise ValueError('Invalid authority format. It should be a string starting with \'A\' or \'S\' followed by 35 alphanumeric characters.')
        
    @staticmethod
    def validate_amount(amount: float, min_amount: float = 10000) -> None:
        if amount < min_amount:
            raise ValueError(f'Amount must be at least {min_amount}.')

    @staticmethod
    def validate_callback_url(callback_url: str) -> None:
        if not re.match(r'^https?:\/\/.*$', callback_url):
            raise ValueError('Invalid callback URL format. It should start with http:// or https://.')

    @staticmethod
    def validate_mobile(mobile: Optional[str]) -> None:
        if mobile is not None and not re.match(r'^09[0-9]{9}$', mobile):
            raise ValueError('Invalid mobile number format.')

    @staticmethod
    def validate_email(email: Optional[str]) -> None:
        if email is not None and not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
            raise ValueError('Invalid email format.')

    @staticmethod
    def validate_currency(currency: Optional[str]) -> None:
        valid_currencies = ['IRR', 'IRT']
        if currency is not None and currency not in valid_currencies:
            raise ValueError('Invalid currency format. Allowed values are "IRR" or "IRT".')

    @staticmethod
    def validate_wages(wages: Optional[List[Dict[str, str]]]) -> None:
        if wages is not None:
            for wage in wages:
                if not re.match(r'^[A-Z]{2}[0-9]{2}[0-9A-Z]{1,30}$', wage['iban']):
                    raise ValueError('Invalid IBAN format in wages.')
                if wage['amount'] <= 0:
                    raise ValueError('Wage amount must be greater than zero.')
                if len(wage['description']) > 255:
                    raise ValueError('Wage description must be provided and less than 255 characters.')

    @staticmethod
    def validate_terminal_id(terminal_id: str) -> None:
        if not terminal_id:
            raise ValueError('Terminal ID is required.')

    @staticmethod
    def validate_filter(filter: Optional[str]) -> None:
        valid_filters = ['PAID', 'VERIFIED', 'TRASH', 'ACTIVE', 'REFUNDED']
        if filter is not None and filter not in valid_filters:
            raise ValueError('Invalid filter value.')

    @staticmethod
    def validate_limit(limit: Optional[int]) -> None:
        if limit is not None and limit <= 0:
            raise ValueError('Limit must be a positive integer.')

    @staticmethod
    def validate_offset(offset: Optional[int]) -> None:
        if offset is not None and offset < 0:
            raise ValueError('Offset must be a non-negative integer.')

    @staticmethod
    def validate_card_pan(card_pan: Optional[str]) -> None:
        if card_pan is not None and not re.match(r'^[0-9]{16}$', card_pan):
            raise ValueError('Invalid card PAN format. It should be a 16-digit number.')

    @staticmethod
    def validate_session_id(session_id: str) -> None:
        if not session_id:
            raise ValueError('Session ID is required.')

    @staticmethod
    def validate_method(method: str) -> None:
        valid_methods = ["PAYA","CARD"]
        if method not in valid_methods:
            raise ValueError('Invalid method. Allowed values are "PAYA" or "CARD".')

    @staticmethod
    def validate_reason(reason: str) -> None:
        valid_reasons = [
            'CUSTOMER_REQUEST',
            'DUPLICATE_TRANSACTION',
            'SUSPICIOUS_TRANSACTION',
            'OTHER'
        ]
        if reason not in valid_reasons:
            raise ValueError('Invalid reason. Allowed values are "CUSTOMER_REQUEST", "DUPLICATE_TRANSACTION", "SUSPICIOUS_TRANSACTION", or "OTHER".')