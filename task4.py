class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        return f"'{self.title}' by {self.author}, published in {self.year_published}."

# Creating book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("Moby-Dick", "Herman Melville", 1851)
book3 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)

# Displaying book details using print()
print(book1)
print(book2)
print(book3)
