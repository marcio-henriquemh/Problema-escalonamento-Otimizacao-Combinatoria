# problema de escalonamento simples usando algoritmo genetico
# criando tarefas

class Tarefas:
    # construtor para inicializar o objeto
    def __init__(self, id, tempo, prioridade, prazo):
        self.id = id
        self.tempo = tempo
        self.prioridade = prioridade
        self.prazo = prazo

    # metodo de acesso (setters)
    def setId(self, id):
        self.id = id

    def setTempo(self, tempo):
        self.tempo = tempo

    def setPrioridade(self, prioridade):
        self.prioridade = prioridade

    def setPrazo(self, prazo):
        self.prazo = prazo

    # metodo get (getters)
    def getId(self):
        return self.id

    def getTempo(self):
        return self.tempo

    def getPrioridade(self):
        return self.prioridade

    def getPrazo(self):
        return self.prazo

    # exibir o objeto
    def exibir(self):
        return f"id:{self.id}, tempo:{self.tempo}, prioridade:{self.prioridade}, prazo:{self.prazo}"

# lista de tarefas
lista_tarefas = []

for i in range(2):
    print(f"\nCadastro da {i+1}ª tarefa:")
    tempo = int(input("Informe o tempo da tarefa: "))
    prioridade = int(input("Informe a prioridade da tarefa (1-10): "))
    prazo = int(input("Informe o prazo: "))
    
    # criando objeto
    tarefa = Tarefas(i+1, tempo, prioridade, prazo)
    # adicionando na lista
    lista_tarefas.append(tarefa)

# estatisticas
def estatisticas_tarefas(tarefas):
    """Calcula e exibe estatísticas sobre as tarefas"""
    if not tarefas:
        print("Nenhuma tarefa para analisar!")
        return 0
    
    tempo_total = sum(t.getTempo() for t in tarefas)
    tempo_medio = tempo_total / len(tarefas)
    
    print(f"\n{'='*50}")
    print(" ESTATÍSTICAS DAS TAREFAS")
    print(f"{'='*50}")
    print(f"Total de tarefas: {len(tarefas)}")
    print(f"Tempo total: {tempo_total} minutos")
    print(f"Tempo médio por tarefa: {tempo_medio:.2f} minutos")
    
    # Calcular tempo médio ideal por impressora (3 impressoras)
    tempo_medio_impressora = tempo_total / 3
    print(f"Tempo médio por impressora (3): {tempo_medio_impressora:.2f} minutos")
    print(f"{'='*50}\n")

# Chamar a função de estatísticas
estatisticas_tarefas(lista_tarefas)



#parte 2

#classe solução(impressora)

class Impressora:
    def __init__(self):
        self.impressora_1=[]
        self.impressora_2=[]
        self.impressora_3=[]
        self.solucao_qualidade=0

    #adicionar tarefa a impressora

    def adicionando_tarefa_a_impressora(self,tarefa,impressora_id):

        if (impressora_id==1):
            self.impressora_1.append(tarefa)
        if(impressora_id==2):
            self.impressora_2.append(tarefa)
        elif(impressora_id==3):
            self.impressora_3.append(tarefa)
        else:
            print(f"ID de impressora inválido: {impressora_id}. A tarefa não foi adicionada.")

def __str__(self):
        """Retorna uma string com a representação da solução"""
        resultado = "SOLUÇÃO:\n"
        resultado += f"Impressora 1: {self.formatar_tarefas(self.impressora1)}\n"
        resultado += f"Impressora 2: {self.formatar_tarefas(self.impressora2)}\n"
        resultado += f"Impressora 3: {self.formatar_tarefas(self.impressora3)}\n"
        resultado += f"Fitness: {self.fitness}"
        return resultado
    
def formatar_tarefas(self, lista_tarefas):
        """Formata a lista de tarefas para exibição"""
        if not lista_tarefas:
            return "Vazia"
        # Pega os IDs das tarefas
        ids = [str(tarefa.getId()) for tarefa in lista_tarefas]
        return "T" + ", T".join(ids)
