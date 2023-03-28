from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from .tasks import send_mail


def order_create(request):
    '''
    Создание заказа
    '''
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)

            subject = f'LogoiskZap, номер заказа: {order.id}'
            message = f'{order.first_name},\n\nВаш заказ принят, номер заказа: {order.id}.'
            
            send_mail(message=f'{order.first_name},Ваш заказ принят, номер заказа: {order.id}.', recipient=order.email, subject=f'LogoiskZap, номер заказа: {order.id}')
            # send email
            
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
