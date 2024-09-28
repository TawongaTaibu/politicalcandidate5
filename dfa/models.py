"""
models.py
---------

This module defines the `News` model for a Django application, which represents
news articles published on the website. Each news article includes a title, content,
and a publication date.

Classes:
    News: A model representing a news article with a title, content, and publication date.
"""

from django.db import models

class News(models.Model):
    """
    A model representing a news article.

    Attributes:
        title (str): The title of the news article. Maximum length is 200 characters.
        content (str): The content or body of the news article.
        date (date): The publication date of the news article.
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        """
        Returns the string representation of the News object.

        The string returned is the title of the news article.

        Returns:
            str: The title of the news article.
        """
        return self.title
