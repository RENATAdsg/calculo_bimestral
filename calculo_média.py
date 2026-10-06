##Introdução de dados 
def calcular_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media
def verificar_situacao(media_final):
 if media_final < 5:
    return "Reprovado nesta matéria!"
 elif media_final <= 6:
  return "Recuperação, fale com seu professor!"
 else:
    return "Aprovado! Parabéns, você foi aprovado nesta matéria"

 ##processamento de dados do usuario 
nome=input("Olá, Digite seu nome:")
for i in range(8):##SÃO 8 DISCIPLINAS!##
 disciplina=input("Digite qual a materia:")
 num1 =float(input("Digite a primeira nota:"))
 num2 =float(input("Digite a segunda nota:"))
 num3 =float(input("Digite a terceira nota:"))

##Saída de dados 
 resultado_media=calcular_media(num1,num2,num3)
 print(f"Sua média bimestral foi de {resultado_media:.1f}")
 situacao_final = verificar_situacao(resultado_media)
 print(f"Situação do(a) {nome}:{disciplina} - {situacao_final}")