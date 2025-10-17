
#Book Data Model
class Book:

    def __init__(self, title, author, content, borrower, is_available):
        self.__title = title
        self.__author = author
        self.__content = content
        self.__borrower = borrower
        self.__is_available = is_available

    @property
    def title(self)->str:
        return self.__title
    
    @title.setter
    def title(self,value:str):
        self.__title = value

    @property
    def author(self)->str:
        return self.__author
    
    @author.setter
    def author(self,value:str):
        self.__author = value

    @property
    def content(self)->str:
        return self.__content
    
    @content.setter
    def content(self,value:str):
        self.__content = value
        
    @property
    def borrower(self)->str:
        return self.__borrower
    
    @borrower.setter
    def borrower(self,value:str):
        self.__borrower = value
    
    @property
    def is_available(self)->bool:
        return self.__is_available
    
    @is_available.setter
    def is_available(self,value:bool):
        self.__is_available= value
    
    def __str__(self) -> str:
        availability = "Available" if self.__is_available else f"Borrowed by {self.__borrower}"
        return (
            f"Title: {self.__title}\n"
            f"Author: {self.__author}\n"
            f"Content: {self.__content}\n"
            f"Status: {availability}\n")
        