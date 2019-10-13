from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 
from .models import Classroom, Student
from .forms import ClassroomForm, StudentForm, SignupForm, SigninForm


def classroom_list(request):
	classrooms = Classroom.objects.all()
	context = {
		"classrooms": classrooms,
	}
	return render(request, 'classroom_list.html', context)


def classroom_detail(request, classroom_id):
	classroom = Classroom.objects.get(id=classroom_id)
	students=classroom.student_set.all().order_by("name","exam_grade")
	context = {
		"classroom": classroom,
		"students": students
	}
	return render(request, 'classroom_detail.html', context)


def classroom_create(request):
	form = ClassroomForm()
	if request.user.is_authenticated:
		if request.method == "POST":
			form = ClassroomForm(request.POST, request.FILES or None)
			if form.is_valid():
				classroom = form.save(commit=False)
				classroom.teacher = request.user
				classroom.save()
				messages.success(request, "Successfully Created!")
				return redirect('classroom-list')
			print (form.errors)
		context = {
		"form": form,
		}
		return render(request, 'create_classroom.html', context)
	else:
	    return redirect('signin')	


def classroom_update(request, classroom_id):
	classroom = Classroom.objects.get(id=classroom_id)
	form = ClassroomForm(instance=classroom)
	if request.user.is_authenticated:
		if request.method == "POST":
			form = ClassroomForm(request.POST, request.FILES or None, instance=classroom)
			if form.is_valid():
				form.save()
				messages.success(request, "Successfully Edited!")
				return redirect('classroom-list')
			print (form.errors)
		context = {
		"form": form,
		"classroom": classroom,
		}
		return render(request, 'update_classroom.html', context)
	else:
	    return redirect('signin')


def classroom_delete(request, classroom_id):
	if request.user.is_authenticated:
		Classroom.objects.get(id=classroom_id).delete()
		messages.success(request, "Successfully Deleted!")
		return redirect('classroom-list')
	else:
	   return redirect('signin')




def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("classroom-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('classroom-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("classroom-list")

def add_student(request, classroom_id ):
	classroom_obj = Classroom.objects.get(id=classroom_id)
	form = StudentForm()
	if request.user == classroom_obj.teacher :
		if request.method == "POST":
			form = StudentForm(request.POST, request.FILES or None)
			if form.is_valid():
				student = form.save(commit=False)
				student.classroom = Classroom.objects.get(id=classroom_id)
				student.save()
				messages.success(request, "Successfully Added !")
				return redirect('classroom-detail', classroom_id)
				# return redirect('classroom-detail', kwargs={"classroom_id": classroom_id})
			print (form.errors)
		context = {
		"form": form,
		"classroom_obj": classroom_obj,
		}
		return render(request, 'add_student.html', context)
	else:
	    return redirect('classroom-detail')

def student_update(request, classroom_id, student_id):
	classroom = Classroom.objects.get(id=classroom_id)
	student = Student.objects.get(id=student_id)
	form = StudentForm(instance=student)
	if request.user == classroom.teacher :
		if request.method == "POST":
			form = StudentForm(request.POST, request.FILES or None, instance=student)
			if form.is_valid():
				form.save()
				messages.success(request, "Successfully Edited!")
				return redirect('classroom-detail',classroom_id)
			print (form.errors)
		context = {
		"form": form,
		"classroom": classroom,
		"student": student,
		}
		return render(request, 'update_student.html', context)
	else:
	    return redirect('signin')


def student_delete(request, classroom_id, student_id):
	classroom = Classroom.objects.get(id=classroom_id)
	if request.user == classroom.teacher :
		Student.objects.get(id=student_id).delete()
		messages.success(request, "Successfully Deleted!")
		return redirect('classroom-detail', classroom_id)
	else:
		return redirect("signin")

	
