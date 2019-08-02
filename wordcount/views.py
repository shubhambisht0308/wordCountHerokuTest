# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {})

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    
    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
    
    sortedDict = sorted(wordDict.items(), key=operator.itemgetter(1), reverse= True)
        
    return render(request, 'count.html', {'text' : fulltext, 'count':len(wordList), 'wordDict' : sortedDict})

def about(request):
    return render(request, 'about.html', {})