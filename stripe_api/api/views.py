import stripe

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from items.models import Item


@csrf_exempt
def stripe_config(request):
    """Получаем публичный ключ stripe из файла настроек Django"""

    if request.method == 'GET':
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLISHABLE_KEY
        }
        return JsonResponse(stripe_config, safe=False)


class OneItemCheckout(generics.RetrieveAPIView):
    """Генерируем checkout session для покупки товара"""

    def get(self, request, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item_id = self.kwargs['id']
        try:
            item = get_object_or_404(Item, pk=item_id)
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': item.currency,
                            'unit_amount': int(item.price * 100),
                            'product_data': {
                                 'name': item.name,
                                 'description': item.description
                            }
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=settings.SITE_URL + '?success=true',
                cancel_url=settings.SITE_URL + '?cancel=true',
            )
            return JsonResponse({
                'sessionId': checkout_session['id']
            })
        except Exception as e:
            return JsonResponse(
                {
                    'msg': 'Something went wrong',
                    'error': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ItemPage(generics.RetrieveAPIView):
    """Возвращаем html шаблон с объектом товара"""
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, **kwargs):
        item_id = self.kwargs['id']
        item = get_object_or_404(Item, pk=item_id)
        return Response({'item': item}, template_name='item.html')
