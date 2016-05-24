from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from .models import *
from django.template.loader import render_to_string
from collections import namedtuple

def index(request):
   return render(request, 'testing/home/home.html')

def sections (request):
   return render_to_response('testing/section/section.html', {'sections': Section.objects.all()})

def tests (request, alias_section,):
   section = Section.objects.get(section_alias=alias_section)
   tests = Test.objects.filter(test_section__section_name=section)

   context = {
      'tests': tests,
      'section': section,
   }
   return HttpResponse(render_to_string('testing/tests/tests.html', context))

def questions (request, alias_test, alias_question, alias_section):
   section = Section.objects.get(section_alias=alias_section)
   test = Test.objects.get(test_alias=alias_test)
   questions = Question.objects.filter(question_parretn_test__test_name=test, question_alias=alias_question)
   context = {
      'section': section,
      'questions': questions,
      'test': test,
   }
   return HttpResponse(render_to_string('testing/tests/one_test/one_test.html', context))

# def question (request, alias_test, alias_question, alias_section):
#    section = Section.objects.get(section_alias=alias_section)
#    test = Test.objects.get(test_alias=alias_test)
#    questions = Question.objects.get(question_parretn_test__test_name=test, question_alias=alias_question)#.values('question_text','question_image', 'question_alias','id')
#    answers = Answer.objects.filter(answer_parretn_question__question_alias=alias_question)
#    context = {
#       'section': section,
#       'questions': questions,
#       'test': test,
#       'answers': answers,
#    }
#    return HttpResponse(render_to_string('testing/tests/one_test/one_test.html', context))

def question (request, alias_section, alias_test, question_number):

   section = Section.objects.get(section_alias=alias_section)
   test = Test.objects.get(test_alias=alias_test)
   questions = Question.objects.get(question_parretn_test__test_name=test)[:1][question_number-1]
   context = {
      'section': section,
      'questions': questions,
      'test': test,
   }
   return HttpResponse(render_to_response('testing/tests/one_test/one_test.html', context))

