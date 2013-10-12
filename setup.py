from setuptools import setup, find_packages

version = '0.1'

setup(name='collective.favoritesstringinterp',
      version=version,
      description="Provides ${id} style string interpolation for "
      "`collective.favorites`",
      long_description=open("README.txt").read() + "\n" +
      open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          ],
      keywords='favorites e-mail string interpretation',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.favorites',
          'plone.stringinterp',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
