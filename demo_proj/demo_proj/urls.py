"""
URL configuration for demo_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from demo_app.reports import ProductSales, TotalProductSales, TotalProductSalesByCountry, MonthlyProductSales, ProductSalesPerCountryCrosstab, ProductSalesPerClientCrosstab, LastTenSales

urlpatterns = [
    path("product-sales/", ProductSales.as_view(), name="product-sales"),
    path("total-product-sales/", TotalProductSales.as_view(), name="total-product-sales"),
    path("total-product-sales-by-country/", TotalProductSalesByCountry.as_view(), name="total-product-sales-by-country"),
    path("monthly-product-sales/", MonthlyProductSales.as_view(), name="monthly-product-sales"),
    path("product-sales-per-client-crosstab/", ProductSalesPerClientCrosstab.as_view(), name="product-sales-per-client-crosstab"),
    path("product-sales-per-country-crosstab/", ProductSalesPerCountryCrosstab.as_view(), name="product-sales-per-country-crosstab"),
    path("last-10-sales/", LastTenSales.as_view(), name="last-10-sales"),

    path("admin/", admin.site.urls),
]
