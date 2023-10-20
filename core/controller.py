import requests as r
from bs4 import BeautifulSoup
import locale

class FundoImobiliario:

    def __init__(self, papel, segmento, cotacao,	ffo_yield, dividend_yield, p_vp, valor_mercado, liquidez, cap_rate, vacancia):
        self.papel = papel
        self.segmento = segmento
        self.cotacao = cotacao
        self.ffo_yeld = ffo_yield
        self.dividend_yield = dividend_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
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
        self.cap_rate_minimo = cap_rate_minimo
        self.vacancia_minima = vacancia_minima

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
                or fundo.cap_rate < self.cap_rate_minimo\
                or fundo.vacancia < self.vacancia_minima:
            return False
        else:
            return True

class Result:

    tabela_result = []
    max_result = []
    min_result = []

    @classmethod
    def result(cls, estrategia: Estrategia = Estrategia()):

        def tratar_porcentagem(porcentagem_str: str):
            return locale.atof(porcentagem_str.split('%')[0])


        def tratar_decimal(decimal_str: str):
            return locale.atof(decimal_str)

        list_cotacao = []
        list_ffo_yield = []
        list_dividend_yield = []
        list_p_vp = []
        list_valor_mercado = []
        list_liquidez = []
        list_cap_rate = []
        list_vacancia = []

        elementos = {
            'cotacao':list_cotacao,
            'ffo_yield':list_ffo_yield,
            'dividend_yield':list_dividend_yield,
            'p_vp':list_p_vp,
            'valor_mercado':list_valor_mercado,
            'liquidez':list_liquidez,
            'cap_rate':list_cap_rate,
            'vacancia':list_vacancia
        }

        max_result = {}
        min_result = {}

        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # padronizando para acentuação BR
        
        headers = {'User-Agent': 'Mozzila/5.0'}

        link_acesso = r.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)

        soup = BeautifulSoup(link_acesso.text, 'html.parser')

        linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

        resultado = []

        estrategia = estrategia #aplica estrategia para filtrar os fundos imobiliarios

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
            cap_rate = tratar_porcentagem(dados_fundo[11].text)
            vacancia = tratar_porcentagem(dados_fundo[12].text)

            fundo_imobiliario = FundoImobiliario(papel, segmento, cotacao, ffo_yield, dividend_yield, p_vp, valor_mercado, liquidez, cap_rate, vacancia)

            if estrategia.aplica_estrategia(fundo_imobiliario):
                resultado.append(fundo_imobiliario)
            
        tabela = []

        for element in resultado:
            tabela.append({'papel':element.papel,'segmento': element.segmento,'cotacao': locale.currency(element.cotacao),'d_yield': f'{locale.str(element.dividend_yield)}%'})

            list_cotacao.append(element.cotacao)
            list_ffo_yield.append(element.ffo_yeld)
            list_dividend_yield.append(element.dividend_yield)
            list_p_vp.append(element.p_vp)
            list_valor_mercado.append(element.valor_mercado)
            list_liquidez.append(element.liquidez)
            list_cap_rate.append(element.cap_rate)
            list_vacancia.append(element.vacancia)

        for chave, element in elementos.items():
            max_result[f'{chave}'] = max(element)
            min_result[f'{chave}'] = min(element)
        


            
        cls.max_result = max_result
        cls.min_result = min_result
        cls.tabela_result = tabela
