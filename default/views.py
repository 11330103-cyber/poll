from django.shortcuts import render
from .models import Poll,Option
from django.views.generic import ListView,DetailView,RedirectView

# Create your views here.
def poll_list(req):
    polls = Poll.objects.all()
    return render(req,"default/list.html",{'poll_list':polls,'msg':'Hello!'})

class polllist(ListView):
    model = Poll
    #會去找 defult/poll_list.html

class pollview(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        option_list = Option.objects.filter(poll_id=self.object.id)
        ctx['option_list']=option_list.filter(poll_id=self.object.id)

        return ctx
class pollvote(RedirectView):
    pass