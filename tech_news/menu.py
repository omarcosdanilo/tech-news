import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)

from tech_news.scraper import get_tech_news


def funcao0():
    value = int(input("Digite quantas notícias serão buscadas:"))

    print(get_tech_news(value))


def funcao1():
    value = input("Digite o título:")

    print(search_by_title(value))


def funcao2():
    value = input("Digite a data no formato aaaa-mm-dd:")

    print(search_by_date(value))


def funcao3():
    value = input("Digite a tag:")

    print(search_by_tag(value))


def funcao4():
    value = input("Digite a categoria:")

    print(search_by_category(value))


def funcao5():
    print(top_5_news())


def funcao6():
    print(top_5_categories())


def funcao7():
    print('Encerrando script')


functions = {
    "0": funcao0,
    "1": funcao1,
    "2": funcao2,
    "3": funcao3,
    "4": funcao4,
    "5": funcao5,
    "6": funcao6,
    "7": funcao7
}


def analyzer_menu():

    options_typed = input(
        """
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
 """
    )

    try:
        functions[options_typed]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
