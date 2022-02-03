from django.db import models
from django import forms
from django.db.models.deletion import SET_NULL
from modelcluster.models import ClusterableModel
from django_extensions.db.fields import AutoSlugField
from wagtail.core.models import Orderable, Page, Collection
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import BaseChooserPanel, RichTextField, RichTextFieldPanel
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from core.blocks import BlockQuote, CardBlock

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey, ParentalManyToManyField

class HomePage(Page):
    """ Page home Model """
    template_name = "/templates/home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(blank=True)
    banner_body = RichTextField(null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False, null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_cta = models.ForeignKey("wagtailcore.Page",
                                blank=True, null=True,
                                on_delete=models.SET_NULL, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel('banner_body', classname="full"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta"),
    ]


    class Meta:
        verbose_name = "Home page Atlas RDV"
        verbose_name_plural = "Accueil Bakery"


#--------------------------------
#---- Standard page
#--------------------------------
class StandardPage(Page):
    created = models.DateField("date de creation")
    intro = models.CharField(max_length=250)

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('block_quote', BlockQuote()),
        ('embedBlock', EmbedBlock()),
        ('card_block', CardBlock()),

    ], blank=True)

    embed_block = EmbedBlock(
        help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks',
        icon="fa-s15",
        template="blocks/embed_block.html")

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('created'),
        StreamFieldPanel('body'),
    ]
    
