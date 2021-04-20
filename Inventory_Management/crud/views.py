from django.http import Http404
from django.shortcuts import render,HttpResponse, redirect
from django.views import View

from .form import EntryForm
from .models import Entries

class IndexView(View):
	def get(self, request):
		return render(request,'index.html',{'entries':Entries.objects.all()})

class CreateView(View):
	entryform = EntryForm()
	def get(self,request):
		return render(request,'create.html',{'form':self.entryform})
	def post(self,request):
		form = EntryForm(request.POST,request.FILES)
		if(form.is_valid()):
			form.save()
		return redirect("crudindex")

class DeleteView(View):
	def get(self,request,entry_id):
		try:
			print(entry_id)
			get_entry = Entries.objects.get(entry_id=entry_id)
			get_entry.delete()
		except Entries.DoesNotExist:
		    raise Http404("Entry does not exist !")
		return redirect("crudindex")

class UpdateView(View):
	def get(self,request,entry_id):
		try:
			get_entry = Entries.objects.get(entry_id=entry_id)
			return render(request,'update.html',{'entry':get_entry})
		except Entries.DoesNotExist:
		    raise Http404("Entry does not exist !")
		return redirect("crudindex")
	def post(self,request,entry_id):
		get_entry = Entries.objects.get(entry_id=entry_id)
		form = EntryForm(request.POST,request.FILES,instance= get_entry)
		if(form.is_valid()):
			form.save()
		return redirect("crudindex")