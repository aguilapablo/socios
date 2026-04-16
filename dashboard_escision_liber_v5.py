```latex
\documentclass[11pt, a4paper]{article}

% --- UNIVERSAL PREAMBLE BLOCK ---
\usepackage[a4paper, top=2cm, bottom=2cm, left=1.5cm, right=1.5cm]{geometry}
\usepackage{fontspec}
\usepackage[spanish, bidi=basic, provide=*]{babel}

\babelprovide[import, onchar=ids fonts]{spanish}
\babelprovide[import, onchar=ids fonts]{english}

% Set default font to Noto Sans (Clean and modern for mobile)
\babelfont{rm}{Noto Sans}

% Minimalist packages
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{titlesec}

% Professional styling
\definecolor{libernavy}{HTML}{0F172A}
\definecolor{liberblue}{HTML}{2563EB}
\definecolor{liberemerald}{HTML}{10B981}

\titleformat{\section}{\color{libernavy}\normalfont\Large\bfseries}{\thesection}{1em}{}[{\titlerule[0.8pt]}]
\titleformat{\subsection}{\color{liberblue}\normalfont\large\bfseries}{\thesubsection}{1em}{}

\setlist[itemize]{label=\textbullet, leftmargin=1.5em}

\begin{document}

% --- PORTADA ---
\begin{center}
    \vspace*{1cm}
    {\color{libernavy}\small\textbf{DOCUMENTO CONFIDENCIAL --- RESERVADO DIRECTORIO}}\\[0.5cm]
    {\color{libernavy}\Huge\textbf{Dictamen Estratégico de Escisión 2026}}\\[0.8cm]
    {\large Liber S.A.I.C.I.}\\[0.3cm]
    \textit{Reorganización Societaria Libre de Impuestos (Art. 82 LIG)}\\[1cm]
    
    \framebox{\parbox{0.9\textwidth}{\centering
        \vspace{0.5cm}
        \textbf{Objetivo Final: Patrimonio Neto \$0.00}\\
        Proporcionalidad Garantizada: 30\% PAMA | 40\% VIFRAN | 30\% NBR\\
        \vspace{0.5cm}
    }}
\end{center}

\vspace{1cm}

\section{Resumen Ejecutivo}
El presente dictamen establece la hoja de ruta contable para disolver Liber S.A. al \textbf{31 de julio de 2026}. El éxito de la operación radica en la neutralidad fiscal y la equivalencia matemática entre el paquete accionario y el activo adjudicado.

\section{Ingeniería del Crédito Malabia}
El saneamiento del rubro ``Inversiones'' es el primer paso crítico para evitar distorsiones impositivas.

\subsection{Ajuste por Realidad Económica (Impairment)}
Se propone el reconocimiento de la brecha entre el valor de libros y mercado:
\begin{itemize}
    \item \textbf{Valor Contable:} \$452,044,937
    \item \textbf{Valor Real Mercado:} \$300,000,000
    \item \textbf{Pérdida Deducible (Escudo Fiscal):} \$152,044,937
\end{itemize}

\subsection{Dación en Pago (Extinción de Pasivos)}
Para evitar el gravamen del 7\% sobre dividendos cedulares, el crédito remanente se aplicará a:
\begin{enumerate}
    \item \textbf{Cancelación Crédito Pablo Aguila:} (\$100M) Compensación por expensas y gastos operativos financiados por el accionista.
    \item \textbf{Cancelación Deuda José/Luis:} Deuda actualizada por \textbf{Tasa Pasiva BNA} (8 meses proyectados).
\end{enumerate}

\section{Pivotes de Nivelación Patrimonial}
Dado que los activos físicos (Inmuebles) son inamovibles, la nivelación del 30/40/30 se ejecutará mediante variables de ajuste técnico.

\begin{table}[htbp]
    \centering
    \caption{Cuentas de Ajuste por Sociedad}
    \begin{tabular}{llp{5cm}}
        \toprule
        \textbf{Sociedad} & \textbf{Ratio} & \textbf{Mecanismo de Ajuste} \\
        \midrule
        \textbf{PAMA} & 30\% & Activación de Mejoras s/ Sarmiento (RT 17). \\
        \textbf{VIFRAN} & 40\% & Amortización Técnica s/ Campos y Libertador. \\
        \textbf{NBR} & 30\% & Asignación de Efectivo y Bienes de Uso. \\
        \bottomrule
    \end{tabular}
\end{table}

\section{Matriz de Proporcionalidad Final}
\begin{figure}[htbp]
  \centering
  \framebox{\parbox{0.8\textwidth}{\centering
    \vspace{2cm}
    \textbf{Esquema de Distribución Jul-2026} \\
    \small\textit{PN PAMA (30\%) | PN VIFRAN (40\%) | PN NBR (30\%)} \\
    \textbf{Delta Residual = 0.00\%}
    \vspace{2cm}
  }}
  \caption{Verificación técnica de adjudicación de capital.}
\end{figure}

\section{Conclusión para el Directorio}
La implementación de este plan garantiza:
\begin{itemize}
    \item \textbf{Costo Fiscal Cero:} Bajo el marco de la reorganización por escisión.
    \item \textbf{Paz Societaria:} Distribución proporcional inatacable ante IGJ.
    \item \textbf{Liquidez:} Optimización del flujo de caja post-malabia.
\end{itemize}

\vspace{1cm}
\begin{flushright}
    \textbf{Lic. Pablo Aguila}\\
    \textit{Dirección Estratégica}\\
    \small Abril de 2026
\end{flushright}

\end{document}

```
