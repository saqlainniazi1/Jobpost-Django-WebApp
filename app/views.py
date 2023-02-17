from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader

from app.models import JobPost

# Create your views here.
# def hello(requeset):
    
#     return HttpResponse("<h1>Hello world</h1>")
job_title = [
    "Job 1",
    "Job 2",
    "Job 3",
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]

class TempClass():
    x = 5

# def home(request):
#     template = loader.get_template('app/hello.html')
#     context = {
#         'name1': 'Atif',
#         'name2': 'Aslam',
#         'names_list': ['Aslam', 'Junaid'],
#         'temp': TempClass() 
#     }
#     return HttpResponse(template.render(context, request))
# OR
def home(request):
    names_list = ["Atif", "Junaid", "Ameer", "Mansoor", "Taimoor"]
    context = {
        'name1': 'Atif',
        'name2': 'Aslam',
        'age' : 27,
        "names": names_list,
        'is_authenticated' : True,
        'names_list': ['Aslam', 'Junaid'],
        'temp': TempClass() 
    }
    return render(request, "app/hello.html", context)


# def hello(request):

#     list_of_jobs = "<ul>"
#     for job in job_title:
#         job_id = job_title.index(job)
#         print(reverse('job_detail', args=(job_id,)))
#         list_of_jobs += f"<li><a href='{reverse('job_detail', args=(job_id,))}'>{job}</a></li>"

#     list_of_jobs += "</ul>"

#     return HttpResponse(list_of_jobs)
# OR

def hello(request):

    jobs = JobPost.objects.all()
    context = {
        'jobs': jobs,
    }

    return render(request, 'app/list-of-jobs.html', context)


# def job(request):
#     return HttpResponse("job one")



def job_detail(request, id):
    # return HttpResponse(f'job {id}')

    # site = "https://www.google.com/"
    # return HttpResponse(f"Visit <a href='{site}'>Google here.</a>")

    try:
        if id == 0:
            # return redirect('/')
            return redirect(reverse('jobs_home'))

        jobs = JobPost.objects.all()
        job = jobs.get(id=id)

        context = {

            'job': job,
        }
        # return HttpResponse(f"<h1>{job_title[id]}</h1> <h2>{job_description[id]}</h2>")
        return render(request, 'app/job_detail.html', context)

    except:
        return HttpResponseNotFound()

