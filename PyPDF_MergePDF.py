#PDF MERGER - yeh 2-3 pdfs ko ek sath merge karega
import  PyPDF2
PDFFiles = ["1.pdf","2.pdf","sample.pdf"]
Merger =  PyPDF2.PdfMerger()
for filename in PDFFiles:
    Files = open(filename,'rb')
    Reader =  PyPDF2.PdfReader(PDFFiles)
    Merger.append(Reader)
PDFFiles.close()
Merger.write('All_IN_ONE.pdf')
