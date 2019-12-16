import requests
from config import TELEGRAM_SEND_MESSAGE_URL, TELEGRAM_SEND_PHOTO_URL
import json
import re

class Bot:

    def __init__(self):
        
        self.chat = None                # ID of Telegram chat
        self.message_received = None    # Message received on Telegram chat
        self.first_name = None          # First name of the user
        self.msg_count = 1              # To control the test order
        self.inputs = []                # Save inputs received
    
    def send_message(self, html_text):

        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat, html_text, 'HTML'))
        if res.status_code == 200:
            return True
        else:
            return False

    def send_movie(self, html_text, banner_url):
        
        res = requests.get(TELEGRAM_SEND_PHOTO_URL.format(self.chat, banner_url, html_text, 'HTML'))
        
        if res.status_code == 200:
            return True
        else:
            return False
    
    def parse_data(self, data):
        
        message = data['message']

        self.chat = message['chat']['id']
        self.message_received = message['text'].lower()
        self.first_name = message['from']['first_name']
        self.inputs.append(self.message_received)

    def save_on_file(self):
        f = open("inputs_received.txt", "a")
        for input in self.inputs:
            f.write(input + '\n')
        f.close()

    def action(self):
        if self.message_received == '/start':
            self.send_message('Olá ' + self.first_name + '!\nEm que te posso ajudar?')
        elif re.match(r'passo [0-9][01234]?', self.message_received):
            words = self.message_received.split(' ')
            count = int(words[1])
            self.msg_count = count
            self.send_message('Ok. Estou agora no passo ' + str(count) + '.')
        else:
            if self.msg_count == 1:
                # Pedir ao utilizador para consultar os cinemas mais próximos.
                self.send_message('Os cinemas NOS perto de si num raio de 20Km são:\nBraga Parque')
            elif self.msg_count == 2:
                # Pedir ao utilizador para consultar os cinemas que existem em Lisboa.
                self.send_message('Os cinemas NOS que correspondem com a sua pesquisa são:\nColombo,\nAmoreiras,\nAlvaláxia,\nVasco da Gama')
            elif self.msg_count == 3:
                # Pedir ao utilizador para consultar os filmes em exibição no Algarve (search_term).
                self.send_message('Os filmes em exibição no Forum Algarve são:\nQu\'est-ce qu\'on a encore fait au Bon Dieu?,\nFrozen II,\nKnives Out,\nCharlie’s Angels,\nThe Aeronauts,\nStar Wars: Episode IX - The Rise of Skywalker')
                self.send_message('Os filmes em exibição no Mar Shopping Algarve são:\nFrozen II,\nKnives Out,\nCharlie’s Angels,\nThe Aeronauts,\nLe Mans 66\',\nBikes,\nStar Wars: Episode IX - The Rise of Skywalker')
            elif self.msg_count == 4:
                # Pedir ao utilizador para consultar filmes com a participação do Kevin Hart.
                self.send_movie(
                    '<b>Título:</b> Jumanji: O Nível Seguinte\n' +
                    '<b>Título original:</b> Jumanji: The Next Level\n' +
                    '<b>Elenco:</b> Dwayne Johnson, Jack Black, Kevin Hart\n' +
                    '<b>Produtor:</b> Jake Kasdan\n' +
                    '<b>Género:</b> Aventura\n' +
                    '<b>Duração:</b> 120 minutos\n' +
                    '<b>Idade:</b> 18 anos\n' +
                    '<b>Sinopse:</b> O gang está de volta, mas o jogo mudou. Quando regressam a Jumanji para resgatar um deles, descobrem que nada é como estavam à espera. Os jogadores terão de enfrentar lugares desconhecidos e inexplorados, desde os áridos desertos às montanhas nevadas, para escapar do jogo mais perigoso do mundo.\n' +
                    '<b>Trailer:</b> https://youtube.com/embed/yx9u6IsJrxM',
                    'http://cinemas.nos.pt/_layouts/15/Handlers/RenderImage.ashx?file=52259.jpg'
                )
            if self.msg_count == 5:
                # Pedir ao utilizador para consultar próximas estreias.
                self.send_message('As próximas estreias dos cinemas NOS são:')
                self.send_movie(
                    '<b>Título:</b> Jumanji: The Next Level\n' +
                    '<b>Elenco:</b> Dwayne Johnson, Jack Black, Kevin Hart\n' +
                    '<b>Género:</b> Aventura',
                    'http://cinemas.nos.pt/_layouts/15/Handlers/RenderImage.ashx?file=52259.jpg'
                )
                self.send_movie(
                    '<b>Título:</b> 21 Bridges\n' +
                    '<b>Elenco:</b> Chadwick Boseman, J.K. Simmons, Sienna Miller\n' +
                    '<b>Género:</b> Ação',
                    'http://cinemas.nos.pt/_layouts/15/Handlers/RenderImage.ashx?file=52264.jpg'
                )
            elif self.msg_count == 6:
                # Pedir ao utilizador para consultar próximas sessões.
                self.send_message('Próximas sessões no Braga Parque:')
                self.send_message(
                    '<b>Filme</b>: Joker\n' +
                    '<b>Data</b>: 09-12-2019\n' +
                    '<b>Hora de início</b>: 21:00:00\n' + 
                    '<b>Lugares disponíveis</b>: 10\n' +
                    '<b>Link de compra</b>: https://bilheteira.cinemas.nos.pt/webticket/bilhete.jsp?CinemaId=WA&CodFilme=1983870&DataSessao=2019-12-09&HoraSessao=21:00&Sala=5'
                )
                self.send_message(
                    '<b>Filme</b>: The Aeronauts\n' +
                    '<b>Data</b>: 09-12-2019\n' +
                    '<b>Hora de início</b>: 21:20:00\n' +
                    '<b>Lugares disponíveis</b>: 17\n' +
                    '<b>Link de compra</b>: https://bilheteira.cinemas.nos.pt/webticket/bilhete.jsp?CinemaId=WA&CodFilme=1728200&DataSessao=2019-12-09&HoraSessao=21:20&Sala=6'
                )
                self.send_message(
                    '<b>Filme</b>: Playing with Fire\n' +
                    '<b>Data</b>: 09-12-2019\n' +
                    '<b>Hora de início</b>: 21:50:00\n' +
                    '<b>Lugares disponíveis</b>: 24\n' +
                    '<b>Link de compra</b>: https://bilheteira.cinemas.nos.pt/webticket/bilhete.jsp?CinemaId=WA&CodFilme=1736700&DataSessao=2019-12-09&HoraSessao=21:50&Sala=9'
                )
            elif self.msg_count == 7:
                # Pedir ao utilizador para consultar próximas sessões do filme Countdown.
                self.send_message('Próximas sessões do filme Countdown no Braga Parque:')
                self.send_message(
                    '<b>Data</b>: 09-12-2019\n' +
                    '<b>Hora de início</b>: 22:00:00\n' +
                    '<b>Lugares disponíveis</b>: 45\n' +
                    '<b>Link de compra</b>: https://bilheteira.cinemas.nos.pt/webticket/bilhete.jsp?CinemaId=WA&CodFilme=1000318&DataSessao=2019-12-09&HoraSessao=22:00&Sala=1'
                )
                self.send_message(
                    '<b>Data</b>: 09-12-2019\n' +
                    '<b>Hora de início</b>: 00:25:00\n' +
                    '<b>Lugares disponíveis</b>: 60\n' +
                    '<b>Link de compra</b>: https://bilheteira.cinemas.nos.pt/webticket/bilhete.jsp?CinemaId=WA&CodFilme=1000318&DataSessao=2019-12-10&HoraSessao=00:25&Sala=1'
                )
            elif self.msg_count == 8:
                # Pedir ao utilizador para consultar a linha de apoio para esclarecimentos sobre pacotes da NOS.
                self.send_message('Linha de apoio para pacotes com televisão:')
                self.send_message(
                    '<b>Número:</b> 16990\n' + 
                    'Para esclarecimentos ou informações adicionais sobre todos os produtos incluídos na fatura de televisão NOS (internet fixa, telefone, telemóvel e internet móvel)'
                )
            elif self.msg_count == 9:
                # Pedir ao utilizador para consultar as informações do Sony Xperia 1.
                self.send_message('Sony Xperia 1')
                self.send_message(
                    '<b>Preço:</b> 959,99€\n' +
                    '<b>Preço:</b> Coluna Bluetooth\n' +
                    '<b>Link:</b> https://www.nos.pt/particulares/loja-equipamentos/pages/details.aspx?p=29783\n' +
                    '* possibilidade de pagamento em prestações\n' +
                    '* possibilidade de pagamento com pontos'
                )
            elif self.msg_count == 10:
                # Pedir ao utilizador para consultar os telemóveis que se encontram em promoção.
                self.send_message('Os telemóveis que correspondem à procura são:')
                self.send_message(
                    '<b>Modelo:</b> Huawei P30 Pro\n' +
                    '<b>Preço:</b> 899,99€'
                )
                self.send_message(
                    '<b>Modelo:</b> Huawei Mate 20 Lite\n' +
                    '<b>Preço:</b> 239,99€'
                )
                self.send_message(
                    '<b>Modelo:</b> Huawei P30\n' +
                    '<b>Preço:</b> 689,99€'
                )
                self.send_message(
                    '<b>Modelo:</b> Samsung Galaxy S10\n' +
                    '<b>Preço:</b> 819,99€'
                )
                self.send_message(
                    '<b>Modelo:</b> Samsung Galaxy S10+\n' +
                    '<b>Preço:</b> 919,99€'
                )
            elif self.msg_count == 11:
                # Pedir ao utilizador para consultar tarifários WTF.
                self.send_message('Os pacotes WTF que correspondem à procura são:')
                self.send_message(
                    '<b>Nome:</b> WTF 1GB\n' +
                    '<b>Preço:</b> 2.75/semana\n' +
                    '<b>Net:</b> 1GB/mês\n' +
                    '<b>SMS:</b> SMS grátis para todas as redes\n' +
                    '<b>Chamadas:</b> 1000 minutos para todas as redes'
                )
                self.send_message(
                    '<b>Nome:</b> WTF 5GB\n' +
                    '<b>Preço:</b> 3.99/semana\n' +
                    '<b>Net:</b> 5GB/mês\n' +
                    '<b>SMS:</b> SMS grátis para todas as redes\n' +
                    '<b>Chamadas:</b> 5000 minutos para todas as redes'
                )
                self.send_message(
                    '<b>Nome:</b> WTF 10GB\n' +
                    '<b>Preço:</b> 4.99/semana\n' +
                    '<b>Net:</b> 5GB/mês\n' +
                    '<b>SMS:</b> SMS grátis para todas as redes\n' +
                    '<b>Chamadas:</b> 10000 minutos para todas as redes'
                )
            elif self.msg_count == 12:
                # Pedir ao utilizador para consultar os pacotes fibra até 25€ por mês.
                self.send_message('Os pacotes fibra com valor entre 0€ e 25€ são:')
                self.send_message(
                    '<b>Nome:</b> MIX\n' +
                    '<b>Preço:</b> 24,99€\n' +
                    '<b>Serviço:</b> TV'
                )
                self.send_message(
                    '<b>Nome:</b> NOS 2\n' +
                    '<b>Preço:</b> 13,49€\n' +
                    '<b>Serviço:</b> TV+VOZ'
                )
                self.send_message(
                    '<b>Nome:</b> Segunda Casa\n' +
                    '<b>Preço:</b> 13,99€\n' +
                    '<b>Serviço:</b> TV'
                )
                self.send_message(
                    '<b>Nome:</b> Light\n' +
                    '<b>Preço:</b> 13,99€\n' +
                    '<b>Serviço:</b> TV'
                )
            elif self.msg_count == 13:
                # Pedir ao utilizador para consultar os pacotes satélite com TV e Internet.
                self.send_message('Os pacotes satélite com serviço TV+NET disponíveis são:')
                self.send_message(
                    '<b>Nome:</b> NOS 2 Segunda Casa + Net\n' +
                    '<b>Preço:</b> 27,99€\n' +
                    '<b>Serviço:</b> TV+NET'
                )
                self.send_message(
                    '<b>Nome:</b> NOS 2 Segunda Casa + Net\n' +
                    '<b>Preço:</b> 30,49€\n' +
                    '<b>Serviço:</b> TV+NET'
                )
                self.send_message(
                    '<b>Nome:</b> NOS 2 Segunda Casa + Net\n' +
                    '<b>Preço:</b> 27,99€\n' +
                    '<b>Serviço:</b> TV+NET'
                )
            elif self.msg_count == 14:
                # Pedir ao utilizador para consultar lojas NOS que existem em Portalegre.
                self.send_message('As lojas NOS existentes em Portalegre são:')
                self.send_message(
                    '<b>Nome:</b> Loja NOS Portalegre - Continente\n' +
                    '<b>Morada:</b> CC Continente Portalegre - R. Joinal, 12 - lj. 1 Portalegre 7300-526\n' +
                    '<b>Serviço:</b> Segunda a Sexta: 09h00 - 21h00 Sábado: 09h00 - 21h00 Domingo: 09h00 - 21h00'
                )
            elif self.msg_count > 14:
                self.send_message('Chegaste ao fim do teste!')

            self.msg_count = self.msg_count + 1