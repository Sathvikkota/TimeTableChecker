import csv

from django.core.checks import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils.html import escape

from .forms import CSVUploadForm
from .models import Admin


def user_login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        print(name, password)
        #
        flag = Admin.objects.filter(Q(name=name) & Q(password=password))
        print(flag)

        if flag:
            request.session['username'] = name
            return redirect('admin_home')
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


filtered_out_rows = []


def check_conditions(new_row, existing_data, clash_data):
    # You need to add the conditions where clashes might occur :)
    for existing_row in existing_data:
        if existing_row['day'] == new_row['day'] and existing_row['empid'] == new_row['empid'] and existing_row[
            'hour'] == new_row['hour'] and existing_row['section'] == new_row['section'] and existing_row['room'] != \
                new_row['room']:
            clash_data.append({'clash_row': new_row, 'other_row': existing_row, 'type': 'Room_Clash!! '})
            return False

        if existing_row['day'] == new_row['day'] and existing_row['hour'] == new_row['hour'] and existing_row[
            'empid'] == new_row['empid'] and existing_row['coursecode'] != new_row['coursecode']:
            clash_data.append({'clash_row': new_row, 'other_row': existing_row, 'type': 'Course_Clash!! '})
            return False

        if existing_row['day'] == new_row['day'] and existing_row['hour'] == new_row['hour'] and existing_row['room'] == \
                new_row['room'] and existing_row['empid'] != new_row['empid']:
            clash_data.append({'clash_row': new_row, 'other_row': existing_row, 'type': 'Emp_Clash!! '})
            return False

        if existing_row['day'] == new_row['day'] and existing_row['hour'] == new_row['hour'] and existing_row[
            'empid'] == new_row['empid'] and existing_row['section'] != new_row['section']:
            clash_data.append({'clash_row': new_row, 'other_row': existing_row, 'type': 'Section_Clash!! '})
            return False

    return True


def get_clashes_by_type(clash_type, filtered_out_rows):
    if clash_type == 'room':
        return [row for row in filtered_out_rows if row.get('type') == 'Room_Clash!! ']
    elif clash_type == 'course':
        return [row for row in filtered_out_rows if row.get('type') == 'Course_Clash!! ']
    elif clash_type == 'emp':
        return [row for row in filtered_out_rows if row.get('type') == 'Emp_Clash!! ']
    elif clash_type == 'section':
        return [row for row in filtered_out_rows if row.get('type') == 'Section_Clash!! ']
    else:
        return filtered_out_rows

csv_data=[]

def admin_home(request,clash_type=None):
    global filtered_out_rows
    clash_data = filtered_out_rows
    global  csv_data 

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            try:
                decoded_file = csv_file.read().decode('utf-8')
                csv_reader = csv.DictReader(decoded_file.splitlines(), delimiter=',')
                csv_data = list(csv_reader)

                # Conditions Check
                for row in csv_data:
                    if not check_conditions(row, csv_data, clash_data):
                        if row not in filtered_out_rows:
                            filtered_out_rows.append(row)
            except Exception as e:
                messages.error(request, 'Error processing CSV file.')
    else:
        form = CSVUploadForm()

    # Filter data based on clash_type
    clash_type = request.GET.get('clash_type')
    print(clash_type)
    # # if clash_type and clash_type != 'all':
    clash_data = get_clashes_by_type(clash_type, filtered_out_rows)
    print(clash_data)
    # print(csv_data)
    
    print(clash_data)
    return render(request, 'admin_home.html', {'form': form, 'csv_data': csv_data, 'clash_data': clash_data})

def filterByclash(request,clash_type):
    
    print(csv_data)
    # # if clash_type and clash_type != 'all':
    clash_data = get_clashes_by_type(clash_type, filtered_out_rows)
    print(clash_data)
    return render(request,"admin_home.html",{'csv_data':csv_data,'clash_data': clash_data})