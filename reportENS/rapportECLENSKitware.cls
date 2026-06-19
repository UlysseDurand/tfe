\LoadClass[a4paper,12pt]{article}

\RequirePackage[english]{babel}
\RequirePackage[utf8]{inputenc}
\RequirePackage[section]{placeins}
\RequirePackage[T1]{fontenc}
\RequirePackage{fontspec}
\RequirePackage{biblatex}
\RequirePackage{mathtools}
\RequirePackage{siunitx}
\RequirePackage{float}
\RequirePackage{graphicx}
\RequirePackage[justification=centering]{caption}
\RequirePackage{subcaption}
\RequirePackage{wallpaper}
\RequirePackage{nomencl}
\RequirePackage{fancyhdr}
\RequirePackage{url}
\RequirePackage[hidelinks]{hyperref}
\RequirePackage[includehead, left=3.5cm,right=3.5cm,top=2cm,bottom=3.5cm]{geometry}
\RequirePackage{cleveref}
\RequirePackage{tikz}
\RequirePackage{listings}
\RequirePackage{xcolor}
\RequirePackage{pdfpages}
\RequirePackage{enumitem}

\lstset{
  basicstyle=\ttfamily\footnotesize,
  backgroundcolor=\color{gray!10},
  frame=single,
  breaklines=true,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{teal},
  showstringspaces=false
}
% --- Color definitions (One Dark palette) ---
\definecolor{vue-bg}{HTML}{282C34}
\definecolor{vue-gutter}{HTML}{3B4048}
\definecolor{vue-gutterfg}{HTML}{636D83}
\definecolor{vue-htmltag}{HTML}{E06C75}
\definecolor{vue-component}{HTML}{61AFEF}
\definecolor{vue-attr}{HTML}{D19A66}
\definecolor{vue-string}{HTML}{98C379}
\definecolor{vue-directive}{HTML}{C678DD}
\definecolor{vue-number}{HTML}{D19A66}
\definecolor{vue-comment}{HTML}{5C6370}
\definecolor{vue-fg}{HTML}{ABB2BF}

% --- Vue language definition ---
\lstdefinelanguage{Vue}{
  sensitive=true,
  morecomment=[s]{<!--}{-->},
  morestring=[b]",
  morestring=[b]',
  % HTML structural tags
  morekeywords=[1]{template, script, style, setup},
  % Vue built-in directives
  morekeywords=[2]{v-for, v-if, v-else, v-show, v-model, v-bind, v-on,
                   v-slot, v-pre, v-once, v-cloak},
  % JS keywords
  morekeywords=[3]{import, from, export, default, const, let, var,
                   defineProps, defineEmits, defineExpose, ref, reactive,
                   computed, watch, onMounted},
}

\usetikzlibrary{graphs, graphdrawing, positioning, arrows.meta, shapes.geometric, fit, calc}
\usegdlibrary{force}

\newcommand{\ttitle}[1]{\renewcommand{\ttitle}{#1}}
\newcommand{\UE}[1]{\renewcommand{\UE}{#1}}
\newcommand{\subject}[1]{\renewcommand{\subject}{#1}}
\newcommand{\tutor}[1]{\renewcommand{\tutor}{#1}}
\newcommand{\student}[1]{\renewcommand{\student}{#1}}

\renewcommand{\sectionmark}[1]{\markboth{#1}{}}
\newcommand{\makemargins}{
  \makenomenclature
  \pagestyle{fancy}
  % \fancyheadoffset{1cm}
  \setlength{\headheight}{1.5cm}
  % \setlength{\headsep}{1.5cm}       % space between header and text
  % \setlength{\footskip}{1.5cm}      % space between text and footer

  \lhead{
    \raisebox{-0.5\height}{\includegraphics[height=0.05\textheight]{assets/logos/logoENS.png}}
    \hspace{1cm}
    \raisebox{-0.5\height}{\includegraphics[height=0.05\textheight]{assets/logos/logoECL.png}}
    \hspace{0.5cm}
    \raisebox{-0.4\height}{\includegraphics[height=0.06\textheight]{assets/logos/logoKitware.png}}
    \vspace{0.5cm}
  }
  \rhead{ \nouppercase{\leftmark} }
  \fancyfoot[L]{\ttitle \hfill \thepage}
  \fancyfoot[C]{}
  \fancyfoot[R]{}
}
\renewcommand{\footrulewidth}{0.4pt}

\newcommand{\makefirstpage}{
  \begin{titlepage}

    \centering
    \includegraphics[height=0.07\textheight]{assets/logos/logoENS.png}\par\vspace{1cm}
    \includegraphics[height=0.07\textheight]{assets/logos/logoECL.png}\par\vspace{1cm}
    \includegraphics[height=0.12\textheight]{assets/logos/logoKitware.png}\par

    \vspace{1.5cm}
    {\scshape\Large \UE \\ \subject \par}
    \vspace{1cm}
    \rule{\linewidth}{0.2 mm} \\[0.4 cm]
    {\huge\bfseries \ttitle \par} \
    \rule{\linewidth}{0.2 mm} \\[1.5 cm]
    \vspace{1cm}

    \begin{minipage}{0.5\textwidth}
      \begin{flushleft} \large
        \emph{\textbf{\student}}\\
      \end{flushleft}
    \end{minipage}
    ~
    \begin{minipage}{0.4\textwidth}
      \begin{flushright} \large
        \emph{\textbf{\tutor}} \\
      \end{flushright}
    \end{minipage}\\[4cm]

    \vfill

  \end{titlepage}
  \clearpage

  \tableofcontents
  \clearpage
}

\newcommand{\insertfigure}[4]{
  \begin{figure}[H]
    \centering
    \includegraphics[keepaspectratio,#2]{#1}
    \caption{#3}
    \label{#4}
  \end{figure}
}

\newcounter{pr}
\crefformat{pr}{(#2PR~#1#3)}
\crefmultiformat{pr}{(#2PRS~#1#3)}{ and~(#2#1#3)}{, (#2#1#3)}{ and~(#2#1#3)}
\Crefformat{pr}{(#2PR~#1#3)}
\newcommand{\definepr}[2]{
  \refstepcounter{pr}
  \hypertarget{#2}{}
  \label{pr:#2}
  PR.\thepr\ \href{#1}{#2}
}

\newcounter{repo}
\crefformat{repo}{(#2repo~#1#3)}
\crefmultiformat{repo}{(#2repos~#1#3)}{ and~(#2#1#3)}{, (#2#1#3)}{ and~(#2#1#3)}
\Crefformat{repo}{(#2Repo~#1#3)}
\newcommand{\definerepo}[2]{
  \refstepcounter{repo}
  \hypertarget{#2}{}
  \label{repo:#2}
  repo.\therepo\ \href{#1}{#2}
}
\newcommand{\Definerepo}[2]{
  \refstepcounter{repo}
  \hypertarget{#2}{}
  \label{repo:#2}
  Repo.\therepo\ \href{#1}{#2}
}

\crefname{lstlisting}{Listing}{Listings}
\Crefname{lstlisting}{Listing}{Listings}

\newcommand{\refrepo}[1]{
  #1\ \cref{repo:#1}
}

\newcommand{\citev}[1]{
  #1\ \cite{#1}
}