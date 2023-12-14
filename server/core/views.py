from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.serializers import IssueTokenRequestSerializer, UserSerializer, GetAnswerSerializer
from rest_framework.exceptions import NotFound
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from core.utils import get_token
from core.swagger_schema import LOG_IN_SCHEME, GET_ANSWER_SHEME, REGISTRATION_SCHEME
from core.models import Dialogs


@swagger_auto_schema(**LOG_IN_SCHEME)
@api_view(['POST'])
@require_http_methods(["POST"])
@permission_classes([AllowAny])
def log_in(request: Request) -> Response:
    """
    User login
    """
    serializer = IssueTokenRequestSerializer(data=request.data)
    if serializer.is_valid():
        val_data = serializer.validated_data
        username = val_data.get('username')
        password = val_data.get('password')

        try:
            user_id = User.objects.filter(
                username=username)[0].id
        except Exception as e:
            user_id = None
            raise Exception('User does not exists!')

        history = list(Dialogs.objects.filter(
            user_id=user_id).order_by('created_at').values('question', 'answer'))

        token = get_token(username=username,
                          password=password)

        return Response({'history': history, **token, 'userId': user_id})

    else:
        return Response(serializer.errors, status=400)


@swagger_auto_schema(**GET_ANSWER_SHEME)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@require_http_methods(["POST"])
def get_answer(request: Request) -> Response:
    """
    Get answer from model
    """
    user_id = None

    if request.method != 'POST':
        raise NotFound('Endpoint does not exists')

    try:
        user_id = request.user.id
    except Exception as e:
        raise Exception('User does not exists!')

    serializer = GetAnswerSerializer(data=request.data)
    if serializer.is_valid():
        val_data = serializer.validated_data

        # -------------псевдо код-----------
        # new_answer = model.get_answer(**val_data) #{'answer': 'new_answer.answer', 'accuracy': 'new_answer.accuracy'}
        # ----------------------------------

        # записываем в историю
        add_dialogs = Dialogs(answer='new_answer', user_id=user_id, **val_data)
        add_dialogs.save()

        return Response({'user_id': user_id, 'answer': 'new_answer.answer', 'accuracy': 'new_answer.accuracy', **val_data})
    else:
        return Response(serializer.errors, status=400)


@swagger_auto_schema(**REGISTRATION_SCHEME)
@api_view(['POST'])
@require_http_methods(["POST"])
def registration(request: Request) -> Response:
    """
    Create new user
    """

    if request.method != 'POST':
        raise NotFound('Endpoint does not exists')

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():

        # try:
        val_data = serializer.validated_data
        username = val_data.get('username')
        password = val_data.get('password')

        user = User.objects.create_user(
            username=username,
            email=val_data.get('email'),
            password=password
        )

        user.save()

        try:
            user_id = User.objects.filter(
                username=username)[0].id
        except Exception as e:
            user_id = None
            raise Exception('User does not exists!')

        history = list(Dialogs.objects.filter(
            user_id=user_id).order_by('created_at').values('question', 'answer'))

        token = get_token(username=username,
                          password=password)

        return Response({'history': history, **token, 'userId': user_id})

    else:
        return Response(serializer.errors, status=400)


# # сделать эндпоинт для получения истории в json или сsv
