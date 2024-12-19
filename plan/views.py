from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('/login/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def reset_password(request):
    form = PasswordResetForm()
    return render(request, 'reset_password.html', {'form': form})

from django.shortcuts import render

def home(request):
    # ข้อมูลตัวอย่างสำหรับแผนอาหาร
    meal_plan = {
        'breakfast': [
            {'name': 'ข้าวโอ๊ตกับผลไม้', 'description': 'ข้าวโอ๊ตไม่ขัดสี เติมผลไม้สด เช่น แอปเปิ้ลหรือเบอร์รี่'},
            {'name': 'ไข่ต้มและขนมปังโฮลวีท', 'description': 'เพิ่มผักสด เช่น แตงกวาหรือมะเขือเทศ'},
        ],
        'lunch': [
            {'name': 'ข้าวกล้องกับอกไก่ย่าง', 'description': 'เสิร์ฟพร้อมผักลวก เช่น บร็อคโคลีหรือแครอท'},
            {'name': 'สลัดปลาทูน่า', 'description': 'ใช้ปลาทูน่าในน้ำเกลือและน้ำสลัดแบบไขมันต่ำ'},
        ],
        'dinner': [
            {'name': 'แกงจืดเต้าหู้ไข่กับผัก', 'description': 'เพิ่มโปรตีนด้วยไก่บดหรือหมูสับแบบไม่ติดมัน'},
            {'name': 'ปลานึ่งกับน้ำจิ้มซีฟู้ด', 'description': 'เสิร์ฟพร้อมผักต้มและข้าวกล้องเล็กน้อย'},
        ],
    }

    return render(request, 'home.html', {'meal_plan': meal_plan})
