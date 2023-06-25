from django.shortcuts import render
from django.views import View


class testpage(View):
        def get(self, request, *args, **kwargs):
            return render(request, 'u_app/index.html')
