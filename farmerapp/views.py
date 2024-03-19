from django.shortcuts import render,redirect
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
from django.core.files.storage import default_storage
from django.conf import settings
import os
import pickle
import numpy as np
from django.contrib.auth import logout
from .models import *
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    return render(request,"farmer/index.html")


def about(request):
    return render(request,"farmer/about.html")


def adminlogin(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")

        if name == "admin" and password == "admin":
            messages.success(request,"Login Successfull !")
            print("success")
            return redirect("admin_dashboard")
        else:
            messages.error(request,"Invalid Details !")
            print("Invalid Details")
            return redirect("adminlogin")
    return render(request,"farmer/admin-login.html")


def farmerregister(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        location = request.POST.get('address')
        profile = request.FILES.get('profile')
        try:
            User.objects.get(user_email = email)
            messages.info(request, 'Email Already Exists!')
            return redirect('farmerregister')
        except:
            user = User.objects.create(user_name=name, user_email=email, user_phone=phone, user_profile=profile, user_password=password, user_location=location)
            print(user)
            messages.success(request, 'Account Created Successfully!')
            return redirect('farmerregister')
    return render(request,"farmer/farmer-register.html")


def farmerlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(user_email=email)   
            if user.user_password == password:
                if user.status == 'Accepted':
                    request.session['user_id'] = user.user_id
                    messages.success(request, 'Login Successful')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Your account is not approved yet.')
                    return redirect('farmerlogin')
            else:
                messages.error(request, 'Incorrect Password')
                return redirect('farmerlogin')
        except User.DoesNotExist:
            messages.error(request, 'Invalid Login Details')
            return redirect('farmerlogin')
    return render(request,"farmer/farmer-login.html")


def govtlogin(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username == 'govt' and password == 'govt':
            messages.success(request, 'Login Successful')
            return redirect('govt_dashboard')
        else:
            messages.error(request, 'Invalid details !')
            return redirect('govtlogin')
    return render(request,"farmer/govtofficer-login.html")



def expertlogin(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username == 'expert' and password == 'expert':
            messages.success(request, 'Login Successful')
            return redirect('expert_dashboard')
        else:
            messages.error(request, 'Invalid details !')
            return redirect('expertlogin')
    return render(request,"farmer/experts.html")



def contact(request):
    return render(request,"farmer/contact.html")



def dashboard(request):
    return render(request,"farmer/farmer-dashboard.html")


def profile(request):
    user_id  = request.session.get('user_id')
    user = User.objects.get(user_id=user_id)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        try:
            profile = request.FILES['profile']
            user.user_profile = profile
        except MultiValueDictKeyError:
            profile = user.user_profile
        password = request.POST.get('password')
        location = request.POST.get('location')
        user.user_name = name
        user.user_email = email
        user.user_phone = phone
        user.user_password = password
        user.user_location = location
        user.save()
        messages.success(request , 'updated succesfully!')
        return redirect('profile')
    return render(request,"farmer/myprofile.html",{'i':user})



def appointments(request):
    user_id = request.session.get('user_id')
    appointments_list = Appointment.objects.filter(user=user_id)
    appointments_per_page = 5
    paginator = Paginator(appointments_list, appointments_per_page)
    page = request.GET.get('page')
    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)

    return render(request, "farmer/appointments.html", {'appointments': appointments})




def askappiontment(request):
    user_id = request.session.get('user_id')
    user = User.objects.filter(user_id=user_id).first()
    if request.method == 'POST':
        form_data = request.POST
        appointment = Appointment(
            name=form_data['name'],
            age=form_data['age'],
            address=form_data['address'],
            contact_number=form_data['contactNumber'],
            appointment_date=form_data['appointmentDate'],
            query_subject=form_data['querySubject'],
            additional_info=form_data['additionalInfo'],
            user=user
        )
        appointment.save()
        messages.success(request,"Request submitted Successfully !")
        return redirect('askappiontment')
    return render(request,"farmer/askappiontment.html")



def feedback(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        user = User.objects.filter(user_id=user_id).first()

        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        rating = request.POST.get('rating')
        additional_comments = request.POST.get('additional_comments')

        feedback_instance = Feedback.objects.create(
            user=user,
            user_name=user_name,
            user_email=user_email,
            rating=rating,
            additional_comments=additional_comments
        )
        feedback_instance.save()
        messages.success(request,"Feedback Submitted Successfully !")
        return redirect('farmer_feedback')

    return render(request,"farmer/farmer-feedback.html")

def user_logout(request):
    logout(request)
    return redirect('farmerlogin')

def chatbot(request):
    return render(request,"farmer/chatbot.html")

def helpdesk_hin(request):
    return render(request,"farmer/helpdesk-hin.html")

def helpdesk_tel(request):
    return render(request,"farmer/helpdesk-tel.html")


def helpdesk(request):
    if request.method == 'POST':
        try:
            user_id = request.session.get('user_id')
            user = User.objects.filter(user_id=user_id).first()
            name = request.POST.get('name')
            email = request.POST.get('email')
            contact_number = request.POST.get('contactNumber')
            query_type = request.POST.get('queryType')
            crop_information = request.POST.get('crop')
            query_subject = request.POST.get('querySubject')
            specific_issue = request.POST.get('issue')
            location = request.POST.get('location')
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            pin_code = request.POST.get('pinCode')

            longitude = request.POST.get('longitude')
            latitude = request.POST.get('latitude')
            print(latitude,"bhrhbrcbhrcbrhbdrbdrbdt")
            weather_condition = request.POST.get('weatherCondition')
            print(weather_condition,"hhhhhhhhhhhhhhhhhhhhhhhhhhhh")

            farmer_query = FarmerQuery(
                user=user,
                name=name,
                email=email,
                contact_number=contact_number,
                query_type=query_type,
                crop_information=crop_information,
                query_subject=query_subject,
                specific_issue=specific_issue,
                location=location,
                country=country,
                state=state,
                city=city,
                pin_code=pin_code,
                longitude=longitude,
                latitude=latitude,
                weather_condition=weather_condition
            )
            farmer_query.save()
            messages.success(request,"Sumitted Successfully !")
            return redirect('helpdesk')
        except Exception as e:
            print(f"Error in helpdesk view: {e}")
            messages.error(request, "An error occurred while submitting the form.")

    return render(request,"farmer/helpdesk.html")



model = load_model('model_inception.h5')

ref = {
    0: 'Pepper__bell___Bacterial_spot',
    1: 'Pepper__bell___healthy',
    2: 'Potato___Early_blight',
    3: 'Potato___Late_blight',
    4: 'Potato___healthy',
    5: 'Tomato - Bacterial_spot',
    6: 'Tomato - Early_blight',
    7: 'Tomato - Healthy',
    8: 'Tomato - Late_blight',
    9: 'Tomato - Leaf_Mold',
    10: 'Tomato - Septoria_leaf_spot',
    11: 'Tomato - Target_Spot',
    12: 'Tomato - Tomato_Yellow_Leaf_Curl_Virus',
    13: 'Tomato - Tomato_mosaic_virus',
    14: 'Tomato - Two-spotted_spider_mite',
    15: 'diseased cotton leaf',
    16: 'diseased cotton plant',
    17: 'fresh cotton leaf',
    18: 'fresh cotton plant',
}


def prediction(path):
    img = image.load_img(path, target_size=(224, 224))
    i = image.img_to_array(img)
    i = np.expand_dims(i, axis=0)
    img = preprocess_input(i)
    pred = np.argmax(model.predict(img), axis=1)
    return ref[pred[0]]


def cropdisease(request):
    result = ""
    if request.method == "POST" and 'image' in request.FILES:
        uploaded_image = request.FILES['image']
        file_path = default_storage.save(uploaded_image.name, uploaded_image)
        path = settings.MEDIA_ROOT + '/' + file_path
        result = prediction(path)
        print(result,"lobkugjrcncjbr")
        messages.success(request,"Detection Completed !")
        return render(request,"farmer/cropdisease.html", {'result': result})
    return render(request,"farmer/cropdisease.html")


