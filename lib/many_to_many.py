class Book:
    _all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        Book._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def contracts(self):
        return [contract for contract in Contract._all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})


class Author:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        Author._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    def contracts(self):
        return [contract for contract in Contract._all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    _all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of the Author class.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of the Book class.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer.")
        self._royalties = value

    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls._all, key=lambda c: datetime.strptime(c.date, "%Y-%m-%d"))

    @classmethod
    def all(cls):
        return cls._all