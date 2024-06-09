class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Value must be an Author instance")
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Value must be a Book instance")
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Value must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Value must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


# Demonstration of the code
if __name__ == "__main__":
    # Create authors
    author1 = Author("Author One")
    author2 = Author("Author Two")

    # Create books
    book1 = Book("Book One")
    book2 = Book("Book Two")

    # Create contracts
    contract1 = author1.sign_contract(book1, "2024-01-01", 5000)
    contract2 = author1.sign_contract(book2, "2024-02-01", 7000)
    contract3 = author2.sign_contract(book1, "2024-03-01", 6000)

    # Display authors and their total royalties
    print(f"Total royalties for {author1.name}: {author1.total_royalties()}")  # Output: 12000
    print(f"Total royalties for {author2.name}: {author2.total_royalties()}")  # Output: 6000

    # Display books and their authors
    print(f"Authors for {book1.title}: {[author.name for author in book1.authors()]}")  # Output: ['Author One', 'Author Two']
    print(f"Authors for {book2.title}: {[author.name for author in book2.authors()]}")  # Output: ['Author One']

    # Display contracts by date
    print(f"Contracts on 2024-01-01: {[contract.author.name for contract in Contract.contracts_by_date('2024-01-01')]}")  # Output: ['Author One']
    print(f"Contracts on 2024-03-01: {[contract.author.name for contract in Contract.contracts_by_date('2024-03-01')]}")  # Output: ['Author Two']
