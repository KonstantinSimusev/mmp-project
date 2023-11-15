from rest_framework.routers import SimpleRouter
from .views import AreaView, ReportView, ProfessionView

router = SimpleRouter()
router.register('api/area', AreaView)
router.register('api/report', ReportView)
router.register('api/profession', ProfessionView)

urlpatterns = []
urlpatterns += router.urls
