from django.shortcuts import render , redirect , get_object_or_404
from datetime import datetime
from django.http import HttpResponse
from atbadminton.models import *
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate , login
from django.contrib import messages
from django.db.models import Q
 
def index(request):
    products = product_data.objects.all()
    return render(request, 'index.html', {'products': products})

def rackets(request):
    products = product_data.objects.all()
    return render(request, 'rackets.html',{'products': products})

def yonex(request):
    products = product_data.objects.all()
    return render(request, 'yonex.html',{'products': products})

def victor(request):
    products = product_data.objects.all()
    return render(request, 'victor.html', {'products': products})

def shoes(request):
    products = product_data.objects.all()
    return render(request, 'shoes.html', {'products': products})

def shoes_yonex(request):
    products = product_data.objects.all()
    return render(request, 'sh_yonex.html', {'products': products})

def shoes_victor(request):
    products = product_data.objects.all()
    return render(request, 'sh_victor.html', {'products': products})

def accessories(request):
    products = product_data.objects.all()
    return render(request, 'accessories.html', {'products': products})

def signup(request):
    return render(request, 'signup.html')

def bag(request):
    products = product_data.objects.all()
    return render(request, 'bag.html', {'products': products})

def bag_yonex(request):
    products = product_data.objects.all()
    return render(request, 'bag_yonex.html', {'products': products})

def bag_victor(request):
    products = product_data.objects.all()
    return render(request, 'bag_victor.html', {'products': products})

def grips(request):
    products = product_data.objects.all()
    return render(request, 'grips.html', {'products': products})

def wristband(request):
    products = product_data.objects.all()
    return render(request, 'wristband.html', {'products': products})

def headband(request):
    products = product_data.objects.all()
    return render(request, 'headband.html', {'products': products})

def socks(request):
    products = product_data.objects.all()
    return render(request, 'socks.html', {'products': products})

def cushion(request):
    products = product_data.objects.all()
    return render(request, 'cushion.html', {'products': products})

def towel(request):
    products = product_data.objects.all()
    return render(request, 'towel.html', {'products': products})

def cart(request):
    user = request.user
    showcart = {'item' : cart_add.objects.filter(email=user.email)}
    return render(request,'cart.html',showcart)

def showMyorder(request):
    user = request.user
    order_show_detail = []
    myorder_count = order_data.objects.filter(order_email=user.email).count()
    if myorder_count > 0:
        if user.is_staff == 0:
            myorder = order_data.objects.filter(order_email=user.email)
            detail = order_detail.objects.all()
            context = {'showmyorder' : myorder , 'dtl' : detail}
            return render(request,'showorder.html',context)
        else :
            myorder = order_data.objects.all()
            detail = order_detail.objects.all()
            context = {'showmyorder' : myorder , 'dtl' : detail}
            return render(request,'showorder.html',context)
    else:
        return render(request,'showorder.html')

def checkout(request):
    user = request.user
    sum_order = cart_add.objects.filter(email=user.email)
    Nowtime = datetime.now()
    total = []
    if sum_order.count() <= 0:
        return redirect("/")
    else:    
        for item in sum_order:
            sum_item = float(item.product_price) * float(item.product_qty)
            total.append(sum_item)
        total_order = (sum(total))
        print(sum_order)
    if request.method == 'POST':
            checkout = order_detail()
            save_order = order_data()
            save_order.order_total = total_order
            save_order.order_date = Nowtime
            save_order.order_address = request.POST.get('order_address')
            save_order.order_tel = request.POST.get('order_tel')
            save_order.order_username = user.username
            save_order.order_email = user.email
            save_order.save()
            for x in sum_order:
                save_order_id = order_data.objects.filter(order_email=user.email).last()
                checkout = order_detail()
                checkout.order_id_ref_id =  int(save_order_id.order_id)
                checkout.p_id = x.product_id
                checkout.p_qty = x.product_qty
                checkout.p_price = x.product_price
                print(checkout.p_id)
                print(checkout.p_qty)
                print(checkout.p_price)
                checkout.save()
                del_cart = cart_add.objects.get(product_id_id= checkout.p_id,email=user.email)
                del_cart.delete()
            messages.success(request,'สำเร็จ')
            return redirect('/showMyorder')
    showcart = {'item' : cart_add.objects.filter(email=user.email) , 
                'total_order' : total_order,
                'nowtime' : Nowtime,
                }
    return render(request,'checkout.html',showcart)

def del_cart_item(request,product_id):
    user = request.user
    item_del = cart_add.objects.get(product_id_id=product_id,email=user.email)
    item_del.delete()
    return redirect("/cart/")

def addtocart(request,product_id):
    user = request.user
    if request.user.is_authenticated :
        if user.email == '':
            pass
        else:
            add_product = product_data.objects.get(product_id=product_id)
            table = cart_add()
            if cart_add.objects.filter(product_id_id=product_id,email=user.email):
                if cart_add.objects.filter(product_id_id=product_id,email=user.email) is not None:
                    increase_qty = cart_add.objects.get(product_id_id=product_id,email=user.email)
                    increase_qty.product_qty = increase_qty.product_qty + 1
                    increase_qty.save()
                    return redirect('/cart/')
            else:
                table.product_id_id = add_product.product_id
                table.product_qty = 1
                table.product_price = int(add_product.product_price)
                table.email = user.email
                table.save()
                return redirect('/cart/')
    else:
        messages.warning(request,'เข้าสู่ระบบเพื่อสั่งสินค้า')
        return redirect('/login')

def login(request):
    return render(request, 'login.html')

def addUser(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            #print("Username นี้ซ้ำ")
            messages.success(request, 'Username นี้ซ้ำ')
            return redirect("/signup")
        elif User.objects.filter(email=email).exists():
            #print("Email นี้ซ้ำ")
            messages.success(request, 'Email นี้ซ้ำ')
            return redirect("/signup")
        else:
            user = User.objects.create_user(
                username = username,
                first_name = firstname,
                last_name = lastname,
                email = email,
                password = password
            )
            user.save()
            return redirect('/')
    else:
        messages.success(request, 'Password ไม่เท่ากับ Re-Password')
        return redirect("/signup")
    
def loginForm(request):
    username = request.POST['username']
    password = request.POST['password']
    
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        #แสดงว่า username, password ถูกต้อง
        auth.login(request,user)
        return redirect('/')
    else:
        #แสดงว่า username, password ไม่ถูกต้อง
        messages.success(request, 'Login ไม่สำเร็จ')
        return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')

def product_list(request):
    products = product_data.objects.all()
    return render(request, 'product_list.html', {'products': products})

def info(request, product_id):
    products = product_data.objects.get(product_id=product_id)
    return render(request, 'info.html', {'p': products})