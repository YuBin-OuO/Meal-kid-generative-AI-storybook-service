from django.utils.deprecation import MiddlewareMixin
from .models import UserSessionData

class UserSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user_key = f'user_{request.user.id}_session_data'
            user_session, created = UserSessionData.objects.get_or_create(user=request.user)
            # 세션 데이터 불러오기
            request.session.update(user_session.session_data)
    
    def process_response(self, request, response):
        if request.user.is_authenticated:
            user_key = f'user_{request.user.id}_session_data'
            user_session, created = UserSessionData.objects.get_or_create(user=request.user)
            # 현재 세션 데이터를 저장
            user_session.session_data = dict(request.session)
            user_session.save()
        return response
