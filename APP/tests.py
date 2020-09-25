# def sendanmail(request):
      
#     if request.method == "POST":
#         to= request.POST.get('tomail')
#         content = request.POST.get('content')
        
#         html_content = render_to_string("email_tamplate.html",{'title':'test email','content':content})
#         text_content =strip_tags(html_content)

#         email = EmailMultiAlternatives(
#             "testing",
#             text_content,

#             settings.EMAIL_HOST_USER,
#             [to]

#         )
#         email.attach_alternative(html_content,"text/html")
#         email.send()
#         return render(
#             request,
#             'email.html',
#             {
#                 'title' : 'send_email'
#             }
#         )
       
#     else:  
#         return render(
#             request,
#             'email.html',
#             {
#              'title': 'send an email'
#             }
#             )
