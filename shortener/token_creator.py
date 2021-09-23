from hashids import Hashids
from main.constants import ALPHABET
from .models import URL
from random import choice
from django.core.exceptions import ObjectDoesNotExist


class TokenCreator:

    @staticmethod
    def get_token(salt, length):
        token = Hashids(salt=salt,
                        min_length=length).encode(len(salt))
        if len(token) != length:
            return TokenCreator.__correct_token(token[:length])
        return token

    @staticmethod
    def __correct_token(token):
        for char in token:
            for letter in ALPHABET:
                new_token = token.replace(char, letter, 1)
                try:
                    URL.objects.get(token=new_token)
                except ObjectDoesNotExist:
                    return new_token
        return TokenCreator.__correct_token(token + choice(ALPHABET))
