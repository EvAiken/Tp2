#!/usr/bin/perl 

use CGI;
$query = new CGI;

print $query->header;

print $query->start_html('My prueba.cgi program');

print <<EOF
<head>
	<title>Inicio</title>
</head>
<body>
	<h1>Elija una opcion</h1>
	<ul>
		<li><a href="Tp2_a.cgi">Crear Entrada</a></li>
		<li><a href="Tp2Ver_a.cgi">Ver todas las entradas</a></li>
		<li><a href="">Buscar entrada</a></li>
	</ul>
</body>
</html>
EOF
