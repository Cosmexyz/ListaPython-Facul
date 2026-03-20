alunos = []

for i in range(3):
    print("\nCadastro do aluno {}".format(i+1))
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade: "))
    notas = []
    
    for j in range(3):
        nota = float(input("Digite a nota {}: ".format(j+1)))
        notas.append(nota)
    
    aluno = {"nome": nome, "idade": idade, "notas": notas}
    alunos.append(aluno)

print("\n--- Médias dos alunos ---")
for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print("{} - Média: {:.2f}".format(aluno["nome"], media))