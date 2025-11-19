from curso import Curso

class Campus:
    def __init__(self, codigo, nome, cidade):
        self.codigo = codigo
        self.nome = nome
        self.cidade = cidade
        self.cursos = []  # lista de objetos Curso

    # ----- CRUD de CURSOS (dentro do campus) -----

    def adicionar_curso(self, curso):
        self.cursos.append(curso)

    def buscar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def remover_curso(self, codigo):
        curso = self.buscar_curso(codigo)
        if curso:
            self.cursos.remove(curso)
            return True
        return False

    def listar_cursos(self):
        return self.cursos

    def __str__(self):
        return f"{self.codigo} - {self.nome} ({self.cidade})"