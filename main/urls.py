from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    #who we are url section
    path('about/',views.AboutView.as_view(), name="about"),
    path('board-of-directors/',views.BoardView.as_view(), name="board"),
    path('company-profile/',views.CompanyProfileView.as_view(), name="company-profile"),
    path('eax-management-team/',views.ManagementTeamView.as_view(), name="eax-management-team"),
    path('partners/',views.PartnersView.as_view(), name="partners"),
    path('faq/',views.FAQView.as_view(), name="faq"),

    #what we do url section
    path('collateral-management-services/', views.CollateralManagementServicesView.as_view(), name="collateral-management-services"),
    path('commodities-grading/', views.CommoditiesGradingView.as_view(), name="commodities-grading"),
    path('commodity-trading-models/', views.CommodityTradingModelsView.as_view(), name="commodity-trading-models"),
    path('electronic-warehouse-receipt/', views.ElectronicWarehouseReceiptView.as_view(), name="electronic-warehouse-receipt"),
    path('market-data/', views.MarketDateView.as_view(), name="market-data"),
    path('membership-application-process/', views.MembershipApplicationProcessView.as_view(), name="membership-application-process"),
    path('membership/', views.MembershipView.as_view(), name="membership"),
    path('our-services/', views.OurServicesView.as_view(), name="our-services"),
    path('regional-trade/', views.RegionalTradeView.as_view(), name="regional-trade"),
    path('risk-management/', views.RiskManagementView.as_view(), name="risk-management"),
    path('trade-settlement/', views.TradeSettlement.as_view(), name="trade-settlement"),
    path('warehouse-services-and-facilities/', views.WarehouseServicesAndFacilitiesView.as_view(), name="warehouse-services-and-facilities"),

    # market data url
    path('current-prices/', views.CurrentPricesView.as_view(), name="current-prices"),
    path('trading-schedules/', views.TradingSchedulesView.as_view(), name="trading-schedules"),

    # Commodities url

    path('commodities/', views.CommoditiesView.as_view(), name="commodities"),
    path('mixed-beans/', views.MixedBeansView.as_view(), name="mixed-beans"),
    path('paddy-rice/', views.PaddyRiceView.as_view(), name="paddy-rice"),
    path('sorghum/', views.SorghumView.as_view(), name="sorghum"),
    path('soya/', views.SoyaView.as_view(), name="soya"),
    path('wheat/', views.WheatView.as_view(), name="wheat"),
    path('white-maize/', views.WhiteMaizeView.as_view(), name="white-maize"),

     # contact , news, single pages views
    path('contact-us/', views.ContactUsView.as_view(), name="contact-us"),
    path('news/', views.NewsView.as_view(), name="news"),
    path('category/<int:category_id>/', views.NewsView.as_view(), name='blog_by_category'),
    path('blog_detail/<int:pk>/', views.SinglePageView.as_view(), name="blog_detail"),

    # partners and managemnt team detail views
    path('partner_detail/<int:pk>/', views.PartnerDetailView.as_view(), name="partner_detail"),
    path('management_detail/<int:pk>/', views.ManagementTeamDetailView.as_view(), name="management_detail"),


]
