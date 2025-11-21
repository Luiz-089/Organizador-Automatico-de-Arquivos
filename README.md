#Organizador Automático de Arquivos

Um script em Python que organiza automaticamente os arquivos de uma pasta, separando-os por categorias como imagens, vídeos e documentos. Simples, útil e ideal para iniciantes que desejam praticar Python e organização de diretórios.
---
Funcionalidades

Organiza arquivos por tipo (imagens, vídeos, documentos, etc.)

Cria pastas automaticamente caso não existam

Evita sobrescrever arquivos repetidos

Código simples, de fácil leitura e edição

Tutorial de Execução
1. Instale o Python

Acesse o site oficial:
https://www.python.org/downloads/

Durante a instalação, marque a opção:
Add Python to PATH

2. Baixe o arquivo organizer.py

Coloque o arquivo dentro da pasta que deseja organizar.

Exemplo de estrutura:

Downloads/
 └── organizer.py

3. Abra o terminal na pasta correta

No Windows:

Abra a pasta onde está o arquivo

Clique na barra de endereço

Digite cmd e pressione Enter

Isso abrirá o terminal já no diretório correto.

4. Execute o script

No terminal, digite:

python organizer.py


ou, se necessário:

py organizer.py

Como funciona

O script cria automaticamente pastas para cada categoria e move os arquivos correspondentes.
Caso um arquivo com o mesmo nome exista dentro da pasta de destino, ele renomeia para evitar sobrescrita.

Tecnologias Utilizadas

Python 3

Módulos padrão: os, shutil

Problemas Comuns

1. "python não é reconhecido"
→ O Python não foi adicionado ao PATH. Reinstale marcando a opção Add Python to PATH.

2. "No such file or directory"
→ O terminal não está na mesma pasta do script.

Use o comando:

dir


para verificar se o arquivo aparece.

3. Permissão negada
→ Tente executar o CMD como administrador ou usar uma pasta diferente.
