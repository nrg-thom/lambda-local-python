default: build

build:
		python setup.py sdist bdist_wheel

publish: build
		twine upload dist/*

clean:
		rm -r build & rm -r dist & rm -r lambda_local_python.egg-info
