import random
# problema de escalonamento simples usando algoritmo genetico
# criando tarefas
import random

# ========== FASE 1: TAREFAS ==========
class Tarefas:
    def __init__(self, id, tempo, prioridade, prazo):
        self.id = id
        self.tempo = tempo
        self.prioridade = prioridade
        self.prazo = prazo

#metodos de acesso

    def setId(self, id):
        self.id = id

    def setTempo(self, tempo):
        self.tempo = tempo

    def setPrioridade(self, prioridade):
        self.prioridade = prioridade

    def setPrazo(self, prazo):
        self.prazo = prazo

    def getId(self):
        return self.id

    def getTempo(self):
        return self.tempo

    def getPrioridade(self):
        return self.prioridade

    def getPrazo(self):
        return self.prazo

    def exibir(self):
        return f"id:{self.id}, tempo:{self.tempo}, prioridade:{self.prioridade}, prazo:{self.prazo}"

# ========== FASE 2: SOLUÇÕES ==========
class Impressora:
    def __init__(self):
        self.impressora_1 = []
        self.impressora_2 = []
        self.impressora_3 = []
        self.solucao_qualidade = 0

    def adicionando_tarefa_a_impressora(self, tarefa, impressora_id):
        if impressora_id == 1:
            self.impressora_1.append(tarefa)
        elif impressora_id == 2:
            self.impressora_2.append(tarefa)
        elif impressora_id == 3:
            self.impressora_3.append(tarefa)
        else:
            print(f"ID de impressora inválido: {impressora_id}")

    def formatar_tarefas(self, lista_tarefas):
        """Formata a lista de tarefas para exibição"""
        if not lista_tarefas:
            return "Vazia"
        ids = [str(tarefa.getId()) for tarefa in lista_tarefas]
        return "T" + ", T".join(ids)

    def __str__(self):
        """Retorna uma string com a representação da solução"""
        resultado = "SOLUÇÃO:\n"
        resultado += f"Impressora 1: {self.formatar_tarefas(self.impressora_1)}\n"
        resultado += f"Impressora 2: {self.formatar_tarefas(self.impressora_2)}\n"
        resultado += f"Impressora 3: {self.formatar_tarefas(self.impressora_3)}\n"
        resultado += f"Qualidade: {self.solucao_qualidade}"
        return resultado

# == funcoes solucao aleatorio ==========
def funcao_aleatorio(lista_tarefas):
    """Cria uma solução aleatória"""
    nova_solucao = Impressora()
    
    for tarefa in lista_tarefas:
        sortear_impressora = random.randint(1, 3)
        nova_solucao.adicionando_tarefa_a_impressora(tarefa, sortear_impressora)
    
    return nova_solucao  

def criando_populacao(tamanho, lista_tarefas):
    """Cria uma população de soluções aleatórias"""
    populacao = []
    for i in range(tamanho):
        solu = funcao_aleatorio(lista_tarefas)
        populacao.append(solu)
    return populacao

def estatisticas_tarefas(tarefas):
    """Calcula estatísticas das tarefas"""
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
    
    tempo_medio_impressora = tempo_total / 3
    print(f"Tempo médio por impressora (3): {tempo_medio_impressora:.2f} minutos")
    print(f"{'='*50}\n")
    return tempo_total

# ========== chamando ==========
def main():
    print("=" * 60)
    print("ALGORITMO GENÉTICO - ESCALONAMENTO DE TAREFAS")
    print("=" * 60)
    
    # FASE 1: Criar tarefas
    print("\n📋 FASE 1: CRIANDO TAREFAS")
    print("-" * 40)
    
    lista_tarefas = []
    
    # Mudar para 8 tarefas (como no enunciado)
    for i in range(8):
        print(f"\nCadastro da Tarefa {i+1}:")
        tempo = int(input("Tempo (minutos): "))
        prioridade = int(input("Prioridade (1-5): "))
        prazo = int(input("Prazo (minutos): "))
        
        tarefa = Tarefas(i+1, tempo, prioridade, prazo)
        lista_tarefas.append(tarefa)
    
    # Mostrar estatísticas
    estatisticas_tarefas(lista_tarefas)
    
    # FASE 2: Criar soluções
    print("\n FASE 2: CRIANDO SOLUÇÕES ALEATÓRIAS")
    print("-" * 40)
    
    # Criar uma solução de teste
    print("\n1. Criando uma solução aleatória:")
    solucao_teste = funcao_aleatorio(lista_tarefas)
    print(solucao_teste)
    
    # Verificar se todas tarefas foram alocadas
    total_tarefas = (len(solucao_teste.impressora_1) + 
                     len(solucao_teste.impressora_2) + 
                     len(solucao_teste.impressora_3))
    print(f"\nVerificação: {total_tarefas} tarefas alocadas de {len(lista_tarefas)}")
    
    # Criar população
    print("\n2. Criando população de 5 soluções:")
    tamanho_populacao = 5
    populacao = criando_populacao(tamanho_populacao, lista_tarefas)
    
    # Mostrar cada solução
    for i, sol in enumerate(populacao, 1):
        print(f"\n--- Solução {i} ---")
        print(sol)
        
        # Verificar integridade
        total = len(sol.impressora_1) + len(sol.impressora_2) + len(sol.impressora_3)
        print(f"Tarefas totais: {total}/8")

# Executar o programa
if __name__ == "__main__":
    main()
