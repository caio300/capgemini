from desafio2 import password


def teste_se_parametro_da_funcao_password_e_inteiro():
    assert password(3) is False


def teste_se_retorno_da_funcao_password_e_um_int():
    assert type(password("Ya3")) == int


def teste_quantos_critérios_faltam_para_completar_uma_senha_forte():
    assert password("Ya3") == 3
    assert password("aaaaaa") == 3
    assert password("Abcd&0") == 0
    assert password("aaaa") == 3
    assert password("a") == 5
    assert password("aW2*") == 2
