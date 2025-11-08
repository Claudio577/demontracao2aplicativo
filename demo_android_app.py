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
# 🎨 Estilo visual moderno (Dribbble-like)
# ===============================
# Mantendo o CSS para o layout clean e moderno, conforme o código fornecido.
st.markdown("""
<style>
/* Configuração de tipografia e fundo */
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3, h4 {
    color: #111;
    font-weight: 600;
}
/* Estilo do container principal */
.main-container {
    background: white;
    padding: 2.5rem 3rem;
    border-radius: 16px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.06);
    margin-top: 2rem;
}
/* Estilo dos botões */
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
# CABEÇALHO PRINCIPAL E TECNOLOGIAS (Clean, sem emotis no título)
# ===============================
st.markdown("<h1 style='text-align:center;'>EduFin AI Cloud</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#666;'>Inteligência Financeira Pessoal com Machine Learning</h4>", unsafe_allow_html=True)
st.markdown("---")

# Informações de tecnologia solicitadas (no início e simples)
st.markdown("### ⚙️ Tecnologias Principais do Projeto")
st.markdown("""
- **Streamlit**: Interface interativa de fácil prototipação e implementação.
- **Firebase Auth + Firestore**: Gerenciamento de login e banco de dados NoSQL em tempo real.
- **TensorFlow / Keras**: Ferramentas para construção de rede neural preditiva.
- **Scikit-Learn**: Utilizado para pré-processamento de dados e métricas de desempenho do modelo.
""")
st.markdown("---")


# ===============================
# 🌐 Utilidades Atuais das Tecnologias
# ===============================
st.markdown("## Aplicações e Utilidades Atuais")
st.markdown("""
O conjunto de tecnologias utilizado neste projeto (Streamlit, Firebase, Keras, Scikit-Learn) é a base para diversas aplicações modernas:

1.  **Streamlit e Prototipação Rápida:**
    * **Utilidade:** Permite que cientistas de dados e desenvolvedores criem **dashboards interativos de IA** e **MVPs (Produtos Mínimos Viáveis)** rapidamente, transformando modelos de *machine learning* complexos em ferramentas de negócios acessíveis.
    * **Exemplos:** Dashboards de monitoramento de saúde de servidores, ferramentas de visualização de dados geográficos.

2.  **Firebase (Auth e Firestore) para Back-end:**
    * **Utilidade:** Oferece um back-end gerenciado, facilitando a **escalabilidade de aplicações** com autenticação segura de usuários e persistência de dados em tempo real.
    * **Exemplos:** Aplicativos móveis e web de grande escala, plataformas de colaboração em tempo real, jogos com ranking de usuários.

3.  **TensorFlow / Keras e Scikit-Learn (O Coração da IA):**
    * **Utilidade:** É a espinha dorsal para a criação de modelos preditivos e analíticos em quase todos os setores.
    * **Exemplos:**
        * **Finanças:** Detecção de fraudes em transações, previsão de risco de inadimplência (como no EduFin).
        * **Saúde:** Análise de imagens médicas para diagnóstico automático, previsão de surtos de doenças.
        * **Indústria:** Manutenção preditiva de equipamentos (identificar falhas antes que ocorram).
""")
st.markdown("---")

# ===============================
# 🧩 Layout principal (duas colunas)
# ===============================
st.markdown('<div class="main-container">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 0.8])

# --- Coluna 1: descrição do projeto ---
with col1:
    st.markdown("## Sobre o Projeto EduFin")
    st.markdown("""
    O EduFin AI Cloud é um demonstrativo que utiliza aprendizado de máquina (ML) para analisar a saúde financeira pessoal em tempo real. A aplicação simula o fluxo completo de uma solução real, desde o cadastro do usuário até a análise preditiva.
    """)
    
    st.markdown("## Fluxo de Análise da Saúde Financeira")
    st.markdown("""
    1. O usuário insere seus dados (renda, gastos, investimentos, etc.).
    2. O sistema de ML calcula um índice de equilíbrio financeiro.
    3. O resultado é classificado para indicar o nível de risco e a necessidade de ação.
    
    **Classificação do Risco:**
    - **🔴 Risco Alto:** Necessidade de intervenção urgente.
    - **🟡 Risco Moderado:** Requer ajustes e otimização.
    - **🟢 Risco Baixo:** Excelente saúde financeira.
    """)

    # === INCLUSÃO DAS IMAGENS E EXPLICAÇÕES (Conforme solicitado) ===
    st.markdown("## Telas do App (Android - Mockup)")
    st.markdown("""
    Essas telas demonstram o design moderno e limpo do aplicativo, projetado para
    uma experiência de usuário agradável e intuitiva, seguindo o padrão Dribbble.
    """)

    col_a, col_b = st.columns(2)
    
    # Imagem 1: Login Screen
    with col_a:
        st.image("uploaded:Captura de Tela 2025-11-08 às 13.37.11.jpg-d5f51bd9-9e70-4ecb-bd6a-96e1564c1bb1", caption="Tela de Login (Autenticação)", use_column_width=True)
        st.markdown("**1. Tela de Login:** Interface de autenticação segura via Firebase Auth, permitindo acesso personalizado e persistência de dados.")
        
    # Imagem 2: Main Screen
    with col_b:
        st.image("uploaded:Captura de Tela 2025-11-08 às 13.46.49.jpg-45d89d75-db6f-4b24-a923-97602349b930", caption="Tela Principal (Análise e Simulação)", use_column_width=True)
        st.markdown("**2. Tela Principal:** Dashboard interativo onde o usuário insere dados e visualiza o impacto da simulação em seu índice de saúde financeira.")
    # ===============================================================

# --- Coluna 2: mini simulação (mantendo o uso de cores) ---
with col2:
    st.markdown("### Mini Simulação — Teste seu Equilíbrio")

    # Sliders para simulação de dados
    renda = st.slider("Renda mensal (R$)", 1000, 20000, 5000)
    gastos = st.slider("Gastos mensais (R$)", 0, 20000, 3000)
    dividas = st.slider("Dívidas (R$)", 0, 50000, 1000)
    poupanca = st.slider("Poupança (R$)", 0, 50000, 2000)
    idade = st.slider("Idade", 18, 80, 30)
    investimentos = st.slider("Investimentos (R$)", 0, 50000, 1000)

    # Mock simples de cálculo de "score"
    # Fator de equilíbrio: (Renda + Poupança + Investimentos) / (Gastos + Dívidas)
    
    # Adicionando um pequeno valor ao denominador para evitar divisão por zero
    denominador = gastos + dividas + 1 
    score = (renda + poupanca + investimentos) / (denominador)

    st.markdown("---")
    st.markdown("#### Resultado da Simulação")

    # Lógica de Classificação Vermelho, Amarelo, Verde
    if score < 1.0:
        st.error(f"🔴 Baixa Saúde Financeira (Fator: {score:.2f})")
    elif score < 2.0:
        st.warning(f"🟡 Média Saúde Financeira (Fator: {score:.2f})")
    else:
        st.success(f"🟢 Alta Saúde Financeira (Fator: {score:.2f})")
        
    st.markdown(f"**Margem Líquida Estimada:** R$ {renda - gastos - dividas:.2f}")

st.markdown('</div>', unsafe_allow_html=True)
