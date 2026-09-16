\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{slidesECLENSKitware}[2026/07/06 Beamer slides class matching report style]

% Pass options through to beamer (e.g. \documentclass[aspectratio=169]{beamerslides})
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{beamer}}
\ProcessOptions\relax
\LoadClass{beamer}

\usetheme{CambridgeUS}
\usecolortheme{seahorse}

\RequirePackage[english]{babel}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{fontspec}
\RequirePackage{mathtools}
\RequirePackage{siunitx}
\RequirePackage{graphicx}
\RequirePackage[justification=centering]{caption}
\RequirePackage{subcaption}
\RequirePackage{tikz}
\RequirePackage{listings}
\RequirePackage{xcolor}
\RequirePackage{cleveref}
\RequirePackage{url}

\usetikzlibrary{graphs, graphdrawing, positioning, arrows.meta, shapes.geometric, fit, calc}
\usegdlibrary{force}

% ------------------------------------------------------------------
% Listings style + Vue language definition (same as report)
% ------------------------------------------------------------------
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

\lstdefinelanguage{Vue}{
  sensitive=true,
  morecomment=[s]{<!--}{-->},
  morestring=[b]",
  morestring=[b]',
  morekeywords=[1]{template, script, style, setup},
  morekeywords=[2]{v-for, v-if, v-else, v-show, v-model, v-bind, v-on,
                   v-slot, v-pre, v-once, v-cloak},
  morekeywords=[3]{import, from, export, default, const, let, var,
                   defineProps, defineEmits, defineExpose, ref, reactive,
                   computed, watch, onMounted},
}

% ------------------------------------------------------------------
% Metadata commands (same names/semantics as the report class)
% ------------------------------------------------------------------
\newcommand{\ttitle}[1]{\renewcommand{\ttitle}{#1}}
\newcommand{\UE}[1]{\renewcommand{\UE}{#1}}
\newcommand{\ssubject}[1]{\renewcommand{\ssubject}{#1}}
\newcommand{\tutor}[1]{\renewcommand{\tutor}{#1}}
\newcommand{\student}[1]{\renewcommand{\student}{#1}}

\newcommand{\logopath}{assets/logos}


% ------------------------------------------------------------------
% Frame title template: puts the three logos in the top corner of
% every content frame, mirroring the \lhead of the report.
% ------------------------------------------------------------------
% \setbeamertemplate{frametitle}{
%   \nointerlineskip
%   \begin{beamercolorbox}[wd=\dimexpr\paperwidth-0.6cm\relax,ht=1.5cm,dp=0.3cm,leftskip=0.3cm,rightskip=0.3cm]{frametitle}
%     \begin{minipage}[c]{0.65\textwidth}
%       \raggedright\insertframetitle\par
%       {\normalfont\small\insertframesubtitle}
%     \end{minipage}%
%     \hfill
%     \begin{minipage}[c]{0.3\textwidth}
%       \raggedleft
%       \includegraphics[height=0.35cm]{\logopath/logoENS.png}\hspace{2mm}%
%       \includegraphics[height=0.35cm]{\logopath/logoECL.png}\hspace{2mm}%
%       \includegraphics[height=0.4cm]{\logopath/logoKitware.png}
%     \end{minipage}
%   \end{beamercolorbox}
% }

% \setbeamertemplate{footline}{
%   \leavevmode
%   \hbox{%
%     \begin{beamercolorbox}[wd=.85\paperwidth, sep=0.6em, leftskip=0.5em]{block title}
%       \textbf{\ttitle}
%     \end{beamercolorbox}%
%     \begin{beamercolorbox}[wd=.15\paperwidth, sep=0.6em, right]{block title}
%       \textbf{\insertframenumber{} / \inserttotalframenumber}
%     \end{beamercolorbox}%
%   }
%   \vskip0pt
% }

\newcommand{\maketitleframe}{
  \begin{frame}[plain]
    \centering
    \includegraphics[height=0.09\paperheight]{\logopath/logoENS.png}\hspace{1cm}%
    \includegraphics[height=0.09\paperheight]{\logopath/logoECL.png}\hspace{1cm}%
    \includegraphics[height=0.14\paperheight]{\logopath/logoKitware.png}


      \author{\student}

      \institute{Kitware, \tutor}
      \title{\ttitle}
      \subtitle{\UE}
      \titlepage

%     \vspace{1.2cm}
%     \begin{columns}
%       \column{0.5\textwidth}
%         \centering \emph{\textbf{\student}}
%       \column{0.4\textwidth}
%         \centering \emph{\textbf{\tutor}}
%     \end{columns}
  \end{frame}
}

% Optional agenda/outline frame, common in slide decks
% \newcommand{\makeagendaframe}{
%   \begin{frame}{Outline}
%     \tableofcontents
%   \end{frame}
% }

\newcommand{\insertfigure}[4]{
  \begin{figure}
    \centering
    \includegraphics[keepaspectratio,#2]{#1}
    \caption{#3}
    \label{#4}
  \end{figure}
}

\crefname{lstlisting}{Listing}{Listings}
\Crefname{lstlisting}{Listing}{Listings}

\AtBeginSection[]
{
  \begin{frame}{Outline}
    \tableofcontents[currentsection]
  \end{frame}
}
\AtBeginSubsection[]
{
  \begin{frame}{Outline}
    \tableofcontents[currentsection, currentsubsection]
  \end{frame}
}