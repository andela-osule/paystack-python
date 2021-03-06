"""Script used to define the paystack Transaction class."""

import requests

from paystackapi.constants import HEADERS, api_url
from paystackapi.base import PayStackBase


class Transaction(PayStackBase):
    """docstring for Transaction."""

    @classmethod
    def initialize(cls, reference, amount, email, plan=None):
        """
        Initialize transaction.

        Args:
            reference: unique transaction reference
            amount: amount
            email: email address
            plan: specified plan(optional)

        Returns:
            Json data from paystack API.
        """
        cls.headers = None
        response = requests.post(
            API_URL + 'transaction/initialize',
            data={"reference": reference,
                  "amount": amount,
                  "email": email,
                  "plan": plan
                  }, headers=cls.headers if cls.headers else HEADERS)

        return response.json()

    @classmethod
    def charge(cls, reference, authorization_code, email, amount):
        """
        Charge authorization.

        Args:
            reference: Unique transaction reference
            authorization_code: Authorization code for the transaction
            email: Email Address of the user with the authorization code
            amount: Amount in kobo

        Returns:
            Json data from paystack API.
        """
        cls.headers = None
        response = requests.post(
            API_URL + 'transaction/charge_authorization',
            data={"reference": reference,
                  "authorizationCode": authorization_code,
                  "email": email,
                  "amount": amount},
            headers=cls.headers if cls.headers else HEADERS,)

        return response.json()

    @classmethod
    def charge_token(cls, reference, token, email, amount):
        """
        Charge token.

        Args:
            reference: unique transaction reference
            token: paystack token
            email: Email Address
            amount: Amount in Kobo

        Returns:
            Json data from paystack API.
        """
        cls.headers = None
        response = requests.post(
            API_URL + 'transaction/charge_token',
            data={"reference": reference,
                  "token": token,
                  "email": email,
                  "amount": amount
                  },
            headers=cls.headers if cls.headers else HEADERS,)
        return response.json()

    @classmethod
    def get(cls, id):
        """
        Get a single transaction.

        Args:
            transaction_id: Transaction id(integer).

        Returns:
            Json data from paystack API.
        """
        cls.headers = None
        response = requests.get(
            api_url + 'transaction/{}'.format(id),
            headers=cls.headers if cls.headers else HEADERS,)
        return response.json()

    @classmethod
    def list(cls):
        """
        List transactions.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        cls.headers = None
        response = requests.get(
            api_url + 'transaction',
            headers=cls.headers if cls.headers else HEADERS,)
        return response.json()

    @classmethod
    def totals(cls):
        """
        Get totals.

        Args:
            No argument required.

        Returns:
            Json data from paystack API.
        """
        cls.headers = None
        response = requests.get(
            api_url + 'transaction/totals',
            headers=cls.headers if cls.headers else HEADERS,)
        return response.json()

    @classmethod
    def verify(cls, reference):
        """
        Verify transactions.

        Args:
            reference: a unique value needed for transaction.

        Returns:
            Json data from paystack API.
        """
        cls.headers = None
        response = requests.get(
            api_url + 'transaction/verify/{}'.format(reference),
            headers=cls.headers if cls.headers else HEADERS,)
        return response.json()
