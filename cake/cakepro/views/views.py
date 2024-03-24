from django.shortcuts import render,redirect
from .models import *
from .models import UserCredentials
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib import messages  



 
# Create your views here.
def list(request):
    all=Cakes.objects.filter(status=1)
    print(all)
    cont={
       'all':all 
    }
    return render(request,'show.html',cont)
def cakes(request):
    if request.method=='POST':
         
        a=request.POST.get('name')
        

        weight_strings = request.POST.getlist('weight')
        g = ', '.join([str(item) for item in weight_strings])
        c=request.POST.get('cost')
        client=Cakes(name=a,weight=g,cost=c)
        print(client)
        client.save()
        return redirect('list')
    return render(request,'show.html')
def cakeup(request,id):
        if request.method=='POST':
             a=request.POST.get('name')
             weight_strings = request.POST.getlist('weight')
             b = ', '.join([str(item) for item in weight_strings])
             c=request.POST.get('cost')
             client=Cakes.objects.get(id=id)
             client.name=a
             client.weight=b
             client.cost=c
             client.save()
             return redirect('list')
        else:
            all=Cakes.objects.get(id=id)
            context={
                  'all':all
             }
            return render(request,'edit.html',context)
def delete(request,id):               
    client=Cakes.objects.get(id=id)
    client.status=False
    client.save()
    return redirect('list')

# def customer(request):
#     customer=Customer.objects.all()
#     cont={
#        'customer':customer
#     }
#     return render(request,'show.html',cont)

def showviews(request):
    
    customerdetail=Customer.objects.all()
    cont={
       'customerdetail':customerdetail
    }
    return render(request,'view.html',cont)

def addcust(request):
    customer=Customer.objects.all()
    cont={
       'customer':customer
    }
    return render(request,'addcustomer.html',cont)

def customeradd(request):
    if request.method=='POST':
         
        a=request.POST.get('name')
        b= request.POST.getlist('mob')
        g = ', '.join([str(item) for item in b])
        c=request.POST.get('address')
        client=Customer(name=a,mob=g,address=c)
        client.save()
        return redirect('showviews')
    return render(request,'addcustomer.html')

def customerdelete(request,id):               
    customerdelete=Customer.objects.get(id=id)
    customerdelete.delete()
    return redirect('showviews')

def customerupdate(request,id):
    if request.method=='POST':
         
        a=request.POST.get('name')
        b= request.POST.getlist('mob')
        g = ', '.join([str(item) for item in b])
        c=request.POST.get('address') 
        cust=Customer.objects.get(id=id)
        cust.name=a
        cust.mob=g
        cust.address=c 
        cust.save()
        return redirect('showviews')
    else:
        
        return render(request,'customerupdate.html')
    
def cutomerup(request,id):
            customer=Customer.objects.get(id=id)
            context={
            'customer':customer
            }
            return render(request,'customerupdate.html',context)

    
    
def customer_order(request):
    if request.method == 'POST':
        print('POST Method')
        a = request.POST.getlist('Cakes')
        b = request.POST.get('Customer')
        c = request.POST.getlist('Quantity')
        d = request.POST.getlist('Amount')
        e = request.POST.get('totalAmount')
        print(len(a),'length.....')
        for i in range(len(a)):
 
            h=int(a[i])
            Order.objects.create(Cakes_id=h, Customer_id=b, Quantity=c[i], Amount=d[i],TotalAmount=e)
        
        # cakeinstance=Cakes.objects.get('name=a')
        # print(cakeinstance)
        # if cakeinstance==None:
        #     pass
        # elif cakeinstance!=None:
        #     order = Order.objects.create(Cakes=cakeinstance, Customer=b, Quantity=c, Amount=d, TotalAmount=e)
        #     print(order)
        #     order.save()
        
        print('Cakes', h)
        print('Customer', b)
        print('Quantity', c[i])
        print('Amount', d[i])
        print('TotalAmount', e)
        return redirect('orderdetails')
    
    # Assuming you have the Cakes, Customer, and Order models
    cakes = Cakes.objects.filter(status=1)
    customer = Customer.objects.all()
    orderfield = Customer.objects.all()
    return render(request, 'order.html', {'cakes': cakes, 'customer': customer, 'orderfield': orderfield}) 

def orderdetails(request):
    orderfield=Order.objects.all()
    return render(request,'orderdetails.html',{'orderfield':orderfield})

def orderfield(request):
    orderfield=Order.objects.all()
    return render(request,'order.html',{'orderfield':orderfield})

def customerviews(request):
    orderfield=Customer.objects.all()
    return render(request,'customerviews.html',{'orderfield':orderfield})

def TotalAmount(request):
    if(request.method == "POST"):
        noofcakes = request.POST.get('quantity')
        print(noofcakes)
        cakeid = request.POST.get('cakeid')
        
        cakecost = Cakes.objects.get(id=cakeid)
        print(cakecost,'joy')
       
        cakepercost = int(cakecost.cost)
        print(cakepercost,'cakepercost')
        totalamount = int(noofcakes)*int(cakecost.cost)
        print(totalamount)
         
        return JsonResponse({'totalamount':totalamount,'cakepercost':cakepercost})

def delete_order(request,id):
    customer_order=Order.objects.get(id=id)
    customer_order.delete()
    return redirect('orderdetails')

def viewsorder(request,pk):
    if(request.method == "GET"):
        print('View Page',pk)
      
        customerorder = Order.objects.filter(Customer_id=pk) 
        print(customerorder,'kkiop...') 
        # total_amount = Order.objects.filter(customer_id=customerorder).aggregate(total_amount=Sum('amount'))['total_amount']
        totalhistoryamount = customerorder.aggregate(totalhistoryamount=Sum('Amount'))['totalhistoryamount']

        print(totalhistoryamount,'komi')

        orderfield = Customer.objects.get(id=pk)
        print(orderfield),'prid.........'
        print('customerorder',customerorder)
        context = {'customerorder':customerorder,'orderfield':orderfield,"totalhistoryamount":totalhistoryamount}
        return render(request, 'customerorder.html',context)

     

def dash(request):
                 return render(request,'dash.html')

def signup(request):
     if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']
        #   user=UserCredentials.objects.create(username=username,password=password)
        #   return redirect('user_login')
          if UserCredentials.objects.filter(password=password,username=username).exists():
                messages.error(request, 'Username is already taken. Please choose a different ra jeffa ')
                return redirect('signup')
          else:
                user=UserCredentials.objects.create(password=password, username=username)
                return redirect('user_login')

                

     return render(request, 'signup.html')

def user_login(request):
     if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            try:
                 user=UserCredentials.objects.get(username=username)
                 if user.password==password:
                        return redirect('dash')
                 else:
                        return render(request,'login.html',{'error_message':'Invalid password ra jeffa'})
            except UserCredentials .DoesNotExist:
                                         return render(request,'login.html',{'error_message':'Invalid password ra jeffa'})
     else:
          return render(request, 'login.html')    
            
            
            
            
            
                 

                    
                 
            
            
     