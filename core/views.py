from django.shortcuts import render


def page_not_found(request, exception):
    # Переменная exception содержит отладочную информацию,
    # выводить её в шаблон пользователской страницы 404 мы не станем
    return render(request, 'core/404.html', {'path': request.path}, status=404)


def server_error(request, *args, **kwargs):
    return render(request, 'core/500.html', status=500)
