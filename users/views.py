from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .permissions import IsAdminRole
from .serializers import RegistrationUserSerializer, UsersSerializer

User = get_user_model()


class RegistrationUserView(views.APIView):

    def post(self, request):
        serializer = RegistrationUserSerializer(data=request.data)
        if serializer.is_valid():
            created_user = serializer.save(
                email=self.request.data.get('email')
            )
            code = default_token_generator.make_token(created_user)
            self.__send_mail(code, created_user.email)
            return Response(serializer.data)
        return Response(serializer.errors)

    @staticmethod
    def __send_mail(code, mail_to):
        mail = EmailMessage()
        mail.subject = 'Activation code for yamdb'
        mail.body = f'{code}'
        mail.to = [mail_to]
        mail.from_email = 'test@test.ru'
        mail.send(fail_silently=False)


class AuthUserView(views.APIView):

    def post(self, request):
        data = self.request.data
        user = get_object_or_404(User, email=data.get('email'))
        if default_token_generator.check_token(
                user, data.get('confirmation_code')):
            return Response({'token': str(AccessToken.for_user(user))})
        return Response(
            {'confirmation_code': 'Incorrect registration code'},
            status=views.status.HTTP_400_BAD_REQUEST
        )


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAdminRole, permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    lookup_field = 'username'

    @action(detail=False,
            methods=['GET', 'PATCH'],
            permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        user = request.user
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        else:
            serializer = self.get_serializer(user)
        return Response(serializer.data)
