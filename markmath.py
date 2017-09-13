# Python 3
# dependencies (python modules):
#		asciimathml
#		markdown
#		pypandoc


import sys
import markdown
import pypandoc

## open file and read contents
mdfile = open(sys.argv[1], 'r')
mdfilecontent = mdfile.read()
mdfile.close()

# convert file content to html
htmlout = markdown.markdown(mdfilecontent, ['asciimathml'])

# not working atm:
#pdfout = pypandoc.convert_text(htmlout, 'pdf', outputfile="outputtestfile.pdf")

print(htmlout)
