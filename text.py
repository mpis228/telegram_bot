from string import Template

statistic_text = Template('Пользователи: $users\n\n'
                        'Заработано пользователями: $money   евро\n\n'
                        'Приглашенных друзей: $friend\n\n'
                        'Выполнено квестов: $quest')


text_level3_after = Template("""🚀Levaremos em conta seus desejos, obrigado por sua resposta!\n
Você tem mais 2 tarefas para completar antes de ganhar 💶$price!""")


text_level2 = Template("""Assista ao vídeo acima até o final para\n
entender como funciona e de onde vem a renda.\n
Depois de assistir ao vídeo, você receberá a
seguinte tarefa!\n
O vídeo mostra Margarida, que ontem ganhou
$price euros e foi capaz de mudar sua vida.\n""")

text_pronto = Template("""Você está pronto para enviar o texto ou deseja modificá-lo?\n
Número de solicitação:\n№$rand \n
Nome:\n$name\n
Ganhos:\n💶$price\n
Seu texto:\n$text""")

text_level4 = Template("""
Descreva brevemente porque você precisa do dinheiro e se você teve alguma experiência de investimento.\n\n
Exemplo:\n
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