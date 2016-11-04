from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-faulthandler',
    'pytest-mock',
    'pytest-qt',
    'pytest-xvfb',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=['{{ cookiecutter.package_name }}', '{{ cookiecutter.package_name }}.images',
              '{{ cookiecutter.package_name }}.tests'],
    package_data={'{{ cookiecutter.package_name }}.images': ['*.png']},
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.application_title }}={{ cookiecutter.package_name }}.{{ cookiecutter.application_name }}:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
