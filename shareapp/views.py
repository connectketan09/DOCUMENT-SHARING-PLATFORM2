
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
import os
import qrcode


def home(request):
    return render(request, 'upload.html')


def upload_file(request):
    if request.method == 'POST' and request.FILES.get('document'):
        file = request.FILES['document']

        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        request.session['file_name'] = filename

        return redirect('/processing/')

    return redirect('/')


def processing(request):
    return render(request, 'processing.html')


def qr_result(request):
    filename = request.session.get('file_name')

    if not filename:
        return redirect('/')

    # ✅ QR LINK (works locally, deploy later for mobile)
    file_url = request.build_absolute_uri('/download/' + filename)

    qr = qrcode.make(file_url)

    qr_name = f"qr_{filename}.png"
    qr_path = os.path.join("media", qr_name)
    qr.save(qr_path)

    return render(request, 'qr_result.html', {
        'qr_url': '/media/' + qr_name,
    })


def download_file(request, filename):
    file_path = os.path.join('media', filename)

    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response