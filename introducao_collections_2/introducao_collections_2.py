from collections import Counter

text = '''Historicamente causadores de inúmeras vítimas, os acidentes de trânsito vêm ocorrendo com frequência cada vez menor, no Brasil. Essa redução se deve, principalmente, à implantação da Lei Seca ao longo de todo o território nacional, diminuindo a quantidade de motoristas que dirigem após terem ingerido bebida alcoólica . A maior fiscalização, aliada à imposição de rígidos limites e à conscientização da população, permitiu que tal alteração fosse possível .

As estatísticas explicitam a queda brusca na ocorrência de óbitos decorrentes de acidentes de trânsito depois da entrada da Lei Seca em vigor. A proibição absoluta do consumo de álcool antes de se dirigir e a existência de diversos pontos de fiscalização espalhados pelo país tornaram menores as tentativas de burlar o sistema. Dessa forma, em vez de fugirem dos bafômetros e dos policiais, os motoristas deixam de beber e, com isso, mantêm-se aptos a dirigir sem que transgridam a lei.

Outro aspecto de suma relevância para essa mudança foi a definição de limites extremamente baixos para o nível de álcool no sangue, próximos de zero. Isso fez com que acaba e a crença de que um copo não causa qualquer diferença nos reflexos e nas reações do indivíduo e que, portanto, não haveria problema em consumir doses pequenas. A capacidade de julgamento de cada pessoa, outrora usada como teste, passou a não mais sê-lo e, logo, todos têm que respeitar os mesmos índices independentemente do que consideram certo para si.

Entretanto, nenhuma melhoria seria possível sem a realização de um amplo programa de conscientização. A veiculação de diversas propagandas do governo que alertavam sobre os perigos da direção sob qualquer estado de embriaguez foi importantíssima na percepção individual das mudanças necessárias. Isso fez com que cada pessoa passa e a saber os riscos que infligia a si e a todos à sua volta quando bebia e dirigia, amenizando a obrigatoriedade de haver um controle severo das forças policiais.

É inegável a eficiência da Lei Seca em todas as suas propostas, formando uma geração mais consciente e protegendo os cidadãos brasileiros. Para torná-la ainda mais eficaz, uma ação válida seria o incremento da frota de transportes coletivos em todo o país, especialmente à noite, para que cada um consuma o que deseja e volte para casa em segurança. Além disso, durante um breve período, a fiscalização poderia ser fortalecida, buscando convencer motoristas que ainda tentam burlar o Estado. O panorama atual já é extremamente animador e as projeções, ainda melhores, porém apenas com a ação conjunta de povo e governo será alcançada a perfeição.'''

count = Counter(text.lower())
char_total = sum(count.values())

print('frequência:')
print(count)
print(f'\ntotal de caracteres: {char_total}')

# calculando porcentagem
percentages = {key: count / char_total for key, count in count.items()}  # dict comprehension

# imprimindo o top 10
percentages = Counter(percentages)

print('\ntop 10:')
for key, value in percentages.most_common(10):
    print(f'"{key}" => {(value*100):.2f}%')
