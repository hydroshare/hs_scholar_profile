from django.views.generic import ListView,DetailView
from .models import Person,Organization,ScholarGroup

class PersonList(ListView):
    model = Person
    template_name = "pages/person_list.html"
    queryset = Person.objects.all()
    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class OrganizationList(ListView):
    model = Organization
    template_name = "pages/organization_list.html"

    def get_context_data(self, **kwargs):
        context = super(OrganizationList, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class ScholarGroupList(ListView):
    model = ScholarGroup
    template_name = "pages/scholargroup_list.html"

class PersonDetail(DetailView):
    model = Person
    queryset = Person.objects.all()
    template_name = "pages/person.html"

    def get_context_data(self, **kwargs):
        context = super(PersonDetail, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

    def get_object(self,**kwargs):
        # Call the superclass
        object = super(PersonDetail, self).get_object(**kwargs)
        # Record the last accessed date
        #object.last_accessed = timezone.now()
        #object.save()
        # Return the object
        return object

class OrganizationDetail(DetailView):
    model = Organization
    queryset = Organization.objects.all()
    template_name = "pages/organization.html"

    def get_context_data(self, **kwargs):
        context = super(OrganizationDetail, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

    def get_object(self,**kwargs):
        # Call the superclass
        object = super(OrganizationDetail, self).get_object(**kwargs)
        # Record the last accessed date
        #object.last_accessed = timezone.now()
        #object.save()
        # Return the object
        return object

class ScholarGroupDetail(DetailView):
    model = ScholarGroup
    queryset = ScholarGroup.objects.all()
    template_name = "pages/scholargroup.html"

    def get_context_data(self, **kwargs):
        context = super(ScholarGroupDetail, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

    def get_object(self,**kwargs):
        # Call the superclass
        object = super(ScholarGroupDetail, self).get_object(**kwargs)
        # Record the last accessed date
        #object.last_accessed = timezone.now()
        #object.save()
        # Return the object
        return object
