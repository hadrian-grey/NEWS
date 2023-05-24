from django import template
from main.models import New,Category


register = template.Library()



@register.inclusion_tag('breaking.html',takes_context=False)
def breaking_news():
    news=New.objects.filter(breaking=True)
    return{'news':news}


@register.inclusion_tag('categories.html',takes_context=False)
def categories():
    categories=Category.objects.all()
    return{'categories':categories}



@register.inclusion_tag('trending.html',takes_context=False)
def trending_news():
    news=New.objects.filter(trending=True).order_by('-id')[:5]
    return{'trends':news}
