from django.shortcuts import render
from neuro.models import Category, Page
from datetime import datetime


def date(request):
    category_list = Category.objects.order_by('-date')
    page_list = Page.objects.all()
    context_dict = {'categories': category_list,
                    'pages': page_list,
                    }

    return render(request, 'neuro/date.html', context_dict)


def page(request, date, order):
    page.output = Page.objects.get(category__date=date, order=order)
    context_dict = {'page': page.output,
                    'category': page.output.category}
    return render(request, 'neuro/page.html', context_dict)


def card(request):
    page_list = Page.objects.order_by('-date')
    context_dict = {'pages': page_list,
                    }
    return render(request, 'neuro/card.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'neuro/about.html', context_dict)
