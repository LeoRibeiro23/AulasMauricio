import streamlit as st
from conexao import conectar
import dashboard

#============================
# Configuracoes da pagina
#============================

st.set_page_config(
    page_title="Sistema de login",
    page_icon="https://img.icons8.com/?size=100&id=fu4OChmjxQuT&format=png&color=000000"
    Layout="centered"

)



#============================
# Controle da Sessão
#============================
if "logado" not in st.session_state:
    st.session_state=false
if "usuario"  not in st.session_state:
    st.session_state=" "
#============================
# Função para verificação do login
#============================
def verificar_login(usuario, senha):
    conexao=conectar()


    cursor = conexao.cursor()

    sql="""
        # instruções de multiplas linhas
        select id, usuraio
        from usuarios
        where usuario=%s
        and senha=%s
    """

cursor.execute(sql, (usuario, senha))

resultado = cursor.fetchone()

cursor.close()

conexao.close()

return resultado


#============================
# Tela de login
#===========================

if not st.session.state.logado:
   st,title("Sistema de login")
   t.write("informe suas credenciais para acessar o sistema.")
   st.divider()

   usuario=st.text.input(
    "Usuario"
   )
   senha=st.text.input(
      "Senha"
   )
if st.button("entrar", use_container_width=true)
    if usuario and senha:
        try:
            resultado=verificar_login(
                usuario,
                senha 
            )
            if resultado:
                st.session_state.logado=true
                st.session_state.usuario = resultado[1]
                st.success("Acesso autorizado!")
                st.return
            else:
                st.error("Usuario ou senha incorretos")

        except Exception as erro:
            st.error("Erro ao accesar o banco: {erro}")

    else:
        st.warning("Preencha os campos acima!")

#=================================================
#redirecionando o usuario para o arquivo dashboard
#=================================================

else: dashboard.exibir()