from django.shortcuts import render,redirect
from .models import Quiz,Trial
import random

i = 0
j = 0
score  = 0
username = ""
qupper = 0
trlist = [0,1,2,3,4]
mnlist = [inx for inx in range(20)]
def home(request):
    global score,i,j
    score = 0
    i = 0
    j = 0
    return render(request, 'home.html')

def demo(request):
    quizz = Trial.objects.using('default').all()
    global j
    if j == 0:
        random.shuffle(trlist)
        print("This will be printed only once. with ",trlist[0])
    if j < 5:
        tp = trlist[j]
    else:
        tp = 0
    content = {
            'ques':  j+1,
            'quizq':  quizz[tp].question,
            'answer':  quizz[tp].ans,
            'option1': quizz[tp].opt1,
            'option2': quizz[tp].opt2,
            'option3': quizz[tp].opt3,
            'option4': quizz[tp].opt4,
    }
    
    if request.method == 'POST':
        corans = quizz[trlist[j-1]].ans
        try:
            filled = request.POST['opt']
        except:
            j += 1
            if j >= 5:
                return redirect(result)
            return render(request, 'demo.html',content)
        if corans == filled:
            global score
            score += 1
        if j >= 5:
            return redirect(result)
    j += 1
    return render(request, 'demo.html',content)


def details(request):
    if request.method == 'POST':
        global username
        global qupper
        username = request.POST['uname']
        qupper = request.POST['qnchoice']
        return(redirect(quiz))
    return render(request, 'details.html')

def quiz(request):
    quizz = Quiz.objects.using('default').all()
    global i
    if i == 0:
        random.shuffle(mnlist)
    if i < int(qupper):
        tp = mnlist[i]
    else:
        tp = 0
    content = {
        'total':qupper,
        'ques':  i+1,
        'quizq':  quizz[tp].question,
        'answer':  quizz[tp].ans,
        'option1': quizz[tp].opt1,
        'option2': quizz[tp].opt2,
        'option3': quizz[tp].opt3,
        'option4': quizz[tp].opt4,
    }
    if request.method == 'POST':
        corans = quizz[mnlist[i-1]].ans
        try:
            filled = request.POST['opt']
        except:
            i += 1
            if i >= int(qupper):
                return redirect(result) 
            return render(request, 'quiz.html',content)
        if corans == filled:
            global score
            score += 1
        if i >= int(qupper):
            return redirect(result) 
    i += 1
    return render(request, 'quiz.html',content)


def result(request):
    half = int(qupper)/2
    message = ""
    if score <= half:
        message = "Keep Trying "+username
    else:
        message = "Well Done "+username
    content = {
        'note':message,
        'user':username,
        'mark':score,
    }
    return render(request, 'result.html',content)
