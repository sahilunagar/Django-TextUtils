# Creater by Sahil

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Sahil', 'place': 'Surat'}
    return render(request, 'index.html', params)


def about(request):
    return HttpResponse("About this app    <a href='/'>Home</a>")


def analyse(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize_all = request.POST.get('capitalize', 'off')
    removenewlines = request.POST.get('removenewlines', 'off')
    removeextraspaces = request.POST.get('removeextraspaces', 'off')
    countchars = request.POST.get('countchars', 'off')

    if removepunc == 'on':
        analysed_text = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in text:
            if char not in punctuations:
                analysed_text += char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed_text}
        text = analysed_text
        # return render(request, 'analyse.html', params)

    if capitalize_all == 'on':
        analysed_text = ""
        for char in text:
            analysed_text += char.upper()
        params = {'purpose': 'Capitalized all characters', 'analysed_text': analysed_text}
        text = analysed_text
        # return render(request, 'analyse.html', params)

    if removenewlines == 'on':
        analysed_text = ""
        for char in text:
            if char != '\n' and char != '\r':
                analysed_text += char
        params = {'purpose': 'Removed new lines', 'analysed_text': analysed_text}
        text = analysed_text
        # return render(request, 'analyse.html', params)

    if removeextraspaces == 'on':
        analysed_text = ""
        prev_char = ' '
        for char in text:
            if char != ' ' or (char == ' ' and prev_char != ' '):
                analysed_text += char
            prev_char = char
        params = {'purpose': 'Removed extra spaces', 'analysed_text': analysed_text}
        text = analysed_text
        # return render(request, 'analyse.html', params)

    if countchars == 'on':
        analysed_text = text
        analysed_text += " => Characters count: " + str(len(text))
        params = {'purpose': 'Removed extra spaces', 'analysed_text': analysed_text}
        text = analysed_text
        # return render(request, 'analyse.html', params)

    analysed_text = text
    params = {'purpose': '', 'analysed_text': analysed_text}
    return render(request, 'analyse.html', params)
