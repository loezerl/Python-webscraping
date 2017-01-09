#encoding: utf-8

H_i = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head>
	<meta http-equiv="CONTENT-TYPE" content="text/html; charset=UTF-8">
	<title></title>
	<meta name="GENERATOR" content="LibreOffice 4.1.6.2 (Linux)">
	<meta name="CREATED" content="0;0">
	<meta name="CHANGED" content="0;0">
	<style type="text/css">
	<!--
		@page { margin: 0.79in }
		P { margin-bottom: 0.08in }
		PRE.ctl { font-family: "Lohit Marathi", monospace }
	-->
	</style>
</head>
<body dir="LTR" vlink="999999" link="999999" lang="en-US" bgcolor="303035" alink="999999">
<pre class="western"><font color="999999">
"""

H_e = """
<style style="text/css">
  	.hoverTable{
		border-collapse:collapse; 
		border-style: hidden;		
	}
	.hoverTable td{ 
	}
	/* Define the default color for all the table rows */
	.hoverTable tr{
		background: 303035;
	}
	/* Define the hover highlight color for the table row */
    .hoverTable tr:hover {
          background-color: 505055;
    }
</style>
"""

Name_i = """<strong><span style="color: #ff9900;">"""
#Nome da Pessoa
Name_e = """</span></strong>"""

Info_i = """<br><span style="color: #009999;">"""
#Tipo do Curso, Nome do Curso
Info_e = """</span>"""

Table_i = """
<table class="hoverTable">
<thead>
<tr>
	<td nowrap="nowrap" colspan="14" align="center"><strong><span style="color: #ff9900;">Notas/Faltas&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
</tr>
</thead>
<tbody><tr rowspan="2">
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Disciplina&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Turma&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Notas 1&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Notas 2&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Notas 3&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Notas 4&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Media&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Av Final&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Media Final&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Conceito&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">HA/HR&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">THrs&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Faltas/Presencas&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Resultado&nbsp;&nbsp;&nbsp;&nbsp;</span></strong></td>
<td nowrap="nowrap"><strong><span style="color: #ff9900;">Situacao Academica&nbsp;&nbsp;&nbsp;&nbsp;</span></strong>
</td>
</tr>
"""

Table_e = """</tbody></table><br>"""

TRow_0 = """<tr rowspan="2">"""
TRow_1 = """<td nowrap="nowrap"><font color="999999">"""
#Info
TRow_2 = """&nbsp;&nbsp;</font></td>"""
TRow_3 = """</tr>""" #When all the information in the row ends

bottom = """
<strong><span style="color: #ff9900;">Any issues or love, contact me through the links below
<a href="https://github.com/loezerl/">Github</a> | <a href="https://twitter.com/loezerl">Twitter</a>
Script by Lucas Loezer
</span></strong></font></pre><font color="999999">
</font>
</body></html>
"""