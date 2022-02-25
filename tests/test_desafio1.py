from desafio1 import triangle


def teste_se_parametro_da_funcao_triangle_e_inteiro():
    assert triangle("3") is False


def teste_se_retorno_da_funcao_triangle_e_um_string():
    assert type(triangle(3)) == str


def teste_se_dado_um_numero_a_funcao_triangle_retorna_um_triangle():
    assert triangle(3) == "  *" + "\n **" + "\n***"
    assert triangle(4) == "   *" + "\n  **" + "\n ***" + "\n****"
