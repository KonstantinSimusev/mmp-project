from rest_framework.routers import SimpleRouter
from .views import EmployeeView, TimeSheetView

router = SimpleRouter()
router.register('api/employee', EmployeeView)
router.register('api/timesheet', TimeSheetView)

urlpatterns = []
urlpatterns += router.urls
