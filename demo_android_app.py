import streamlit as st
from PIL import Image, ImageChops

# =====================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================
st.set_page_config(
    page_title="EduFin AI Cloud — Inteligência Financeira Pessoal",
    layout="wide"
)

# =====================================
# ESTILO VISUAL DRIBBBLE + CORES ALEGRES (SEM BARRA SUPERIOR)
# =====================================
st.markdown("""
<style>
body {
    background-color: #f8f9fb;
    color: #222;
    font-family: 'Poppins', sans-serif;
}
header, [data-testid="stHeader"] {
    display: none;
}
h1, h2, h3, h4 {
    font-weight: 600;
}
.main-container {
    background: white;
    padding: 2.5rem 3rem;
    border-radius: 16px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.06);
    margin-top: 2rem;
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

# =====================================
# FUNÇÃO AUXILIAR — REMOVER BORDAS BRANCAS
# =====================================
def crop_white_borders(img_path):
    """Remove automaticamente bordas brancas das imagens."""
    try:
        img = Image.open(img_path)
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        if bbox:
            img = img.crop(bbox)
        return img
    except FileNotFoundError:
        st.warning(f"Imagem não encontrada: {img_path}")
        return None


# =====================================
# CABEÇALHO E APRESENTAÇÃO PESSOAL
# =====================================
st.markdown("<h1 style='text-align:center; color:#4B7BE5;'>EduFin AI Cloud</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#FF5B6A;'>Aplicativo de Inteligência Financeira com IA e Firebase</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#777;'>Um aplicativo educacional que une tecnologia e aprendizado de máquina para ensinar finanças de forma prática e interativa.</p>", unsafe_allow_html=True)

# Apresentação pessoal no topo
st.markdown("""
### Sobre o Desenvolvedor  
Sou **estudante e desenvolvedor na área de Inteligência Artificial aplicada (Machine Learning)**,  
atualmente atuando em projetos de **IA Educacional, FinTech e Blockchain Inteligente**.

No **curso em Machine Learning**, desenvolvo **protótipos funcionais** que conectam modelos de IA  
a sistemas reais, utilizando ferramentas como **Streamlit, Firebase, TensorFlow e Scikit-Learn**.

O **EduFin AI Cloud** é um **aplicativo desenvolvido nessa área**, unindo **IA aplicada e educação financeira**,  
mostrando como a tecnologia pode ser usada para **ensinar, simular e orientar decisões financeiras** de forma acessível.
""")

# =====================================
# DESCRIÇÃO E APLICAÇÃO NO MERCADO
# =====================================
st.markdown("## <span style='color:#6C63FF;'>Aplicações e Contexto do Projeto</span>", unsafe_allow_html=True)
st.markdown("""
O **EduFin AI Cloud** combina **educação financeira** e **inteligência artificial** para ajudar pessoas e instituições a compreenderem melhor sua **saúde financeira**.  
A aplicação utiliza IA para simular e avaliar o equilíbrio entre **renda, gastos, dívidas e investimentos**, fornecendo um diagnóstico claro e visual.

### Onde o projeto pode ser aplicado:
- **Educação e Escolas:** ensino de educação financeira com simulações em tempo real.  
- **Bancos e Fintechs:** criação de módulos de análise de risco e perfis financeiros.  
- **Consultorias Financeiras:** suporte a decisões personalizadas com base em dados.  
- **Projetos Sociais:** conscientização sobre controle de gastos e importância da poupança.  

O sistema serve tanto como ferramenta **didática** quanto **analítica**, mostrando como a IA pode ser aplicada de forma **acessível e educativa**.
""")

# =====================================
# BLOCO PRINCIPAL COM 2 COLUNAS
# =====================================
st.markdown('<div class="main-container">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 0.8])

# --- COLUNA 1: DESCRIÇÃO E IMAGENS ---
with col1:
    st.markdown("## <span style='color:#6C63FF;'>Como funciona</span>", unsafe_allow_html=True)
    st.markdown("""
    1. Faça login com seu e-mail.  
    2. Insira seus dados financeiros (renda, gastos, dívidas, etc).  
    3. A IA analisa e retorna sua **saúde financeira**:
        - Baixa  
        - Média  
        - Alta  
    """)

    st.markdown("## <span style='color:#FF5B6A;'>Tecnologias usadas</span>", unsafe_allow_html=True)
    st.markdown("""
    - **Streamlit** → Interface interativa  
    - **Firebase Auth + Firestore** → Login e banco de dados  
    - **TensorFlow / Keras** → Rede neural preditiva  
    - **Scikit-Learn** → Pré-processamento e métricas  
    """)

    st.markdown("## <span style='color:#2ECC71;'>Telas do App Android</span>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)

    login_img = crop_white_borders("login_screen2.png")
    main_img = crop_white_borders("main_screen2.png")

    with col_a:
        if login_img:
            st.image(login_img, caption="Tela de Login", use_column_width=True)
    with col_b:
        if main_img:
            st.image(main_img, caption="Tela Principal", use_column_width=True)

# --- COLUNA 2: MINI SIMULAÇÃO ---
with col2:
    st.markdown("### <span style='color:#F4A261;'>Mini Simulação — Teste sua Saúde Financeira</span>", unsafe_allow_html=True)

    renda = st.slider("Renda mensal (R$)", 500, 20000, 5000)
    gastos = st.slider("Gastos mensais (R$)", 0, 20000, 3000)
    dividas = st.slider("Dívidas (R$)", 0, 50000, 1000)
    poupanca = st.slider("Poupança (R$)", 0, 50000, 2000)
    investimentos = st.slider("Investimentos (R$)", 0, 50000, 1000)

    score = (renda - gastos - dividas + poupanca + investimentos) / (renda + 1)

    st.markdown("<h4 style='color:#3E8E7E;'>Resultado da Simulação</h4>", unsafe_allow_html=True)

    if score < 0.3:
        st.error("Baixa Saúde Financeira")
        st.metric("Índice de Equilíbrio", f"{score*100:.0f}%", "-15%", delta_color="inverse")
    elif score < 0.6:
        st.warning("Média Saúde Financeira")
        st.metric("Índice de Equilíbrio", f"{score*100:.0f}%", "+5%", delta_color="off")
    else:
        st.success("Alta Saúde Financeira")
        st.metric("Índice de Equilíbrio", f"{score*100:.0f}%", "+10%", delta_color="normal")

st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# SEÇÃO EDUCACIONAL
# =====================================
st.markdown("""
<h2 style='
  text-align:center;
  background: linear-gradient(90deg, #6C63FF, #4B7BE5);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
'>
Educação Financeira e Inteligência Artificial
</h2>
""", unsafe_allow_html=True)

col_edu1, col_edu2, col_edu3 = st.columns(3)

with col_edu1:
    st.markdown("### <span style='color:#3A86FF;'>Visão Educacional</span>", unsafe_allow_html=True)
    st.info("""
    O **EduFin AI Cloud** ajuda pessoas a entenderem seu **equilíbrio financeiro pessoal**,
    tornando o aprendizado de finanças mais simples, visual e prático.
    """)

with col_edu2:
    st.markdown("### <span style='color:#FFB703;'>Funcionamento</span>", unsafe_allow_html=True)
    st.warning("""
    1. O usuário insere dados financeiros.  
    2. O modelo calcula o **índice de saúde**.  
    3. O app apresenta **mensagens intuitivas e coloridas**.
    """)

with col_edu3:
    st.markdown("### <span style='color:#06D6A0;'>Design Educacional</span>", unsafe_allow_html=True)
    st.success("""
    O layout foi criado com base em **UX visual e cores** para facilitar o entendimento
    e estimular a interação de alunos e educadores.
    """)

# =====================================
# SEÇÃO DE PORTFÓLIO PROFISSIONAL + CONTATO
# =====================================
st.markdown("## <span style='color:#4B7BE5;'>Sobre o Desenvolvedor</span>", unsafe_allow_html=True)
st.markdown("""
**Autor:** *Claudio Hideki Yoshida*  
**Função:** *Desenvolvedor de Machine Learning e Criador de Soluções em IA Aplicada*  

**Contato:**  
📧 [claudio.y@hotmail.com](mailto:claudio.y@hotmail.com)  
📱 [WhatsApp: (11) 98636-4794](https://wa.me/5511986364794)

Atua como **AI Solutions Prototyper**, unindo dados, design e tecnologia para demonstrar
como a inteligência artificial pode resolver **problemas práticos e sociais**.
""")

st.caption("© 2025 EduFin AI Cloud — Aplicativo demonstrativo de IA e Educação Financeira | Desenvolvido por Claudio Hideki Yoshida 💡")
