from io import BytesIO
from conf.celery import app
import pdfkit
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@app.task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)

    # create invoice e-mail
    subject = f'My Shop - EE Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'ferdinand-f@mail.ru',
                         [order.email])
    # generate PDF

    html = render_to_string('orders/order/pdf.html', {'order': order})
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_string(html, f'order_{order_id}.pdf', css=settings.STATIC_ROOT + '\css\pdf.css', configuration=config)

    # out = BytesIO()

    # stylesheets = settings.STATIC_ROOT + 'css/pdf.css'
    # weasyprint.HTML(string=html).write_pdf(out,
    #                                        stylesheets=stylesheets)
    # attach PDF file
    # email.attach(f'order_{order.id}.pdf')

    with open(f'order_{order.id}.pdf', 'rb') as content_file:
        content = content_file.read()
    email.attach(f'order_{order.id}.pdf', content, 'application/pdf')

    # email.attach(f'order_{order.id}.pdf',
    #              out.getvalue(),
    #              'application/pdf')
    # send e-mail
    email.send()
