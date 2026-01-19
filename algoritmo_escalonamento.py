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
    
    
    def funcao_fitnes(self):
        """
        Calcula o fitness (qualidade) desta solução
        Quanto MAIOR o fitness, MELHOR a solução
        """
        # 1. Calcular para impressora 1
        tempo_impressora_1 = 0
        atrasos_impressora_1 = 0
        prioridade_impressora_1 = 0
        
        for tarefa in self.impressora_1:
            tempo_impressora_1 += tarefa.getTempo() 
            if tempo_impressora_1 > tarefa.getPrazo():  
                atrasos_impressora_1 += (tempo_impressora_1 - tarefa.getPrazo())
            prioridade_impressora_1 += tarefa.getPrioridade()  
        
        # 2. Calcular para impressora 2
        tempo_impressora_2 = 0
        atrasos_impressora_2 = 0
        prioridade_impressora_2 = 0
        
        for tarefa in self.impressora_2:
            tempo_impressora_2 += tarefa.getTempo()
            if tempo_impressora_2 > tarefa.getPrazo():
                atrasos_impressora_2 += (tempo_impressora_2 - tarefa.getPrazo())
            prioridade_impressora_2 += tarefa.getPrioridade()
        
        # 3. Calcular para impressora 3
        tempo_impressora_3 = 0
        atrasos_impressora_3 = 0
        prioridade_impressora_3 = 0
        
        for tarefa in self.impressora_3:
            tempo_impressora_3 += tarefa.getTempo()
            if tempo_impressora_3 > tarefa.getPrazo():
                atrasos_impressora_3 += (tempo_impressora_3 - tarefa.getPrazo())
            prioridade_impressora_3 += tarefa.getPrioridade()
        
        # 4. Calcular makespan (tempo da impressora mais lenta)
        makespan = max(tempo_impressora_1, tempo_impressora_2, tempo_impressora_3)
        
        # 5. Calcular totais 
        atraso_total = atrasos_impressora_1 + atrasos_impressora_2 + atrasos_impressora_3
        prioridade_total = prioridade_impressora_1 + prioridade_impressora_2 + prioridade_impressora_3
        
        # 6. Aplicar fórmula do fitness
        VALOR_BASE = 10000
        PENALIDADE_MAKESPAN = makespan * 0.5
        PENALIDADE_ATRASO = atraso_total * 2.0
        BONUS_PRIORIDADE = prioridade_total * 10
        
        fitness = VALOR_BASE - PENALIDADE_MAKESPAN - PENALIDADE_ATRASO + BONUS_PRIORIDADE
        
        # Armazenar o fitness calculado
        self.solucao_qualidade = fitness
        
        return fitness
    
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
        resultado += f"Qualidade: {self.solucao_qualidade:.2f}"  # Mostrar com 2 casas decimais
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



# ========== FASE 3: FUNÇÕES PARA AVALIAR POPULAÇÃO ==========
def avaliar_populacao(populacao):
    """
    Calcula o fitness para todas as soluções na população
    e ordena da melhor (maior fitness) para a pior
    """
    # Calcular fitness para cada solução
    for solucao in populacao:
        solucao.funcao_fitnes()  # Mudado para funcao_fitnes()
    
    # Ordenar população por fitness (maior primeiro)
    populacao_ordenada = sorted(populacao, 
                                key=lambda x: x.solucao_qualidade, 
                                reverse=True)
    
    return populacao_ordenada

def exibir_resultados_avaliacao(populacao):
    """
    Exibe os resultados da avaliação de fitness
    """
    print("\n" + "="*60)
    print(" FASE 3: RESULTADOS DA AVALIAÇÃO DE FITNESS")
    print("="*60)
    
    # Ordenar população primeiro
    populacao_ordenada = avaliar_populacao(populacao)
    
    # Coletar todos os valores de fitness
    fitness_values = [sol.solucao_qualidade for sol in populacao_ordenada]
    
    # Exibir cada solução
    for i, solucao in enumerate(populacao_ordenada, 1):
        print(f"\n--- Solução {i} (Fitness: {solucao.solucao_qualidade:.2f}) ---")
        if i == 1:
            print(" MELHOR SOLUÇÃO DA POPULAÇÃO ")
        print(solucao)
    
    # Estatísticas
    print("\n" + "-"*60)
    print(" ESTATÍSTICAS DO FITNESS:")
    print(f"Número de soluções: {len(populacao_ordenada)}")
    print(f"Melhor fitness: {max(fitness_values):.2f}")
    print(f"Pior fitness: {min(fitness_values):.2f}")
    print(f"Média de fitness: {sum(fitness_values)/len(fitness_values):.2f}")
    print("="*60)
    
    return populacao_ordenada



# ========== chamando ==========
def main():
    print("=" * 60)
    print("ALGORITMO GENÉTICO - ESCALONAMENTO DE TAREFAS")
    print("=" * 60)
    
    # FASE 1: Criar tarefas
    print("\n FASE 1: CRIANDO TAREFAS")
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
    
    # ========== FASE 3: TESTE DO FITNESS ==========
    print("\n" + "="*60)
    print(" FASE 3: TESTANDO O CÁLCULO DE FITNESS")
    print("="*60)
    
    # Testar com a primeira solução
    if populacao:
        primeira_solucao = populacao[0]
        print("\n Calculando fitness da primeira solução:")
        
        try:
            # Chamar o método correto
            fitness = primeira_solucao.funcao_fitnes()
            print(f" Fitness calculado: {fitness:.2f}")
            print(f" Valor armazenado: {primeira_solucao.solucao_qualidade:.2f}")
            
            # Mostrar detalhes (CORRIGIDO - string dividida)
            print("\n Detalhes do cálculo:")
            tempo_imp1 = sum(t.getTempo() for t in primeira_solucao.impressora_1)
            tempo_imp2 = sum(t.getTempo() for t in primeira_solucao.impressora_2)
            tempo_imp3 = sum(t.getTempo() for t in primeira_solucao.impressora_3)
            print(f"Makespan: {max(tempo_imp1, tempo_imp2, tempo_imp3)}")
            
        except Exception as e:
            print(f" ERRO ao calcular fitness: {e}")
            import traceback
            traceback.print_exc()
    
    # Testar com todas as soluções
    print("\n Calculando fitness para TODA a população:")
    try:
        populacao_avaliada = exibir_resultados_avaliacao(populacao)
        print(" Fitness calculado para toda a população!")
    except Exception as e:
        print(f" ERRO: {e}")
        import traceback
        traceback.print_exc()

# Executar o programa
if __name__ == "__main__":
    main()
