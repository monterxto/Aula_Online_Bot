# Aula_Online_Bot
Bot para o sistema Blackboard Collaborate, que é usado na minha faculdade para as aulas onlines inclusive as aulas que ficaram online para a quarentena

Ele é um bot que entra na sala, manda algumas mensagens aleatórias que estão no arquivo txt "mensagens" escolhe um integrante aleátorio e manda algunas mensagens aleátorias no pv deleue estáo no arquivo txt "mensagensPV".
E para usar a funcionalidade para ele conseguir streamar vídeos do youtube ele precisa de permissão para ligar a cam e para ligar o mic.
O guia de como usar completamente e de maneira correta o bot é:

  Dependencias:
    Programas:
		- https://obsproject.com/pt-br/download
		- https://obsproject.com/forum/resources/obs-virtualcam.949/
		- https://www.vb-audio.com/Voicemeeter/banana.htm
		- https://www.videolan.org/vlc/download-windows.pt-BR.html
    Modulos (que precisam ser instalado):
		- selenium
		- youtube-dl

Configuração:
	Após instalar todos os programas, abrir vlc
	clicar em ferramentas->preferencias->audio->dispositivo->voicemeeter input...
	depois
	abrir obs, fechar qualquer guia de tutorial
	clicar com o botão direito em fontes depois
	adicionar->captura de jogo->ok->modo(capturar janela especifica)->janela(vlc...)->ok. pode fechar o vlc agora.
	depois ainda no obs ir ferramentas->virtual cam->start

Iniciar programa:
	com os modulos já instalados, inicie o arquivo Main
	assim que o bot mandar a mensagem que está iniciou
	pode usar os comandos.

Comandos (ignorar o "<>"):
    Adicionar um vídeo na fila:
		- !xto play <url_youtube>
    O bot falar os comandos que possui:
		- !xto help
    Listar os próximos vídeos:
		- !xto lista
    Passar para o próximo vídeo:
		- !xto skip
    Fechar programa
		- !xto exit
	
