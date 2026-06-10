import json
import os

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "funcionarios.json")

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def cadastrar(dados):
    print("\n--- CADASTRAR FUNCIONARIO ---")
    cpf = input("CPF (somente numeros): ").strip()
    if cpf in dados:
        print("ERRO: CPF ja cadastrado!")
        return
    nome    = input("Nome completo: ").strip()
    cargo   = input("Cargo: ").strip()
    salario = input("Salario (R$): ").strip()
    dados[cpf] = {"nome": nome, "cargo": cargo, "salario": salario}
    salvar(dados)
    print("Funcionario cadastrado com sucesso!")

def listar(dados):
    print("\n--- LISTA DE FUNCIONARIOS ---")
    if not dados:
        print("Nenhum funcionario cadastrado.")
        return
    print(f"{'CPF':<15} {'Nome':<25} {'Cargo':<20} {'Salario':>10}")
    print("-" * 72)
    for cpf, f in dados.items():
        print(f"{cpf:<15} {f['nome']:<25} {f['cargo']:<20} {f['salario']:>10}")

def buscar(dados):
    print("\n--- BUSCAR FUNCIONARIO ---")
    cpf = input("CPF do funcionario: ").strip()
    if cpf not in dados:
        print("ERRO: Funcionario nao encontrado.")
        return
    f = dados[cpf]
    print(f"Nome  : {f['nome']}")
    print(f"Cargo : {f['cargo']}")
    print(f"Sal.  : R$ {f['salario']}")

def atualizar(dados):
    print("\n--- ATUALIZAR FUNCIONARIO ---")
    cpf = input("CPF do funcionario: ").strip()
    if cpf not in dados:
        print("ERRO: Funcionario nao encontrado.")
        return
    f = dados[cpf]
    print("Deixe em branco para manter o valor atual.")
    novo_nome  = input(f"Novo nome [{f['nome']}]: ").strip()
    novo_cargo = input(f"Novo cargo [{f['cargo']}]: ").strip()
    novo_sal   = input(f"Novo salario [{f['salario']}]: ").strip()
    if novo_nome:  f["nome"]    = novo_nome
    if novo_cargo: f["cargo"]   = novo_cargo
    if novo_sal:   f["salario"] = novo_sal
    salvar(dados)
    print("Dados atualizados com sucesso!")

def excluir(dados):
    print("\n--- EXCLUIR FUNCIONARIO ---")
    cpf = input("CPF do funcionario: ").strip()
    if cpf not in dados:
        print("ERRO: Funcionario nao encontrado.")
        return
    confirm = input(f"Excluir '{dados[cpf]['nome']}'? (s/n): ").strip().lower()
    if confirm == "s":
        del dados[cpf]
        salvar(dados)
        print("Funcionario excluido com sucesso!")
    else:
        print("Operacao cancelada.")

def menu():
    dados = carregar()
    while True:
        print("\n==============================")
        print("  SISTEMA DE FUNCIONARIOS")
        print("==============================")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Atualizar")
        print("5. Excluir")
        print("0. Sair")
        print("------------------------------")
        opcao = input("Escolha: ").strip()

        if   opcao == "1": cadastrar(dados)
        elif opcao == "2": listar(dados)
        elif opcao == "3": buscar(dados)
        elif opcao == "4": atualizar(dados)
        elif opcao == "5": excluir(dados)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    menu()
