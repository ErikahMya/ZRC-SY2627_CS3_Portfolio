
class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.number_of_pages = number_of_pages
        else:
            print("Number of pages must be positive.")
            self.number_of_pages = None

    def display_info(self):
        super().display_info()
        if self.number_of_pages is not None:
            print("Number of pages:", self.number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("Issue number must be positive.")
            self.issue_number = None

    def display_info(self):
        super().display_info()
        if self.issue_number is not None:
            print("Issue number:", self.issue_number)



publication1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)
publication2 = Publication(
    "The Science Journal",
    "John Smith"
)

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Invalid Book", "Unknown Author", 0)


magazine1 = Magazine(
    "National Geographic",
    "Various Authors",
    202
)
magazine2 = Magazine(
    "Science Monthly",
    "Various Authors",
    15
)



print("Publication Information:")
publication1.display_info()
print()


print("Book Information:")
book2.display_info()
print("Title:", book1.get_title())
print("Author:", book1.get_author())
print("Number of pages:", book1.get_number_of_pages())
print()


print("Magazine Information:")
magazine1.display_info()
