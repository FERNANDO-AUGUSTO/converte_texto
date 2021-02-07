import streamlit as st


def main():
    # função q converte o texto
    def converte_texto(texto):
        texto_1 = texto.replace('\n', ' / ')
        texto_1 = texto_1.replace('R$ ', ' R$ ')
        return texto_1



    # parte grafica da aplicação
    st.header('CONVERSOR DE TEXTO')


    texto = st.text_area('Cole o texto aqui',height= 200)

    btn = st.button('Converter')

    # Ação do botão
    if btn:
        resultado = st.write(converte_texto(texto))



if __name__ =='__main__':
    main()