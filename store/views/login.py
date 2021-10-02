from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
        pass;


    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                if Login.return_url:  # When redirecting with help of name redirect() is used but when redirecting with
                    return HttpResponseRedirect(Login.return_url)  # the help of url then HttpResponseRedirect() is used
                else:
                    Login.return_url = None
                return redirect('homepage')
            else:
                error_message = 'Email or Password Invalid'
        else:
            error_message = 'Email or Password Invalid'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
