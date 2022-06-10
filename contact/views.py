from django.shortcuts import render,redirect
from.models import Contact
# Create your views here.
def index(request):    
    contacts= Contact.objects.all() # used to show all details contained in the model Contact
   
    search_input=request.GET.get('search_area')
    if search_input:
        contacts=Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts=Contact.objects.all()
        search_input =''

    context={'contacts':contacts, 'search_input':search_input}
    return render(request, 'index.html', context)

def addContact(request):


    if request.method=='POST':
        new_contact= Contact(
            
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],            
            phone_number=request.POST['phone-number'],
            address=request.POST['address']

        )
        
        new_contact.save()
        return redirect('/') # we redirect using the value in path('value')
    return render(request, 'edit.html')

def contactProfile(request, pk):
    
    details=Contact.objects.get(id=pk)
    # NB when using id=pk in 'contact':details , we must use the model name 
    # in small letters i.e the model is Contact and small letters are contact
    context={'contact':details} 
    return render(request, 'contact-profile.html', context)

def editContact(request, pk):
    contact=Contact.objects.get(id=pk)
    
    # NB when using id=pk in 'contact':details , we must use the model name 
    # in small letters i.e the model is Contact and small letters are contact
    if request.method=='POST':
 #N.B contact.full_name etc is the value in our model and
 #  request.POST['fullname'] etc is the name in our template in the form
        contact.full_name=request.POST['fullname']
        contact.phone_number=request.POST['phone-number']         
        contact.relationship=request.POST['relationship']
        contact.email=request.POST['email']
        contact.address=request.POST['address']
        contact.save()

        # we use  +str(contact.id) in return redirect for url
        #  where we are retrieving each item in a model
        # we use

        return redirect('/profiles/' +str(contact.id))

    context={'contact':contact} 
    return render(request, 'update-contact.html', context)

def deleteContact(request,pk):

    contact=Contact.objects.get(id=pk)

    if request.method=='POST':
        contact.delete()

        return redirect('/')

    context={'contact': contact}
    return render(request, 'delete.html', context)

