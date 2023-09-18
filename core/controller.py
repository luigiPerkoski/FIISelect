import requests as r
from bs4 import BeautifulSoup
import locale

class FundoImobiliario:

    def __init__(self, papel, segmento, cotacao,	ffo_yield, dividend_yield, p_vp, valor_mercado, liquidez, quantidade_imóveis, preço_m2, aluguel_m2, cap_rate, vacancia):
        self.papel = papel
        self.segmento = segmento
        self.cotacao = cotacao
        self.ffo_yeld = ffo_yield
        self.dividend_yield = dividend_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.quantidade_imóveis = quantidade_imóveis
        self.preço_m2 = preço_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia = vacancia

class Estrategia:

    def __init__(self, segmento='', cotacao_minima=0, ffo_yield_minima=0, dividend_yield_minimo=0, p_vp_minimo=0, valor_mercado_minimo=0, liquidez_minima=0, quantidade_imóveis_minima=0, preço_m2_minimo=0, aluguel_m2_minimo=0, cap_rate_minimo=0, vacancia_minima=0):
        self.segmento = segmento
        self.cotacao_minima = cotacao_minima
        self.ffo_yield_minimo = ffo_yield_minima
        self.dividend_yield_minimo = dividend_yield_minimo
        self.p_vp_minimo = p_vp_minimo
        self.valor_mercado_minimo = valor_mercado_minimo
        self.liquidez_minima = liquidez_minima
        self.preço_m2_minimo = preço_m2_minimo
        self.aluguel_m2_minimo = aluguel_m2_minimo
        self.cap_rate_minimo = cap_rate_minimo
        self.vacancia_minima = vacancia_minima
        self.quantidade_imoveis_minima = quantidade_imóveis_minima

    def aplica_estrategia(self, fundo: FundoImobiliario):
        if self.segmento != '':
            if self.segmento != fundo.segmento:
                return False
        elif fundo.cotacao < self.cotacao_minima \
                or fundo.ffo_yeld < self.ffo_yield_minimo\
                or fundo.dividend_yield < self.dividend_yield_minimo\
                or fundo.p_vp < self.p_vp_minimo\
                or fundo.valor_mercado< self.valor_mercado_minimo\
                or fundo.liquidez < self.liquidez_minima\
                or fundo.quantidade_imóveis < self.quantidade_imoveis_minima\
                or fundo.preço_m2 < self.preço_m2_minimo\
                or fundo.aluguel_m2 < self.aluguel_m2_minimo\
                or fundo.cap_rate < self.cap_rate_minimo\
                or fundo.vacancia < self.vacancia_minima:
            return False
        else:
            return True


def result():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # padronizando para acentuação BR


    def tratar_porcentagem(porcentagem_str: str):
        return locale.atof(porcentagem_str.split('%')[0])


    def tratar_decimal(decimal_str: str):
        return locale.atof(decimal_str)
    
    headers = {'User-Agent': 'Mozzila/5.0'}

    link_acesso = r.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)

    soup = BeautifulSoup(link_acesso.text, 'html.parser')

    linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

    resultado = []

    estrategia = Estrategia() #aplica estrategia para filtrar os fundos imobiliarios

    for linha in linhas:

        dados_fundo = linha.find_all('td')
        papel = dados_fundo[0].text
        segmento = dados_fundo[1].text
        cotacao = tratar_decimal(dados_fundo[2].text)
        ffo_yield = tratar_porcentagem(dados_fundo[3].text)
        dividend_yield = tratar_porcentagem(dados_fundo[4].text)
        p_vp = tratar_decimal(dados_fundo[5].text)
        valor_mercado = tratar_decimal(dados_fundo[6].text)
        liquidez = tratar_decimal(dados_fundo[7].text)
        quantidade_imoveis = int(dados_fundo[8].text)
        preço_m2 = tratar_decimal(dados_fundo[9].text)
        aluguel_m2 = tratar_decimal(dados_fundo[10].text)
        cap_rate = tratar_porcentagem(dados_fundo[11].text)
        vacancia = tratar_porcentagem(dados_fundo[12].text)

        fundo_imobiliario = FundoImobiliario(papel, segmento, cotacao, ffo_yield, dividend_yield, p_vp, valor_mercado, liquidez, quantidade_imoveis, preço_m2, aluguel_m2, cap_rate, vacancia)

        if estrategia.aplica_estrategia(fundo_imobiliario):
            resultado.append(fundo_imobiliario)
        
    tabela = []

    for element in resultado:
        tabela.append({'papel':element.papel,'segmento': element.segmento,'cotacao': locale.currency(element.cotacao),'d_yield': f'{locale.str(element.dividend_yield)}%'})

    return tabela

print(result())

#tranformando saida de dados em tabela
# head = ['PAPEL', 'SEGMENTO', 'COTAÇÃO ATUAL ', 'D.Y']

# tabela = []

# for element in resultado:
#     tabela.append([element.papel, element.segmento, locale.currency(element.cotacao), f'{locale.str(element.dividend_yield)}%'])

# print(tabulate.tabulate(tabela, headers=head, tablefmt='fancy_grid', showindex='always'))
