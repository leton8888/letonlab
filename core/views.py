from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Article, SideBar, NavBar
from .helper import generate_ss_string
import datetime
import qrcode
from cStringIO import StringIO

from .forms import LoginForm
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == 'GET':
        # form = LoginForm()
        return render_to_response('core/login.html', RequestContext(request))
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return index(request)
        else:
            return render_to_response('core/fail.html', RequestContext(request))


def logout_view(request):
    logout(request)
    return redirect('login')


def fail(request):
    content = {'id': 1}
    return render_to_response('core/fail.html', content)

@login_required
def index(request):
        # nb = NavBar.objects.get(id=1)
        # print(nb.name, nb.tittle)

    return pages(request, 1, 1)

@login_required
def pages(request, navbar_id, sidebar_id):
    
    if int(navbar_id) == 1:
        
        return shadowsocks(request, navbar_id, sidebar_id)
    elif int(navbar_id) == 2:
        
        return youtubedownloader(request, navbar_id, sidebar_id)
    else:
        
        return render_to_response('core/fail.html', RequestContext(request))

@login_required
def youtubedownloader(request, navbar_id, sidebar_id):
    nb = NavBar.objects.get(id=navbar_id)
    nb_list = NavBar.objects.all()
    sb = SideBar.objects.filter(navbar=nb).first()
    sb_list = SideBar.objects.filter(navbar=nb)

    content = {
        'nb_list': nb_list,
        'nb_id': int(navbar_id),
        'sb_list': sb_list,
        'sb_id': int(sidebar_id),
        'content': None,
    }
    return render_to_response('core/youtubedownloader.html', content)

@login_required
def shadowsocks(request, navbar_id, sidebar_id):

    nb = NavBar.objects.get(id=navbar_id)
    nb_list = NavBar.objects.all()
    sb = SideBar.objects.filter(navbar=nb).first()
    sb_list = SideBar.objects.filter(navbar=nb)
    article = Article.objects.get(sidebar=sb)

    content = {
        'nb_list': nb_list,
        'nb_id': int(navbar_id),
        'sb_list': sb_list,
        'sb_id': int(sidebar_id),
        'content': article,
    }
    return render_to_response('core/shadowsocks.html', content)

#@login_required

@login_required
def generate_qrcode(request, id):
    #print(generate_qrcode, id, 'lala')
    # if not request.user.is_authenticated():
    #   return render_to_response('core/fail.html', RequestContext(request))
    article_list = Article.objects.all()
    id_now = int(id) - 1

    ss_string = generate_ss_string(article_list[id_now].server,
                                   article_list[id_now].server_port,
                                   article_list[id_now].password,
                                   article_list[id_now].method)

    img = qrcode.make(ss_string)
    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = datetime.datetime.now()
    response['Cache-Control'] = 'max-age=31536000'
    return response
