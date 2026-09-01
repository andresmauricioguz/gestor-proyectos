from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.models import User

def registro(request):
    datos= ''
    errores = []

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        passaword1 = request.POST.get('passaword1')
        passaword2 = request.POST.get('passaword2')

        datos = request.POST

        if passaword1 != passaword2:
            errores.append('las contraseñas no conciden')

        if User.objects.filter(username=username).exists():
            errores.append('el nombre del usuario ya existe')

        if User.objects.filter(email=email).exists():
            errores.append('el correo electronico ya esta registrado')

        if not errores:
            #create_user hashea la contraseña automatica
            user = User.objects.create_user(
                username=username,
                email=email,
                password=passaword1,
                first_name=first_name,
                last_name=last_name
            )

            login(request, user)
            return redirect('home')
    return render (request, 'registro.html', {'errores': errores, 'datos':datos})