from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    version='0.0.1',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    long_description="README.md",
{% if cookiecutter.python_interpreter == 'python3' %}
    python_requires='>3.5',
{% endif %}
    install_requires=[
                     "click",
                     "python-dotenv>=0.5.1",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
