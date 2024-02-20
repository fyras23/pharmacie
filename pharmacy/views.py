
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pharmacy.models import Medicament,Typee
from django.contrib.auth.models import User
from pharmacy.forms import FormUser
from pharmacy.forms import formConnection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.models import LogEntry
from django.core.exceptions import ObjectDoesNotExist, ValidationError

#<--------------------for the med------------------------------------->
@login_required(login_url='connect')
def index(request):
 med = Medicament.objects.all().values()
 type = Typee.objects.all().values()
 template = loader.get_template('home.html')
 context = {
 'med': med,
 'type':type,
 }
 return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def del_med(request, id):
 med = Medicament.objects.get(id=id)
 med.delete()
 return HttpResponseRedirect(reverse('medicaments'))

@login_required(login_url='connect')
def update_med(request, id):
 med = Medicament.objects.get(id=id)
 type = Typee.objects.all().values()
 template = loader.get_template('updateMed.html')
 context = {
 'med': med,
 'type':type, }
 return HttpResponse(template.render(context, request))


def update_med_aplly(request, id):
    if request.method == 'POST':
        try:
            n = request.POST['name']
            p = request.POST['price']
            q = request.POST['quantity']
            d = request.POST['expirationDate']
            t = request.POST['type']
        except KeyError as e:
            return HttpResponse(f'Missing field: {e}', status=400)
        
        try:
            tp = Typee.objects.get(id=t)
        except ObjectDoesNotExist:
            return HttpResponse('Invalid type', status=400)
        
        try:
            medc = Medicament.objects.get(id=id)
            medc.name = n
            medc.price = p
            medc.quantity = q
            medc.expirationDate = d
            medc.typee = tp
            medc.full_clean()  # validate model fields before saving
            medc.save()
        except (ObjectDoesNotExist, ValidationError) as e:
            return HttpResponse(str(e), status=400)
        else:
            return HttpResponseRedirect(reverse('medicaments'))

@login_required(login_url='connect')
def add(request):
    type = Typee.objects.all().values()
    template = loader.get_template('addMed.html')
    context = {
    'type': type,
    }
    return HttpResponse(template.render(context, request))


def add_med(request):
 n = request.POST['name']
 q = request.POST['quantity']
 p = request.POST['price']
 da = request.POST['expirationdate']
 c = request.POST['type']
 type = Typee.objects.get(id=c)
 med = Medicament(name=n, quantity=q, price=p, expirationDate=da,typee=type)
 med.save()
 return HttpResponseRedirect(reverse('medicaments')) 
#<------------------------------------------------------------------------>



#<----------------------------for the type-------------------------------->
@login_required(login_url='connect')
def skills(request):
    med = Medicament.objects.all().values()
    type=Typee.objects.all().values()
    template = loader.get_template('type.html')
    context = {
    'med': med,
    'type':type, 
        }
    return HttpResponse(template.render(context, request))

@login_required(login_url='connect')
def del_type(request, id):
 type = Typee.objects.get(id=id)
 type.delete()
 return HttpResponseRedirect(reverse('type'))


@login_required(login_url='connect')
def update_type(request, id):
 type = Typee.objects.get(id=id)
 
 template = loader.get_template('updateType.html')
 context = {

 'type':type, }
 return HttpResponse(template.render(context, request))



def update_type_aplly(request, id):
 n = request.POST['Ntype']
 d= request.POST['descri']

 type = Typee.objects.get(id=id)
 type.Ntype = n
 type.descri = d

 type.save()
 return HttpResponseRedirect(reverse('type'))


@login_required(login_url='connect')
def addType(request):
    type = Typee.objects.all().values()
    template = loader.get_template('addType.html')
    context = {
    'type': type,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='connect')
def add_type(request):
 n = request.POST['Ntype']
 d = request.POST['descri']
 
 t = Typee(Ntype=n, descri=d)
 t.save()
 return HttpResponseRedirect(reverse('type'))

#<--------------------------------------------------------------------->


#<----------------------------for the user--------------------------->

@login_required(login_url='connect')
def list_users(request):
 users = User.objects.all().values()
 template = loader.get_template('user.html')
 context = {
 'users':users,
 }
 return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def del_user(request, id):
 user = User.objects.get(id=id)
 user.delete()
 return HttpResponseRedirect(reverse('users'))
#<--------------------------------------------------------------------->




#<----------------------------for login-------------------------------->
@login_required(login_url='login')
def create_compte(request):
 user_form = FormUser ()
 return render(request, 'createUser.html', {'user_form' :user_form})




def create_user_action(request):
    adrEmail = request.POST['email']
    username = request.POST['login']
    password = request.POST['password']
    confirm = request.POST['confirm']
    Lname = request.POST['lastName']
    fName = request.POST['firstName']
    if (password==confirm):
        user = User.objects.create_user(username, adrEmail, password)
        user.first_name = fName
        user.last_name = Lname
        user.save()
        return HttpResponseRedirect(reverse('users'))
    else:
        print ("Password and confirmation password are not identical")
        return HttpResponseRedirect(reverse('create_account'))




#<------------------------the log in and out---------------------------------------->

def connect (request):
    connect_form = formConnection ()
    return render(request, 'connection.html', {'connect_form' :connect_form,'error':False})


def signIn(request):
 username = request.POST['login']
 password = request.POST['password']
 user = authenticate(request, username=username,password=password)
 if user is not None:
    login(request, user)
    request.session['username'] = username
    return HttpResponseRedirect(reverse('medicaments'))

 else:
    print("Login or password is is incorrect")
    return render(request,'connection.html', {'error':True,})
    return HttpResponseRedirect(reverse('connect'))

def signOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('connect'))



#<---------------------------------------------------------------------------------------------------------->





#<---------------------------------------get history------------------------------------------------------------>
""" def change_history(request):
    log_entries = LogEntry.objects.filter(content_type__model='Medicament')
    return render(request, 'change_history.html', {'log_entries': log_entries}) """







""" def change_history(request, object_id):
    instance = Medicament.objects.get(id=object_id)
    history = instance.history.all()
    return render(request, 'change_history.html', {'history': history}) """


@login_required(login_url='login')
def change_history(request):
    changes = []
    for obj in Medicament.objects.all():
        for change in obj.history.all():
            changes.append((obj.id, change.history_type,  change.history_date, change.history_user))
    return render(request, 'change_history.html', {'changes': changes})





from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def add_hours(value, hours):
    return value + timedelta(hours=hours)
