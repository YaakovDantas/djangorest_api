from django.conf.urls import include, url
from portfolios.views import PortfolioListView ,PortfolioView

urlpatterns = [
   
   url(r'^portfolios/$' , PortfolioListView.as_view(), name="portifolios"),
   url(r'^portfolios/(?P<pk>\d+)/$', PortfolioView.as_view(), name="get_portfolio")
]
