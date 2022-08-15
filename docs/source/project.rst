=======
project
=======

Pacote destinado a conter funcionalidades genéricas aos projetos.


utils.py
--------

.. function:: themispy.project.utils.split_filepath(url: str) -> list[str, str]

    Divide a URL de um arquivo e retorna uma tupla contendo dois elementos, respectivamente: o nome do arquivo e sua extensão.

    :param str url: URL do arquivo.

    :returns: Nome do arquivo e sua extensão como uma tupla de dois elementos.   



.. function:: themispy.project.utils.get_logpath(tz: str = 'America/Sao_Paulo') -> str

    Função utilizada para construir um padrão de data com o formato adequado para utilização nas pastas do sistema.

    :param str tz: Fuso-horário. (Padrão: ``America/Sao_Paulo``)

    :returns: Data atual com o formato adequado.
