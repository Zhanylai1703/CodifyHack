from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.response import Response
from .models import Form, FormHistory
from .serializers import FormSerializer, FormHistorySerializer


class FormCreateView(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def create(self, request,  *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        form = serializer.save()
        FormHistory.objects.create(form=form)
        send_mail(
            'Новая форма на сайте',
            f'Имя: {serializer.validated_data["name"]}\nEmail: {serializer.validated_data["email"]}\nСообщение: {serializer.validated_data["text_form"]}',
            'kasymkulovajanylai@gmail.com',
            ['kasymkulovajanylai@gmail.com'], 
            fail_silently=False,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class FormHistoryListAPIView(generics.ListAPIView):
    queryset = FormHistory.objects.all()
    serializer_class = FormHistorySerializer