import telebot
from django.shortcuts import render, redirect
from django.db.models import Sum


from .forms import OrderForm
from .models import HomepageBlock, MainContent, Order



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
                  f"адрес: {address}\n" \
                  f"примечание: {note}"
            bot.send_message(chat_id=-406255858, text=msg)
            form.save()
            return redirect('home')
    else:
        form = OrderForm()
        return render(request, 'index.html', {'items': items, 'form': form, 'main': main})


def dashboard(request):
    orders = Order.objects.all()
    count = len(orders)
    result_sum = Order.objects.aggregate(Sum('summ'))
    result_costs = Order.objects.aggregate(Sum('costs'))
    # result_total = result_sum - result_costs
    return render(
        request,
        'dashboard.html',
        {
            'sum': result_sum,
            'costs': result_costs,
            # 'total': result_total,
            'count': count,
        }
    )