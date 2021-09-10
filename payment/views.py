from django.shortcuts import render
from app.models import Customer, Payment, ShippingAddress
from basket.basket import Basket
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session;




# Create your views here.
@login_required
def payment(request):
    basket = Basket(request)
    if request.method =="POST":
        total_amount = basket.get_total_price()
        amount = int(float(request.POST.get("amount"))) *100
        client = razorpay.Client(auth=('rzp_test_WZAUJmKEmtiuuR','dmcfJOgTdCgB7Fmvbxe8P9ed'))
        payment = client.order.create({'amount':amount, 'currency': 'INR', 'payment_capture': '1'})
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        pcode = request.POST.get('pcode')
        payment_id = payment['id']
        order_status = payment['status']
        if order_status =="created":
            checkout = Payment(name=fname,
            amount=total_amount,
            payment_id=payment_id,
            paid=True)
            checkout.save()
    

        shippingaddress = ShippingAddress(
            first_name = fname,
            last_name = lname,
            address1 = address1,
            address2 = address2,
            city = city,
            state = state,
            country = country,
            pincode = pcode,
            email_id = email,
            contact_no = mobile)
        shippingaddress.save()

    return render(request, 'app/payment/payment.html',{'payment':payment,'name':fname,'email':email})
# return render(request, 'app/payment/payment.html')
@login_required
@csrf_exempt
def success(request):
    basket = Basket(request)
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        # basket.clear()
      
        
    return render(request, 'app/payment/success.html')