from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
from selenium.webdriver.common.keys import Keys
import urllib.parse
from webdriver_manager.chrome import ChromeDriverManager


app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


@app.route('/')
def index():
    return render_template('inicio.html')


# Rota para exibir o formulário HTML
@app.route("/formulario.html")
def formulario():
    return render_template('formulario.html')


@app.route("/modo2")
def modo2():
    return render_template('modo2.html')


@app.route('/automação/modo2.py', methods=['POST'])
def enviar_excel():
    excel_file = request.files['excel_file']

    if excel_file.filename.endswith('.xlsx'):
        # Cria o diretório temporário, se não existir
        if not os.path.exists('temp'):
            os.makedirs('temp')

        # Salva o arquivo temporariamente no diretório 'temp'
        file_path = os.path.join('temp', excel_file.filename)
        excel_file.save(file_path)

        # Leitura do arquivo Excel usando pandas
        contatos_df = pd.read_excel(file_path)

        navegador = webdriver.Chrome(ChromeDriverManager().install())  # Utiliza o ChromeDriverManager para obter o caminho do ChromeDriver
        navegador.get("https://web.whatsapp.com/")

        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(2)

        # Já estamos com o login feito no WhatsApp Web
        for i, mensagem in enumerate(contatos_df['Mensagem']):
            pessoa = contatos_df.loc[i, "Pessoa"]
            numero = contatos_df.loc[i, "Número"]
            Codigo = contatos_df.loc[i, "Cod"]
            texto = urllib.parse.quote(f"Boa tarde! {pessoa}, Tudo bem? Me chamo Lucas e faço parte da equipe de atendimento Femme9. Vi que você realizou uma compra conosco e estou entrando em contato para disponibilizar o seu código de rastreio.🦋💜💙\nAssim que seu pedido chegar, nos informe que estaremos a disposição para te auxiliar no que for preciso.\n\nPara rastreio de sua peça, basta acessar o site : https://rastreae.com.br/busca e inserir esse\n\nCódigo: {Codigo}{mensagem}")
            link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
            navegador.get(link)
            time.sleep(10)  # Aguarda 5 segundos para carregar a página do WhatsApp

            # Verifica se o chat foi aberto
            if len(navegador.find_elements(By.ID, "side")) < 1:
                print(f"Não foi possível abrir o chat para o número {numero}. Pulando para o próximo número.")
                continue

            try:
                input_box = WebDriverWait(navegador, 40).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'))
                )
                input_box.send_keys(Keys.ENTER)
                time.sleep(8)
            except:
                print(f"Erro ao enviar mensagem para o número {numero}. Pulando para o próximo número.")
                continue

        # Fecha o navegador após o envio das mensagens
        navegador.quit()

        return "Mensagens enviadas com sucesso!"
    else:
        return "Por favor, selecione um arquivo Excel (.xlsx)"


@app.route('/automação/modo1.py', methods=['POST'])

def enviar_mensagem():
    # Ler os números de telefone e mensagens enviados pelo formulário
    telefones = []
    mensagens = []
    for key in request.form.keys():
        if key.startswith('telefone-'):
            telefone = request.form[key]
            telefones.append(telefone)
        elif key.startswith('mensagem-'):
            mensagem = request.form[key]
            mensagens.append(mensagem)

    # Ler a planilha existente ou criar uma nova
    try:
        planilha = pd.read_excel('mensagens.xlsx')
    except FileNotFoundError:
        dados = {'Número': [], 'Mensagem': []}
        planilha = pd.DataFrame(dados)

    # Salvar os números de telefone e mensagens na planilha
    dados = {'Número': telefones, 'Mensagem': mensagens}
    df = pd.DataFrame(dados)
    planilha = pd.concat([planilha, df], ignore_index=True)
    planilha.to_excel('mensagens.xlsx', index=False)

    # Inicializar o driver do Chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())  # Utiliza o ChromeDriverManager para obter o caminho do ChromeDriver
    driver.get('https://web.whatsapp.com')

    # Aguardar até que o usuário faça o login manualmente
    input('Faça o login no WhatsApp Web e pressione Enter para continuar...')

    # Iterar sobre os números de telefone e mensagens e enviar as mensagens correspondentes
    for telefone, mensagem in zip(telefones, mensagens):
        texto = urllib.parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
        driver.get(link)
        time.sleep(5)  # Aguarda 5 segundos para carregar a página do WhatsApp

        # Verifica se o chat foi aberto
        if len(driver.find_elements(By.ID, "side")) < 1:
            print(f"Não foi possível abrir o chat para o número {telefone}. Pulando para o próximo número.")
            continue

        try:
            input_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'))
            )
            input_box.send_keys(Keys.ENTER)
            time.sleep(5)
        except:
            print(f"Erro ao enviar mensagem para o número {telefone}. Pulando para o próximo número.")
            continue

    # Fechar o navegador
    driver.quit()

    return 'Mensagens enviadas com sucesso!'


def carregar_planilha():
    return pd.read_excel('Teste1.xlsx')


def obter_numeros(planilha):
    return planilha['numero'].tolist()


df = carregar_planilha()
numeros = obter_numeros(df)


@app.route('/modo3')
def modo3():
    return render_template('modo3.html', contatos=numeros)


@app.route('/automação/modo3.py', methods=['POST'])

def enviar_mensagens():
    # Ler as mensagens do formulário HTML
    mensagem_input = request.form['mensagem']
    mensagens_adicionadas = request.form.getlist('mensagens_adicionadas')

    # Combinar a mensagem do campo de entrada e as mensagens adicionadas
    mensagens = [mensagem_input] + mensagens_adicionadas

    # Ler novamente a planilha para obter os contatos
    df = carregar_planilha()
    numeros = obter_numeros(df)

    # Abre o Chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://web.whatsapp.com/')

    while len(driver.find_elements(By.ID, "side")) < 1:
        time.sleep(1)

    # Aguarda o login manual no WhatsApp Web
    # ...

    for numero in numeros:
        enviar_link(numero, driver)

        # Aguardar até que o chat esteja aberto
        timeout = 15  # Tempo máximo de espera em segundos
        start_time = time.time()

        while not chat_aberto(driver):
            elapsed_time = time.time() - start_time

            if elapsed_time > timeout:
                print(f"O chat não foi aberto para o número {numero}. Pulando para o próximo número.")
                break

            time.sleep(1)

        if not chat_aberto(driver):
            continue

        for mensagem in mensagens:
            enviar_mensagem(mensagem, driver)

        time.sleep(3)

    # Fechar o navegador
    driver.quit()

    return 'Mensagens enviadas com sucesso!'


def enviar_link(numero, driver):
    link = f"https://web.whatsapp.com/send?phone={numero}&text="
    driver.get(link)


def enviar_mensagem(mensagem, driver):
    campo_mensagem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
    )
    campo_mensagem.click()
    time.sleep(2)
    campo_mensagem.send_keys(str(mensagem) + Keys.ENTER)


def chat_aberto(driver):
    try:
        campo_mensagem = driver.find_element(By.XPATH,
                                             '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        return True
    except:
        return False



if __name__ == '__main__':
    app.run(debug=True)
