from django.shortcuts import render
from neuro.models import Category, Page
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def date(request):
    category_list = Category.objects.order_by('-date')
    page_list = Page.objects.order_by('-id')
    context_dict = {'categories': category_list,
                    'pages': page_list,
                    }

    return render(request, 'neuro/date.html', context_dict)


def page(request, date, id):
    page.output = Page.objects.get(category__date=date, id=id)
    context_dict = {'page': page.output,
                    'category': page.output.category}
    return render(request, 'neuro/page.html', context_dict)


def card(request):
    page_list = Page.objects.order_by('-id')
    paginator = Paginator(page_list, 9)
    page = request.GET.get('page')
    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cards = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cards = paginator.page(paginator.num_pages)
    context_dict = {'cards': cards}

    return render(request, 'neuro/card.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'neuro/about.html', context_dict)
