# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Political Candidate'
copyright = '2024, Tawonga Taibu'
author = 'Tawonga Taibu'
release = '25/09/2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.imgconverter',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Using Read the Docs theme for better appearance
html_static_path = ['_static']

# Adding path to your project to enable autodoc
import os
import sys

# Adjust the path as necessary to point to your project directory
sys.path.insert(0, os.path.abspath('../..'))

# Set the environment variable for Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'politicalcandidate.settings'  # Replace with your Django project settings


