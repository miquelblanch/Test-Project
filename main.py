import streamlit as st 

## para arrancar, escribir por terminal "streamlit run main.py"
## Local URL: http://localhost:8501
##  Network URL: http://192.168.4.36:8501

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

def main():
    st.title("Formulario de Registro")

    # Pregunta el nombre
    nombre = st.text_input("Ingrese su nombre")

    # Muestra el nombre ingresado
    if nombre:
        st.write(f"Hola, {nombre}!")

if __name__ == "__main__":
    main()
