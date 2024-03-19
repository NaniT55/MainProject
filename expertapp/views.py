from django.shortcuts import render,redirect,get_object_or_404
from farmerapp.models import *
from expertapp.models import Response
from django.contrib import messages
import os
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')



def index(request):
    total_users_count = Appointment.objects.count()
    total_qurey_count = FarmerQuery.objects.count()
    total_response = Response.objects.count()
    total_pending_appointments = Appointment.objects.filter(status="Pending").count()
    total_scheduled_appointments = Appointment.objects.filter(status="Accepted").count()

    return render(request, "expert/index.html", {
        'total_users_count': total_users_count,
        'total_response': total_response,
        'total_pending_appionments': total_pending_appointments,
        'total_scheduled_appointments': total_scheduled_appointments,
        'total_qurey_count':total_qurey_count,
    })




def pending_appionments(request):
    pending_appionments = Appointment.objects.filter(status="Pending")
    paginator = Paginator(pending_appionments, 5)
    page = request.GET.get('page')
    pending_appionments = paginator.get_page(page)
    return render(request, "expert/pending-appionments.html", {'pending_appionments': pending_appionments})


def view_responses(request):
    responses = Response.objects.all()
    paginator = Paginator(responses, 5)
    page = request.GET.get('page')
    responses = paginator.get_page(page)
    return render(request, "expert/view-responses.html", {'responses': responses})


def edit_response(request,response_id):
    response = get_object_or_404(Response, id=response_id)
    query_id = response.query_id
    user = FarmerQuery.objects.get(query_id=query_id)
    if request.method == 'POST':
        response_text = request.POST.get('response_text')
        response.response_text = response_text
        response.save()
        subject = 'Response is Updated For Your Agriculture Query'
        message = f'Hello {user.name},\n\nYour agriculture query  response had been Updated from our expert.\n\n This is Updated Response: {response_text}'
        from_email = os.environ.get('EMAIL_HOST_USER')
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.info(request,"Response Text is Updated !")
        return redirect('expert_view_responses')  
    return render(request,"expert/edit-responses.html",{'response':response})


def helpdesk(request):
    all_queries = FarmerQuery.objects.all()
    items_per_page = 5  
    paginator = Paginator(all_queries, items_per_page)
    page = request.GET.get('page')
    try:
        queries = paginator.page(page)
    except PageNotAnInteger:
        queries = paginator.page(1)
    except EmptyPage:
        queries = paginator.page(paginator.num_pages)
    return render(request, "expert/helpdesk.html", {'queries': queries})



def view_appiontment(request):
    view_appionments = Appointment.objects.filter(status="Accepted")
    paginator = Paginator(view_appionments, 5)
    page = request.GET.get('page')
    view_appionments = paginator.get_page(page)
    return render(request, "expert/view-appiontment.html", {'view_appionments': view_appionments})



def view_queries(request, query_id):
    query = get_object_or_404(FarmerQuery, query_id=query_id)
    request.session["query"] = query.query_id
    return render(request, "expert/view-queries.html", {'query': query})


def accept_appointment(request, appiontment_id):
    try:
        appointment = Appointment.objects.get(id=appiontment_id)
        name = appointment.name
        email = appointment.user.user_email
        appointment.status = 'Accepted'
        appointment.save()
        subject = 'Response for Your Agriculture Query'
        message = f'Hello {name},\n\nYour agriculture appointment scheduled for {appointment.appointment_date.strftime("%Y-%m-%d")} has been accepted. Our expert will be available to assist you. Thank you!'
        from_email = os.environ.get('EMAIL_HOST_USER')
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        messages.success(request,"Appointment Scheduled successfully and Email Sent !")
        return redirect("pending_appionments")
    except Appointment.DoesNotExist:
        messages.error(request,"Appointment Not Found !")
        return redirect("pending_appionments")



def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    subject = 'Appointment is Rejected !'
    message = f'Hello {appointment.name},\n\nYour agriculture appointment scheduled for {appointment.appointment_date.strftime("%Y-%m-%d")} has been Rejected. We apologize for any inconvenience. If you still need assistance, please feel free to request a new appointment. Thank you!'
    from_email = os.environ.get('EMAIL_HOST_USER')
    recipient_list = [appointment.user.user_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    messages.success(request,"Appointment Deleted successfully !")
    return redirect('pending_appionments')


def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = "Cancelled"
    appointment.save()
    subject = 'Appointment is Canceled !'
    message = f'Hello {appointment.name},\n\nYour agriculture appointment scheduled for {appointment.appointment_date.strftime("%Y-%m-%d")} has been canceled. We apologize for any inconvenience. If you still need assistance, please feel free to request a new appointment. Thank you!'
    from_email = os.environ.get('EMAIL_HOST_USER')
    recipient_list = [appointment.user.user_email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    messages.success(request,"Appointment Deleted successfully !")
    return redirect('view_appiontment')





def view_queries_respond(request):
    query_id = request.session.get('query')
    query = get_object_or_404(FarmerQuery, query_id=query_id)
    print(query_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        response_text = request.POST.get('responseText')
        response = Response(name=name, email=email, query_id=query_id, response_text=response_text)
        response.save()
        subject = 'Response for Your Agriculture Query'
        message = f'Hello {name},\n\nYour agriculture query has received a response from our expert.\n\nResponse: {response_text}'
        from_email = os.environ.get('EMAIL_HOST_USER')
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, "Response sent successfully! Email notification sent.")
        except Exception as e:
            messages.error(request, f"Error sending email notification: {e}")

        return redirect("view_queries_respond")

    return render(request, "expert/view-queries.html",{'query':query})






