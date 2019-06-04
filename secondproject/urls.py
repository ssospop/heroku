from django.contrib import admin
from django.urls import path, include # include : 따로 blog 앱 폴더에서 blog와 관련된 url을 관리 하겠다는 것
import blog.views
# blog 폴더의 views 
import portfolio.views
#밑 두개는 그냥 외워
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/', include('blog.urls')), #blog 폴더에 있는 urls를 include해오고, 그 url형식은 blog/ 일 것이다
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#blog.views.create : blog 앱 폴더 안의 views.py 파일 안의 create함수를 실행 시킬 거야 !
