#######################
Django Chinese Medicine
#######################

Django chinese medicine is a django app to search by symtoms for disease
patterns in chinese medicine. After coosing a disease pattern you get a list of
apropriate therapys. Which you can investigate in detail.


Installation
============


Requirements:

* `Django==1.8`_
* `django-crispy-forms`_ ==1.5
* `Hide Seek`_


Change to the directory where the `manage.py` is. Clone the repo::

   $ git clone https://github.com/shoul/django_chinese_medicine.git

Add `django_chinese_medicine` to `INSTALLED_APPS` in youre settings.py::

   INSTALLED_APPS = (
       ...
       'django_chinese_medicine',
       ...
   )


Include the `urls.py` somehow like this::

   urlpatterns = [
       ...
       url(r'^chinese_medicine/', include('django_chinese_medicine.urls')),
       ...
   ]

Migrate django_chinese_medicine to the database::

   $ python manage.py makemigrations django_chinese_medicine
   $ python manage.py migrate


Template
--------

Make shour your'e base template is named `base.html` and has the following
block tags:

* `{% block content %}`
* `{% block footer_script %}`


Now jou can go to you're admin site and insert symptoms and diesease patterns.

.. _Hide Seek: https://github.com/vdw/HideSeek
.. _django-cirspy-forms: https://github.com/maraujop/django-crispy-forms
.. _Django==1.8: https://docs.djangoproject.com/en/1.8/

