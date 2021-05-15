import telebot
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import HomepageBlock, MainContent

bot = telebot.TeleBot('1891341441:AAFnpC0ifzToTxYYwMueJJuvtmshQqJz4j4')


def homepage(request):
    items = HomepageBlock.objects.all()
    main = MainContent.objects.first()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            subject = "Новая заявка на сайте.\n"
            machine = form.cleaned_data['machine']
            malfunction = form.cleaned_data['malfunction']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            note = form.cleaned_data['note']
            msg = f"{subject}" \
                  f"сма: {machine}\n" \
                  f"неисправность: {malfunction}\n" \
                  f"телефон: {phone}\n" \
                  f"алрес: {address}\n" \
                  f"примечание: {note}"
            bot.send_message(chat_id=959339948, text=msg)
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
        return render(request, 'index.html', {'items': items, 'form': form, 'main': main})
