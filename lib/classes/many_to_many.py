class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Validate author
        if not isinstance(author, Author):
            return
        # Validate magazine
        if not isinstance(magazine, Magazine):
            return
        # Validate title
        if not (isinstance(title, str) and 5 <= len(title) <= 50):
            return
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title is immutable and must be a string of length 5-50
        if hasattr(self, "_title"):
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value

class Author:
    def __init__(self, name):
        if not (isinstance(name, str) and len(name) > 0):
            return
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Name is immutable and must be a non-empty string
        if hasattr(self, "_name"):
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})

class Magazine:
    def __init__(self, name, category):
        if not (isinstance(name, str) and 2 <= len(name) <= 16):
            return
        if not (isinstance(category, str) and len(category) > 0):
            return
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (isinstance(value, str) and 2 <= len(value) <= 16):
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not (isinstance(value, str) and len(value) > 0):
            return
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    def contributing_authors(self):
        from collections import Counter
        authors = [article.author for article in self.articles()]
        count = Counter(authors)
        result = [author for author, num in count.items() if num > 2]
        return result if len(result) > 0 else None