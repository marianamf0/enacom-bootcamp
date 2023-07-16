import pandas as pd

def melhoresInvestimentos(investimentos, parametros, capital): 
    opSelecionadas = pd.DataFrame()
    
    parametros = parametros.join(pd.DataFrame({'Total': [0, 0, 0], 'Quant': [0, 0, 0]}))
    
    # Cria uma nova coluna no dataframe 'opcoesInvestimento' com a informação de taxa de retorno 
    investimentos = investimentos.join(pd.DataFrame({'Taxa de retorno (%)': 100*(investimentos['Retorno esperado (R$)']/investimentos['Custo'])}))

    # Organiza os dados de maneira decrescente de acordo com o valor da taxa de retorno para cada opção de investimento
    investimentos = investimentos.sort_values(by='Taxa de retorno (%)', ascending=False)
    investimentos.reset_index(inplace=True, drop=True)
    
    for indice, risco in zip(parametros.index, parametros['Risco']): 
        aux_opcoes = investimentos.query(f'Risco == "{risco}"')
        aux_opcoes.reset_index(inplace=True, drop=True)
        
        i = 0
        while (parametros['Quant'][indice] < parametros['Quant. Mínima'][indice]) and (i < len(aux_opcoes)): 
            
            if (aux_opcoes['Custo'][i] + parametros['Total'][indice] < parametros['Teto'][indice]) and (parametros['Total'].sum() + aux_opcoes['Custo'][i] < capital):
                opSelecionadas = pd.concat([opSelecionadas, aux_opcoes[aux_opcoes['Opção'] == aux_opcoes['Opção'][i]]], ignore_index=True)
                parametros.loc[indice, 'Total'] += aux_opcoes.loc[i, 'Custo']
                parametros.loc[indice, 'Quant'] += 1
                investimentos = investimentos.drop(investimentos[investimentos['Opção'] == aux_opcoes['Opção'][i]].index)
            
            i +=1

    investimentos.reset_index(inplace=True, drop=True)
                
    for i in range(0, len(investimentos)):
        parametro = parametros[parametros['Risco'] == investimentos['Risco'][i]]
        
        if ((investimentos['Custo'][i] + parametro['Total'].item()) < parametro['Teto'].item()) and (parametros['Total'].sum() + investimentos['Custo'][i] < capital):
            opSelecionadas = pd.concat([opSelecionadas, investimentos[investimentos['Opção'] == investimentos['Opção'][i]]], ignore_index=True)
            parametros.loc[parametro.index, 'Total'] += investimentos['Custo'][i]
            investimentos = investimentos.drop(i)
            
        if (capital - parametros['Total'].sum()) < min(investimentos['Custo']): break

    return opSelecionadas.drop(columns={'Taxa de retorno (%)'}) 
