from django import template
from main.models import News,Category


register = template.Library()



@register.inclusion_tag('breaking.html',takes_context=False)
def breaking_news():
    news=News.objects.filter(breaking=True)
    return{'news':news}


@register.inclusion_tag('categories.html',takes_context=False)
def categories():
    categories=Category.objects.all()
    return{'categories':categories}