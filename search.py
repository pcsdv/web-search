# views + url + template
from django.db.models import Q


def psearch_view(request):
	if request.method == 'POST':
		srch = request.POST['srhav']

		if srch:
			match = Patient.objects.filter(Q(name__icontains=srch))

			if match:
				return render(request,'dems/psearch.html',{'srp': match})
	#		else:
	#			messages.error(request,'no result found')
			else:
				return HttpResponseRedirect("/dems/search/")

	return render(request,'dems/psearch.html')
	---------------------------------
	# url below

	path('search/',views.psearch_view,name='search'),
	-----------------------------------------
	# template below

<body>
	<div class="container">
	<div class="jumbotron">
	<h1>Patient's information</h1>
	<form method="POST" action="{% url 'search' %}">
	{% csrf_token %}
	<div class="form-group">
	<div class="col-lg-5">
	<input type="text" name="srhav" class="form-control" placeholder="Enter name"/>
	</div>
	</div>
	<label class="col-lg-2">
	<button type="submit" class="btn btn-danger">Search</button>
	</label>
	</form><br><br>

	<div>
	{% if messages %}
	<ul class="messages">
	{% for k in messages %}
	<li style="color:red">{{ k }}</li>
	{% endfor %}
	</ul>
	{% endif %}
	</div><br>

	<div style="color:white">
	{% if srp %}
	{% for p in srp %}
	<table border="0px" width="1000px">
	<tr>
	<td><h4>{{p.name}}</h4></td>
	<td><h4>{{p.remedy}}</h4></td>
	<td><h4>{{p.dated}}</h4></td>
	</tr>
	</table>
	<br>
	{% endfor %}
	{% endif %}
	</div>
	</div>
	</div>
</body>
