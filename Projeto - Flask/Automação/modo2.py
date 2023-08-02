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
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

@app.route('/modo2.py', methods=['POST'])
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

        navegador = webdriver.Chrome(service=Service('path_to_chromedriver'))  # Insira o caminho para o chromedriver
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

if __name__ == '__main__':
    app.run(debug=True)
