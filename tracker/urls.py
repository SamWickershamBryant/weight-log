from django.urls import path
from .views import CreateWeightEntryView, WeightEntryListView

urlpatterns = [
    path('weight-entry/', CreateWeightEntryView.as_view(), name='create-weight-entry'),
    path('all-weights/', WeightEntryListView.as_view(), name='all_weights'),
]
