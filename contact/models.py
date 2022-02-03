from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import ( 
                                FieldPanel,
                                InlinePanel, 
                                MultiFieldPanel,
                                FieldRowPanel,
                                )
from wagtail.core.fields import  RichTextField
from wagtail.contrib.forms.models import  (
    AbstractFormField, AbstractEmailForm)

# Create your models here.

class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    http://docs.wagtail.io/en/latest/reference/contrib/forms/index.html
    """
    page = ParentalKey('ContactPage',
                       on_delete=models.CASCADE,
                       related_name="form_fields",)
    

class ContactPage(AbstractEmailForm):
    template_name = 'contact/contact_page.html'

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        FieldPanel('thank_you_text'),
        InlinePanel('form_fields', label="Form fields"),
        MultiFieldPanel([
                        FieldRowPanel([ 
                                        FieldPanel('from_address', classname='col6'), 
                                        FieldPanel('to_address', classname='col6')
                                        ])
                        ,
                        FieldPanel('subject'),
        ],
        heading = "Email settings")
    ]
