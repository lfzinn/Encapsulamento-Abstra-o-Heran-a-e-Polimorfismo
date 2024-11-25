from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade, numero_matricula):
        self.nome = nome
        self.idade = idade
        self.numero_matricula = numero_matricula

    @abstractmethod
    def exibir_informacoes(self):
        pass


class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, numero_matricula):
        super().__init__(nome, idade, numero_matricula)
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.disponivel = False
            print(f"Livro '{livro.titulo}' emprestado com sucesso.")
        else:
            print("Não é possível realizar o empréstimo.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"Livro '{livro.titulo}' devolvido com sucesso.")

    def exibir_informacoes(self):
        print(f"Usuário: {self.nome}, Livros emprestados: {[livro.titulo for livro in self.livros_emprestados]}")


class Administrador(Pessoa):
    def exibir_informacoes(self):
        print(f"Administrador: {self.nome}")

    def cadastrar_livro(self, livro, catalogo):
        catalogo.append(livro)
        print(f"Livro '{livro.titulo}' cadastrado com sucesso.")


class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    @abstractmethod
    def exibir_detalhes(self):
        pass


class Livro(ItemBiblioteca):
    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {status}")


if __name__ == "__main__":
    catalogo_livros = []
    usuarios = []

    admin = Administrador("Ana", 35, "A001")
    usuario = UsuarioComum("João", 20, "U001")

    livro1 = Livro("Python Básico", "Autor A", 2020)
    livro2 = Livro("POO Avançada", "Autor B", 2021)

    admin.cadastrar_livro(livro1, catalogo_livros)
    admin.cadastrar_livro(livro2, catalogo_livros)

    usuario.emprestar_livro(livro1)
    usuario.exibir_informacoes()
    usuario.devolver_livro(livro1)
    usuario.exibir_informacoes()
