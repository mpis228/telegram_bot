from string import Template

statistic_text = Template('📝 *Estatísticas "Mustang BOT"*\n\n'
                        '📈 Users:  *$users*\n'
                        '📈 Earned pelos usuários:  *$money евро*\n'
                        '📈 Amigos convidados:  *$friend*\n'
                        '📈 Followed quests:  *$quest*\n\n'
                        'Os dados são atualizados uma vez por dia')

text_level2_after = Template("""🚀*Você já viu o vídeo até o final* e está pronto para seguir em frente?\n
 Você tem mais 3 tarefas para completar antes de ganhar 💶*$price*!""")

text_level3 = Template("""🔎Confira nosso site e cadastre-se nele.\n
 Escreva a palavra "PRONTO" para continuar!\n
  Nosso website tem todas as informações necessárias sobre como ganhar dinheiro e todas as feedback⤵️""")

text_level3_after = Template("""🚀Levaremos em conta seus desejos, obrigado por sua resposta!\n
Você tem mais 2 tarefas para completar antes de ganhar 💶*$price!*""")

text_level1 = Template("""📱 Assine meu Instagram, dê uma olhada de perto nas últimas 5 Stories. Depois voltar para o bot!\n
Você se inscreve no Instagram da Fernando Cardoso para que possa nos contatar a qualquer momento para garantir seus ganhos.\n
Para obter 💶*$price*, você precisa completar 5 tarefas. Depois de concluir com sucesso todas as tarefas, você receberá a quantia desejada! ⤵️""")


text_level2 = Template("""🎬*Assista ao vídeo acima até o final para\n
entender como funciona e de onde vem a renda.\n
Depois de assistir ao vídeo, você receberá a
seguinte tarefa!*\n\n
O vídeo mostra Margarida, que ontem ganhou
💶$price euros e foi capaz de mudar sua vida.\n\n
Você pode escrever para o vencedor⤵️""")

text_pronto = Template("""✉️Você está pronto para enviar o texto ou deseja modificá-lo?\n
◽️Número de solicitação:\n№$rand \n
◽️Nome:\n$name\n
◽️Ganhos:\n💶$price\n
◽️Seu texto:\n$text""")

text_level4 = Template("""
📝Descreva brevemente porque você precisa do dinheiro e se você teve alguma experiência de investimento.\n\n
✏️Exemplo:\n
"Estou arrecadando dinheiro para realizar meu sonho e ajudar minha familia. Eu não tenho experiência em investir."\n\n
As vagas no projeto são limitadas, portanto, nosso gerente processará sua solicitação o mais rápido possível!\n\n
Digite seu texto abaixo e submeta-o para verificação""")

text_level5 = Template("""Seu solicitação está sendo verificado atualmente...\n
Não leva mais do que 10 minutos.\n
🔂Se sua inscrição não for aprovada, você poderá tentar novamente após 24 horas.\n
Em breve você receberá as instruções finais e ganhar 💶$price""")

text_end = Template("""✍️Envie a palavra "Última tarefa" a nosso Telegram, WhatsApp ou Instagram\n
Desta forma, saberei que você completou com sucesso todas as tarefas e lhe darei as instruções finais, após as quais você poderá ganhar $price para sua conta bancária!\n
Escolha um mensageiro com o qual você se sinta confortável e me envie uma mensagem de texto "Última tarefa"⤵️ """)

text_author = Template("""🖊 Aqui você pode conhecer o autor Fernando Cardoso e sua história.\n
Você também pode fazer qualquer pergunta ou pedir ajuda.\n
Selecione o item do menu ⤵️""")

text_start = Template("""Uma vez completadas *5 tarefas*, você ganhará *$price* e poderá retirá-las para sua conta bancária!

2 Meu interesse é que depois de ganhar você transfira *15% para mim* e você fica com o resto. É por isso que estamos interessados em seu sucesso.
 
Para prosseguir para a primeira tarefa, pressione *"START"* ⤵️""")

question_1 = ['Por que você pode confiar em mim?', """Meu trabalho é dar a você tarefas especiais pelas quais empresa
 "Ford" e "Binance" paga dinheiro. Este é um evento especial de caridade.
 
Se você tiver alguma dúvida, eu pode lhe deixar mais informações na forma de documentos e contatos.

Eu cobro apenas 15% por meus serviços e você fica com o resto. Por isso estou tão interessado no vosso sucesso como vós."""]

question_2 = ["Como exatamente você ganha dinheiro?", """É necessário fazer participações mínimas na instituição de caridade "Ford".

Binance (um dos participantes da instituição de caridade) faz o seu investimento e ganha uma grande soma de dinheiro, que depois vai parar à sua conta bancária.

Quanto maior o seu investimento de caridade, mais você pode ganhar."""]

question_3 = ['Quanto você pode ganhar?', """Você escolhe a quantia que ganha e as tarefas dependem dessa quantia.

Os ganhos podem chegar a 8.500 euros.
 Você pode convidar amigos e para cada um você recebe 10% além de seus ganhos."""]

question_4 = ['Com que freqüência posso usar o tarefas?', """A mesma pessoa não pode usar o tarefas mais de uma vez por semana.

 Para completar a tarefa novamente, você precisará entrar em contato conosco"""]

question_5 = ['Como você poderá retirar o dinheiro?', """A retirada pode ser feita para os seus dados bancários.

O dinheiro chegará em 2 horas, às vezes demora um pouco mais."""]
question_6 = ['А ganhos é garantida?', """A empresa "Ford" gera tarefas especiais que pagam dinheiro.
Fernando, sócio da "Ford" e autor do projeto "Mustang BOT", verifica pessoalmente todas as tarefas, para que você não tenha que se preocupar.

Nossos ganhos estão diretamente relacionados aos seus, portanto, é de nosso interesse que você conclua corretamente todas as tarefas e receba o valor desejado.

Sua tarefa é completar todas as tarefas corretamente e seguir nossas instruções."""]

questions = {0: question_1, 1: question_2, 2: question_3, 3: question_4, 4: question_5, 5: question_6}