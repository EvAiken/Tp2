#!/usr/bin/perl 

use CGI;
$query = new CGI;

print $query->header(-charset=>'UTF-8');

print $query->start_html(-title=>'Guarda Códigos',
                         -author=>'Eva Figueroba',
                         -BGCOLOR=>'#E6E6FA',
                         -text=>'blue',
                         );
#-linkrel=>'"stylesheet" type="text/css" href="./main.css"');

print $query->img({-src=>'http://localhost/images/img.jpg',
					-alt=>'Imagen de Perl'});

if(!$query->param){
	print $query->start_form;
	print $query->h3('Introduzca sus datos');

	print $query->label('Nombre: ');
	print $query->textfield(-name=>'nombre',
			-size=>25,
			-maxlength=>80);
	print $query->br;
	print $query->label('Apellidos: ');

	print $query->textfield(-name=>'apellidos',
			-size=>25,
			-maxlength=>80);
			
	print $query->br;
	print $query->label('Titulo: ');
	print $query->textfield(-name=>'titulo',
			-size=>25,
			-maxlength=>80);
	print $query->br;
	open F,'/var/www/html/conf/lenguajes.txt' or die "Imposible abrir: $!";

	# Leer linea a linea e ir añadiendo a un array con push
	while(<F>){
		chomp;
		push @lineas, $_;
		# Para imprimir el array con salto de linea: print $_,"<br>";	
	}
	# Imprimir el array en pantalla
	#foreach $linea(@lineas){
	#	print $query->p($linea);
		# otra forma: print $l,"<br>";
	#}

	# Ahora meteremos los valores del array en un scroling_list

	print $query->scrolling_list(-name=>'opciones',
									 -values=>\@lineas,
									  -size=>4,
									  -multiple=>'true',
									  -default=>'perl');
	print $query->br;
	print $query->br;
	print $query->label('Escriba su código:');
	print $query->br;
	print $query->textarea(-name=>'codigo',
		-rows=>15,
		-columns=>100);
	print $query->br;

	print $query->submit(-value=>'Aceptar');
	print $query->end_form;
	}else{
		$nombre = $query->param('nombre');
		$apellidos = $query->param('apellidos');
		$titulo = $query->param('titulo');
		@months = qw( Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec );
		@days = qw(Sun Mon Tue Wed Thu Fri Sat Sun);
		($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
		$codigo = $query->param('codigo');
		# Abre el archivo (o lo crea si no existe)
		open (FILE, ">> /var/www/html/conf/guardar.txt") or die "no puede abrir: $!";
		#escribe
		print FILE "---ENTRADA---\n";
		@lineas = $query->param('opciones');
		foreach $linea(@lineas){
		print FILE $linea,":::","\n";
		}
		print FILE $titulo,":::", "\n";
		print FILE $nombre," ",$apellidos,":::","\n";
		print FILE "$mday $months[$mon] $days[$wday]",":::","\n";
		
		
		print FILE $codigo,":::","\n";
		# Cierra el archivo
		close FILE;
		print $query->h3('Tus códigos han sido guardados un un fichero en /usr/lib/cgi-bin/Tp2Files/texto.txt');
	}
