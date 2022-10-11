======
scrapy
======

Neste pacote, os módulos foram criados seguindo do modelo do Scrapy,
a fim de manter um padrão de documentação e uso.

A única novidade é o módulo denominado ``readers.py``,
onde existe uma função criada para ler fontes de dados de blobs na Azure.


items.py
--------

.. class:: themispy.project.items.FileDownloader

    Classe de Item do Scrapy que serve como base para baixar arquivos.
    Extende a classe de 'Item' do Scrapy.

    .. attribute:: file_urls

        Campo que receberá a URL do arquivo a ser baixado.

    .. attribute:: files

        Campo que registrará o status do arquivo a ser baixado.


pipelines.py
------------

.. class:: themispy.project.items.AzureBlobUploadPipeline

    Classe criada a fim de subir arquivos para o Azure Storage.
    Extende a classe 'Spider' padrão do Scrapy.


    .. attribute:: blob_client

        Cliente de conexão com um Blob no Azure Storage.
        O Blob não precisa existir previamente.
        Para que o cliente possa ser criado, são necessários:
        ``conn_str``, ``container_name``, ``blob_name``.
        Também, por padrão, ``logging_enable`` possui o valor ``True``.


    .. attribute:: content

        String vazia que será preenchida, linha a linha, com o dicionário
        será retornado da sentença ``yield`` na construção da Spider.


    .. method:: open_spider(self, spider)

        Neste método será criada a conexão com o Blob e também inicializado atributo ``content``.

    
    .. method:: process_item(self, item, spider)

        Aqui será processado o retorno dos dados do crawler e convertido para ``.jsonl``.


    .. method:: close_spider(self, spider)

        É aqui, durante o encerramento da spider, que o todo o conteúdo gerado
        durante o processamento será enviado para o Azure Storage, através do método ``upload_blob``.
        Por padrão, será passado como argumento ``overwrite=True``.



.. class:: themispy.project.items.AzureFileDownloaderPipeline
    
    Classe extendida a partir da classe ``FilesPipeline`` do Scrapy.
    É utilizada para se baixar arquivos (os quais são fornecidas suas URLs de download).
    Os arquivos são enviados diretamente para o Azure Storage.

    .. note::
        Não esquecer de passar nas configurações do Scrapy a chave ``FILES_STORE``.


    .. attribute:: spiderinfo
        
        Informações da spider que serão necessárias para o registro do status de download dos arquivos.


    .. attribute:: container_client

        Cliente de conexão com um container no Azure Storage.
        O Container precisa existir previamente.
        Para que o cliente possa ser criado, são necessários:
        ``conn_str`` e ``container_name``.
        Também, por padrão, ``logging_enable`` possui o valor ``True``.


    .. attribute:: blob_client

        Cliente de conexão com um Blob no Azure Storage.
        O Blob não precisa existir previamente.
        Para que o cliente possa ser criado, é necessário passar o nome do ``blob`` que será criado.


    .. method:: open_spider(self, spider)

        É durante a abertura da spider que a conexão com o container é criada.
        Dessa maneira, independentemente de quantos arquivos serão baixados, apenas uma conexão com o container é criada.

    .. method:: file_downloaded(self, response, request, info, *, item=None)
    
        É precisamente neste método, exatamente no momento em que os dados do arquivo
        baixado estão em memória, que é criado um cliente com o Blob e o arquivo é subido no Azure Storage.
        Por padrão, é passado ao ``upload_blob`` o argumento ``overwrite=True``.



readers.py
------------

.. function:: themispy.project.readers.list_blob_content(url: str, encoding: str = 'UTF-8', logging_enable: bool = True) -> list[str]

    Lê o conteúdo do blob em questão, convertendo para lista utilizando as quebras de linhas.

    :param str url: Caminho completo do blob dentro da Azure. Exemplo: ``https://<nome_do_storage>.blob.core.windows.net/<container>/meu_arquivo.jsonl``.

    :param str encoding: Formato de codificação dos caracteres. (``UTF-8`` é o padrão.)

    :param bool logging_enable: Indica se a função deverá ativar o logger ou não. (Padrão é ``True``.)

    :returns: Conteúdo do blob como lista de strings.



spiders.py
------------

.. function:: themispy.project.spiders.run_spider(spider: scrapy.Spider, pipeline: str = None, settings: dict = None, override: bool = False) -> None

    Processo para executar spiders.


    :param scrapy.Spider spider: Spider a ser executada.

    :param str pipeline: Pipeline a ser utilizada durante a execução da spider. Deve ser ``blob`` ou ``download``. Referindo, respectivamente, as pipelines de AzureBlobUpload ou AzureFileDownloader.

    :param dict settings: Configurações do Scrapy para a execução das spiders. Passe aqui suas configurações personalizáveis para serem adicionadas às padrões.

    :param bool override: Caso seja ``True``, as configurações recebidas sobrescreverão todas as anteriores.
