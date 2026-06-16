import customtkinter as ctk

# Configurações de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppPDV(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Mini PDV - Escola da Nuvem")
        self.geometry("550x750")
        
        # Variáveis de controle de valores
        self.total_bruto = 0.0
        self.produtos_adicionados = []

        # Título Principal
        self.label_titulo = ctk.CTkLabel(self, text="🛒 CAIXA RÁPIDO - MINI PDV", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # Container de Entradas (Inputs)
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=30, fill="x")

        self.entry_produto = ctk.CTkEntry(self.frame, placeholder_text="Nome do Produto")
        self.entry_produto.pack(pady=10, padx=20, fill="x")

        self.entry_preco = ctk.CTkEntry(self.frame, placeholder_text="Preço Unitário (R$)")
        self.entry_preco.pack(pady=10, padx=20, fill="x")

        self.entry_qtd = ctk.CTkEntry(self.frame, placeholder_text="Quantidade")
        self.entry_qtd.pack(pady=10, padx=20, fill="x")

        # Container para os Botões Ficarem Lado a Lado
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(pady=15, padx=30, fill="x")

        # Botão 1: Adicionar Item
        self.btn_add = ctk.CTkButton(self.frame_botoes, text="Adicionar Item", command=self.adicionar_item, fg_color="#1f538d", hover_color="#14375e")
        self.btn_add.pack(side="left", padx=10, expand=True, fill="x")

        # Botão 2: Fechar Caixa / Emitir Nota
        self.btn_fechar = ctk.CTkButton(self.frame_botoes, text="Emitir Nota Fiscal", command=self.emitir_nota_fiscal, fg_color="#27ae60", hover_color="#1e8449")
        self.btn_fechar.pack(side="right", padx=10, expand=True, fill="x")

        # Campo de Exibição (Cupom / Nota Fiscal)
        self.lista_itens = ctk.CTkTextbox(self, font=("Courier New", 14), height=300)
        self.lista_itens.pack(pady=10, padx=30, fill="both", expand=True)
        self.limpar_tela_cupom()

    def limpar_tela_cupom(self):
        self.lista_itens.delete("0.0", "end")
        self.lista_itens.insert("0.0", "            CUPOM EMITIDO EM TELA            \n")
        self.lista_itens.insert("end", "=============================================\n")
        self.lista_itens.insert("end", " Adicione produtos acima para iniciar...\n")

    def adicionar_item(self):
        try:
            nome = self.entry_produto.get().strip()
            preco = float(self.entry_preco.get())
            qtd = int(self.entry_qtd.get())
            
            if not nome or preco <= 0 or qtd <= 0:
                raise ValueError

            subtotal = preco * qtd
            self.total_bruto += subtotal
            
            # Salva na lista interna do programa
            self.produtos_adicionados.append((nome, qtd, preco, subtotal))
            
            # CORREÇÃO DA QUEBRA: Se for o primeiro item, limpa e quebra a linha antes do texto
            if len(self.produtos_adicionados) == 1:
                self.lista_itens.delete("3.0", "end")
                self.lista_itens.insert("end", "\n") # Pula a linha logo após os sinais de igual ====

            # Formatação limpa: Nome e valores alinhados
            texto_item = f" -> {nome} ({qtd}x) - R$ {subtotal:.2f}\n"
            self.lista_itens.insert("end", texto_item)
            
            # Limpa os campos de texto para o próximo produto
            self.entry_produto.delete(0, 'end')
            self.entry_preco.delete(0, 'end')
            self.entry_qtd.delete(0, 'end')
            self.entry_produto.focus()
            
        except ValueError:
            self.lista_itens.insert("end", "\n [ERRO]: Dados inválidos! Tente novamente.\n")

    def emitir_nota_fiscal(self):
        if not self.produtos_adicionados:
            self.lista_itens.delete("0.0", "end")
            self.lista_itens.insert("0.0", " [AVISO]: O carrinho está vazio!\n Adicione itens antes de fechar a compra.")
            return

        # Regra de negócio: Cálculo do Desconto de 10% se passar de R$ 100
        desconto = 0.0
        if self.total_bruto > 100.00:
            desconto = self.total_bruto * 0.10
        
        total_liquido = self.total_bruto - desconto

        # Montagem Visual Estilizada da Nota Fiscal (Formato Cupom)
        self.lista_itens.delete("0.0", "end")
        nota =  "=============================================\n"
        nota += "           NOTA FISCAL DE VENDA              \n"
        nota += "=============================================\n"
        nota += f" {'ITEM':<18} {'QTD':<5} {'PRECO':>8} {'TOTAL':>9}\n"
        nota += "---------------------------------------------\n"
        
        for nome, qtd, preco, subtotal in self.produtos_adicionados:
            nome_cortado = nome if len(nome) <= 16 else nome[:13] + "..."
            nota += f" {nome_cortado:<18} {qtd:<5} {preco:>8.2f} {subtotal:>9.2f}\n"
            
        nota += "---------------------------------------------\n"
        nota += f" Subtotal Bruto:               R$ {self.total_bruto:>8.2f}\n"
        
        if desconto > 0:
            nota += f" Desconto Aplicado (10%):     -R$ {desconto:>8.2f}\n"
        else:
            nota += " Desconto Aplicado (10%):      R$     0.00\n"
            
        nota += "---------------------------------------------\n"
        nota += f" TOTAL A PAGAR:                R$ {total_liquido:>8.2f}\n"
        nota += "=============================================\n"
        nota += "        OBRIGADO PELA PREFERÊNCIA!           \n"
        nota += "=============================================\n"
        
        self.lista_itens.insert("0.0", nota)
        
        # Reseta os acumuladores para uma nova venda futura
        self.total_bruto = 0.0
        self.produtos_adicionados = []

if __name__ == "__main__":
    app = AppPDV()
    app.mainloop()
