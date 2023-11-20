import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "392781",
    database = "academiaturmac"
)
meucursor = banco.cursor()

menu = '''Tabelas:
1 - Alunos
2 - Funcionarios
3 - Personal
4 - Modalidades
---------------
5 - Encerrar'''

opc = '''1 - Adicionar
2 - Deletar
3 - Exibir
4 - Trocar tabela'''

dadosALUNOS = ['Nome:', 'CPF:', 'Telefone:', 'Endereço:']
dadosalunos = [''] * 4
dadosFUNC = ['Nome:', 'CPF:', 'Departamento:', 'Salario:']
dadosfunc = [''] * 4
dadosPERSONAL = ['Nome:', 'cref:']
dadospersonal = [''] * 2
dadosMODAL = ['Nome', 'Duração']
dadosmodal = [''] * 2

print(menu)

while True:
    escolhatabela = int(input("Escolha a TABELA:"))
    if escolhatabela == 1:
        print("-" * 20)
        print("Tabela ALUNOS")
        print("-" * 20)
        print(opc)
        operação = int(input("Escolha a operação:"))
        if operação == 1:
            print("-" * 20)
            print("Adicionar ALUNO")
            print("-" * 20)
            adição = 'insert into alunos(nome, cpf, telefone, endereço);'
            for c in range(4):
                dadosalunos[c] = str(input(f"Insira o {dadosALUNOS[c]}"))
            sql = "insert into alunos (nome, telefone, cpf, endereço) values (%s, %s, %s, %s)"
            data = (dadosalunos[0], dadosalunos[1], dadosalunos[2], dadosalunos[3])
            meucursor.execute(sql, data)
            banco.commit()
            userid = meucursor.lastrowid
        if operação == 2:
            pesquisa = 'select * from alunos;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
            delet = int(input("ID do aluno:"))
            deletar = (f'''delete from alunos
            where matricula = {delet}''')
            meucursor.execute(deletar)
            banco.commit()
            userid = meucursor.lastrowid
        if operação == 3:
            pesquisa = 'select * from alunos;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        if operação == 4:
            break
    elif escolhatabela == 2:
        print("-" * 20)
        print("Tabela FUNCIONARIOS")
        print("-" * 20)
        print(opc)
        operação = int(input("Escolha a operação:"))
        if operação == 1:
            print("-" * 20)
            print("Adicionar Funcionario")
            print("-" * 20)
            adição = 'insert into alunos(nome, cpf, departamento, salario;'
            for c in range(4):
                dadosfunc[c] = str(input(f"Insira o {dadosFUNC[c]}"))
            sql = "insert into funcionarios (nome, cpf, departamento, salario) values (%s, %s, %s, %s)"
            data = (dadosfunc[0], dadosfunc[1], dadosfunc[2], dadosfunc[3])
            meucursor.execute(sql, data)
            banco.commit()
            userid = meucursor.lastrowid
        if operação == 2:
            pesquisa = 'select * from funcionarios;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
            delet = int(input("ID do funcionarios:"))
            deletar = (f'''delete from funcionarios
            where id_funcionario = {delet}''')
            meucursor.execute(deletar)
            banco.commit()
            userid = meucursor.lastrowid

        if operação == 3:
            pesquisa = 'select * from modalidades;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
            pesquisa = 'select * from funcionarios;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        if operação == 4:
            break

    elif escolhatabela == 3:
        print("-" * 20)
        print("Tabela PERSONAL")
        print("-" * 20)
        print(opc)
        operação = int(input("Escolha a operação:"))
        if operação == 1:
            print("-" * 20)
            print("Adicionar Personal")
            print("-" * 20)
            adição = 'insert into alunos(nome, cref;'
            for c in range(2):
                dadospersonal[c] = str(input(f"Insira o {dadosPERSONAL[c]}"))
            sql = "insert into personal (nome, cref) values (%s, %s)"
            data = (dadospersonal[0], dadospersonal[1])
            meucursor.execute(sql, data)
            banco.commit()
            userid = meucursor.lastrowid

        if operação == 2:
            pesquisa = 'select * from personal;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
            delet = int(input("ID do personal:"))
            deletar = (f'''delete from personal
            where cod_personal = {delet}''')
            meucursor.execute(deletar)
            banco.commit()
            userid = meucursor.lastrowid

        if operação == 3:

            pesquisa = 'select * from modalidades;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
            pesquisa = 'select * from personal;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        if operação == 4:
            break

    elif escolhatabela == 4:
        print("-" * 20)
        print("Tabela MODALIDADES")
        print("-" * 20)
        print(opc)
        operação = int(input("Escolha a operação:"))
        if operação == 1:
            print("-" * 20)
            print("Adicionar Modalidade")
            print("-" * 20)
            adição = 'insert into modalidades(nome, duração;'
            for c in range(2):
                dadosmodal[c] = str(input(f"Insira o {dadosMODAL[c]}"))
            sql = "insert into modalidades (nome, duracao) values (%s, %s)"
            data = (dadosmodal[0], dadosmodal[1])
            meucursor.execute(sql, data)
            banco.commit()
            userid = meucursor.lastrowid

        if operação == 2:
            pesquisa = 'select * from modalidades;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
            delet = int(input("ID do modalidades:"))
            deletar = (f'''delete from modalidades
            where id_modalidade = {delet}''')
            meucursor.execute(deletar)
            banco.commit()
            userid = meucursor.lastrowid

        if operação == 3:
            pesquisa = 'select * from modalidades;'
            meucursor.execute(pesquisa)
            resultado = meucursor.fetchall()
            for x in resultado:
                print(x)
        if operação == 4:
            break
    elif escolhatabela == 5:
        break

    else:
        print("Opção Inválida")
        escolhatabela = int(input("Escolha a TABELA:"))
