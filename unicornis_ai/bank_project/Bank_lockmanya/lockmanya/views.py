from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import ProductForm
from .models import Product
from django.contrib import messages
from django.utils.dateparse import parse_date
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import Campaign

def signup(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('password1')
       pass2=request.POST.get('password2')
       if pass1!=pass2:
           return HttpResponse(request,"incorrect")
       else:

           my_user= User.objects.create_user(uname,email,pass1)
           my_user.save()
           return redirect('index')
    return render(request,'login.html')


def index(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse(request,"invalid")
    return render(request, 'signup.html')


def Dashboard(request):
    return render(request,'dashboard.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        product_name = request.POST.get('name')

        # Check if the product with the same name already exists
        if Product.objects.filter(name=product_name).exists():
            messages.error(request, 'A product with the same name already exists.')
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Product added successfully!')
                return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})
    

def Report(request):
    return render(request, 'Report.html')

def Setting(request):
    return render(request, 'Setting.html')

def View(request):
    return render(request, 'View.html')

def product_list(request):
    products = Product.objects.all()

    # Get date range from GET parameters
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')

    # If both dates are provided, filter the products based on date_added
    if from_date and to_date:
        from_date = parse_date(from_date)
        to_date = parse_date(to_date)
        products = products.filter(date_added__range=[from_date, to_date])

    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product removed successfully!')
        return redirect('product_list')
    return render(request, 'product_list.html')


def profile(request):
    return render(request,'profile.html')


from django.shortcuts import render, redirect
from .models import Campaign
from .forms import CampaignForm

# Create Campaign View
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_campaigns')
    else:
        form = CampaignForm()
    return render(request, 'create_campaign.html', {'form': form})

# View Campaigns View
def view_campaigns(request):
    created_campaigns = Campaign.objects.filter(status='created')
    running_campaigns = Campaign.objects.filter(status='running')
    closed_campaigns = Campaign.objects.filter(status='closed')

    context = {
        'created_campaigns': created_campaigns,
        'running_campaigns': running_campaigns,
        'closed_campaigns': closed_campaigns
    }
    return render(request, 'view_campaigns.html', context)


def report(request):
    return render(request,'report.html')



from django.shortcuts import render
from .models import Audience

from django.db.models import Q

def search_view(request):
    products = Product.objects.all()

   

    # Get name search query from GET parameters
    name_query = request.GET.get('name')

    # If both dates are provided, filter the products based on date_added
    
        

    # If a name search query is provided, filter products by name
    if name_query:
        products = products.filter(name__icontains=name_query)

    context = {
        'products': products,
        'name_query': name_query,
    }
    return render(request, 'search.html', context)



def setting(request):
    return render(request,'setting.html')

def notification(request):
    return render(request,'notification.html')