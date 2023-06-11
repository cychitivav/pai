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
extensions = ['myst_nb']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    'ipynb': 'myst-nb'
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
# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
latex_engine = 'xelatex'

# latex_documents = ['main', 'informe', 'Vehículo de muestreo', 'Camilo Andrés Barrera Castellanos\\Camilo Andrés Borda Gil\\Cristian Yesid Chitiva Vela\\Johan Andrés Díaz Roa\\Juan Sebastian Dueñas Salamanca\\Juan Fernando Mendieta Hernández\\Juan Pablo Vallejo Montañez', 'howto', 'true']

# latex_logo = 'images/logounal.png'
latex_toplevel_sectioning = 'section'
latex_show_urls = 'footnote'

latex_elements = {
    'papersize': r'letterpaper',
    'pointsize': r'12pt',
    'babel': r'\usepackage[spanish,mexico]{babel}',
    'fontpkg': r'''
        \usepackage{fontspec}
        \setmainfont{Ancizar Sans}[
            ItalicFont = * Italic, 
            BoldFont = * Bold, 
            BoldItalicFont = * Bold Italic
        ]
    ''',
    'preamble': r'''
        \usepackage{mathtools}
        \usepackage{pdfpages}
        \usepackage{amsmath}
        \usepackage{amsfonts}
        \usepackage{amssymb}
        \usepackage{graphicx}
        \usepackage{float}
        \usepackage{pdfpages}
        \usepackage[titles]{tocloft}
    ''',
    'maketitle': r'''
        \begin{titlepage}
            \centering
            \includegraphics[width=0.7\textwidth]{logounal.png}     \\  \vspace{\fill}
            \LARGE \textbf{Vehículo de muestreo}                     \\  \vspace{\fill}
            \normalsize \textsl{Camilo Andrés Barrera Castellanos\\
                                Camilo Andrés Borda Gil\\
                                Cristian Yesid Chitiva Vela\\
                                Johan Andrés Díaz Roa\\
                                Juan Sebastian Dueñas Salamanca\\
                                Juan Fernando Mendieta Hernández\\
                                Juan Pablo Vallejo Montañez}        \\  \vspace{\fill}
            \textbf{Profesor:}                                      \\
            \textsl{Ing. Carlos Alberto Narváez Tovar}              \\   \vspace{\fill}
            Universidad Nacional de Colombia                        \\
            Facultad de Ingeniería                                  \\
            Departamento de Ingeniería Mecánica y Mecatrónica       \\
            Proyecto Aplicado de Ingeniería                         \\
            Bogotá, Colombia                                        
            \the\year
        \end{titlepage}
    ''',
    'figure_align': 'H',
    'geometry': '\\usepackage[letterpaper,margin=3cm]{geometry}',
    'hyperref': '\\usepackage{hyperref}'
}