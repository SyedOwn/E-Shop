from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):

    def validateCustomer(self, customer):

        error_message = None

        if not customer.first_name:
            error_message = "First Name Required"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 characters long"

        # Last Name
        elif not customer.last_name:
            error_message = "Last Name Required"

        # email
        elif not customer.email:
            error_message = "Email Required"

        # Password
        elif not customer.password:
            error_message = "Password Required"
        elif len(customer.password) < 8:
            error_message = "Password must be at least 8 digits long"

        # Phone
        elif not customer.phone:
            error_message = "Contact Number Required"
        elif len(customer.phone) < 11:
            error_message = "Phone Number must be of at least 11 digits"

        elif customer.isExists():
            error_message = "Email Address Already Registered"

        return error_message


    def get(selfself, request):
        return render(request, 'signup.html')

    def post(self, request):

        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)
        # validation

        value = {'first_name': first_name,
                 'last_name': last_name,
                 'phone': phone,
                 'email': email
                 }

        if not error_message:
            print((first_name, last_name, phone, email, password))
            customer.password = make_password(customer.password)  # will create and store hashed password
            customer.register()
            return redirect('homepage')

        else:
            data = {'error': error_message,
                    'values': value
                    }
            return render(request, 'signup.html', data)
        # return HttpResponse("Signup Success")
