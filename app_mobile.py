import streamlit as st
from gtts import gTTS
import base64

# Configuração da página para celular/tablet
st.set_page_config(page_title="Mini PDV Mobile", page_icon="🛒", layout="centered")

def falar_web(texto):
    """Gera um áudio que o navegador do celular ou tablet consegue reproduzir nativamente"""
    try:
        tts = gTTS(text=texto, lang='pt', slow=False)
        # Salva temporariamente o arquivo de áudio
        tts.save("audio_temp.mp3")
        
        # Converte o arquivo para um formato que o navegador lê direto em segundo plano
        with open("audio_temp.mp3", "rb") as f:
            audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()
        
        # Injeta um elemento de áudio invisível na página que toca automaticamente
        audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        """
        st.components.v1.html(audio_html, height=0)
    except Exception:
        pass

# Inicializa as variáveis de memória da página web se não existirem
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []
if "total_bruto" not in st.session_state:
    st.session_state.total_bruto = 0.0

st.title("🛒 Caixa Rápido - Mobile")
st.subheader("Uso Pessoal e Tablet")

# Formulário de entrada de dados (Compacto para telas de toque)
with st.form("formulario_produto", clear_on_submit=True):
    produto = st.text_input("Nome do Produto")
    preco = st.number_input("Preço Unitário (R$)", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    botao_add = st.form_submit_button("➕ Adicionar Item")

# Lógica de Adicionar Produto
if botao_add and produto:
    subtotal = preco * quantidade
    st.session_state.total_bruto += subtotal
    st.session_state.carrinho.append({
        "produto": produto,
        "qtd": quantidade,
        "preco": preco,
        "subtotal": subtotal
    })
    st.success(f"{produto} adicionado com sucesso!")
    # Dispara a voz na Web
    falar_web(f"{quantidade} unidades de {produto} adicionadas.")

# Exibição do Cupom Dinâmico na Tela
if st.session_state.carrinho:
    st.write("### 📄 Cupom Atual")
    for item in st.session_state.carrinho:
        st.text(f"-> {item['produto']} ({item['qtd']}x) - R$ {item['subtotal']:.2f}")
    
    st.write("---")
    st.write(f"**Subtotal Bruto:** R$ {st.session_state.total_bruto:.2f}")

    # Botões de Controle e Finalização
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔴 Limpar Caixa", use_container_width=True):
            st.session_state.carrinho = []
            st.session_state.total_bruto = 0.0
            falar_web("Caixa limpo.")
            st.rerun()

    with col2:
        if st.button("🟢 Emitir Nota", use_container_width=True):
            # Regra de negócio de 10% de desconto para compras acima de R$ 100
            desconto = 0.0
            if st.session_state.total_bruto > 100.00:
                desconto = st.session_state.total_bruto * 0.10
            
            total_liquido = st.session_state.total_bruto - desconto
            
            st.balloons() # Efeito visual de balões subindo na tela do celular
            st.info(f"**Resumo da Venda:**\n\n"
                    f"Desconto aplicado: R$ {desconto:.2f}\n\n"
                    f"**Total Líquido a Pagar: R$ {total_liquido:.2f}**")
            
            # Formata o número trocando ponto por vírgula para a voz web ler por extenso certinho
            v_liquido_falar = f"{total_liquido:.2f}".replace('.', ',')
            if desconto > 0:
                falar_web(f"Venda finalizada com desconto. Total a pagar: {v_liquido_falar} reais.")
            else:
                falar_web(f"Venda finalizada. Total a pagar: {v_liquido_falar} reais.")
