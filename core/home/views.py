from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""<h1>hey i am Veda Priya </h1>
    <p>Hey this is my first django trail</p>
    <hr>
    <h3 style ="color:red">Hope i am doing pretty good</p>
    """)

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>this is over sucess page</h1> ")


def about(request):
    context={"page":'About'}
    return render(request,'home/about.html',context)

def contact(request):
    context={"page":'Contact'}
    return render(request,'home/contact.html',context)

def show_template(request):
    peoples = [
        {'name': 'veda', 'age': 20},
        {"name": "priya", 'age': 14},
        {'name': 'arun', 'age': 19},
    ]

   
    text = """
       Lorem ipsum, dolor sit amet consectetur adipisicing elit. Quod dolorem corporis 
       distinctio nam velit veniam? Quae repellat, quam doloremque, voluptate sunt itaque consequuntur consectetur obcaecati laboriosam fuga maiores eligendi minus.
    """
    vegetables = ['pumpkin', 'tomato', 'potato']

    return render(request, "home/index.html", context={'page': "django 2024 start", 'peoples': peoples, 'text': text, 'vegetables': vegetables})

def tags(request):
    context = {
        'heading': 'Hello &lt;i&gt;my&lt;/i&gt; World!',
    }
    return render(request, 'home/tags.html', context)
