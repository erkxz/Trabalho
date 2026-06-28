import streamlit as st
import json
import os

ARQUIVO = "funcionarios.json"

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {}

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

if "dados" not in st.session_state:
    st.session_state.dados = carregar()

dados = st.session_state.dados

st.set_page_config(page_title="Sistema de Funcionários", page_icon="👥", layout="centered")

st.title("👥 Sistema de Cadastro de Funcionários")
st.caption("CRUD completo com persistência em JSON")

aba = st.tabs(["📋 Listar", "➕ Cadastrar", "🔍 Buscar", "✏️ Atualizar", "🗑️ Excluir"])

with aba[0]:
    st.subheader("Funcionários Cadastrados")
    if not dados:
        st.info("Nenhum funcionário cadastrado ainda.")
    else:
        for cpf, f in dados.items():
            with st.container(border=True):
                col1, col2, col3, col4 = st.columns([2, 2, 2, 1.5])
                col1.markdown(f"**CPF:** {cpf}")
                col2.markdown(f"**Nome:** {f['nome']}")
                col3.markdown(f"**Cargo:** {f['cargo']}")
                col4.markdown(f"**Salário:** R$ {float(f['salario']):,.2f}")

with aba[1]:
    st.subheader("Cadastrar Novo Funcionário")
    with st.form("form_cadastrar"):
        cpf = st.text_input("CPF")
        nome = st.text_input("Nome")
        cargo = st.text_input("Cargo")
        salario = st.number_input("Salário (R$)", min_value=0.0, step=100.0, format="%.2f")
        enviar = st.form_submit_button("Cadastrar", use_container_width=True)

    if enviar:
        if not cpf or not nome or not cargo:
            st.error("Preencha todos os campos.")
        elif cpf in dados:
            st.warning("CPF já cadastrado.")
        else:
            dados[cpf] = {"nome": nome, "cargo": cargo, "salario": str(salario)}
            salvar(dados)
            st.success(f"Funcionário **{nome}** cadastrado com sucesso!")

with aba[2]:
    st.subheader("Buscar Funcionário por CPF")
    cpf_busca = st.text_input("CPF", key="cpf_busca")
    if st.button("Buscar", use_container_width=True):
        if cpf_busca in dados:
            f = dados[cpf_busca]
            st.success("Funcionário encontrado!")
            col1, col2, col3 = st.columns(3)
            col1.metric("Nome", f["nome"])
            col2.metric("Cargo", f["cargo"])
            col3.metric("Salário", f"R$ {float(f['salario']):,.2f}")
        else:
            st.error("CPF não encontrado.")

with aba[3]:
    st.subheader("Atualizar Funcionário")
    cpf_atualizar = st.text_input("CPF do funcionário", key="cpf_atualizar")

    if cpf_atualizar in dados:
        f = dados[cpf_atualizar]
        st.info(f"Editando: **{f['nome']}** — {f['cargo']} — R$ {float(f['salario']):,.2f}")
        with st.form("form_atualizar"):
            novo_nome = st.text_input("Novo nome", value=f["nome"])
            novo_cargo = st.text_input("Novo cargo", value=f["cargo"])
            novo_salario = st.number_input("Novo salário (R$)", value=float(f["salario"]), min_value=0.0, step=100.0, format="%.2f")
            salvar_btn = st.form_submit_button("Salvar alterações", use_container_width=True)

        if salvar_btn:
            dados[cpf_atualizar] = {"nome": novo_nome, "cargo": novo_cargo, "salario": str(novo_salario)}
            salvar(dados)
            st.success("Dados atualizados com sucesso!")
    elif cpf_atualizar:
        st.error("CPF não encontrado.")

with aba[4]:
    st.subheader("Excluir Funcionário")
    cpf_excluir = st.text_input("CPF do funcionário", key="cpf_excluir")

    if cpf_excluir in dados:
        f = dados[cpf_excluir]
        st.warning(f"Você está prestes a excluir **{f['nome']}** ({cpf_excluir}). Esta ação é irreversível.")
        if st.button("Confirmar exclusão", type="primary", use_container_width=True):
            del dados[cpf_excluir]
            salvar(dados)
            st.success("Funcionário removido com sucesso!")
    elif cpf_excluir:
        st.error("CPF não encontrado.")
