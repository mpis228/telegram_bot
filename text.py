from string import Template

text_level2 = Template("""Assista ao vídeo acima até o final para\n
entender como funciona e de onde vem a renda.\n
Depois de assistir ao vídeo, você receberá a
seguinte tarefa!\n
O vídeo mostra Margarida, que ontem ganhou
$price euros e foi capaz de mudar sua vida.\n""")

text_pronto = Template("""Você está pronto para enviar o texto ou deseja modificá-lo?\n\n
Número de solicitação:\nNº 03088\n\n
Nome:\n $name\n\n
Ganhos:\n $many\n\n
Seu texto:\n $text""")

text_level4 = Template("""Descreva brevemente porque você precisa do dinheiro e se você teve alguma experiência de investimento.\n\n
Exemplo:\n
"Estou arrecadando dinheiro para realizar meu sonho e ajudar minha familia. Eu não tenho experiência em investir."\n\n
As vagas no projeto são limitadas, portanto, nosso gerente processará sua solicitação o mais rápido possível!\n\n
Digite seu texto abaixo e submeta-o para verificação""")
