# Django

# Comandos principais

1. Criando um ambiente virtual -> python -m venv venv
2. Ativando o ambiente virtual -> venv\Scripts\activate
3. Instalar o django no projeto -> pip install django
4. Para criar um projeto Django -> django-admin startproject project .
5. Para subir o servidor -> python manage.py runserver
6. Para criar um novo app -> python manage.py startapp sistema
7. Para criar um superuser -> python manage.py createsuperuser
8. Para alterar a senha caso você esqueça -> python manage.py changepassword nomedousuario
9. Para instalar o Pillow no projeto-> python -m pip install Pillow
10. Para gerar o pacote de migração -> python manage.py makemigrations
11. Para rodar as alterações desse pacote -> python manage.py migrate
12. Para coletar todos os arquivos estaticos do projeto -> python manage.py collectstatic



# Principais Arquivos/Pastas do Project
1. settings.py -> é o arquivo de configuração do projeto.
2. urls.py -> é o arquivo base[principal] de urls do projeto.

# Documentação
1. ``urls`` -> https://docs.djangoproject.com/en/5.1/topics/http/urls/
2. ``settings`` -> https://docs.djangoproject.com/en/5.1/topics/settings/ ; https://docs.djangoproject.com/en/5.1/ref/settings/


# Criação das entidades do Sistema

[Paciente:]
nome
sobrenome
email
telefone
dt.criação
mensagem
ativo
imagem

[Especialidade]
ortopedia
cardiologia
neurologia
clinico geral

[Medico]
nome
sobrenome
crm
email
data de cadastro
telefone
imagem
ativo
mensagem

[Consulta]

[Endereço]

## Aula do dia 08/04/2025
1. INJEÇÃO DE CONTEXTO -> utilizando o dicionário ``CONTEXT`` para acessar todos os objetos.
- class Paciente (Modelo - Tabela)
- Acessar todos os objetos(instancias) que foram criadas a partir do Paciente
- Renderizar todos esses contatos no arquivo lista.html



## 1. Incluir alguns comandos no settings.py para tratar as imagens;
## 2. Ir no urls.py e incluir uma rota dinamica para imagens;
## 3 ir no listar.html e incluir o campo imagem;