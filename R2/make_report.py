# make_report.py
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Relatorio - Efeito Fotoeletrico', ln=True)
pdf.ln(4)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 6, 'Resultados experimentais e figuras geradas pelo script analyze.py')
pdf.ln(6)
# insere figura gerada previamente
pdf.image('V0_vs_f_regressao.png', w=170)
pdf.ln(6)
pdf.multi_cell(0, 6, 'Observacoes: use os arquivos resultados_medios.csv e as figuras geradas para compor o relatorio final.')
pdf.output('Relatorio_Efeito_Fotoeletrico.pdf')
print('PDF gerado: Relatorio_Efeito_Fotoeletrico.pdf')
