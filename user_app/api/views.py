from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from user_app import models
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.exceptions import AuthenticationFailed



@api_view(['POST'])
def logout_view(request):
    
    if request.method == 'POST':
        # request.user.auth_token.delete()
        # return Response(status= status.HTTP_200_OK)
        
        if request.user.is_authenticated:
            try:
                request.user.auth_token.delete()
                return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
            except Exception as e:
                # Optional: Log the error for debugging purposes
                print(f"Error during token deletion for user {request.user}: {e}")
                # You might return a different status if token deletion specifically failed
                return Response({"detail": "Logout attempted, but token could not be deleted."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
             return Response({"detail": "No active session to log out from or already logged out."}, status=status.HTTP_200_OK)



@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user = account).key
            data['token'] = token
            
            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
            #                     'refresh': str(refresh),
            #                     'access': str(refresh.access_token),
            #                 }
            
            
            
        else:
            data =  serializer.errors
            
        return Response(data, status=status.HTTP_201_CREATED)
        
    
        
    
    