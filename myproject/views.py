# This is file created by me
from django.http import HttpResponse
from django.shortcuts import render


def home(request):

     return render(request, 'index.html')


def analyze(request):
    # Get the text as a input
    iptext = request.POST.get('text', 'default')


    # Store checkbox values on/off
    removepunc = request.POST.get('removepunc', 'off')
    capall = request.POST.get('capall', 'off')
    newline = request.POST.get('newlineremove', 'off')
    extraspace = request.POST.get('extraspaceremove', 'off')
    countcar = request.POST.get('count_car', 'off')


    # logic for removepunc
    if removepunc == 'on':
        analyzed = ""
        punctuations = '''~`!@#$%^&*()_+-=/|,.?{}"'[]'''
        for char in iptext:
            if char not in punctuations:
              analyzed += char

        params = {
                "purpose": "Punctuations",
                "analyzed_txt": analyzed
        }
        iptext = analyzed
        # return render(request, 'analyze.html', params)


    # logic for caps all
    if capall == 'on':
        analyzed = ""

        for char in iptext:
            analyzed += str.capitalize(char)

        params = {
            "purpose": "Upper text",
            "analyzed_txt": analyzed
        }
        iptext = analyzed
        # return render(request, 'analyze.html', params)


    # logic to remove new lines
    if newline == 'on':
        analyzed = ""
        for char in iptext:
            if char != "\n" and char != "\r":
                analyzed += char

        params = {
            "purpose": "Remove New Lines",
            "analyzed_txt": analyzed
        }
        iptext = analyzed
        # return render(request, 'analyze.html', params)


    # Logic to remove extra space
    if extraspace == 'on':
        analyzed = ""
        for ids, char in enumerate(iptext):
            if iptext[ids] == " " and iptext[ids+1] == " ":
                pass
            else:
                analyzed += char

        params = {
            "purpose": "Remove extra spaces",
            "analyzed_txt": analyzed
        }
        iptext = analyzed
        # return render(request, 'analyze.html', params)

    if countcar == 'on':
        analyzed = 0
        for char in iptext:
            no_of_chars = []
            no_of_chars += char
            analyzed += len(no_of_chars)

        params = {
            "purpose": "Count characters",
            "analyzed_txt": analyzed
        }

    if removepunc != "on" and countcar != 'on' and capall != "on" and newline != "on" and extraspace != "on" and countcar != "on":
        return HttpResponse("Error!!!  Select Filter First")

    return render(request, 'analyze.html', params)
