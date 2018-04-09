from django.core.mail import send_mail
from django.template import Template, Context

from products.models import Product
from my_shop.celery import app

REPORT_TEMPLATE = """
Here's how you did till now:

{% for product in products %}
        "{{ product.name }}": viewed {{ product.views }} times |
{% endfor %}
"""


@app.task
def send_view_count_report():
    products = Product.objects.all()
    template = Template(REPORT_TEMPLATE)
    send_mail('Your shop activity',
              template.render(context=Context({'products': products})),
              'panaev.smtp@gmail.com',
              ['2853@inbox.ru'], fail_silently=False
              )
