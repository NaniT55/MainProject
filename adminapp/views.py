from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from farmerapp.models import *
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
import os
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# Create your views here.
def admin_index(request):
    total_farmers = User.objects.count()
    total_feedbacks = Feedback.objects.count()
    five_star_ratings = Feedback.objects.filter(rating=5).count()
    context = {
        'total_farmers': total_farmers,
        'total_feedbacks': total_feedbacks,
        'five_star_ratings': five_star_ratings,
    }
    return render(request, "admin/index.html", context)


def farmer_details(request):
    farmer_details = User.objects.all()
    paginator = Paginator(farmer_details, 5)

    page = request.GET.get('page')
    try:
        farmer_details = paginator.page(page)
    except PageNotAnInteger:
        farmer_details = paginator.page(1)
    except EmptyPage:
        farmer_details = paginator.page(paginator.num_pages)

    return render(request, "admin/farmer-details.html", {'farmer_details': farmer_details})


def view_farmer_details(request,farmer_id):
    user = User.objects.get(user_id = farmer_id)
    print(user)
    return render(request,"admin/view-farmers-deatils.html",{'user':user})


def model_train(request):
    return render(request,"admin/model-training.html")


def graph(request):
    feedback_data = Feedback.objects.all()
    sentiment_counts = {'5': 0, '4': 0, '3': 0, '2': 0, '1': 0}

    for feedback_entry in feedback_data:
        rating = feedback_entry.rating
        sentiment_counts[str(rating)] += 1
    return render(request,"admin/graph.html", {'sentiment_counts': sentiment_counts})



def delete_feedback(request, feedback_id):
    feedback_entry = get_object_or_404(Feedback, pk=feedback_id)
    feedback_entry.delete()
    messages.info(request,"Deleted Successfully !")
    return render(request, 'admin/feedback.html')


def reply_feedback(request, feedback_id):
    feedback_entry = get_object_or_404(Feedback, pk=feedback_id)
    if feedback_entry.rating > 3:
        subject = 'Thank You for Your Feedback'
        message = f'Thank you for providing valuable feedback! We appreciate your positive rating.'
    elif feedback_entry.rating in [1, 2]:
        subject = 'We Appreciate Your Feedback'
        message = 'Thank you for your feedback. We apologize for any inconvenience and assure you that we are working to improve our services.'
    else:
        subject = 'Feedback Received'
        message = 'Thank you for your feedback.'
    send_mail(subject, message, 'your@email.com', [feedback_entry.user_email], fail_silently=False)
    messages.info(request, "Email Sent Successfully!")
    return redirect('admin_feedback') 
    

def sentiment_graph(request):
    rating_values = [1, 2, 3, 4, 5]
    rating_counts = {}

    for rating_value in rating_values:
        count = Feedback.objects.filter(rating=rating_value).count()
        rating_counts[rating_value] = count

    return render(request, "admin/sentiment-graph.html", {'rating_counts': rating_counts})




def sentiment(request):
    feedback_data = Feedback.objects.all()
    sentiment_data = []

    for feedback_entry in feedback_data:
        rating = feedback_entry.rating
        if rating == 5:
            sentiment = "🌟" 
        elif rating == 4:
            sentiment = "😄"
        elif rating == 3:
            sentiment = "😊"
        elif rating == 2:
            sentiment = "😐"  
        else:
            sentiment = "😢" 

        sentiment_data.append({
            'sno': feedback_entry.feedback_id,
            'name': feedback_entry.user_name,
            'email': feedback_entry.user_email,
            'sentiment': sentiment,
        })

    paginator = Paginator(sentiment_data, 5) 
    page = request.GET.get('page')
    try:
        sentiment_data = paginator.page(page)
    except PageNotAnInteger:
        sentiment_data = paginator.page(1)
    except EmptyPage:
        sentiment_data = paginator.page(paginator.num_pages)

    return render(request, "admin/sentiment.html", {'sentiment_data': sentiment_data})



def feedback(request):
    feedback_data = Feedback.objects.all()
    paginator = Paginator(feedback_data, 3) 
    page = request.GET.get('page')
    try:
        feedback_data = paginator.page(page)
    except PageNotAnInteger:
        feedback_data = paginator.page(1)
    except EmptyPage:
        feedback_data = paginator.page(paginator.num_pages)
    return render(request, "admin/feedback.html", {'feedback_data': feedback_data})


def upload_dataset(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file')

        if csv_file:
            file_path = default_storage.save('savedimg/' + csv_file.name, csv_file)
            messages.success(request,"Image Uploaded Succesfully")
            print(file_path,"succesfully!")
    return render(request,"admin/upload-dataset.html")
