from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.template.loader import render_to_string
import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login


class LoginFormView(LoginView):
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("base:index")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                data = {
                'stat': True}
            return JsonResponse(data)
        else:
            data = {
                'stat': False,
                'form': render_to_string(self.template_name, {'form': form}, request=request)}
            return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context


# class LogoutFormView(LogoutView):
#     def dispatch(self,request,*args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect("base:index")
#         return super().dispatch(request, *args, **kwargs)

    # def form_valid(self,form):
    #     login(self.request,form.get_user())
    #     return HttpResponseRedirect(self.success_url)
