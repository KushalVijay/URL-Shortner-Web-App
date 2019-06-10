
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Onway
# Create your views here.
from .forms import SubmitUrlForm
class Home(View):

    def get(self,request,*args,**kwargs):
        form =  SubmitUrlForm()
        context = {
            'form':form,
        }

        return render(request,"Onway/home.html",context)

    def post(self,request,*args,**kwargs):

        form = SubmitUrlForm(request.POST)
        context = {
            'form':form,
        }
        template = "Onway/home.html"

        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj,created= list(Onway.objects.get_or_create(url=new_url))
            print(form.cleaned_data)

            print(obj.url)
            print(obj.get_short_url)
            context = {
                "object":obj,

            }


            template = "Onway/success.html"


        return render(request,template,context)

class URLRedirectView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        qs = Onway.objects.filter(shortcode__iexact=shortcode)
        if qs.count() !=1 and not qs.exists():
            raise Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)
