
#problema de escalonamento simples usando algoritmo genetico

# criando tareffas

#construtor para inicializar o objeto
class Tarefas:
    def __init__(self,id,tempo,prioridade,prazo):
        self.tarefa1=id
        self.tarefa1=tempo
        self.tarefa1=prioridade,
        self.tarefa1=prazo


    #metodo de acesso :
    def setId(self,id):
        self.id=id
    def setTempo(self,tempo):
        self.tempo=tempo
    def setPrioridade(self,prioridade):
        if 1 <= self.prioridade <= 5:
            self.prioridade=prioridade  
    def setPrazo(self,prazo):
        self.prazo=prazo
    #metodo get

    def getId(self,id):
        self.id=id
    def getTempo(self,tempo):
        self.tempo=tempo
    def getPrioridade(self,prioridade):
        self.prioridade=prioridade
    def getPrazo(self,prazo):
        self.prazo=prazo

#exibir o objeto

    def exibir(self):
       return f"id:{self.id}, tempo:{self.tempo},prioridade:{self.prioridade}, prazo:{self.prazo}"

#lista de tarefas

lista_tarefas=[]

for i in range(8):
    print(f"\nCadastro da {i+1}ª tarefa:")
    tempo=int(input("Informe o tempo da tarefa"))
    prioridade=int(input("Informe a prioridade da tarefa"))
    prazo=int(input("Informe o prazo"))
    
    #criando objeto
    tarefa=Tarefas(id+1,tempo,prioridade,prazo)
    #adicionando na lista

    lista_tarefas.append(tarefa)

print("Tarefas cadastradas")
for x in lista_tarefas:
    print(x.exibir())
 
 
    

