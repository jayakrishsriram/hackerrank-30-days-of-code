from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):  #metaclass is also required
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod #this statement is required are 
    def display(): pass
class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price=price
    def display(self):
        print('Title: '+ self.title)
        print('Author: '+ self.author)
        print('Price: '+ str(self.price))

title=input("Enter the title of the book:")
author=input("Name of the author:")
price=int(input("cost of the book:"))
new_novel=MyBook(title,author,price)
new_novel.display()        
