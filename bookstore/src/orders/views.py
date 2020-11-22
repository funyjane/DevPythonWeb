from django.views.generic import TemplateView, DeleteView, RedirectView
from django.urls import reverse_lazy

from book import models as book_models
from . import models



class CartView(TemplateView):
    template_name = 'orders/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        # step-1: get a cart
        if not isinstance(user, models.User):
            user = None
        
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = models.Cart.objects.create(customer=user)
                self.request.session['cart_id'] = cart.pk
        else:
            cart = models.Cart.objects.create(customer=user)
            self.request.session['cart_id'] = cart.pk
        context["cart"] = cart
        # step-2: add a book to the cart
        book_id = self.request.GET.get('book')
        if not book_id:
            return context

        book =  book_models.Book.objects.filter(pk=int(book_id)).first()
        #check if book exists
        if book:
            book_in_cart, created = models.BookInCart.objects.get_or_create(
                book = book,
                cart = cart,
                defaults = {
                    'quantity': 1,
                    'price': book.price
                } 
            )
            if not created:
                book_in_cart.quantity = book_in_cart.quantity + 1
                book_in_cart.price = book_in_cart.book_total_price()
                book_in_cart.save()

        context["book"] = book
        return context
    
class DeleteBookInCart(DeleteView):
    model = models.BookInCart
    template = template_name = 'orders/delete-book-in-cart.html'
    success_url = reverse_lazy('orders:cart')

class CartUpdateView(RedirectView):
    def get_redirect_url(self):
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
        else:
            #redirect to error page
            pass
        button = self.request.POST.get('submit_button')
        if button == 'edit':
            obj_list = []
            for book_in_cart_id, quantity in self.request.POST.items():
                if book_in_cart_id not in ['csrfmiddlewaretoken', 'submit_button']:
                    book_in_cart = models.BookInCart.objects.get(pk=int(book_in_cart_id))
                    if book_in_cart.cart.pk == self.cart_id:
                        book_in_cart.quantity = int(quantity)
                        obj_list.append(book_in_cart)
            models.BookInCart.objects.bulk_update(obj_list, ['quantity'])
        else:
            pass
            #checkout

        return reverse_lazy('orders:cart')