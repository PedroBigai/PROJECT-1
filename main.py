from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import re


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID_ROMANA = '1RzQF3jagzS0JsDORB1RKWDoz4pxHv0EIpxu_rhY3keQ'
SAMPLE_RANGE_NAME_ROMANA = 'Table 1!A4:G49'

SAMPLE_SPREADSHEET_ID_PH = '1-kh7dcM5GBXW34KnpKAwh7s-UXrPYXCrzuug2_j2wco'
SAMPLE_RANGE_NAME_PH = 'Table 2!A2:G22'

SAMPLE_SPREADSHEET_ID_DV_SCRREN = '1CBiupLEQ6zNUjQk10hJJKkeNE_zzDD1_-qtq5BuRyRg'
SAMPLE_RANGE_NAME_DV_SCREEN = 'Table 2!A2:G18'

SAMPLE_SPREADSHEET_ID_ROLO = '1LvYFBPUNEcqWR6VJdF3PB-8qTcAcP5wcMQturwkXIXM'
SAMPLE_RANGE_NAME_ROLO = 'Table 1!A3:I39'

SAMPLE_SPREADSHEET_ID_ROLO_PV_BK = '1p7wjIS6fQWBy_Y_jcWjw5xsWhW3dEHqOFmAJ9nA1n9I'
SAMPLE_RANGE_NAME_PV_BK = 'Table 2!A2:F17'

SAMPLE_SPREADSHEET_ID_PV = '1OuPv0OV29ysJUUsdF1IJBxt4dH9bAsjd32lKxejRmGc'
SAMPLE_RANGE_NAME_PV = 'Table 2!A2:F38'

SAMPLE_SPREADSHEET_ID_ACESS_ROLO = '1Of0qgsk2-gwyFl9YUpXJmSaBCtuSBIoJU-R_OS8sRj0'
SAMPLE_RANGE_NAME_ACESS_ROLO = 'Table 2!A2:E28'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


