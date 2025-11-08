import streamlit as st
from PIL import Image, ImageChops

# =====================================
# ⚙️ CONFIGURAÇÃO GERAL
# =====================================
st.set_page_config(
    page_title="EduFin AI Cloud — Educação Financeira com IA",
    layout="wide",
    page_icon="💡" 
)

# =====================================
# 🧩 FUNÇÃO AUXILIAR — CORTAR BORDAS BRANCAS
# =====================================
def crop_white_borders(img_path):
    """Remove automaticamente bordas brancas ou vazias."""
    try:
        # Nota: As imagens 'loguinnova.png' e 'calculo.png' devem estar disponíveis no mesmo diretório
        img = Image.open(img_path)
        # Tenta pegar a cor do pixel (0, 0) para usar como fundo
        bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        if bbox:
            img = img.crop(bbox)
        return img
    except FileNotFoundError:
        # Adiciona uma mensagem de erro no Streamlit se a imagem não for encontrada
        st.error(f"Erro: Imagem não encontrada em {img_path}. Certifique-se de que o arquivo existe.")
        return None

# =====================================
# CABEÇALHO PRINCIPAL E INTRODUÇÃO
# =====================================
with st.container():
    # Cores alegres no título
    st.title(":blue[EduFin AI Cloud] — Inteligência Financeira com IA")

    st.markdown("""
    O **EduFin AI Cloud** é um aplicativo educativo que une **educação financeira** e **inteligência artificial (IA)**.  
    Ele foi criado para ajudar pessoas a **entenderem sua situação financeira** e **aprenderem a tomar melhores decisões com base em dados**.
    """)
    
    with st.expander("Habilidades de Machine Learning (ML) e Aplicações"):
        st.write("""
        As habilidades de **Machine Learning (ML)** utilizadas aqui podem ser aplicadas hoje em diversas áreas:
        - **Finanças pessoais e bancárias**, para prever gastos, detectar padrões de consumo e identificar riscos.  
        - **Educação**, em sistemas que personalizam o aprendizado e sugerem trilhas de conhecimento.  
        - **Empresas e startups**, na tomada de decisões, análise de dados e automação inteligente de processos.  

        Com o EduFin, o objetivo é trazer esses conceitos para o **cotidiano de forma simples, visual e interativa**.
        """)


# =====================================
# IMAGEM DE LOGIN — Layout Centralizado
# =====================================
login_img = crop_white_borders("loguinnova.png")

if login_img is not None:
    # Redimensiona proporcionalmente
    base_width = 600
    w_percent = base_width / float(login_img.size[0])
    h_size = int(float(login_img.size[1]) * w_percent)
    login_img = login_img.resize((base_width, h_size), Image.Resampling.LANCZOS)

    # Uso de st.columns para centralizar a imagem no layout wide (colunas [1, 2, 1])
    col1_login, col2_login, col3_login = st.columns([1, 2, 1])

    st.write("") # Espaçamento
    with col2_login:
        st.subheader(":green[Login] — Interface Aprimorada")
        st.image(login_img, use_column_width='always')
        st.caption("Interface de autenticação aprimorada — simples, acessível e moderna.")


# =====================================
# DEMONSTRAÇÃO DO ÍNDICE DE SAÚDE FINANCEIRA (CORES E PORCENTAGENS ORIGINAIS)
# =====================================
st.write("")
st.header(":red[Demonstração do Índice de Saúde Financeira]")
st.write("O sistema fornece um feedback imediato com base na sua situação, usando cores para indicar o nível de saúde financeira.")

col_baixa, col_media, col_alta = st.columns(3)

with col_baixa:
    # Título em vermelho para Baixa Saúde Financeira
    st.markdown("#### :red[Baixa Saúde Financeira]")
    # Porcentagem e Delta ORIGINAIS
    st.metric(label="Risco Alto", value="35%", delta="-15% (Ruim)", delta_color="inverse")
    st.write("Alerta: Seus gastos e/ou dívidas estão muito acima da sua renda. Ação imediata é necessária.")

with col_media:
    # Título em laranja/amarelo para Média Saúde Financeira
    st.markdown("#### :orange[Média Saúde Financeira]")  
    # Porcentagem e Delta ORIGINAIS
    st.metric(label="Risco Moderado", value="65%", delta="+5% (Regular)", delta_color="off")
    st.write("Atenção: Você está no caminho certo, mas ainda pode otimizar seus gastos e aumentar a poupança.")

