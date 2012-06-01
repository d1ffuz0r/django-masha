from setuptools import setup
import django_masha


setup(
    name='django-masha',
    version=django_masha.__version__,
    url='https://github.com/d1ffuz0r/django-masha',
    author=django_masha.__author__,
    author_email='d1fffuz0r@gmail.com',
    description='Easy integration MaSha in django',
    long_description=open('README.rst').read(),
    packages=['django_masha', 'django_masha.templatetags'],
    keywords='django, MaSha, javascript, integration',
    platforms='Any',
    include_package_data=True,
    zip_safe=False
)
