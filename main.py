import numpy as np
import pandas as pd 
import melhoresInvestimentos as Investimento

def main(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [2, 2, 1], 
        'Teto': [1200000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)

    print(Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital))

if __name__ == "__main__": 
    main()