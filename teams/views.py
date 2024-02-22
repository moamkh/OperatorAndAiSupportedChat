from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated,AllowAny)
from rest_framework.authentication import BasicAuthentication

from users.authentication import BearerTokenAuthentication