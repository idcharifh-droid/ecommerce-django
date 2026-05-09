from django.shortcuts import get_object_or_404, render
from .models import Product
from django.shortcuts import redirect
from .models import CartItem, Order

def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        'products/product_list.html',
        {'products': products}
    )


def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )

from django.contrib.auth.decorators import login_required


@login_required
def cart(request):

    return render(
        request,
        'products/cart.html'
    )

@login_required
def add_to_cart(request, id):

    product = get_object_or_404(Product, id=id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    total = sum(item.total_price() for item in cart_items)

    return render(
        request,
        'products/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


@login_required
def place_order(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    total = sum(item.total_price() for item in cart_items)

    Order.objects.create(
        user=request.user,
        total=total
    )

    cart_items.delete()

    return redirect('orders')


@login_required
def orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'products/orders.html',
        {
            'orders': orders
        }
    )