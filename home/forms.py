from django import forms
from .models import Order

CHOICES = (
    ('Диагностика', 'Диагностика'),
    ('Модуль управления', 'Модуль управления'),
    ('Не нагревает воду', 'Не нагревает воду'),
    ('Ремонт электродвигателя', 'Ремонт электродвигателя'),
    ('Не сливает воду', 'Не сливает воду'),
    ('Не набирает воду', 'Не набирает воду'),
    ('Утечка воды', 'Утечка воды'),
    ('Не крутит барабан', 'Не крутит барабан'),
    ('Устранение засора', 'Устранение засора'),
    ('Установка', 'Установка'),
    ('Не включается', 'Не включается'),
    ('Прочие неисправности', 'Прочие неисправности'),
)

MACHINES = (
    ('---------', '---------'),
    ('Ariston', 'Ariston'),
    ('LG', 'LG'),
    ('Indesit', 'Indesit'),
    ('Samsung', 'Samsung'),
    ('Beko', 'Beko'),
    ('Gorenje', 'Gorenje'),
    ('Candy', 'Candy'),
    ('Ardo', 'Ardo'),
    ('Electrolux', 'Electrolux'),
    ('Eurolux', 'Eurolux'),

)

TIME = (
    ('**:**', '**:**'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('machine', 'malfunction', 'phone', 'address', 'time', 'note')
        widgets = {
            'machine': forms.Select(choices=MACHINES),
            'malfunction': forms.Select(choices=CHOICES),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0 *** ** ** **'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш домашний адрес'}),
            'time': forms.Select(choices=TIME),
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Дополнительная информация...'}),
        }
