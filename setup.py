from setuptools import setup, find_packages

setup(
    name='django-filebrowser',
    version='3.0nograppelli',
    description='Media-Management with the Django Admin-Interface.',
    author='Patrick Kranzlmueller',
    author_email='patrick@vonautomatisch.at',
    url='http://code.google.com/p/django-filebrowser/',
    packages=find_packages(),
    include_package_data=True,
    package_data = {'filebrowser': ['templates/filebrowser/*.html',
                                    'templates/filebrowser/include/*',
                                    'locale/*/LC_MESSAGES/*',
                                    'static/filebrowser/*/*'],
                    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
