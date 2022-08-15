import datetime
import os

import pytz


def split_filepath(url: str) -> 'tuple[str, str]':
    """Divide a URL de um arquivo e retorna uma tupla contendo dois
    elementos, respectivamente: o nome do arquivo e sua extensão.
    
    Args:
        url (str): URL do arquivo.
        
    Returns:
        Nome do arquivo e sua extensão como uma tupla de dois
        elementos.
    
    """
    docname, docext = os.path.splitext(url)
    docname = docname.rsplit('/')[-1]
    return docname, docext


def get_logpath(tz: str = 'America/Sao_Paulo') -> str:
    """Função utilizada para construir um padrão de data com o formato
    adequado para utilização nas pastas do sistema.
    
    Args:
        tz (str): Fuso-horário. (São Paulo é utilizado por padrão).
        
    Returns:
        Data atual com o formato adequado.
        
    Example:
        Supondo dia atual como 14/08/2022 a função retornará: '2022/08/14'.
    
    """
    tz = pytz.timezone(tz)
    return datetime.datetime.now(tz=tz).strftime('/%Y/%m/%d')
