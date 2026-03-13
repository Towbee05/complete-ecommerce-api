from django.shortcuts import render

# Create your views here.

class RandomAPIClass:
    def get(self, request):
        return {
            "details": "Just getting a random url"
        }