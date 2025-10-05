from fpdf import FPDF
import analyze 

results = analyze.run_analysis(make_plot=True)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Capa simples
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Relatório - Efeito Fotoelétrico', ln=True, align='C')
pdf.ln(10)

# Resultados principais
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, "Constantes obtidas:", ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 8,
    f"h experimental = {results['h_exp']:.3e} J·s\n"
    f"h esperado     = {results['h_ref']:.3e} J·s\n"
    f"Função trabalho = {results['w0_eV']:.3f} eV\n"
    f"Frequência de corte = {results['f_cut_Hz']:.3e} Hz"
)
pdf.ln(6)

# Inserir figura gerada automaticamente
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 8, "Figura:", ln=True)
pdf.image("V0_vs_f_regressao.png", w=170)
pdf.ln(8)

pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, "Observações: relatório gerado automaticamente a partir dos dados de analyze.py.")

pdf.output("Relatorio_Efeito_Fotoeletrico.pdf")
print("PDF gerado: Relatorio_Efeito_Fotoeletrico.pdf")
