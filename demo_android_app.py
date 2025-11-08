import streamlit as st
from PIL import Image

# ===============================
# ⚙️ Configuração da página
# ===============================
st.set_page_config(page_title="EduFin Mobile — Demo", page_icon="📱", layout="wide")

# ===============================
# 🎨 Estilo visual tipo Dribbble
# ===============================
st.markdown("""
<style>
body {
    background-color: #fafafa;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
    color: #111;
    font-weight: 600;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.stButton>button {
    border-radius: 8px;
    background-color: #FF5B6A;
    color: white;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #E14B58;
}
a {
    color: #FF5B6A !important;
    text-decoration: none;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 🧩 Cabeçalho do projeto
# ===============================
st.title("📱 EduFin — App Mobile de Saúde Financeira com IA")
st.subheader("Aplicativo Android nativo com Firebase e IA para previsão financeira pessoal.")

st.markdown("""
💡 **Descrição do Projeto**
> O aplicativo EduFin ajuda o usuário a avaliar sua **saúde financeira** com base em sua renda, gastos, dívidas, poupança e investimentos.
> O design foi construído em **XML Android Studio** com um layout simples e intuitivo.
""")

# ===============================
# 🎨 Mockup / Captura de tela
# ===============================
col1, col2 = st.columns([1.2, 0.8])
with col1:
    st.markdown("""
    ### 🧠 Funcionalidades
    - Cadastro e login com Firebase Authentication  
    - Armazenamento de dados no Firestore  
    - Previsão da saúde financeira com modelo Keras  
    - Interface leve com ícones intuitivos  
    - Atualização em tempo real via botão 🔁  

    ### ⚙️ Tecnologias usadas
    - **Android Studio (Java/Kotlin + XML)**  
    - **Firebase Authentication / Firestore**  
    - **TensorFlow Lite (modelo de IA)**  
    - **Material Design Components**
    """)
with col2:
    st.image("app_mockup.png", caption="Tela principal do app EduFin (UI XML)", use_container_width=True)

# ===============================
# 💬 Mini Simulação (demo interativa)
# ===============================
st.markdown("---")
st.header("💰 Simule sua Saúde Financeira")

renda = st.slider("Renda mensal (R$)", 500, 20000, 4000)
gastos = st.slider("Gastos mensais (R$)", 0, 20000, 2500)
dividas = st.slider("Dívidas (R$)", 0, 50000, 1000)
poupanca = st.slider("Poupança (R$)", 0, 50000, 1500)
idade = st.slider("Idade", 18, 80, 30)
investimentos = st.slider("Investimentos (R$)", 0, 50000, 2000)

score = (renda - gastos - dividas + poupanca + investimentos) / (renda + 1)
if score < 0.3:
    st.error("🔴 Baixa Saúde Financeira")
elif score < 0.6:
    st.warning("🟡 Média Saúde Financeira")
else:
    st.success("🟢 Alta Saúde Financeira")

st.markdown("---")
st.caption("© 2025 EduFin Mobile — Projeto Android com IA e Firebase")
