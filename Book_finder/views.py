from django.shortcuts import render
import requests

def home(request):
    try:
        books = []
        query = ''
        if request.method == "POST":
            query = request.POST['q']
            api = f'https://www.googleapis.com/books/v1/volumes?q={query}'

            response = requests.get(api)

            if response.status_code == 200:
                books = response.json().get('items', [])

            return render(request, 'index.html',{"books": books, "query": query})
        else:
            return render(request, 'index.html',{"books": books, "query": query} )
    except:
        return render(request, 'error.html')