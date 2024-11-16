from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # myproject/views.py에서 가져오기

urlpatterns = [
    path('admin/', admin.site.urls),  # Django 관리자 페이지
    path('', views.index, name='index'),  # 루트 URL에 React 연결
    path('pdf/', include('pdf_processor.urls')),  # PDF 처리 URL
    path('handler/', include('pdfhandler.urls')),  # pdfhandler.urls 연결
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
