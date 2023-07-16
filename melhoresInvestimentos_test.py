import pandas as pd
import numpy as np
import melhoresInvestimentos as Investimento


def test_capital(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [2, 2, 1], 
        'Teto': [1200000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)

    assert np.sum(Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital)['Custo']) <= capital
    
def test_quantBaixo(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [4, 2, 1], 
        'Teto': [1200000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)
    
    assert len((Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital)).query('Risco == "Baixo"')) >= parametros_risco.loc[0, 'Quant. Mínima']


def test_quantMedio(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [3, 2, 1], 
        'Teto': [1200000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)
    
    assert len((Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital)).query('Risco == "Médio"')) >= parametros_risco.loc[1, 'Quant. Mínima']

def test_quantAlto(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [2, 2, 1], 
        'Teto': [1200000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)
    
    assert len((Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital)).query('Risco == "Alto"')) >= parametros_risco.loc[2, 'Quant. Mínima']

def test_tetoBaixo(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [3, 2, 1], 
        'Teto': [1000000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)
    
    assert np.sum(((Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital)).query('Risco == "Baixo"'))['Custo']) <= parametros_risco.loc[0, 'Teto']


def test_tetoMedio(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [3, 2, 1], 
        'Teto': [1200000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)
    
    assert np.sum(((Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital)).query('Risco == "Médio"'))['Custo']) <= parametros_risco.loc[1, 'Teto']

def test_tetoAlto(): 
    parametros_risco = pd.DataFrame({
        'Risco': ['Baixo', 'Médio', 'Alto'], 
        'Quant. Mínima': [3, 2, 1], 
        'Teto': [1200000, 1500000, 900000]
    })
    
    capital = 2400000
    
    # Ler um arquivo com as opçoes de investimento 
    opcoesInvestimento = pd.read_excel('listInvestimento.xlsx')
    opcoesInvestimento.rename(columns={'Custo do investimento (R$)': 'Custo', 'Risco do investimento': 'Risco'}, inplace=True)
    
    assert np.sum(((Investimento.melhoresInvestimentos(opcoesInvestimento, parametros_risco, capital)).query('Risco == "Alto"'))['Custo']) <= parametros_risco.loc[2, 'Teto']
