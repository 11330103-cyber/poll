from django.shortcuts import render
from .models import Poll,Option
from django.views.generic import ListView,DetailView,RedirectView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
    #redirect_url = "https://www.youtube.com/?authuser=0"
    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id = self.kwargs['oid'])
        option.votes +=1
        option.save()
 
        #return "/poll/{}/".format(option.poll_id)
        #return f"/poll/{option.poll_id}"
        #return reverse('poll_view',args=[option.poll_id])
        return reverse('poll_view',kwargs={'pk':option.poll_id})
    
class pollcreate(LoginRequiredMixin,CreateView):
    model=Poll
    fields='__all__'#['subject','desc']
    success_url=reverse_lazy('poll_list')

class polledit(LoginRequiredMixin,UpdateView):
    model=Poll
    fields='__all__'#['subject','desc']

    def get_success_url(self):
        return reverse('poll_view',kwargs={'pk':self.object.id})#改某個主題，到某個主體的頁面

class optioncreate(LoginRequiredMixin,CreateView):
    model=Option
    fields=['title']

    def form_valid(self, form):
        form.instance.poll_id=self.kwargs['pid']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk': self.kwargs['pid']})
    
class optionedit(LoginRequiredMixin,UpdateView):
    model=Option
    fields=['title']
    pk_url_kwarg='oid'  #讓他去讀取 oid

    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk': self.object.poll_id}) #self.object代表目前在操作的那筆紀錄
    
class polldelete(LoginRequiredMixin,DeleteView):
    model=Poll
    success_url=reverse_lazy('poll_list')

class optiondelete(LoginRequiredMixin,DeleteView):
    model=Option
    
    def get_success_url(self):
        return reverse_lazy('poll_view',kwargs={'pk': self.object.poll_id})

