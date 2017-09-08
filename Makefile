docs:
	pandoc --from=markdown --to=rst --output=README.rst README.md

upload: docs
	python2.7 setup.py sdist upload -r pypi
	python2.7 setup.py bdist_wheel upload -r pypi

develop: docs
	python setup.py develop
