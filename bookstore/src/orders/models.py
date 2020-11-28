from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        related_name = 'carts',
        on_delete = models.PROTECT,
        blank = True,
        null = True
    )

    created_date = models.DateTimeField(
        "Created Date",
        auto_now_add=True,
        null=True,
        blank=True
    )

    updated_date = models.DateTimeField(
        "Updated Date",
        auto_now=True,
        null=True,
        blank=True
    )

    def total_price(self):
        price = 0
        for book in self.books.all():
            price += book.price
        return price


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books'
    )

    quantity = models.IntegerField(
        'Quantity',
        default=1
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='book_in_cart',
        default=1
    )

    price = models.DecimalField(
        'Price',
        max_digits=5,
        decimal_places=2,
    )

    def book_total_price(self):
        return self.quantity * self.book.price
    
    def __str__(self):
        return f"{self.book} in cart"


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='orders',
        blank=True,
        null=True
    )

    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT,
        related_name='order',
        verbose_name='Order',
    )
    name = models.CharField(
        verbose_name='name',
        max_length=255,
    )
    phone = models.CharField(
        verbose_name='Phone number',
        max_length=20,
    )
    email = models.EmailField(
        verbose_name='E-mail',
        max_length=40,
    )
    DELIVERY_CHOICES = [
        ('pu', 'Self pickup'),
        ('cr', ' Courrier delivery'),
        ('pt', 'Postal delivery')
    ]
    delivery = models.CharField(
        verbose_name='Delivery type',
        max_length=2,
        choices=DELIVERY_CHOICES,
        default='pu'
    )
    create_date = models.DateTimeField(
        verbose_name='Created date',
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        verbose_name='Update date',
        auto_now=True,
        auto_now_add=False,
    )
    already_paid = models.BooleanField(
        verbose_name='Paid',
        default=False
    )
