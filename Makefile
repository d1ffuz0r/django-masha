all:
	@echo 'deps - get MaSha from repository'
	@echo 'build - update MaSha files in django_masha and build (default: /static/ url for static)'
	@echo 'install - install django-masha'
	@echo 'clean - clean directory'

build:
	@cp -rv ./MaSha/src/* ./django_masha/static/masha/
	@sed -e 's/..\/img/\/static\/masha\/img/g' ./MaSha/src/css/masha.css > ./django_masha/static/masha/css/masha.css
	@python setup.py build

install:
	python setup.py install

deps:
	@git clone git://github.com/SmartTeleMax/MaSha.git

clean:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf django_masha.egg-info/
	@rm -rf MaSha/