with col_alta:
    # Título em verde para Alta Saúde Financeira
    st.markdown("#### :green[Alta Saúde Financeira]")
    # Porcentagem e Delta ORIGINAIS
    st.metric(label="Risco Baixo", value="95%", delta="+10% (Excelente)", delta_color="normal")
    st.write("Parabéns: Seu equilíbrio financeiro é excelente! Foque em estratégias de investimento de longo prazo.")
    
st.write("") # Espaçamento


# =====================================
# SEÇÕES 1, 2 E 3 — Layout de "Cartões" em 3 Colunas
# =====================================
st.header(":orange[Visão Geral, Funcionamento e Design]")
st.write("Conheça os pilares do **EduFin AI Cloud** e como ele transforma a educação financeira.")

# Organiza os 3 tópicos iniciais em 3 colunas para um layout dinâmico horizontal
col_visao, col_funciona, col_design = st.columns(3)

with col_visao:
    st.markdown("#### :blue[1. Visão Geral]")
    st.info("""
    O **EduFin AI Cloud** foi desenvolvido para **ensinar conceitos de educação financeira** de forma prática e intuitiva.
    Com ele, qualquer pessoa pode compreender rapidamente **como está sua saúde financeira** e **como melhorar suas finanças pessoais**.
    """)

with col_funciona:
    st.markdown("#### :blue[2. Como Funciona]")
    st.warning("""
    1. O usuário informa dados simples: **renda, gastos, dívidas, poupança e investimentos**.
    2. O sistema calcula um **índice de saúde financeira** com base nesses valores.
    3. O resultado aparece em **cores e mensagens fáceis de entender**.
    """)

with col_design:
    st.markdown("#### :blue[3. Design Educacional]")
    st.success("""
    O layout foi projetado para **facilitar o aprendizado visual**.
    Cores, ícones e controles deslizantes tornam o uso **leve e intuitivo**, incentivando o usuário a testar diferentes cenários.
    """)

st.write("")

# =====================================
# SEÇÃO 4 — SIMULAÇÃO INTERATIVA (Texto e Imagem Lado a Lado)
# =====================================
st.header(":violet[Simulação Interativa e Impacto de Decisão]")

# Uso de colunas para apresentar texto e imagem lado a lado (ajuste a proporção [2, 3])
col_texto_calc, col_img_calc = st.columns([2, 3])

with col_texto_calc:
    st.markdown("""
    A principal tela do EduFin permite **simular situações reais** com base em Machine Learning e finanças:
    - E se eu gastar menos?
    - E se eu guardar mais por mês?
    - Como minhas dívidas impactam meu equilíbrio financeiro?

    Essas simulações ajudam o usuário a entender de forma prática o **impacto de suas decisões no futuro financeiro**, reforçando o **aprendizado visual e participativo**.
    """)

calc_img = crop_white_borders("calculo.png")

with col_img_calc:
    if calc_img is not None:
        # Largura ajustada para 450px
        base_width = 450 
        w_percent = base_width / float(calc_img.size[0])
        h_size = int(float(calc_img.size[1]) * w_percent)
        calc_img = calc_img.resize((base_width, h_size), Image.Resampling.LANCZOS)
        
        # Uso de colunas internas para centralizar a imagem menor na coluna
        _, col_center, _ = st.columns([1, 4, 1]) 
        with col_center:
            st.image(calc_img, caption="Tela de Simulação — EduFin AI Cloud", use_column_width='always')

st.write("")

# =====================================
# SEÇÃO 5 E 6 — OBJETIVO E CONCLUSÕES (Lado a Lado)
# =====================================
col_objetivo, col_conclusoes = st.columns(2)

with col_objetivo:
    st.header(":red[Objetivo Educacional]")
    st.markdown("""
    O EduFin AI Cloud busca **democratizar o acesso à educação financeira**.  
    Ele ajuda o usuário a entender conceitos como:
    - **Equilíbrio entre ganhos e gastos** - **Importância de poupar e investir** - **Efeitos das dívidas** - **Planejamento financeiro pessoal** É ideal para **escolas, universidades e projetos sociais**, onde o aprendizado acontece de forma **visual e participativa**.
    """)

with col_conclusoes:
    st.header(":green[Conclusões e Próximos Passos]")
    st.markdown("""
    O **EduFin AI Cloud** mostra como a tecnologia pode **tornar a educação financeira acessível e prática**.  
    Próximos passos incluem:
    - Expansão do modelo de IA com mais variáveis financeiras;  
    - Geração de **recomendações personalizadas** para o usuário;  
    - Integração com **painéis para educadores e mentores**.  
    """)

