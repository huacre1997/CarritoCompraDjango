from django.shortcuts import render
from django.contrib.auth.views import LoginView

class LoginFormView(LoginView):
    template_name="login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context
    

    # def dispatch(self,request,*args, **kwargs):
    #     print(request.user)
    #     if request.user.is_authenticated:
    #         return HttpResponseRedirect(self.success_url)
    #     return super().dispatch(request, *args, **kwargs)

    # def form_valid(self,form):
    #     login(self.request,form.get_user())
    #     return HttpResponseRedirect(self.success_url)
        