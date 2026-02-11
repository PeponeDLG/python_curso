class Libro():
    
    def __init__(self, isbn, titulo, autor, disponible):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = int(disponible)