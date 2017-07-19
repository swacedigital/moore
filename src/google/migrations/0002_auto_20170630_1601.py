# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 14:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googleformpage',
            name='results_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(template='blocks/paragraph.html')), ('image_description', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('image_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('icons', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Material icon font icon text, as found on: https://material.io/icons')), ('title', wagtail.wagtailcore.blocks.CharBlock()), ('description', wagtail.wagtailcore.blocks.CharBlock()))))), ('hide_on_med', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('image_icons', wagtail.wagtailcore.blocks.StructBlock((('description', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('image_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('hide_on_med', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('overlay', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('logos', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), icon='fa-pied-piper', label='Logos', template='blocks/logos.html')), ('counters', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('counters', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Material icon font icon text, as found on: https://material.io/icons')), ('value', wagtail.wagtailcore.blocks.CharBlock()), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)))))), ('style', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark')]))))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='blocks/image.html'))), blank=True),
        ),
        migrations.AlterField(
            model_name='googleformpage',
            name='results_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(template='blocks/paragraph.html')), ('image_description', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('image_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('icons', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Material icon font icon text, as found on: https://material.io/icons')), ('title', wagtail.wagtailcore.blocks.CharBlock()), ('description', wagtail.wagtailcore.blocks.CharBlock()))))), ('hide_on_med', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('image_icons', wagtail.wagtailcore.blocks.StructBlock((('description', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('image_alignment', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')])), ('hide_on_med', wagtail.wagtailcore.blocks.BooleanBlock(required=False))))), ('overlay', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('button', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('logos', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailimages.blocks.ImageChooserBlock(), icon='fa-pied-piper', label='Logos', template='blocks/logos.html')), ('counters', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock()), ('counters', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Material icon font icon text, as found on: https://material.io/icons')), ('value', wagtail.wagtailcore.blocks.CharBlock()), ('description', wagtail.wagtailcore.blocks.CharBlock(required=False)))))), ('style', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('light', 'Light'), ('dark', 'Dark')]))))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='blocks/image.html'))), blank=True),
        ),
    ]