import streamlit as st
from PIL import Image

# ===============================
# ⚙️ Configuração da página
# ===============================
st.set_page_config(
    page_title="EduFin AI Cloud — Inteligência Financeira Pessoal",
    page_icon="💡",
    layout="wide"
)

# ===============================
# 🎨 Estilo visual tipo Dribbble
# ===============================
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
    color: #111;
    font-weight: 600;
}
.main-container {
    background: white;
    padding: 2.5rem 3rem;
    border-radius: 16px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.06);
    margin-top: 2rem;
}
.stButton>button {
    border-radius: 8px;
    background-color: #FF5B6A;
    color: white;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: bold;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #E14B58;
    transform: translateY(-2px);
}
a {
    color: #FF5B6A !important;
    text-decoration: none;
    font-weight: 500;
}
a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 🧠 Cabeçalho principal
# ===============================
st.markdown("<h1 style='text-align:center;'>💡 EduFin AI Cloud</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#666;'>Inteligência Financeira com IA e Firebase</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#777;'>Analise sua saúde financeira com aprendizado de máquina em tempo real.</p>", unsafe_allow_html=True)

# ===============================
# 🧩 Layout principal (duas colunas)
# ===============================
st.markdown('<div class="main-container">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 0.8])

# --- Coluna 1: descrição do projeto ---
with col1:
    st.markdown("## 🧠 Como funciona")
    st.markdown("""
    1. Faça login com seu e-mail.  
    2. Insira seus dados financeiros (renda, gastos, dívidas, etc).  
    3. A IA analisa e retorna sua **saúde financeira**:
       - 🔴 Baixa  
       - 🟡 Média  
       - 🟢 Alta  
    """)

    st.markdown("## ⚙️ Tecnologias usadas")
    st.markdown("""
    - **Streamlit** → Interface interativa  
    - **Firebase Auth + Firestore** → Login e banco de dados  
    - **TensorFlow / Keras** → Rede neural preditiva  
    - **Scikit-Learn** → Pré-processamento e métricas
    """)

    st.markdown("## 📱 Telas do App Android")
    try:
        col_a, col_b = st.columns(2)
        with col_a:
            st.image("login_screen2.png", caption="🔐 Tela de Login", use_column_width=True)
        with col_b:
            st.image("main_screen2.png", caption="📊 Tela Principal", use_column_width=True)
    except Exception as e:
        st.warning(f"⚠️ Erro ao carregar imagens: {e}")

# --- Coluna 2: mini simulação ---
with col2:
    st.markdown("### 🧩 Mini Simulação — Teste sua Saúde Financeira")

    renda = st.slider("💰 Renda mensal (R$)", 500, 20000, 5000)
    gastos = st.slider("💳 Gastos mensais (R$)", 0, 20000, 3000)
    dividas = st.slider("📉 Dívidas (R$)", 0, 50000, 1000)
    poupanca = st.slider("🏦 Poupança (R$)", 0, 50000, 2000)
    idade = st.slider("🎂 Idade", 18, 80, 30)
    investimentos = st.slider("📈 Investimentos (R$)", 0, 50000, 1000)

    # Mock simples de cálculo de "score"
    score = (renda - gastos - dividas + poupanca + investimentos) / (renda + 1)

    if score < 0.3:
        st.error("🔴 Baixa Saúde Financeira")
    elif score < 0.6:
        st.warning("🟡 Média Saúde Financeira")
    else:
        st.success("🟢 Alta Saúde Financeira")

st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 📄 Rodapé
# ===============================
st.markdown("---")
st.caption("© 2025 EduFin AI Cloud — Projeto de Demonstração com IA, Firebase e Streamlit")
