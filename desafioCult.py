import streamlit as st
import pandas as pd

# favicon do site
st.set_page_config(page_title="Desafio Cultural", page_icon="images.ico")

# criando as paginas
tab1, tab2 = st.tabs(["Geral", "Conteúdo"])
# pagina 1
with tab1:
    
    # titulo
    st.header("""
    Acessibilidade para as pessoas com deficiência fisica 
    """)

    # coluna de imagem
    col1, col2 = st.columns(2)
    with col1:
        st.image("criança_triste(1).jpg", caption="Imagem representativa")
    with col2:
        st.image("criança_triste(2).jpg", caption="Imagem representativa")

    # texto
    st.write("""
    Das 1.771.430 matrículas na educação especial computadas no Censo Escolar 2023,
    a maior concentração está no ensino fundamental, com 62,90% (1.114.230) das matrículas.
    Em seguida está a educação infantil, com 16% (284.847), e o ensino médio, que contabilizou
    12,6% (223.258) dos estudantes.

    ㅤ
    
    Pessoas com deficiência física acabam sendo excluídas na sociedade
    e apenas 15% de todos os colégios (públicos e privados) possuem 
    100% das salas acessíveis e banheiros adaptados para pessoas com 
    dificuldade de locomoção.
    # 
    """)

    # ################################
    # SideBar
    st.sidebar.write("""
    # Desafio Cultural
    Tema: Inovação
    """)
    st.sidebar.image("youxx.png")
    st.write("""
    ##### Fonte: INEP
    """)

# pagina 2
with tab2:
    
    # titulo
    st.write("""
    ## Lixeira Eletrônica para as pessoas cadeirantes
    """)
    
    # coluna de imagem
    brr1, brr2, brr3 = st.columns(3)
    with brr1:
        st.image("desafio_cultural(1).jpg", caption="Materiais necessários")
    with brr2:
        st.image("desafio_2.jpg", caption="Construindo")
    with brr3:
        st.image("desafio_1.jpg", caption="Pintando")
    
    
    # texto
    st.write("""
    A lixeira tem como intuito facilitar o uso por cadeirantes na escola, utilizando
    um Arduino e um sensor ultrassônico. O sistema funciona de forma automatizada: o sensor detecta a aproximação
    do usuário e aciona o Arduino, que controla a abertura da tampa da lixeira. Essa solução foi pensada para
    tornar o ambiente escolar mais acessível, permitindo que os cadeirantes utilizem a lixeira de forma prática
    e independente."
    """)