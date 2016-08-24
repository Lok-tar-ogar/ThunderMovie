from django.test import TestCase

# Create your tests here.
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    # return ["Hello World"] # python2
    return "Hello World"  # python3