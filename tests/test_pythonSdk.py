import pytest
import requests_mock
from utils.Config import Config
from zarinpal import ZarinPal
from utils.Validator import Validator



def mock_http_request(mock_adapter, method, url, response_data):
    mock_adapter.register_uri(method, url, json=response_data, status_code=200)

@pytest.fixture
def zarinpal():
    config = Config(
        merchant_id='test-merchant-id',
        access_token='test-access-token',
        sandbox=True,
    )
    return ZarinPal(config)

@pytest.fixture
def mock_http_client():
    with requests_mock.Mocker() as mock_adapter:
        yield mock_adapter

@pytest.fixture
def mock_graphql_client():
    with requests_mock.Mocker() as mock_adapter:
        yield mock_adapter

# Inquiries Tests
def test_inquire_transaction_success(zarinpal, mock_http_client):
    authority = 'A0000000000000000000000000006qpmlj9d'
    response_data = {
        'data': {
            'code': 100,
            'message': 'Operation was successful',
            'authority': authority,
            'amount': 10000,
            'ref_id': 123456789,
        }
    }
    mock_http_request(mock_http_client, 'POST', '/pg/v4/payment/inquiry.json', response_data)

    response = zarinpal.inquiries.inquire({'authority': authority})

    assert response == response_data

def test_inquire_transaction_invalid_authority(zarinpal):
    invalid_authority = 'invalid_authority'

    with pytest.raises(ValueError):
        zarinpal.inquiries.inquire({'authority': invalid_authority})


# Payments Tests
def test_create_payment_request_success(zarinpal, mock_http_client):
    payment_data = {
        'amount': 10000,
        'callback_url': 'https://yourwebsite.com/callback',
        'description': 'Test Payment',
        'mobile': '09123456789',
        'email': 'customer@example.com',
    }
    response_data = {
        'data': {
            'code': 100,
            'message': 'Operation was successful',
            'authority': 'A0000000000000000000000000006qpmlj8d',
            'fee_type': 'Merchant',
            'fee': 0,
        }
    }
    mock_http_request(mock_http_client, 'POST', '/pg/v4/payment/request.json', response_data)

    response = zarinpal.payments.create(payment_data)

    assert response == response_data

def test_create_payment_request_invalid_amount(zarinpal):
    payment_data = {
        'amount': 500,  # Less than the minimum amount
        'callback_url': 'https://yourwebsite.com/callback',
        'description': 'Test Payment',
    }

    with pytest.raises(ValueError, match="Amount must be at least 1000."):
        zarinpal.payments.create(payment_data)

def test_create_payment_request_invalid_callback_url(zarinpal):
    payment_data = {
        'amount': 10000,
        'callback_url': 'invalid_url',
        'description': 'Test Payment',
    }

    with pytest.raises(ValueError, match="Invalid callback URL format. It should start with http:// or https://."):
        zarinpal.payments.create(payment_data)


# Refunds Tests
def test_create_refund_success(zarinpal, mock_graphql_client):
    refund_data = {
        'session_id': 'session_id',
        'amount': 50000,
        'description': 'Refund for order #1234',
        'method': 'CARD',
        'reason': 'CUSTOMER_REQUEST',
    }
    response_data = {
        'data': {
            'resource': {
                'terminal_id': 'terminal_id',
                'id': 'refund_id',
                'amount': 50000,
                'timeline': {
                    'refund_amount': 50000,
                    'refund_time': '2023-01-01T00:00:00Z',
                    'refund_status': 'COMPLETED',
                },
            },
        },
    }
    
    mock_http_request(mock_graphql_client, 'POST', 'https://next.zarinpal.com/api/v4/graphql/', response_data)
    
    response = zarinpal.refunds.create(refund_data)

    assert response == response_data


def test_create_refund_invalid_method(zarinpal):
    refund_data = {
        'session_id': 'session_id',
        'amount': 50000,
        'method': 'INVALID_METHOD'
    }

    with pytest.raises(ValueError, match="Invalid method. Allowed values are \"PAYA\" or \"CARD\"."):
        zarinpal.refunds.create(refund_data)


# Verifications Tests
def test_verify_payment_success(zarinpal, mock_http_client):
    verification_data = {
        'amount': 10000,
        'authority': 'A0000000000000000000000000006qpmlj8d',
    }
    response_data = {
        'data': {
            'code': 100,
            'message': 'Verification successful',
            'card_hash': 'card-hash',
            'card_pan': '123456******1234',
            'ref_id': 987654321,
            'fee_type': 'Merchant',
            'fee': 0,
        }
    }
    mock_http_request(mock_http_client, 'POST', '/pg/v4/payment/verify.json', response_data)

    response = zarinpal.verifications.verify(verification_data)

    assert response == response_data

def test_verify_payment_invalid_amount(zarinpal):
    verification_data = {
        'amount': 500, 
        'authority': 'A0000000000000000000000000006qpmlj8d',
    }

    with pytest.raises(ValueError, match="Amount must be at least 1000."):
        zarinpal.verifications.verify(verification_data)

#Fee calcuter Test
def test_fee_calculation_success(zarinpal, mock_graphql_client):
    fee_data = {
        "amount": 5050543,
        "currency": "IRR"
    }

    expected_response = {
        "data": {
            "amount": 5050543,
            "fee": 1220,
            "fee_type": "Merchant",
            "suggested_amount": 5051763,
            "code": 100,
            "message": "Success"
        },
        "errors": []
    }

    mock_http_request(mock_graphql_client, 'POST', "/pg/v4/payment/feeCalculation.json", expected_response)

    response = zarinpal.fee.calculate(fee_data)

    assert response["data"]["amount"] == 5050543
    assert response["data"]["fee"] == 1220
    assert response["data"]["fee_type"] == "Merchant"
    assert response["data"]["suggested_amount"] == 5051763
    assert response["data"]["code"] == 100
    assert response["data"]["message"] == "Success"
    assert response["errors"] == []

# Validator Tests
def test_validate_merchant_id():
    assert Validator.validate_merchant_id('123e4567-e89b-12d3-a456-426614174000') is None
    with pytest.raises(ValueError, match="Invalid merchant_id format. It should be a valid UUID."):
        Validator.validate_merchant_id('invalid-uuid')


def test_validate_authority():
    # Test for valid authority
    assert Validator.validate_authority('A12345678901234567890123456789012345') is None
    # Test for invalid authority
    with pytest.raises(ValueError) as excinfo:
        Validator.validate_authority('invalid_authority')
    # Ensure that the correct error message is raised (supporting both ' and ")
    expected_message = "Invalid authority format. It should be a string starting with 'A' or 'S' followed by 35 alphanumeric characters."
    assert str(excinfo.value) == expected_message or str(excinfo.value) == expected_message.replace("'", "\"")


def test_validate_amount():
    Validator.validate_amount(15000)  # Valid case
    with pytest.raises(ValueError, match="Amount must be at least 1000."):
        Validator.validate_amount(500)  # Invalid case


