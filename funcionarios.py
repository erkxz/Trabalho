import json
import os
pasta = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(pasta, "funcionarios.json")
def carregar():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except:
        return {}
def cadastrar(dados):
    cpf = input("cpf: ")
    if cpf in dados:
        print("ja cadastrado")
        return
    nome = input("nome: ")
    cargo = input("cargo: ")
    sal = input("salario: ")
    dados[cpf] = {"nome": nome, "cargo": cargo, "salario": sal}
    salvar(dados)
    print("cadastrado!")
def salvar(dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f)
def listar(dados):
    if not dados:
        print("nenhum funcionario")
        return
    for cpf, f in dados.items():
        print(cpf, "-", f["nome"], "-", f["cargo"], "- R$", f["salario"])
def buscar(dados):
    cpf = input("cpf: ")
    if cpf not in dados:
        print("nao encontrado")
        return
    f = dados[cpf]
    print(f["nome"], "|", f["cargo"], "| R$", f["salario"])
def excluir(dados):
    cpf = input("cpf: ")
    if cpf not in dados:
        print("nao encontrado")
        return
    del dados[cpf]
    salvar(dados)
    print("removido")
def atualizar(dados):
    cpf = input("cpf: ")
    if cpf not in dados:
        print("nao encontrado")
        return
    f = dados[cpf]
    n = input("novo nome (enter pra manter): ")
    c = input("novo cargo (enter pra manter): ")
    s = input("novo salario (enter pra manter): ")
    if n: f["nome"] = n
    if c: f["cargo"] = c
    if s: f["salario"] = s
    salvar(dados)
    print("atualizado")
dados = carregar()
while True:
    print("\n1-cadastrar 2-listar 3-buscar 4-atualizar 5-excluir 0-sair")
    op = input("> ")
    if op == "1": cadastrar(dados)
    elif op == "2": listar(dados)
    elif op == "3": buscar(dados)
    elif op == "4": atualizar(dados)
    elif op == "5": excluir(dados)
    elif op == "0": break
