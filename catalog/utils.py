from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


class ObjectCreateMixin:
    form_model = None
    template_name = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, ):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template_name, context={'form': bound_form})


class ObjectEditMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, *args, **kwargs):
        edit_obj = self.model.objects.get(pk=self.kwargs['pk'])
        form = self.form_model(instance=edit_obj)
        return render(request, self.template, context={'form': form, 'obj': edit_obj})

    def post(self, request, *args, **kwargs):
        edit_obj = self.model.objects.get(pk=self.kwargs['pk'])
        bound_form = self.form_model(request.POST, instance=edit_obj)

        if bound_form.is_valid():
            edit_obj = bound_form.save()
            return redirect(edit_obj)
        return render(request, self.template, context={'form': bound_form, 'obj': edit_obj})


class ObjectDeleteMixin:
    model = None
    template = None
    success_url = None

    def get(self, request,  *args, **kwargs):
        obj = self.model.objects.get(pk=self.kwargs['pk'])
        return render(request, self.template, context={'obj': obj})

    def post(self, request,  *args, **kwargs):
        obj = self.model.objects.get(pk=self.kwargs['pk'])
        obj.delete()
        return redirect(self.success_url)


