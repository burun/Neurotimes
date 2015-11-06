from django.contrib.syndication.views import Feed
from neuro.models import Category, Page

# RSS
class LatestPosts(Feed):
    title = "New Post on NeuroTimes"
    link = "/feeds"

    def items(self):
        return Page.objects.order_by('-id')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return "http://neurotim.es/page/" + str(item.category.date) + "/" + str(item.id) + "/"
