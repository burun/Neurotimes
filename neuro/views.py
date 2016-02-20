from django.shortcuts import render
from neuro.models import Category, Page, Fragment, FragmentImage
from datetime import datetime
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404


def date(request):
    category_list = Category.objects.order_by('-date')
    page_list = Page.objects.order_by('-id')

    paginator = Paginator(category_list, 12)
    page = request.GET.get('page', 1)
    try:
        category_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        category_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        category_list = paginator.page(paginator.num_pages)
    context_dict = {'categories': category_list,
                    'pages': page_list,
                    }

    return render(request, 'neuro/date.html', context_dict)


def page(request, date, id):
    page.output = Page.objects.get(category__date=date, id=id)

    try:
        page_pre = Page.objects.get(id=str(int(id) - 1))
    except:
        page_pre = {}

    try:
        page_next = Page.objects.get(id=str(int(id) + 1))
    except:
        page_next = {}
    context_dict = {'page': page.output,
                    'page_pre': page_pre,
                    'page_next': page_next,
                    'category': page.output.category}
    return render(request, 'neuro/page.html', context_dict)


def card(request):
    page_list = Page.objects.order_by('-id')
    paginator = Paginator(page_list, 9)
    page = request.GET.get('page', 1)
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


def message(request):
    context_dict = {}
    return render(request, 'neuro/message.html', context_dict)


def tag(request, tag):
    tag_list = Page.objects.filter(tags__name__in=[tag])
    context_dict = {'tags': tag_list,
                    'tag_name': tag,
                    }

    return render(request, 'neuro/tags.html', context_dict)


# Generate daily summary page
def daily(request, date):
    page.output = Page.objects.filter(category__date=date).order_by('id')
    fragment.output = Fragment.objects.filter(category__date=date).order_by('id')
    context_dict = {'pages': page.output,
                    'fragments': fragment.output,
                    'category_date': date,
                    }
    return render(request, 'neuro/daily.html', context_dict)


def fragment(request):
    fragment_list = Fragment.objects.order_by('-id')
    paginator = Paginator(fragment_list, 3)
    page = request.GET.get('page')

    try:
        fragments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        fragments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        raise Http404('<h1>Page not found</h1>')


    context_dict = {'fragments': fragments,
                    }

    return render(request, 'neuro/fragment.html', context_dict)
