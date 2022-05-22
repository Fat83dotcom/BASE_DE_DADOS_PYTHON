import sqlite3


class Agenda:
    def __init__(self, arquivo) -> None:
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
    
    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()
    
    def editar(self, identificador, nome=None, telefone=None):
        if nome != None:
            consulta = 'UPDATE agenda SET nome=? WHERE id=?'
            self.cursor.execute(consulta, (nome, identificador))
            self.conn.commit()
        if telefone != None:
            consulta = 'UPDATE agenda SET telefone=? WHERE id=?'
            self.cursor.execute(consulta, (telefone, identificador))
    
    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id, ))
        self.conn.commit()
    
    def listar(self):
        resultado = []
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            resultado.append(linha)

        return resultado
    
    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%', ))
        resultado = []
        for linha in self.cursor.fetchall():
            resultado.append(linha)
        
        return resultado

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = Agenda('agenda.db')
    # agenda.inserir('JJ charles', 64993057605)
    # agenda.listar()
    # print(agenda.buscar('3432'))
    agenda.editar(6, nome='Jao')