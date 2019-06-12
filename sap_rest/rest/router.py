from rest_framework import routers
from sap_rest.rest.views import FolderViewSet, QuestionViewSet, ResourceViewSet

router = routers.DefaultRouter()
router.register(r'folders', FolderViewSet, base_name='folder')
router.register(r'questions', QuestionViewSet, base_name='question')
router.register(r'resources', ResourceViewSet, base_name='resource')
