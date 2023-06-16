def glc_para_fng(glc):
    fng = {'S': [], 'A': [], 'B': [], 'C': []}  # Dicionário para armazenar as regras da FNG

    # Passo 1: Remover regras vazias
    regras_vazias = encontrar_regras_vazias(glc)  # Encontra as variáveis que produzem a cadeia vazia
    glc_sem_vazias = remover_regras_vazias(glc, regras_vazias)  # Remove as produções com regras vazias

    # Passo 2: Remover produções unitárias
    producoes_unitarias = encontrar_producoes_unitarias(glc_sem_vazias)  # Encontra as produções unitárias
    glc_sem_unitarias = remover_producoes_unitarias(glc_sem_vazias, producoes_unitarias)  # Remove as produções unitárias

    # Passo 3: Transformar produções em formas adequadas
    for variavel in glc_sem_unitarias:
        for producao in glc_sem_unitarias[variavel]:
            nova_producao = transformar_producao(producao, fng)  # Transforma a produção na forma adequada
            fng[variavel].append(nova_producao)  # Adiciona a nova produção ao dicionário da FNG

    return fng

def encontrar_regras_vazias(glc):
    regras_vazias = set()
    for variavel, producoes in glc.items():
        if '' in producoes:  # Verifica se há produção vazia para a variável
            regras_vazias.add(variavel)  # Adiciona a variável ao conjunto de regras vazias
    novas_vazias = set()
    while novas_vazias != regras_vazias:  # Repete até que não haja novas regras vazias
        novas_vazias = set(regras_vazias)
        for variavel, producoes in glc.items():
            for producao in producoes:
                if all(simbolo in regras_vazias for simbolo in producao):  # Verifica se todos os símbolos da produção estão nas regras vazias
                    regras_vazias.add(variavel)  # Adiciona a variável ao conjunto de regras vazias
    return regras_vazias

def remover_regras_vazias(glc, regras_vazias):
    glc_sem_vazias = glc.copy()
    for variavel, producoes in glc.items():
        glc_sem_vazias[variavel] = [producao for producao in producoes if not any(simbolo in regras_vazias for simbolo in producao)]  # Remove as produções com regras vazias
    return glc_sem_vazias

def encontrar_producoes_unitarias(glc):
    producoes_unitarias = set()
    for variavel, producoes in glc.items():
        for producao in producoes:
            if len(producao) == 1 and producao.isupper():  # Verifica se a produção é uma produção unitária (A -> B)
                producoes_unitarias.add((variavel, producao))  # Adiciona a produção ao conjunto de produções unitárias
    return producoes_unitarias

def remover_producoes_unitarias(glc, producoes_unitarias):
    glc_sem_unitarias = glc.copy()
    for variavel, producoes in glc.items():
        glc_sem_unitarias[variavel] = [producao for producao in producoes if (variavel, producao) not in producoes_unitarias]  # Remove as produções unitárias
    return glc_sem_unitarias

def transformar_producao(producao, fng):
    nova_producao = ''
    for simbolo in producao:
        if simbolo.isupper():  # Verifica se o símbolo é uma variável
            nova_producao += simbolo + "'"  # Adiciona um apóstrofo à variável
            fng[simbolo + "'"] = []  # Cria uma nova entrada no dicionário da FNG para a variável transformada
            fng[simbolo + "'"].append(simbolo)  # Adiciona uma produção na forma adequada
        else:
            nova_producao += simbolo
    return nova_producao

# Exemplo de uso do algoritmo
glc = {
    'S': ['A', 'ABa', 'AbA'],
    'A': ['Aa', 'y*'],
    'B': ['Bb', 'BC'],
    'C': ['CB', 'CA', 'bB']
}

fng = glc_para_fng(glc)
print(fng)