class AplicativoPersiana(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.largura_input = TextInput(hint_text="Largura", font_size=20, foreground_color=(1, 1, 1), background_color=(0, 0, 0), padding=10)
        self.layout.add_widget(self.largura_input)
        
        self.altura_input = TextInput(hint_text="Altura", font_size=20, foreground_color=(1, 1, 1), background_color=(0, 0, 0))
        self.layout.add_widget(self.altura_input)

        self.codigo_input = TextInput(hint_text="Qual o código do tecido:", font_size=20, foreground_color=(1, 1, 1), background_color=(0, 0, 0))
        self.layout.add_widget(self.codigo_input)

        self.modelo_persiana_input = Button(text="Modelo", on_press=self.abrir_popup_modelos)
        self.layout.add_widget(self.modelo_persiana_input)

        self.acess_button = Button(text="Acessórios", on_press=self.abrir_janela_acessorios)
        self.layout.add_widget(self.acess_button)

        
        self.resultado_label = Label(text="", font_size=20, size_hint_y=5, height=100)
        self.layout.add_widget(self.resultado_label)
        
        return self.layout
    
    def abrir_popup_modelos(self, instance):
        from kivy.uix.popup import Popup
        content = BoxLayout(orientation='vertical', spacing=10, padding=20)
        botão_rolo = Button(text="Rolô", on_press=self.modelo_rolo)
        content.add_widget(botão_rolo)
        botão_romana = Button(text="Romana", on_press=self.modelo_romana)
        content.add_widget(botão_romana)
        botão_ph = Button(text="PH", on_press=self.modelo_ph)
        content.add_widget(botão_ph)
        botão_dv = Button(text="DV Screen", on_press=self.modelo_dv)
        content.add_widget(botão_dv)
        botão_pv = Button(text="PV", on_press=self.modelo_pv)
        content.add_widget(botão_pv)
        botão_pv_bk = Button(text="PV BK", on_press=self.modelo_pv_bk)
        content.add_widget(botão_pv_bk)
        self.popup = Popup(title="Escolher o modelo", content=content, size_hint=(None, None), size=(600, 600))
        self.popup.open()

    def modelo_rolo(self, instance) :
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_ROLO,
                                        range=SAMPLE_RANGE_NAME_ROLO).execute()
            values = result.get('values', [])
            largura = float(self.largura_input.text)
            altura = float(self.altura_input.text)
            resultado = altura * largura
            formatacao = "{:.2f}".format(resultado)
            modelo_persiana = self.modelo_persiana_input.text
            perguntar_tecido = self.codigo_input.text
            if not values:
                print('No data found.')
                return
            modelo_persiana = "Rolô"
            if modelo_persiana == "Rolô":
                for row in values:
                    tecido = row[0]
                    codigo = row[1]
                    largura = row[4]
                    preco_vista = row[6]
                    preco_prazo = row[8]
                    if perguntar_tecido in str(codigo) or perguntar_tecido == str(tecido):
                        self.resultado_label.text = f"Tecido encontrado na tabela:\n"
                        self.resultado_label.text += f"Tecido: {tecido}\n"
                        self.resultado_label.text += f"Código: {codigo}\n"
                        self.resultado_label.text += f"Largura: {largura}\n"
                        preco_vista_match = re.search(r"(\d+\,\d+)", preco_vista)
                        preco_prazo_match = re.search(r"(\d+\,\d+)", preco_prazo)
                        if preco_vista_match and preco_prazo_match:
                            preco_vista_float = float(preco_vista_match.group(1).replace(',', '.'))
                            preco_prazo_float = float(preco_prazo_match.group(1).replace(',', '.'))

                            # Atualizar as strings dos preços com os valores inteiros
                            self.resultado_label.text += f"Preço à vista: R${preco_vista_float}\n"
                            self.resultado_label.text += f"Preço a prazo: R${preco_prazo_float}\n"
                        
                            self.resultado_label.text += f"Total de tecido: {formatacao}m\n"

                            preco_total_vista = (preco_vista_float * resultado) * 1.5
                            preco_total_prazo = (preco_prazo_float * resultado) * 1.5

                            self.resultado_label.text += f"Preço total à vista: R${preco_total_vista:.2f}\n"
                            self.resultado_label.text += f"Preço total a prazo: R${preco_total_prazo:.2f}\n"

                            self.total_vista_acessorios =  preco_total_vista
                            self.total_prazo_acessorios =  preco_total_prazo
                        break
                    else:
                        self.resultado_label.text = "Modelo/Código de cortina não encontrado."
            self.popup.dismiss()
        
        except ValueError:
            self.resultado_label.text = "Digite números válidos"
            
            return
        
    def modelo_romana(self, instance) :
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_ROMANA,
                                        range=SAMPLE_RANGE_NAME_ROMANA).execute()
            values = result.get('values', [])

            largura = float(self.largura_input.text)
            altura = float(self.altura_input.text)
            resultado = altura * largura
            formatacao = "{:.2f}".format(resultado)

            modelo_persiana = self.modelo_persiana_input.text
            perguntar_tecido = self.codigo_input.text
            
            if not values:
                print('No data found.')
                return
            modelo_persiana = "Romana"
            if modelo_persiana == "Romana":
                for row in values:
                    tecido = row[0]
                    codigo = row[1]
                    largura = row[4]
                    preco_vista = row[5]
                    preco_prazo = row[6]
                    if perguntar_tecido in str(codigo) or perguntar_tecido == str(tecido):
                        self.resultado_label.text = f"Tecido encontrado na tabela:\n"
                        self.resultado_label.text += f"Tecido: {tecido}\n"
                        self.resultado_label.text += f"Código: {codigo}\n"
                        self.resultado_label.text += f"Larguta: {largura}\n"
                        preco_vista_match = re.search(r"(\d+\,\d+)", preco_vista)
                        preco_prazo_match = re.search(r"(\d+\,\d+)", preco_prazo)
                        if preco_vista_match and preco_prazo_match:
                            preco_vista_float = float(preco_vista_match.group(1).replace(',', '.'))
                            preco_prazo_float = float(preco_prazo_match.group(1).replace(',', '.'))

                            # Atualizar as strings dos preços com os valores inteiros
                            self.resultado_label.text += f"Preço à vista: R${preco_vista_float}\n"
                            self.resultado_label.text += f"Preço a prazo: R${preco_prazo_float}\n"
                        
                            self.resultado_label.text += f"Total de tecido: {formatacao}m\n"

                            preco_total_vista = (preco_vista_float * resultado) * 1.5
                            preco_total_prazo = (preco_prazo_float * resultado) * 1.5

                            self.resultado_label.text += f"Preço total à vista: R${preco_total_vista:.2f}\n"
                            self.resultado_label.text += f"Preço total a prazo: R${preco_total_prazo:.2f}\n"

                            self.total_vista_acessorios =  preco_total_vista
                            self.total_prazo_acessorios =  preco_total_prazo
                        break
                    else:
                        self.resultado_label.text = "Modelo/Código de cortina não encontrado."
            self.popup.dismiss()
        
        except ValueError:
            self.resultado_label.text = "Digite números válidos"
            
            return
        
    def modelo_ph(self, instance) :
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_PH,
                                        range=SAMPLE_RANGE_NAME_PH).execute()
            values = result.get('values', [])

            largura = float(self.largura_input.text)
            altura = float(self.altura_input.text)
            resultado = altura * largura
            formatacao = "{:.2f}".format(resultado)

            modelo_persiana = self.modelo_persiana_input.text
            perguntar_tecido = self.codigo_input.text
            
            if not values:
                print('No data found.')
                return
            modelo_persiana = "PH"
            if modelo_persiana == "PH":
                for row in values:
                    tecido = row[0]
                    codigo = row[1]
                    preco_vista = row[3]
                    preco_prazo = row[5]
                    if perguntar_tecido == str(codigo) or perguntar_tecido == str(tecido):
                        self.resultado_label.text = f"Tecido encontrado na tabela:\n"
                        self.resultado_label.text += f"Tecido: {tecido}\n"
                        self.resultado_label.text += f"Código: {codigo}\n"
                        preco_vista_match = re.search(r"(\d+\,\d+)", preco_vista)
                        preco_prazo_match = re.search(r"(\d+\,\d+)", preco_prazo)
                        
                        preco_vista_float = float(preco_vista_match.group(1).replace(',', '.'))
                        preco_prazo_float = float(preco_prazo_match.group(1).replace(',', '.'))

                        # Atualizar as strings dos preços com os valores inteiros
                        self.resultado_label.text += f"Preço à vista: R${preco_vista_float}\n"
                        self.resultado_label.text += f"Preço a prazo: R${preco_prazo_float}\n"
                        
                        self.resultado_label.text += f"Total de tecido: {formatacao}m\n"

                        preco_total_vista = (preco_vista_float * resultado) * 1.5
                        preco_total_prazo = (preco_prazo_float * resultado) * 1.5

                        self.resultado_label.text += f"Preço total à vista: R${preco_total_vista:.2f}\n"
                        self.resultado_label.text += f"Preço total a prazo: R${preco_total_prazo:.2f}\n"

                        self.total_vista_acessorios =  preco_total_vista
                        self.total_prazo_acessorios =  preco_total_prazo
                        break
                    else:
                        self.resultado_label.text = "Modelo/Código de cortina não encontrado."
            self.popup.dismiss()
        
        except ValueError:
            self.resultado_label.text = "Digite números válidos"
            
            return
        
    def modelo_dv(self, instance) :
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_DV_SCRREN,
                                        range=SAMPLE_RANGE_NAME_DV_SCREEN).execute()
            values = result.get('values', [])

            largura = float(self.largura_input.text)
            altura = float(self.altura_input.text)
            resultado = altura * largura
            formatacao = "{:.2f}".format(resultado)

            modelo_persiana = self.modelo_persiana_input.text
            perguntar_tecido = self.codigo_input.text
            
            if not values:
                print('No data found.')
                return
            modelo_persiana = "DV"
            if modelo_persiana == "DV":
                for row in values:
                    tecido = row[0]
                    codigo = row[1]
                    largura = row[2]
                    preco_vista = row[4]
                    preco_prazo = row[6]
                    if perguntar_tecido in str(codigo) or perguntar_tecido == str(tecido):
                        self.resultado_label.text = f"Tecido encontrado na tabela:\n"
                        self.resultado_label.text += f"Tecido: {tecido}\n"
                        self.resultado_label.text += f"Código: {codigo}\n"
                        preco_vista_match = re.search(r"(\d+\,\d+)", preco_vista)
                        preco_prazo_match = re.search(r"(\d+\,\d+)", preco_prazo)
                        if preco_vista_match and preco_prazo_match:
                            preco_vista_float = float(preco_vista_match.group(1).replace(',', '.'))
                            preco_prazo_float = float(preco_prazo_match.group(1).replace(',', '.'))

                            # Atualizar as strings dos preços com os valores inteiros
                            self.resultado_label.text += f"Preço à vista: R${preco_vista_float}\n"
                            self.resultado_label.text += f"Preço a prazo: R${preco_prazo_float}\n"
                        
                            self.resultado_label.text += f"Total de tecido: {formatacao}m\n"

                            preco_total_vista = (preco_vista_float * resultado) * 1.5
                            preco_total_prazo = (preco_prazo_float * resultado) * 1.5

                            self.resultado_label.text += f"Preço total à vista: R${preco_total_vista:.2f}\n"
                            self.resultado_label.text += f"Preço total a prazo: R${preco_total_prazo:.2f}\n"

                            self.total_vista_acessorios =  preco_total_vista
                            self.total_prazo_acessorios =  preco_total_prazo
                        break
                    else:
                        self.resultado_label.text = "Modelo/Código de cortina não encontrado."
            self.popup.dismiss()
        
        except ValueError:
            self.resultado_label.text = "Digite números válidos"
            
            return
        
    def modelo_pv(self, instance) :
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_PV,
                                        range=SAMPLE_RANGE_NAME_PV).execute()
            values = result.get('values', [])

            largura = float(self.largura_input.text)
            altura = float(self.altura_input.text)
            resultado = altura * largura
            formatacao = "{:.2f}".format(resultado)

            modelo_persiana = self.modelo_persiana_input.text
            perguntar_tecido = self.codigo_input.text
            
            if not values:
                print('No data found.')
                return
            modelo_persiana = "PV"
            if modelo_persiana == "PV":
                for row in values:
                    tecido = row[0]
                    codigo = row[1]
                    preco_vista = row[3]
                    preco_prazo = row[5]
                    if perguntar_tecido in str(codigo) or perguntar_tecido == str(tecido):
                        self.resultado_label.text = f"Tecido encontrado na tabela:\n"
                        self.resultado_label.text += f"Tecido: {tecido}\n"
                        self.resultado_label.text += f"Código: {codigo}\n"
                        preco_vista_match = re.search(r"(\d+\,\d+)", preco_vista)
                        preco_prazo_match = re.search(r"(\d+\,\d+)", preco_prazo)
                        if preco_vista_match and preco_prazo_match:
                            preco_vista_float = float(preco_vista_match.group(1).replace(',', '.'))
                            preco_prazo_float = float(preco_prazo_match.group(1).replace(',', '.'))

                            # Atualizar as strings dos preços com os valores inteiros
                            self.resultado_label.text += f"Preço à vista: R${preco_vista_float}\n"
                            self.resultado_label.text += f"Preço a prazo: R${preco_prazo_float}\n"
                        
                            self.resultado_label.text += f"Total de tecido: {formatacao}m\n"

                            preco_total_vista = (preco_vista_float * resultado) * 1.5
                            preco_total_prazo = (preco_prazo_float * resultado) * 1.5

                            self.resultado_label.text += f"Preço total à vista: R${preco_total_vista:.2f}\n"
                            self.resultado_label.text += f"Preço total a prazo: R${preco_total_prazo:.2f}\n"

                            self.total_vista_acessorios =  preco_total_vista
                            self.total_prazo_acessorios =  preco_total_prazo
                        break
                    else:
                        self.resultado_label.text = "Modelo/Código de cortina não encontrado."
            self.popup.dismiss()
        
        except ValueError:
            self.resultado_label.text = "Digite números válidos"
            
            return
        
    def modelo_pv_bk(self, instance) :
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_ROLO_PV_BK,
                                        range=SAMPLE_RANGE_NAME_PV_BK).execute()
            values = result.get('values', [])

            largura = float(self.largura_input.text)
            altura = float(self.altura_input.text)
            resultado = altura * largura
            formatacao = "{:.2f}".format(resultado)

            modelo_persiana = self.modelo_persiana_input.text
            perguntar_tecido = self.codigo_input.text
            
            if not values:
                print('No data found.')
                return
            modelo_persiana = "PV BK"
            if modelo_persiana == "PV BK":
                for row in values:
                    tecido = row[0]
                    codigo = row[1]
                    preco_vista = row[3]
                    preco_prazo = row[5]
                    if perguntar_tecido in str(codigo) or perguntar_tecido == str(tecido):
                        self.resultado_label.text = f"Tecido encontrado na tabela:\n"
                        self.resultado_label.text += f"Tecido: {tecido}\n"
                        self.resultado_label.text += f"Código: {codigo}\n"
                        preco_vista_match = re.search(r"(\d+\,\d+)", preco_vista)
                        preco_prazo_match = re.search(r"(\d+\,\d+)", preco_prazo)
                        if preco_vista_match and preco_prazo_match:
                            preco_vista_float = float(preco_vista_match.group(1).replace(',', '.'))
                            preco_prazo_float = float(preco_prazo_match.group(1).replace(',', '.'))

                            # Atualizar as strings dos preços com os valores inteiros
                            self.resultado_label.text += f"Preço à vista: R${preco_vista_float}\n"
                            self.resultado_label.text += f"Preço a prazo: R${preco_prazo_float}\n"
                        
                            self.resultado_label.text += f"Total de tecido: {formatacao}m\n"

                            preco_total_vista = (preco_vista_float * resultado) * 1.5
                            preco_total_prazo = (preco_prazo_float * resultado) * 1.5

                            self.resultado_label.text += f"Preço total à vista: R${preco_total_vista:.2f}\n"
                            self.resultado_label.text += f"Preço total a prazo: R${preco_total_prazo:.2f}\n"

                            self.total_vista_acessorios =  preco_total_vista
                            self.total_prazo_acessorios =  preco_total_prazo
                        break
                    else:
                        self.resultado_label.text = "Modelo/Código de cortina não encontrado."
            self.popup.dismiss()
        
        except ValueError:
            self.resultado_label.text = "Digite números válidos"
            
            return
        
    def abrir_janela_acessorios(self, instance):
        from kivy.uix.popup import Popup
        content = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.acessorios_input = TextInput(hint_text="Acessórios", font_size=20, foreground_color=(1, 1, 1), background_color=(0, 0, 0))
        content.add_widget(self.acessorios_input)
        self.resultado_label_popup = Label(text="", font_size=16, halign="left", valign="top")
        content.add_widget(self.resultado_label_popup)
        save_button = Button(text="Buscar Acessórios", on_press=self.mostrar_acessorios)
        content.add_widget(save_button)
        save_button2 = Button(text="Adicionar", on_press=self.adicionar_acessorios)
        content.add_widget(save_button2)
        save_button3 = Button(text="Sair", on_press=self.sair)
        content.add_widget(save_button3)
        try:    
            self.resultado_label_popup.text += f"Total Preço à Vista Acessórios: R${self.total_vista_acessorios:.2f}\n"
            self.resultado_label_popup.text += f"Total Preço a Prazo Acessórios: R${self.total_prazo_acessorios:.2f}\n"

            self.popup = Popup(title="Inserir Acessórios", content=content, size_hint=(None, None), size=(600, 600))
            self.popup.open()
        except AttributeError:
            return
        
    def mostrar_acessorios(self, instance):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_ACESS_ROLO,
                                        range=SAMPLE_RANGE_NAME_ACESS_ROLO).execute()
            values = result.get('values', [])
            result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_ROLO_PV_BK,
                                        range=SAMPLE_RANGE_NAME_PV_BK).execute()
            values2 = result.get('values', [])
            acessorios_digitados = self.acessorios_input.text
            encontrados = False
            resultados = []
            if acessorios_digitados:
                    for row in values:  # Substitua o número de linhas máximo conforme necessário
                        acess = row[0]
                        preco_vista = row[2]
                        preco_prazo = row[4]
                        if acessorios_digitados in str(acess):
                            encontrados = True
                            resultado = f"Acessório: {acess}\n"
                            if preco_vista is not None:
                                resultado += f"A vista: R${preco_vista:.2f}\n"
                            if preco_prazo is not None:
                                resultado += f"A prazo: R${preco_prazo:.2f}\n"
                                
                                resultados.append(resultado)

                            self.preco_vista_acessorio = preco_vista if preco_vista is not None else 0.0
                            self.preco_prazo_acessorio = preco_prazo if preco_prazo is not None else 0.0
            else:
                return
                
            if encontrados:
                self.resultado_label_popup.text = "\n".join(resultados)

            else:
                self.resultado_label_popup.text = "Nenhum acessório encontrado."
                
            for row in values2:  # Substitua o número de linhas máximo conforme necessário
                acess = row[0]
                preco_vista = row[3]
                preco_prazo = row[5]
                if acessorios_digitados in str(acess):
                    encontrados = True
                    resultado = f"Acessório: {acess}\n"
                    if preco_vista is not None:
                        resultado += f"A vista: R${preco_vista:.2f}\n"
                    if preco_prazo is not None:
                        resultado += f"A prazo: R${preco_prazo:.2f}\n"
                        
                        resultados.append(resultado)

                    self.preco_vista_acessorio = preco_vista if preco_vista is not None else 0.0
                    self.preco_prazo_acessorio = preco_prazo if preco_prazo is not None else 0.0
                    
            if encontrados:
                self.resultado_label_popup.text = "\n".join(resultados)
                
            else:
                self.resultado_label_popup.text = "Nenhum acessório encontrado."

        except AttributeError:
            return
            
    def adicionar_acessorios(self, instance):
    
        valor_a_vista = self.preco_vista_acessorio
        valor_a_prazo = self.preco_prazo_acessorio
        
        
        I = 0
        I2 = 0
        
        total_vista_acessorio = (valor_a_vista + I) * 1.5
        total_prazo_acessorio = (valor_a_prazo + I2) * 1.5
        
        self.total_vista_acessorios += total_vista_acessorio
        self.total_prazo_acessorios += total_prazo_acessorio
        
        self.resultado_label_popup.text = f"Total Preço à Vista C/ Acessórios: R${self.total_vista_acessorios:.2f}\n"
        self.resultado_label_popup.text += f"Total Preço a Prazo C/ Acessórios: R${self.total_prazo_acessorios:.2f}\n"

         
    def sair(self, instance):
        self.total_vista_acessorios 
        self.total_prazo_acessorios 
        self.popup.dismiss()


        
        
        

        





if __name__ == '__main__':
    main()

if __name__ == '__main__':
    AplicativoPersiana().run()

