import os
import xml.dom.minidom
import xml.etree.ElementTree as ET
from datetime import datetime


def update_last_update_minidom(xml_file_path:str, output_directory:str):
    """Função para atualizar o atributo lastUpdate usando o minidom"""
    
    print(xml_file_path)
    # Carrega o XML
    dom = xml.dom.minidom.parse(xml_file_path)
    
    # Encontrar a tag entity-relation-data
    entity_relation_data = dom.getElementsByTagName('entity-relation-data')[0]
    
    # Atualizar o atributo lastUpdate com a data e hora atual
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entity_relation_data.setAttribute('lastUpdate', current_time)
    
    # Monta o caminho de saída para salvar o XML atualizando, preservando assim o original
    output_file_path = os.path.join(output_directory, os.path.basename(xml_file_path))
    
    # Salvar o XML atualizado
    with open(output_file_path, 'w', encoding='ISO-8859-1') as output_file:
        # dom.encoding = 'ISO-8859-1'
        # output_file.write(dom.toxml())

        output_file.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
        # Escreve o conteúdo do XML sem a declaração
        output_file.write(dom.toxml()) 

        # xmlString = dom.toprettyxml(encoding='ISO-8859-1')
        # output_file.write(xmlString.decode('ISO-8859-1')) 

def update_last_update_elementtree(xml_file_path:str, output_directory:str):
    try:
        """Função para atualizar o atributo lastUpdate usando o ElementTree"""
        print(xml_file_path)

        # Carregar o arquivo XML
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        # Atualizar o atributo lastUpdate com a data e hora atual
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        root.set('lastUpdate', current_time)
        
        # Monta o caminho de saída para salvar o XML atualizando, preservando assim o original
        output_file_path = os.path.join(output_directory, os.path.basename(xml_file_path))
        
        # Salvar o XML atualizado
        tree.write(output_file_path, encoding='ISO-8859-1', xml_declaration=True)
    except Exception as error:
        print('Erro no arquivo:' ,xml_file_path)


if __name__== '__main__':

    print("Processo de atualização iniciado concluída.")

    # Diretório com as entidades de origem
    input_directory = 'C:\\DATABASE-IBICT\\Finalizados\\2024\\PatentsLattes'
    # Diretório de armazenamento das entidades atualizadas
    output_directory = 'C:\\DATABASE-IBICT\\Finalizados\\2025\\PatentsLattes'

    # Criar o diretório de saída caso não exista
    os.makedirs(output_directory, exist_ok=True)

    # Iterar sobre todos os arquivos XML no diretório de entrada
    for filename in os.listdir(input_directory):
        if filename.endswith('.xml'):
            xml_file_path = os.path.join(input_directory, filename)
            update_last_update_elementtree(xml_file_path, output_directory)

    print("Atualização concluída.")