#!/bin/bash
rm -rf ./dist
pip uninstall s2tutil
python setup.py sdist bdist_wheel
pip install -e .
# twine upload dist/*