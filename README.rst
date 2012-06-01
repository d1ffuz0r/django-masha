============
django-masha
============

Django app for easy integration MaSha_ to your django project


Setup
_____


::

  $ git clone git://github.com/d1ffuz0r/django-masha.git
  $ cd django-masha
  $ make deps
  $ make build
  $ [sudo] python setup.py install


Use
___


settings.py
~~~~~~~~~~~


::
  
  INSTALLED_APPS = (
      ...
      'django_masha'
  )


also you can setup settings MaSha


::

  MASHA_CFG = {
      'selectable': 'selectable'
  }
  MASHA_JQUERY = True # if you use jQuery


templates
~~~~~~~~~
  

::
  
  {% load masha %}
  <html>
  <head>
  ...
  {% masha %}
  </head>
  ...


.. _MaSha: http://mashajs.com