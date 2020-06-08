from django.http import HttpResponse
from django.shortcuts import render
def start(request):
    return render(request, 'start.html')
def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == "on":
        punctuations = '''[]()#@{}$%^&*,.;:'"_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
              analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if newlineremover == "on":
         analyzed = ""
         for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
         params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
         djtext = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
    if(removepunc!= "on" and fullcaps != "on" and newlineremover!= "on" and extraspaceremover!= "on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)










