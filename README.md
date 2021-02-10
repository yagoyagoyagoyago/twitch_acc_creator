# twitch_acc_creator
# modo de uso: py acc_creator.py proxies.txt 2captcha_api_key
criador de contas pra twitch, que checa as proxies antes e usa a api do 2captcha.

é basicamente um script que cria conta pra twitch. cria um nick aleatorio, senha, data de nascimento, etc.
pega a conta e coloca em um txt.

o grande problema desse script é o fato do 2captcha enviar uma resposta errada pro funcaptcha as vezes, ai vc manda isso pra twitch e eles respondem que o captcha tá invalido. os workers do 2captcha não fazem o captcha da maneira certa, mandam pro script, o dinheiro é retirado da carteira do 2cpatcha, o script tenta criar a conta e a twitch rejeita...
ou seja, voce perde dinheiro e não cria a conta.
tambem são pouquissimas proxies free que passam pelo filtro de constancia do script.
talvez se voce usar algumas proxies pagas o script crie muitas contas e funcione.
mas se voce for só usar proxies free, não sei se voce vai se contentar com isso.

bom, o script é meio merda pelos fatos ditos acima, mas mesmo assim resolvi colocar aqui.

é isso.

formato das contas que são criadas: oauth:s9fhja8s:username:sf9jasf:user_id:2598525:client_id:824hy8252525
