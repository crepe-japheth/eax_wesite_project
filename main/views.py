from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category, Partner, ManagementTeamMember

class IndexView(TemplateView):
    template_name = "main/index.html"


class AboutView(TemplateView):
    template_name = "main/who_are_we/about.html"


class BoardView(TemplateView):
    template_name = "main/who_are_we/board-of-directors.html"

    

class CompanyProfileView(TemplateView):
    template_name = "main/who_are_we/company-profile.html"





class FAQView(TemplateView):
    template_name = "main/who_are_we/faq.html"



# What we do views 


class CollateralManagementServicesView(TemplateView):
    template_name = "main/what_we_do/collateral-management-services.html"


class CommoditiesGradingView(TemplateView):
    template_name = "main/what_we_do/commodities-grading.html"


class CommodityTradingModelsView(TemplateView):
    template_name = "main/what_we_do/commodity-trading-models.html"


class ElectronicWarehouseReceiptView(TemplateView):
    template_name = "main/what_we_do/electronic-warehouse-receipt-financing.html"


class MarketDateView(TemplateView):
    template_name = "main/what_we_do/market-data.html"


class MembershipApplicationProcessView(TemplateView):
    template_name = "main/what_we_do/membership-application-process.html"



class MembershipView(TemplateView):
    template_name = "main/what_we_do/membership.html"


class OurServicesView(TemplateView):
    template_name = "main/what_we_do/our-services.html"


class RegionalTradeView(TemplateView):
    template_name = "main/what_we_do/regional-trade.html"



class RiskManagementView(TemplateView):
    template_name = "main/what_we_do/risk-management.html"


class TradeSettlement(TemplateView):
    template_name = "main/what_we_do/trade-settlement.html"


class WarehouseServicesAndFacilitiesView(TemplateView):
    template_name = "main/what_we_do/warehouse-services-and-facilities.html"


# Market Data View

class CurrentPricesView(TemplateView):
    template_name = "main/market_data/current-prices.html"


class TradingSchedulesView(TemplateView):
    template_name = "main/market_data/trading-schedules.html"

# Commodities View

class CommoditiesView(TemplateView):
    template_name = "main/commodities/commodities.html"


class MixedBeansView(TemplateView):
    template_name = "main/commodities/mixed-beans.html"


class PaddyRiceView(TemplateView):
    template_name = "main/commodities/paddy-rice.html"


class SorghumView(TemplateView):
    template_name = "main/commodities/sorghum.html"


class SoyaView(TemplateView):
    template_name = "main/commodities/soya.html"


class WheatView(TemplateView):
    template_name = "main/commodities/wheat.html"


class WhiteMaizeView(TemplateView):
    template_name = "main/commodities/white-maize.html"

 # contact , news, single pages views


class ContactUsView(TemplateView):
    template_name = "main/contact-us.html"


class NewsView(ListView):
    model =  BlogPost
    context_object_name = "posts"
    template_name = "main/news.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get("category_id")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["active_category"] = self.kwargs.get("category_id")
        return context


class SinglePageView(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "main/single-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
class PartnersView(ListView):
    model =  Partner
    context_object_name = "partners"
    template_name = "main/who_are_we/partners.html"
    paginate_by = 10

class PartnerDetailView(DetailView):
    model = Partner
    context_object_name = "partner"
    template_name = "main/partners_detail.html"


class ManagementTeamView(ListView):
    model =  ManagementTeamMember
    context_object_name = "team_members"
    template_name = "main/who_are_we/eax-management-team.html"

class ManagementTeamDetailView(DetailView):
    model = ManagementTeamMember
    context_object_name = "team_member"
    template_name = "main/management_team_detail.html"