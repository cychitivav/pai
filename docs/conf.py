# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Vehículo de muestro'
copyright = '2023, Grupo 3B Proyecto Aplicado de Ingeniería'
author = 'Camilo Andrés Barrera Castellanos, Camilo Andrés Borda Gil, Cristian Yesid Chitiva Vela, Johan Andrés Díaz Roa, Juan Sebastian Dueñas Salamanca, Juan Fernando Mendieta Hernández, Juan Pablo Vallejo Montañez'
version = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ['myst_nb', 'sphinx_favicon']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
}

numfig = True

# -- Options for internationalization -----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization
language = 'es'

# -- Options for Math --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-math
math_number_all = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_book_theme'

html_search_language = 'es'

html_theme_options = {
    'repository_url': 'https://github.com/cychitivav/pai',
    'repository_branch': 'main',
    'path_to_docs': 'docs/source',
    'use_repository_button': True,
    "logo": {
        "text": "Documentación vehículo de muestreo",
    }
}

html_logo = 'https://user-images.githubusercontent.com/30636259/235979806-03ed419c-5748-45eb-b5bb-1ab401ddd267.png'

favicons = [
    {"href": 'https://user-images.githubusercontent.com/30636259/235979806-03ed419c-5748-45eb-b5bb-1ab401ddd267.png'}
]

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
latex_engine = 'xelatex'

latex_logo = 'images/logounal.png'
latex_toplevel_sectioning = 'section'
# latex_appendices = ['source/appendices/appendix-a']
latex_show_urls = 'footnote'
lates_show_pagerefs = True 

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt',
    'babel': '\\usepackage[spanish,mexico]{babel}',
    'fontpkg': '''
        \\usepackage{fontspec}
        \\setmainfont{Ancizar Sans}[
            ItalicFont = * Italic, 
            BoldFont = * Bold, 
            BoldItalicFont = * Bold Italic
        ]
    ''',
    'preamble': '''
        \\usepackage{mathtools}
        \\usepackage{pdfpages}
        \\usepackage{amsmath}
        \\usepackage{amsfonts}
        \\usepackage{amssymb}
        \\usepackage{graphicx}
        \\usepackage{float}
        \\usepackage{pdfpages}
        \\usepackage[titles]{tocloft}
    ''',
    'maketitle': '''
        \\begin{titlepage}
            \\centering 
            \\includegraphics[width=0.4\\textwidth]{logounal.png}   \\\\    \\vspace{\\fill}
            \\LARGE \\textbf{%s}                                    \\\\    \\vspace{\\fill}
            \\normalsize \\textsl{%s}                               \\\\    \\vspace{\\fill}
            \\textbf{Profesor:}                                     \\\\
            \\textsl{Ing. Carlos Alberto Narváez Tovar}             \\\\    \\vspace{\\fill}
            Universidad Nacional de Colombia                        \\\\
            Facultad de Ingeniería                                  \\\\
            Departamento de Ingeniería Mecánica y Mecatrónica       \\\\
            Proyecto Aplicado de Ingeniería                         \\\\
            Bogotá, Colombia                                        \\\\
            \\the\\year
        \end{titlepage}
    ''' % (project, author.replace(', ', '\\\\')),
    'figure_align': 'H',
    'hyperref': '\\usepackage{hyperref}',
    'tableofcontents': '''
        \\listoffigures
        \\listoftables
        \\tableofcontents\\newpage
    '''
}

latex_docclass = {'howto': 'article'}
latex_theme = 'howto'
