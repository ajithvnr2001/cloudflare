---
url: https://blog.cloudflare.com/pt-br/rss/
title: Blog da Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:08:01.158095+00:00
---

# Blog da Cloudflare

> Source: https://blog.cloudflare.com/pt-br/rss/

Blog da CloudflareMergulhos técnicos aprofundados, atualizações de produtos e insights das equipes que ajudam a construir uma Internet melhor.https://blog.cloudflare.com/pt-br/ pt-brhttps://blog.cloudflare.com/favicon.icoBlog da Cloudflarehttps://blog.cloudflare.com Thu, 08 Oct 2026 08:07:56 GMTApresentamos o Forge: o pipeline de código aberto para gerar SDKs, CLIs, documentação e muito maishttps://blog.cloudflare.com/pt-br/forge-open-source-generation-pipeline/ Thu, 08 Oct 2026 07:40:08 GMTO Forge é um pipeline de código aberto e modular que roda em CI para gerar SDKs, CLIs e documentação diretamente a partir de definições de API. Ao mover a geração para o início do processo, nos repositórios individuais de cada equipe, o Forge mantém as ferramentas para desenvolvedores sempre atualizadas e sincronizadas.AgentesAPIBirthday WeekCLIDesenvolvedoresSDKHoje apresentamos o [Forge](https://github.com/cloudflare/forge), uma abordagem renovada para gerar SDKs, CLIs, documentação e bibliotecas. O Forge é um pipeline de geração de código aberto e modular, que qualquer pessoa pode implantar e executar gratuitamente.

O Forge ainda está em um estágio inicial, mas já gera as saídas necessárias para a [cf CLI](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) e, ao longo dos próximos meses, ele irá impulsionar a documentação da API, os SDKs e muito mais da Cloudflare.

Criamos o Forge para, internamente, tratar agentes como nossos clientes. Agora estamos disponibilizando-o como código aberto porque acreditamos que todos devem ser capazes de gerar todas as superfícies de que os agentes precisam. Antes, apenas produtos para desenvolvedores precisavam de CLIs, SDKs de API e servidores MCP, todos com documentação impecável. Hoje, esses são requisitos básicos para qualquer produto.

## **Nossa API superou nossos geradores**

A API da Cloudflare conta com mais de 3.500 operações, e as centenas de serviços que a alimentam são escritos em muitas linguagens, incluindo Rust, Go, TypeScript e Python. Ao embarcar na construção de uma CLI para toda a API da Cloudflare, incluindo nossos SDKs e documentação da API, precisávamos de um pipeline de geração de código capaz de operar nessa escala. Esse pipeline precisa ser flexível o suficiente para funcionar entre linguagens e se adaptar à forma de trabalhar de cada um em nossas equipes de engenharia.

Precisávamos de uma forma de reduzir o esforço de coordenação entre equipes. Quando uma equipe de produto da Cloudflare faz uma alteração na API, ela precisa conseguir usar uma versão prévia da CLI, do SDK e do site de documentação comuns à Cloudflare, tudo isso antes de mesclar essa alteração e entregá-la aos clientes. Também era necessário encontrar uma maneira de garantir que não quebrassem inadvertidamente o pipeline de geração. E por fim, havia a necessidade de um sistema que pudesse gerar mais do que apenas um SDK, desde o Cap’n Web ao MCP e além.

Testamos vários produtos hospedados que tentam resolver isso e chegamos a contar com alguns deles em produção. Nenhum resolveu o problema para nós, e alguns foram até mesmo descontinuados. Uma equipe mesclava uma alteração que acabava quebrando o pipeline de geração, outra só descobria isso no momento do lançamento, e perdemos tempo demais nadando contra a corrente usando ferramentas hospedadas que não podíamos controlar, coordenando alterações entre equipes e fornecedores.

Foi assim que começamos a desenvolver o Forge.

O Forge foi criado para resolver todos esses problemas: ele roda em CI, nos repositórios de API de cada equipe, assim como o nosso revisor de código com IA e os pipelines de teste. Ele analisa cada alteração e, em seguida, gera versões prévias da CLI, da documentação e dos SDKs com apenas suas alterações destacadas, que podem ser instaladas para teste. É o mesmo princípio do [Workers Previews](https://blog.cloudflare.com/worker-previews/): uma versão prévia completa para cada alteração, mas aplicada à geração de SDKs em escala, mesmo quando a superfície da API está distribuída em centenas de serviços e repositórios. É isso que o Forge pretende entregar.

## **Os transformadores do Forge podem gerar qualquer coisa, incluindo Cap’n Web**

Mais do que ninguém, a Cloudflare tem vários motivos para querer um gerador capaz de ir além dos alvos de linguagem habituais. O [Cap’n Web](https://capnweb.com/) é o sistema RPC da Cloudflare que permite ao TypeScript chamar uma API remota como se fosse uma chamada de método local:

O Forge permite usar uma especificação OpenAPI para gerar diretamente Cap’n Web, o que, por sua vez, possibilita gerar [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) de Workers para outras APIs. Afinal, os bindings no runtime do Workers são implementados como Workers que expõem métodos RPC.

Isso não é exclusivo do Cap’n Web: outras ferramentas populares que vocês talvez já utilizem precisam do mesmo. Se você usa [TanStack Query](https://tanstack.com/query/), o ideal seria poder gerar bindings do TanStack Query para seu aplicativo, criados diretamente a partir de sua própria API, sempre atualizados e validados em relação à sua API real. O mesmo vale para gerar schemas Zod ou Valibot, servidores MCP ou qualquer outra coisa que facilite o consumo da sua API.

Isso é possível porque os geradores de código do Forge são flexíveis. Eles foram desenvolvidos para permitir o fluxo de informações de uma saída para outra.

## **Os transformadores do Forge podem ser encadeados: gerando saídas a partir de outras saídas.**

Projetamos o Forge para ser extensível e compatível com diversos tipos de entrada e saída. O Forge oferece geradores de CLI, SDK e documentação, mas nada impede você de adicionar um transformador que gere um pacote específico de uma biblioteca ou até mesmo um painel ou aplicativo completo. Atualmente, o Forge é compatível com OpenAPI como tipo de entrada, mas ele foi projetado para permitir [AsyncAPI](http://asyncapi.com), GraphQL, Cap’n Proto, Protobuf ou outros formatos de entrada no futuro.

Além de simples compatibilidade, isso permite que você encadeie destinos, usando a saída de um destino para produzir outros. Isso é comum em outros geradores, onde os destinos de CLI e Terraform são produzidos a partir do SDK Go. Mas o que falta, e o que o Forge oferece, é uma forma de o usuário controlar esse sistema de encadeamento por conta própria.

Internamente, nós buscávamos uma solução para essa questão, pois nossa própria cf CLI é escrita em TypeScript, algo que outros geradores de SDK geralmente não encadeiam para CLIs. Mas a nossa própria situação nos fez perceber qual era o real problema: por que uma ferramenta geradora de SDK deveria tomar essa decisão por você? Talvez sua equipe use Python e você queira que a CLI também seja em Python.

Se você está pensando: “E quem se importa se é em Python ou não? O código é gerado automaticamente”, saiba que CLIs são _diferentes_. As CLIs frequentemente introduzem comportamentos exclusivamente locais que não fariam sentido em um SDK, comportamentos que você escreve manualmente porque, por natureza, não são respaldados por nenhuma chamada de API. Por exemplo, a cf CLI tem comandos como cf dev e cf build que são adicionados ao restante da saída gerada. Estes comandos precisam chamar APIs TypeScript de outros pacotes como o Vite.

Agora adicione a documentação à mistura. Se você está gerando sua CLI e sua documentação _puramente_ a partir de sua especificação OpenAPI, como você reintroduz esses comandos escritos manualmente em sua documentação, para que possam ser documentados junto com o restante?

Não encontramos nenhuma ferramenta existente que faça isso hoje, e ainda assim é exatamente o que precisamos para a cf. Por isso, estamos incorporando isso ao Forge.

## **Altere sua API sem comprometer os usuários**

O Forge também está nos preparando para um melhor versionamento de API. A API v4 da Cloudflare é a única versão principal de nossa API há 10 anos; desde então, pode parecer que não lançamos novas versões principais, mas pelas definições do SemVer, fizemos algumas mudanças que justificam uma nova versão principal. Ao mesmo tempo, diversas operações em nossa API têm tags internas “v2” ou identificadores “beta” que sobreviveram por muito tempo àquela fase do ciclo de vida do produto.

Após tantos anos com a nossa API v4, temos plena consciência de que uma nova v5 deixaria muitos de nossos clientes para trás. Por isso, com o Forge publicando artefatos ao longo do caminho, estamos trabalhando em uma abordagem ao versionamento de API que nos permita lançar novas versões principais sem comprometer clientes ou SDKs antigos.

Em breve teremos muito mais informações sobre nossos SDKs, incluindo TypeScript, Rust, Python, Go, PHP e Terraform. Especialmente o Terraform. Sabemos que atualizar qualquer provedor Terraform exige seu próprio nível de rigor, e vamos prestar atenção especial à transição do Terraform.

## **Ferramentas essenciais devem ser acessíveis a todos**

Acreditamos que construir ferramentas para APIs é uma parte fundamental da internet, e todos devem poder fazê-lo sem precisar de um produto SaaS. Você deve ser o dono de seus SDKs, CLIs e documentação. E se você os gera, deve poder fazer o que quiser com eles, onde quiser, gratuitamente.

Por isso estamos disponibilizando o [Forge como código](https://github.com/cloudflare/forge) aberto sob a licença permissiva Apache 2.0. Queremos que as pessoas se juntem a nós nessa jornada e contribuam.

Ou não? Talvez você queira guardar tudo para si. Também pode. Você pode executar o Forge para qualquer finalidade, com modificações personalizadas, de forma gratuita e privada na sua própria infraestrutura.

_Agradecimentos: Este projeto também foi viabilizado graças aos esforços de design e implementação de Dan Carter, Steven Chong, Krishna Paritala e Shelley Jones._

]]>01M4D5NK5NBE2ACGAMTPKBRQJMA internet tem um segundo públicohttps://blog.cloudflare.com/pt-br/agentic-web/ Thu, 08 Oct 2026 07:31:36 GMTMais da metade do tráfego que chega aos sites na Cloudflare já é automatizado, e os agentes de IA são a parte que cresce mais rapidamente. Estamos dando aos proprietários de sites as ferramentas para ver quem os visita, decidir quem entra e cobrar pelo acesso.AgentesAIBirthday WeekBots de IABusca de IADurante a maior parte de sua história, a internet teve apenas um público que pagava as contas: as pessoas. Nós líamos os artigos, víamos os anúncios e comprávamos as assinaturas. Os bots sempre estiveram lá, mas eram principalmente grandes operações automatizadas que não visualizavam anúncios, não pagavam nada e não liam em nenhum sentido significativo.

Isso está mudando rapidamente. No final de 2024, a Cloudflare processava uma média de 63 milhões de requisições HTTP _por segundo_. Hoje, esse número quase dobrou para 115 milhões, com picos acima de 150 milhões. No último ano, as requisições diárias de agentes de IA em nossa rede cresceram mais de 1.700 %. Este ano, pela primeira vez, mais da metade do tráfego da internet não era humano.

A web humana não encolheu para dar espaço. Um segundo público surgiu ao lado dela: agentes, software agindo em nome das pessoas. Eles se situam em algum lugar entre os humanos e os bots tradicionais. Eles não respondem a anúncios, mas geralmente há uma pessoa por trás deles com uma tarefa a realizar. Para as empresas que aprendem a atendê-los e a extrair valor deles, os agentes agregam valor. Para as que não o fazem, eles extraem valor.

O que nossos clientes precisam não mudou: ser descobertos, contar grandes histórias, criar experiências excelentes e vender. O que mudou é que mais da metade de seus visitantes agora são softwares. Nossa missão é ajudar você a atender a ambos os públicos.

## Mais tráfego, menos receita

Por trinta anos, a web funcionou com um único arranjo: você permitia que os mecanismos de busca rastreassem seu site, eles lhe enviavam visitantes e você transformava esses visitantes em negócios. Ser encontrado e ser pago eram a mesma coisa.

A IA fez esse delicado equilíbrio entrar em colapso. Agora, os mecanismos de respostas leem a página e dão ao leitor um resumo. Isso custa largura de banda para os sites sem levar um humano a um site onde os anúncios ou pagamentos acontecem. As máquinas continuaram chegando, e o público que pagava pela web parou de chegar a esses sites. Algumas das categorias mais rastreadas, como varejo, software de computador, TI e serviços e serviços financeiros, viram o tráfego humano cair até 40 % em menos de um ano.

O resultado é que a receita por solicitação está caindo enquanto os custos sobem. Cada solicitação automatizada ainda custa largura de banda, computação e recursos de origem, e uma parcela crescente dessas solicitações não gera referências, impressões de anúncio ou assinaturas. Nosso primeiro instinto foi bloquear todo o tráfego automatizado. No ano passado, recomendamos bloquear os crawlers de treinamento de IA em novos domínios para que os proprietários de sites pudessem ao menos dizer não ao uso de seu conteúdo para desenvolver modelos. Na primavera de 2025, 22% das requisições de crawlers que vimos eram para treinamento de IA (de acordo com o propósito declarado dos crawlers). Em junho de 2026, era 52%. O problema é que um “não” generalizado não é uma abordagem suficientemente refinada para a economia da internet que está sendo construída agora.

Existe uma oportunidade de atender os agentes. Faça certo e você estará na vanguarda de um novo modelo de negócio. Faça errado e os resultados serão os mesmos de gerações de sites que estiveram no lado errado das mudanças de algoritmo dos mecanismos de busca.

## Parte desse tráfego é um cliente

Um agente que reserva uma mesa, compara cotações de seguro ou compra um conjunto de dados para um pesquisador é um cliente. Só que não é humano.

A parte do tráfego automatizado que cresce mais rapidamente não são mais os crawlers. São os agentes: softwares que buscam páginas em nome de uma pessoa, muitas vezes porque o humano perguntou algo a um chatbot. Esse tráfego de agentes segue as rotinas humanas, com um ritmo semanal e uma queda durante as férias de verão. Recusar um agente pode ser recusar a pessoa que o enviou.

Os agentes também se comportam de maneira diferente dos crawlers de treinamento. Um crawler de treinamento coleta suas páginas para desenvolver um modelo. Um agente volta cada vez que alguém pergunta sobre esse conteúdo, então esse tráfego cresce com o número de perguntas que as pessoas fazem, não com o quanto você publica.

Não dá para fazer negócios com um público que você não pode ver, não pode distinguir, não pode definir termos e não pode cobrar. Até recentemente, para a maior parte do tráfego web não humano, nenhuma dessas quatro coisas era possível.

### Veja quem realmente visita seu site

**O termo "bot de IA" já não significa muita coisa por si só.** O que importa é o que um bot faz. O **AI Crawl Control** , o **Business Insights** e o **BotBase** da Cloudflare mostram aos proprietários de sites quem está rastreando, o que está sendo coletado, o que volta e quais de seus URLs são mais requisitados.

O nome de um bot só tem valor se você puder confiar nele. Com o **Web Bot Auth** , operadores, incluindo OpenAI, Google e AWS, assinam criptograficamente as solicitgações de seus agentes, para que um site possa distinguir um agente real de um impostor sem precisar adivinhar por endereços de IP ou strings de user-agent. Processamos mais de 500 bilhões de solicitações de bots verificadas por semana.

### Defina seus termos

Em julho, substituímos o único switch de “bloqueio de bots de IA” por [controles separados para busca, agentes e treinamento](https://blog.cloudflare.com/content-independence-day-ai-options/), disponíveis em todos os planos, inclusive no gratuito. Os dados mostraram por que essa distinção era necessária. Menos de 1% dos sites na Cloudflare bloqueiam crawlers de busca, enquanto 17% bloqueiam os de treinamento. Os proprietários de sites nunca tentaram se esconder. Mas com o crescimento do tráfego agêntico e as novas formas como os agentes usam as informações, eles de repente não tinham transparência sobre como seu conteúdo estava sendo usado, nem escolha sobre isso. Ser encontrado não garante mais que serão pagos, e eles querem ser encontrados sem serem explorados.

Isso é particularmente difícil no caso de crawlers de uso misto. Quando um bot faz tanto busca quanto treinamento, recusar um significa recusar o outro. Em 15 de setembro, lançamos o [Disallow AI Training](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/). Ele mantém você indexado para buscas enquanto usa mecanismos específicos do crawler para instruir o operador a não usar seus dados para treinamento. Apple, Google e Microsoft se comprometeram a respeitar isso. O [Cloudflare Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) também rastreia publicamente o comportamento dos crawlers.

Novos domínios agora veem configurações recomendadas com base em como o site ganha dinheiro, em vez do tipo de software que o visita. Para sites financiados por publicidade, você pode facilmente proibir o treinamento e bloquear agentes em páginas que exibem anúncios, porque um anúncio só paga quando uma pessoa o vê. Você pode alterar qualquer uma dessas configurações a qualquer momento.

### Seja pago

Em agosto de 2026, descrevemos [a internet agêntica que estamos construindo](https://blog.cloudflare.com/the-agentic-internet/) como legível, detectável, acionável e que permite pagamento. O último termo, que permite pagamento, é o que determina se a web aberta consegue se autofinanciar. A web precisa de uma forma de dizer “ _sim, se você pagar_ ” em vez de um binário “ _sim_ ” ou “ _não_ ”.

O mercado de licenciamento mostra tanto a enorme demanda quanto onde estão as lacunas. Mais de 50 acordos entre produtores de conteúdo e IA foram assinados desde 2023. Quase todos são personalizados e bilaterais, envolvendo grandes produtores de conteúdo e grandes empresas de IA. Eles provam que o conteúdo tem valor. Mas não alcançam a maior parte da web, e não alcançam a maioria dos compradores.

Nem todo ativo deve ser vendido da mesma forma. Conteúdo e conjuntos de dados de alto valor precisam de uma rede confiável, onde os compradores sejam identificados e relatem como o trabalho foi usado. Serviços como APIs e ferramentas MCP não funcionam assim: cada solicitação é o uso.

Por isso estamos desenvolvendo para os dois.

O [Pagamento por uso](http://blog.cloudflare.com/pay-per-use) alcança os sites que o licenciamento direto não consegue. A maioria dos produtores de conteúdo nunca conseguirá um acordo personalizado com cada empresa de IA, e nenhuma empresa de IA pode negociar com milhões de sites. O Pagamento por uso é a ponte. Ele não cobra pelo rastreamento. O pagamento ocorre apenas quando o conteúdo é realmente usado. Cada comprador é um crawler verificado, o que garante a confiabilidade da rede, definindo seus próprios critérios para o que constitui uso e qual valor será pago. 

Os produtores de conteúdo veem a oferta, escolhem se querem aderir e podem cancelar a participação quando deixar de funcionar para eles. O comprador relata cada utilização, a Cloudflare verifica esses relatórios, cobra o comprador e paga o produtor de conteúdo. O relatório é tão importante quanto o pagamento. Os produtores de conteúdo veem o que foi utilizado, quando e quanto ganharam, e, quando o comprador informa, informações sobre quais perguntas trouxeram seu trabalho à tona. Acordos de licenciamento raramente oferecem esse nível de transparência. Isso cria um ciclo de feedback: os produtores de conteúdo aprendem o que as pessoas realmente perguntam e, a partir disso, podem decidir o que abordar, o que atualizar e o que disponibilizar facilmente para os agentes.

Não haverá uma única definição de uso. Um mecanismo de busca citando uma fonte, um agente de pesquisa citando uma passagem e um agente de compras completando uma compra criam tipos diferentes de valor, e cada um vai querer seu próprio modelo de negócio. Os compradores podem participar por meio de vários modelos de negócio utilizando a mesma infraestrutura, sem necessidade de novas integrações por parte dos produtores de conteúdo. Pegue uma publicação especializada para engenheiros navais, com alguns milhares de assinantes e pouca perspectiva de um acordo de licenciamento de IA. Ela é paga por cada empresa de IA participante que se baseia em seu trabalho.

O [Monetization Gateway](https://blog.cloudflare.com/monetization-gateway-beta) captura valor que, até então, não tinha como ser transacionado. Contas, chaves de API e assinaturas funcionam para clientes que você já conhece, não para um agente que quer uma única consulta de um serviço que nunca usou antes. Nosso beta fechado permite que clientes da Cloudflare nos EUA qualificáveis definam preços para qualquer conteúdo que passe por nós, usando a linguagem de regras que já conhecem. Quando uma regra corresponde, retornamos HTTP 402 Payment Required usando o protocolo aberto x402, e o agente paga ao vendedor diretamente.

Isso faz muito além de recuperar receita perdida. Os agentes são clientes por direito próprio: pagam pelos dados, APIs e ferramentas que usam, seja a solicitação a compra inteira ou uma etapa em uma tarefa maior.

O Monetization Gateway precifica por solicitação, por consulta ou por token, a preços fixos ou com teto máximo. Um site de estatísticas esportivas baseado em anúncios pode cobrar uma fração de centavo cada vez que um agente pergunta: “Quem lidera a liga em assistências?” Quando anunciamos o Monetization Gateway, milhares de vendedores entraram na lista de espera, e a solicitação mais comum foi “cobrar dos agentes, não dos humanos”. Também somos nosso primeiro cliente. O AI Gateway da Cloudflare usa o Monetization Gateway para permitir que os agentes paguem pela inferência, para que encontremos os pontos problemáticos antes que nossos clientes o façam.

Para os compradores, os dois produtos superam uma página de bloqueio: acesso confiável e uma forma de alcançar milhões de sites em vez de um acordo de licenciamento ou chave de API por vez. Cada solicitação paga gera um recibo mostrando o que foi comprado e o pagamento.

Tanto o Pagamento por uso quanto o Monetization Gateway são apostas, desenvolvidas em conjunto com clientes utilizando elementos fundamentais compartilhados: identidade, medição, precificação, liquidação e análises. Eles funcionam juntos, de modo que um produtor de conteúdo pode proibir o treinamento, permitir a busca, ganhar com respostas de IA e cobrar dos agentes por artigo a partir de um único painel. Precificação e descoberta ainda não estão resolvidas, por isso os dois são lançados como betas, moldados por clientes reais e transações reais.

### Tornar cada solicitação mais barata

O pagamento é a resposta para a queda de receita. O aumento de custos é um problema diferente, e boa parte dele é simplesmente desperdício. A maioria dos crawlers ainda baixa páginas criadas para humanos, repetidamente, para extrair alguns parágrafos de texto. Com muita frequência, os bots rastreiam sites que não mudaram desde a última tentativa. Isso queima largura de banda para o site e capacidade de computação para o crawler, e acontece antes que qualquer resposta seja escrita. Estamos trabalhando com nossos clientes e os crawlers em ferramentas que vão ajudar. Hoje, você pode ver o consumo de largura de banda por operador em nosso painel.

Em julho, anunciamos um [projeto de pesquisa conjunto com a OpenAI](https://www.cloudflare.com/press/press-releases/2026/cloudflare-announces-research-pilot-with-openai/), um piloto pioneiro para explorar como as informações da rede global da Cloudflare podem ajudar os mecanismos de busca de IA a descobrir e indexar conteúdo relevante na web aberta de forma mais eficiente e eficaz. Planejamos compartilhar nossos resultados iniciais nas próximas semanas.

Para nossos clientes, estamos lançando ferramentas e experiências de um clique para otimizar seus sites para esse novo tipo de tráfego. O [Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) permite que os agentes leiam uma página sem o estilo adicional voltado para olhos humanos, e o [WebMCP](https://blog.cloudflare.com/webmcp/) permite que um site exponha ações diretamente em vez de fazer os agentes adivinharem qual botão pressionar.

## Por que desenvolver na Cloudflare

Mais de 20 % da web está atrás da rede da Cloudflare, assim como quase 80 % das principais empresas de IA. Vemos os dois lados deste mercado. Construímos a infraestrutura para visibilidade, identidade, controles e liquidação, e deixamos o mercado definir o valor das coisas.

O antigo acordo acabou, e o novo ainda está sendo escrito. Juntos podemos moldar o que vem a seguir.

Em uma versão, poucas empresas controlam como os agentes encontram as coisas, provam quem são e pagam, e todos os demais passam por elas. Na outra, esses elementos são padrões abertos que qualquer um pode implementar, e um site de qualquer tamanho pode definir seus termos e ser pago. Preferimos a segunda.

É por isso que essa infraestrutura opera com base em padrões abertos como x402 e Web Bot Auth, para que qualquer um possa desenvolver a partir deles. Os proprietários de domínio escolhem seus próprios provedores de identidade, seus próprios processadores de pagamentos, seus próprios parceiros agentes. A Cloudflare é uma opção, não toda a pilha.

Por décadas, a web foi custeada pelas pessoas que a visitavam. Agora o software que a visita em nome delas também pode pagar sua parte.

]]>01M4D6JRHPB2KTM0AMH90AB1ZGUma autoridade certificadora para toda a internethttps://blog.cloudflare.com/pt-br/cloudflare-certificate-authority/ Thu, 08 Oct 2026 07:11:21 GMTDoze anos após o lançamento do Universal SSL, a Cloudflare está se candidatando para se tornar uma autoridade certificadora. Combinando uma raiz estabelecida, uma abordagem ACME-first e Merkle Tree Certificates, estamos construindo uma AC pós-quântica para a web aberta.Birthday WeekCriptografiaPós-quânticoSegurançaTLSHá doze anos, durante a Birthday Week 2014, [ativamos o Universal SSL](https://blog.cloudflare.com/introducing-universal-ssl/) e quase dobramos da noite para o dia o número de sites criptografados na web, oferecendo TLS gratuito a todos os sites por trás da Cloudflare, incluindo os que nunca nos pagaram um centavo. A criptografia deixou de ser um empreendimento caro e trabalhoso para se tornar o padrão.

Para a Birthday Week deste ano, damos o próximo passo nesse caminho. Por mais de uma década, fomos um dos maiores consumidores de certificados de confiança pública na internet, sem jamais termos emitido um sequer nós mesmos. Isso está mudando. A Cloudflare anuncia sua intenção de se tornar uma autoridade certificadora (AC) pública.

Hoje anunciamos os primeiros marcos concretos nesse esforço: solicitamos a inclusão nos programas raiz do Chrome, Apple, Microsoft e Mozilla, e assinamos um acordo definitivo para adquirir uma raiz estabelecida e amplamente reconhecida da GlobalSign, de modo que possamos oferecer certificados com o maior alcance possível de dispositivos no dia em que começarmos a emitir. Também anunciamos nossos planos de ser uma das primeiras ACs a oferecer certificados pós-quânticos, com foco no [Quantum-resistant Root Program](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) recentemente anunciado pelo Chrome.

Ainda não estamos emitindo certificados, e levará um tempo até que o façamos. O que estamos fazendo é assumir publicamente o compromisso com esse trabalho, compartilhando os marcos à medida que são alcançados e dizendo exatamente o que estamos construindo enquanto trabalhamos com os programas raiz e outros membros da comunidade WebPKI para alcançar esse objetivo.

## **Dois caminhos para a confiança**

Uma raiz completamente nova não é amplamente útil por anos. Mesmo depois que um programa raiz a aceita, essa raiz precisa se propagar pelos sistemas operacionais, navegadores e dispositivos do mundo, e nunca alcança o grande conjunto de dispositivos que pararam de receber atualizações, ou que nunca as receberam. Essa longa cauda de clientes mais antigos é o ponto de origem de grande parte do tráfego de internet mundial, e onde reside um conjunto correspondentemente grande de falhas evitáveis. Acreditamos que todos os clientes merecem o mais alto nível de segurança possível, independentemente do fabricante, sistema operacional ou tempo desde a última atualização.

A aquisição de uma raiz existente com alto grau de cobertura nos repositórios de confiança de um conjunto diversificado de clientes resolve isso desde o primeiro dia. A raiz GlobalSign existente é reconhecida por navegadores, sistemas operacionais e dispositivos desde 2012, e alcança clientes mais antigos que uma raiz nova nunca alcançará. A nova raiz que submeteremos para inclusão nos programas de chave raiz foi construída para onde o ecossistema está indo, incluindo os programas que estão começando a limitar a idade máxima de uma raiz confiável. A raiz estabelecida nos dá alcance aos dispositivos do passado. As novas raízes nos dão posição sob as políticas do futuro. Queremos as duas para garantir que os certificados emitidos pela nossa AC ofereçam o mais amplo conjunto possível de compatibilidade com os clientes.

## **Uma nova fonte de certificados gratuitos**

O modelo de certificados gratuitos e automatizados agora sustenta a maior parte da web criptografada, e grande parte dela passa por um operador notável. A Let's Encrypt emite cerca de dez milhões de certificados por dia, atende mais de 500 milhões de sites e ultrapassou quatro bilhões de certificados ativos em 2025. É uma das melhores coisas que aconteceram à internet em vinte anos, e dizemos isso como um de seus maiores usuários.

Esse sucesso traz um risco sistêmico: se a autoridade certificadora gratuita dominante tivesse uma semana ruim, grande parte da web não teria nenhuma alternativa gratuita e automatizada comparável pronta para assumir a carga. No nível do pacote de certificados, passamos anos construindo exatamente esse tipo de redundância para nossos próprios clientes. Cada certificado Cloudflare Universal SSL já vem acompanhado de um certificado de backup, assinado com uma chave separada e emitido por uma autoridade diferente, pronto para ser implantado automaticamente caso o primário seja revogado ou comprometido. Uma AC pública é essa mesma ideia, mas na escala de toda a internet.

Para facilitar a adoção, seremos [ACME](https://www.globalsign.com/en/acme-automated-certificate-management)-first (Automated Certificate Management Environment), um protocolo padrão aberto amplamente aceito. A emissão e a renovação automatizadas via ACME serão a forma de obter um certificado conosco, o que significa que qualquer pessoa já apontada para qualquer AC gratuita existente pode migrar para nós simplesmente alterando uma URL de diretório, sem novas ferramentas e sem necessidade de rearquitetar nada.

## **As projeções de crescimento de certificados são enormes**

A Cloudflare está à frente de mais de vinte por cento do tráfego global de requisições da internet e encerra o TLS para milhões de domínios, dependendo de milhões de certificados por ano para isso. Provisionamos esses certificados por meio de múltiplas ACs, com caminhos primários e de backup para que os serviços dos clientes permaneçam ativos durante interrupções de ACs e eventos de revogação.

Isso nos ensinou não só como o ecossistema WebPKI funciona, mas também que ocasionalmente falha, do lado do consumidor, da maneira mais difícil. Lidamos com limites de taxa, casos extremos de validação, latência de revogação, construção de cadeia e atraso na distribuição de raiz. Vivenciamos a instabilidade das ACs dos últimos anos e a sentimos por meio de nossos clientes. Sabemos como a emissão confiável precisa parecer por fora, porque o tempo de atividade dos nossos clientes depende de sermos resilientes e responsivos quando um emissor tem um dia ruim.

E à medida que o [período máximo de validade dos certificados diminui](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/#ballot-contents) nos próximos anos, a atividade agêntica aumenta e os certificados PQ se tornam comuns, esperamos que o número bruto de certificados de que dependemos anualmente continue crescendo rapidamente, e não somos os únicos. Queremos não apenas resolver esse problema para nós mesmos, mas também fazer parte do fornecimento dessa utilidade para a internet e garantir que a cadeia de fornecimento de certificados para nossos clientes tenha ainda mais provedores.

## **Design para a resiliência: transparência e "fail small"**

Ao assumir essa nova responsabilidade de ser nossa própria AC, nos comprometemos a construir a AC mais confiável e resiliente possível. Pretendemos construir uma autoridade certificadora cuja confiabilidade não dependa apenas de evitar erros, mas que, assim como o restante dos produtos da Cloudflare, pratique o "fail small" e limite o impacto de qualquer problema.

Isso significa instituir processos para projetar e testar a recuperação antes que qualquer incidente ocorra. Como exemplo, tornaremos a automação de renovação uma condição para a emissão. Emitiremos apenas para clientes que suportem [ACME Renewal Information](https://www.rfc-editor.org/info/rfc9773/) (ARI), padronizado na RFC 9773. Os assinantes devem manter uma automação que consulte nosso endpoint de renovação, aja nas janelas de renovação que publicamos e identifique o certificado que está substituindo.

Também estamos aprendendo com o que observamos ao longo dos últimos 16 anos. Vimos autoridades certificadoras presas entre a revogação oportuna e manter os sites dos assinantes on-line porque muitos assinantes não conseguiam substituir seus certificados com rapidez suficiente. Quando os certificados precisam ser descontinuados, seja por um problema de conformidade ou um incidente de segurança, podemos antecipar as janelas de renovação dos certificados afetados, distribuir as substituições ao longo do tempo disponível e acompanhar a emissão de substituições.

Este é apenas um dos muitos aspectos da forma como pretendemos desenvolver. Seremos transparentes com nossa pilha de emissão e operações, publicaremos desenvolvimentos reproduzíveis do software que assina certificados, atestaremos os módulos de segurança de hardware que guardam nossas chaves e administraremos um painel público para a integridade da emissão e incidentes. As auditorias são pontuais e indicam que uma AC passou, não como ela funciona em uma terça-feira comum. Queremos que os programas raiz, pesquisadores e proprietários de sites comuns acompanhem como uma AC moderna realmente opera entre as auditorias.

## **Uma autoridade certificadora para a internet pós-quântica**

Também pretendemos liderar para onde os certificados vão, não apenas onde estão agora. Planejamos ser uma das primeiras ACs a emitir Merkle Tree Certificates (MTCs) em produção, com os primeiros certificados emitidos no primeiro trimestre de 2027.

Os MTCs são uma forma nova e muito mais compacta de entregar certificados de confiança pública, projetados para um mundo pós-quântico em que as cadeias de certificados tradicionais crescem o suficiente para sobrecarregar os handshakes TLS. Defendemos a [proposta baseada em padrões](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) para os MTCs no IETF, e no início deste ano, [o Chrome nomeou os MTCs](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) como o caminho preferido para a autenticação pós-quântica. Emiti-los em produção nos permite proteger os clientes da Cloudflare, bem como a internet em geral, contra a ameaça pós-quântica, com volume real por trás de uma transição que toda a web precisa realizar. Compartilhamos muito mais sobre os MTCs e como será essa nova Infraestrutura de Chaves Públicas (PKI) da web [em uma publicação do blog sobre o tema](http://blog.cloudflare.com/pq-ca-with-mtcs).

Não esperamos que essa transição seja repentina. Grande parte da internet continuará dependendo de certificados clássicos e da WebPKI existente por muitos outros anos. Mas ao longo desse período, esperamos que os MTCs ocupem uma parcela cada vez maior da emissão, e é por isso que estamos construindo um serviço que faz as duas coisas. Ao reunir certificados clássicos e Merkle Tree Certificates sob uma única AC, com um ciclo de vida e um conjunto de garantias, os clientes podem adotar no ritmo que lhes for conveniente e ajudar a web a fazer a travessia sem um corte abrupto. Os clientes não devem ter que escolher um lado em uma migração de várias décadas, operar dois sistemas ou reconstruir tudo quando o equilíbrio mudar.

## **Como sempre, a Cloudflare será o cliente zero**

Além de fornecer pacotes de certificados via Universal SSL para nossos clientes, a Cloudflare consome certificados de muitas ACs diferentes para operar nossos sistemas e operações internas. Assim como com nossos outros produtos, seremos o [cliente](https://www.cloudflare.com/the-net/top-of-mind-security/customer-zero/) zero da nova AC e seus certificados (tanto WebPKI quanto MTC), garantindo que todos os aspectos dos novos sistemas e processos atendam aos nossos altos padrões internos e que a infraestrutura da nossa AC seja exercida na escala da Cloudflare.

## **O que acontece a seguir**

Estamos avançando no processo de solicitação e aprovação com cada um dos principais programas de chave raiz da web. Esses processos acontecem de forma aberta, e compartilharemos mais atualizações conforme avançam, até os primeiros Merkle Tree Certificates no início de 2027. Se você quiser acompanhar esse trabalho ou ser um dos primeiros a usar um certificado da AC da Cloudflare no futuro, pode [se cadastrar para receber atualizações](http://cloudflare.com/resource/certificate-authority). E se quiser fazer parte da construção dessa nova capacidade dentro da Cloudflare, estamos [contratando](https://boards.greenhouse.io/cloudflare/jobs/8237801?gh_jid=8237801).

À medida que desenvolvemos essa nova capacidade, continuaremos a trabalhar em estreita colaboração com a rede de ACs públicas parceiras de que temos dependido por muitos anos (dezesseis!) enquanto todos trabalhamos juntos para garantir uma internet confiável e aberta.

Quando lançamos o Universal SSL, o argumento era simples: cada byte que flui criptografado pela internet torna mais difícil interceptar, limitar ou censurar, e a web aberta é algo que todos construímos juntos. Uma autoridade certificadora pública, redundante e transparente é esse mesmo argumento levado uma camada abaixo, até a confiança que torna possível a web criptografada em primeiro lugar. Trabalhamos em direção a isso por muito tempo, e estamos felizes de finalmente estar no caminho.

Feliz Birthday Week!

]]>01M4D4R8MW7TB70VYHZEQEZDB4Carta anual dos fundadores da Cloudflare, 2026https://blog.cloudflare.com/pt-br/cloudflares-2026-annual-founders-letter/ Thu, 08 Oct 2026 06:48:35 GMTA internet está mudando hoje mais do que em qualquer outro momento desde o lançamento da Cloudflare em 27 de setembro de 2010. À medida que o tráfego automatizado supera a atividade humana, refletimos sobre a ascensão dos agentes de IA, dos novos criadores e sobre como podemos ajudar a construir um futuro justo e sustentável para a web.AIBirthday WeekFounders' LetterPlataforma para desenvolvedoresTendências da internetEsta semana, a Cloudflare celebra seu 16º aniversário e, como muitos jovens de 16 anos atualmente, olhamos para o mundo em que crescemos com a sensação de estarmos entre o passado e o futuro. E assim como eles, às vezes enxergamos riscos diante de tantas mudanças. Mas, no geral, somos bastante otimistas quanto ao que está por vir. O que alimenta esse otimismo, assim como nossos receios, é a consciência de que a mudança sempre traz consigo rupturas.

A internet está mudando hoje mais do que em qualquer outro momento desde o lançamento da Cloudflare em 27 de setembro de 2010. Algumas destas mudanças parecem indiscutivelmente positivas, enquanto outras transformam drasticamente a forma com que entendemos a internet.

Uma das mudanças mais significativas diz respeito à velocidade de crescimento da web em si. De 2012 a 2025, a web estagnou e, por algumas métricas, até encolheu. Isso mudou em meados de 2025, com uma explosão de novos sites. A narrativa popular atribui esse crescimento ao conteúdo de baixa qualidade gerado por IA (AI slop) mas, embora exista um fundo de verdade nisso, não é apenas isso que observamos.

A IA deu origem a uma nova geração de criadores. Agora, pessoas com ideias, mas sem habilidade em programação conseguem dar vida a novas criações com o auxílio das chamadas ferramentas de "vibe coding". Nos orgulhamos do fato de que a maioria dessas ferramentas utiliza a plataforma para desenvolvedores da Cloudflare como destino de implementação. Afinal, o melhor aspecto da tecnologia é permitir que mais pessoas possam expressar sua criatividade. Temos o privilégio de estar na primeira fila vendo estudantes do mundo inteiro criando aplicativos para resolver problemas reais, e startups com novas ideias de negócio sendo construídas em tempo recorde. Hoje, mais de sete milhões de desenvolvedores estão construindo o futuro na plataforma para desenvolvedores da Cloudflare.

O último ano também mudou em termos de quem (e também o quê) usa a internet. Nossas projeções iniciais eram de que o tráfego automatizado ultrapassaria o tráfego humano no segundo semestre de 2027. A ascensão dos agentes e dos crawlers de IA antecipou essa data para maio de 2026. Se as tendências atuais continuarem assim, o que pode inclusive ser uma estimativa conservadora, o tráfego automatizado será mil vezes maior que o tráfego humano em apenas cinco anos. Não porque acreditemos que o tráfego humano vai diminuir, mas porque o tráfego gerado por agentes está explodindo.

Para quem os usa, esses agentes de IA já são impressionantes. Peça a um que encontre uma passagem aérea, um prestador de serviços ou um plano de celular mais barato, e ele lerá mais páginas em um minuto do que você conseguiria em uma tarde, para então voltar com uma resposta. Ele faz o trabalho por você.

Mas esse trabalho não é gratuito. Se você pedir ao seu agente de IA que sugira um lugar para almoçar, ele pode analisar mil cardápios de restaurantes da região para sugerir apenas um. Aquele restaurante pode conquistar sua preferência, mas os outros 999 tiveram que arcar com o custo de atender ao agente sem receber nada em troca. O risco aqui é o de uma tragédia dos comuns: os usuários que se beneficiam dos agentes de IA e de seu tráfego não assumem os custos da carga que impõem ao sistema e, por isso, não exercem a moderação adequada.

A IA tornou mais fácil do que nunca para estudantes e startups criarem algo. Os agentes de IA podem tornar muito mais difícil para qualquer pessoa encontrar essas criações. Hoje, pequenas empresas conquistam clientes com emoção ou conveniência. Você frequenta certo mercadinho porque a pessoa no balcão lembra seu nome ou porque isso faz parte de como você se define. Ou compra em uma loja local mesmo sabendo que ela não tem a melhor seleção ou os melhores preços, mas ela fica no caminho de volta para casa.

Seu agente de IA não se importa com quem lembra seu nome, e ele não passa em frente à loja local. Ele escolhe o que tem mais informações disponíveis, e isso geralmente é quem está no mercado há mais tempo. O risco, então, é que, à medida que os agentes gerenciam cada vez mais transações comerciais, eles dificultem ainda mais a entrada de novos entrantes. Isso, por sua vez, deve levar à consolidação e a um ambiente de negócios menos dinâmico.

Um dia, também fomos novos entrantes. Dezesseis anos atrás nesta semana, lançamos a Cloudflare no palco do TechCrunch Disrupt enquanto nossos engenheiros, na plateia, corrigiam falhas no sistema. Ainda havia oito para resolver quando subimos ao palco. Quando saímos, estavam corrigidas, e estávamos operando em cinco data centers em três continentes. Nenhum agente teria nos recomendado. Mesmo assim, as pessoas apostaram em nós. Queremos que os próximos novos entrantes tenham a mesma chance.

É por isso que lutamos. Não queremos um futuro com apenas cinco empresas de IA, mas um com quinhentas mil, espalhadas pelo mundo. Não queremos um cenário em que criadores de conteúdo definham e desaparecem porque não conseguem ser remunerados, mas um em que qualquer pessoa pode criar, alcançar um público global e ser paga pelo seu trabalho. E não queremos um mundo em que poucas megacorporações vencem por padrão, mas sim um em que novos entrantes com produtos melhores possam atender bem seus clientes, e vencer.

No ano passado, escrevemos sobre o que a IA estava fazendo com criadores de conteúdo. Este ano, a mesma transformação está chegando ao restaurante e ao mercadinho. O que vai substituir o antigo modelo de negócios da internet é a pergunta mais interessante dos próximos cinco anos e, esta semana, tentamos novamente respondê-la.

Como em todo aniversário, celebramos dando presentes em vez de recebê-los, e alguns desses presentes são para os 999 restaurantes. Os agentes percorrem a web da mesma forma que os mecanismos de busca sempre fizeram: tudo, repetidamente, independentemente de ter havido mudanças ou não. Nossos dados indicam que mais da metade do que os bots legítimos buscam não mudou desde a última visita. Temos trabalhado para que os crawlers vejam mais da web buscando apenas o que é novo, o que reduz a carga sobre os sites que percorrem. E estamos dando a qualquer pessoa que publique conteúdo ou aplicativos on-line uma forma de ser remunerada quando agentes usam o que ela criou.

A missão da Cloudflare não é construir uma internet melhor, mas ajudar a construir uma internet melhor, o que significa que não podemos fazê-lo sozinhos. Por isso, esta semana também anunciaremos parcerias com empresas e organizações que desejam o mesmo futuro que nós.

Como outros jovens de 16 anos nesta nova era da IA, temos a oportunidade de colocar nossas ideias em prática. Estamos fazendo isso para que a Internet ainda tenha espaço para um adolescente lançando seu primeiro aplicativo, para o mercadinho onde lembram do seu nome e para quem está construindo a próxima Cloudflare.

E nunca estivemos tão entusiasmados com isso.

]]>01M4D46JANM8AZJBEP90R6AWW5Desastres naturais e interferência governamental: examinando os principais eventos de interrupção da internet no segundo trimestre de 2026https://blog.cloudflare.com/pt-br/q2-2026-internet-disruption-summary/ Fri, 31 Jul 2026 06:46:50 GMTO Cloudflare Radar acompanhou as interrupções na internet causadas por desastres naturais, interrupções ordenadas por governos e trocas de chaves DNSSEC no último trimestre. Este post analisa a telemetria de tráfego para explicar como esses eventos impactaram a conectividade global.AWSInterrupçãoInterrupção da internetRadarTendências da internetTráfego da internetComo a maioria das infraestruturas, é fácil ignorar a fragilidade da internet, desde que esteja funcionando. Quando falha, sua complexidade fica evidente. A Cloudflare está em uma posição privilegiada para detectar e documentar os momentos em que um dos sistemas interconectados dos quais a internet depende, falha resultando em problemas de conectividade. A cada trimestre, resumimos as interrupções que detectamos e anotamos no [Cloudflare Radar](https://radar.cloudflare.com/pt-br). 

No segundo trimestre de 2026, o supertufão Sinlaku ao norte de Guam causou a interrupção mais longa, enquanto as interrupções ordenadas pelo governo no Sudão, durante os períodos de exame, foram as mais frequentes. O Irã restabeleceu o acesso nacional à internet, reconectando seus cidadãos à rede global após um blecaute de 88 dias, mesmo enquanto danos causados por ataques de drones continuavam a afetar a infraestrutura da AWS em outras partes da região. Finalmente, o rompimento de cabo em Santa Lúcia e a distribuição de assinaturas DNSSEC defeituosas na Alemanha destacaram a fragilidade da infraestrutura da internet, mas também a notável estabilidade que esses sistemas regionais e globais mantêm quando operam normalmente.

Aqui, vamos analisar as interrupções da internet mais significativas que observamos no segundo trimestre de 2026, baseando-nos nos dados de tráfego do Cloudflare Radar para mostrar como cada uma ocorreu e o que significou para os usuários locais. Como sempre, este é um resumo de interrupções notáveis e confirmadas, e não uma lista completa; uma visão mais completa das anomalias de tráfego detectadas está disponível no [Central de interrupções do Cloudflare Radar](https://radar.cloudflare.com/outage-center?dateStart=2026-04-01&amp;dateEnd=2026-06-30). 

## Desastres naturais e eletricidade causaram interrupções em Guam, na Venezuela e na Tanzânia

O super tufão Sinlaku, a tempestade mais forte da temporada de tufões do Pacífico de 2026, até o momento, deslocou-se pelas Ilhas Marianas em meados de abril, passando bem ao norte de Guam. Embora a ilha tenha escapado de um impacto direto, a tempestade trouxe ventos com força de tempestade tropical, causando interrupções de energia em Guam e afetando os sistemas de abastecimento de água, o que teve um impacto direto na conectividade da internet. O tráfego do território caiu até 80% em relação aos níveis esperados entre 13 e 14 de abril.

Dois meses depois, em 24 de junho, dois grandes terremotos atingiram o norte da Venezuela com cerca de um minuto de diferença entre si, em Yumare e San Felipe, seguidos por um tremor secundário perto da costa, nas imediações de Caracas. O primeiro terremoto de magnitude 7,5 ocorreu por volta das 22h04 UTC (18h04, horário local). O impacto imediato desses eventos pode ser observado no Radar, que mostra uma acentuada diminuição nos bytes HTTP transferidos no mesmo momento dos terremotos. Essa queda é particularmente visível na Fibex Telecom, que, de acordo com os [dados da APNIC](https://stats.labs.apnic.net/aspop/), tem 1,6 milhão de usuários estimados. A queda também é visível na [CANTV](https://radar.cloudflare.com/traffic/as8048?dateStart=2026-06-24&amp;dateEnd=2026-06-25#traffic-trends), a operadora estatal dominante e na [VNET](https://radar.cloudflare.com/traffic/as263703?dateStart=2026-06-24&amp;dateEnd=2026-06-25), um provedor de internet regional um pouco menor.

Do outro lado do Atlântico, apenas alguns dias depois, uma interrupção no fornecimento de energia na Tanzânia, em 27 de junho, causou uma queda acentuada no tráfego HTTP, que durou pelo menos cinco horas. Embora a causa tenha sido diferente daquela do apagão relacionado às eleições no país em outubro de 2025 (uma ação deliberada do governo em vez de uma falha de infraestrutura), o impacto na telemetria e nos usuários foi quase idêntico: uma perda drástica de conectividade que deixou os residentes incapazes de se comunicarem com seus entes queridos ou de acessar notícias críticas. 

É impressionante como eventos tão fundamentalmente diferentes deixam marcas tão semelhantes nos dados e na experiência dos usuários. Em conjunto, essas interrupções relacionadas ao clima e causadas por falhas no fornecimento de energia demonstram o imenso impacto que o mundo físico pode ter sobre o digital, e a importância da resiliência da internet e da construção de redes com redundância suficiente em energia, roteamento e rotas físicas para resistir a choques inevitáveis.

## Governos e geopolítica impactam a conectividade no Irã, nos Emirados Árabes Unidos, no Iraque e no Sudão

A partir de 26 de maio, o Radar começou a detectar sinais da previamente [anunciada](https://x.com/ir_aref/status/2059261258566877640?s=20) restauração da internet no Irã, marcando o possível fim de uma interrupção de 88 dias que deixou o país praticamente desconectado desde o seu início, em 28 de fevereiro. Em 27 de maio, o Radar [informou](https://blog.cloudflare.com/iran-internet-partially-restored-may-2026/) que o tráfego havia sido restabelecido para 40% dos níveis anteriores à interrupção, uma reabertura parcial consistente com relatórios de que o acesso estava sendo restabelecido de forma seletiva e não simultânea. Desde então, observamos os bytes HTTP subir para até 90% antes de estabilizar em aproximadamente 59% dos níveis anteriores à interrupção. Este volume é consistente com o tráfego que observamos em fevereiro, período entre esta interrupção recente e uma anterior em janeiro, sugerindo que a conectividade retornou a um patamar próximo à sua base de referência mais recente antes da interrupção mais recente, em vez de se normalizar completamente. Em nossa [análise sobre a Copa do Mundo de 2026](https://blog.cloudflare.com/2026-world-cup-internet-traffic/#streaming-makes-some-countries-appear-more-online), o Irã destacou-se como um ponto fora da curva: enquanto o tráfego na maioria dos países participantes oscilava conforme os horários das partidas, as leituras do Irã foram dominadas pelo contraste entre seus níveis após a restauração e a perda quase total de conectividade que a antecedeu.

Enquanto isso, o tráfego HTTP para me-central-1, uma região da nuvem AWS localizada nos Emirados Árabes Unidos, [permaneceu baixo](https://radar.cloudflare.com/cloud-observatory/amazon/me-central-1?dateRange=24w#http-traffic), alinhando-se com os [relatórios de serviço da AWS](https://health.aws.amazon.com/health/status#multipleservices-me-central-1_1777533954) em 30 de abril que indicavam que a região "sofreu danos devido ao conflito no Oriente Médio e atualmente não consegue oferecer suporte confiável às aplicações dos clientes." Esta atualização segue os relatórios de 3 de março, segundo os quais instalações tanto nos Emirados Árabes Unidos quanto no Bahrein “tiveram impactos físicos na infraestrutura como resultado de ataques de drones.” Nos Emirados Árabes Unidos, duas instalações foram "atingidas diretamente" e no Bahrein um ataque de drone próximo à instalação causou "impacto físico" em sua infraestrutura. A redução do tráfego é uma consequência direta dos danos físicos à infraestrutura subjacente do data center, em vez de uma falha na rede, e continua a afetar os sites e aplicativos hospedados naquela região, independentemente da disponibilidade individual de cada um deles.

O segundo trimestre de 2026 também registrou três interrupções ordenadas pelo governo no Iraque (nos dias [2](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-01&amp;dateEnd=2026-06-02), [11](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-10&amp;dateEnd=2026-06-11) e [28 de junho](https://radar.cloudflare.com/traffic/iq?dateStart=2026-06-27&amp;dateEnd=2026-06-28)), bem como [10 interrupções no Sudão](https://radar.cloudflare.com/traffic/sd?dateStart=2026-04-13&amp;dateEnd=2026-04-23#traffic-trends) entre 13 e 23 de abril, todas impostas para evitar fraudes em exames nacionais, um padrão sazonal que documentamos em vários trimestres anteriores em ambos os países. As interrupções no Sudão seguiram um ritmo consistente, cada uma durando aproximadamente três horas e meia, das 11h45 às 15h15 UTC (13h45 às 17h15, horário local), coincidindo com o horário de realização dos exames. No Iraque, as interrupções foram mais curtas, durando cerca de 90 minutos cada, e também foram programadas para coincidir com os horários de aplicação das provas.

Cada um desses exemplos, seja uma restauração ou uma interrupção, ilustra o controle significativo que os governos exercem sobre sua conectividade nacional e a facilidade com que o acesso pode ser desligado, restringido ou seletivamente reintroduzido como uma questão de política, e não de infraestrutura.

## Vulnerabilidades de infraestrutura afetaram usuários na Alemanha e em Santa Lúcia 

Em 5 de maio, uma troca de chaves DNSSEC no DENIC, o registro do domínio .de da Alemanha, [começou a gerar assinaturas inválidas](https://blog.denic.de/technische-storung-bei-de-domains-behoben/). Essas renovações de chaves consistem na substituição periódica das chaves criptográficas usadas para assinar os registros de DNS de uma zona; trata-se de uma tarefa de manutenção rotineira, porém crucial, visto que os resolvedores que validam o DNSSEC só confiam em respostas cujas assinaturas correspondam às chaves publicadas atualmente. Em outras palavras, se as assinaturas digitais não corresponderem aos valores esperados, o resolvedor assume que o site foi adulterado e bloqueia o acesso. Quando a geração de assinaturas inválidas começou, resolvedores com validação de DNSSEC em todo o mundo rejeitaram todas as solicitações para sites .de e retornaram erros do tipo SERVFAIL, até que a operação normal fosse restabelecida às 23h15 UTC (01h15 do dia 6 de maio, horário local). 

O Cloudflare Radar registrou um aumento no volume global de consultas a domínios .de durante a interrupção. Embora possa parecer contraintuitivo à primeira vista, isso ocorre porque respostas com falha não podem ser armazenadas em cache; assim, consultas que normalmente seriam atendidas silenciosamente a partir do cache precisaram ser resolvidas novamente e repetidas várias vezes, provocando um aumento acentuado no número de consultas.

Do ponto de vista do usuário, o incidente não foi percebido como uma falha de DNS ou criptográfica, mas simplesmente como uma onda de sites e serviços com domínio .de que, de repente, ficaram inacessíveis. Embora os usuários ainda conseguissem acessar sites que não utilizavam o TLD .de, a experiência incluiu falhas no carregamento de páginas, devolução de e-mails e esgotamento do tempo limite de aplicativos, situações que podem se assemelhar à experiência de uma interrupção. Você pode ler mais sobre DNSSEC e o impacto dos eventos [em nosso blog](https://blog.cloudflare.com/de-tld-outage-dnssec/).

No Caribe, uma falha de infraestrutura causou uma queda semelhante na disponibilidade. Em 21 de junho, o tráfego de solicitações HTTP da rede da Karib Cable caiu para praticamente zero por volta das 21h UTC (17h no horário local) e permaneceu baixo durante a maior parte do dia antes de retornar aos níveis esperados por volta das 17h UTC em 22 de junho (13h no horário local). [Segundo relatos](https://stluciatimes.com/181838/2026/07/flow-reveals-details-of-customer-rebates-after-major-outage/), a interrupção foi causada pelo rompimento de um cabo de fibra óptica próximo à ilha, um risco comum para redes do Caribe que dependem de poucas rotas terrestres e submarinas para se conectar à internet global, o que significa que uma única ruptura pode interromper uma parcela desproporcional da capacidade de transmissão. Como a Karib Cable é um dos maiores provedores, a perda também foi visível em nível nacional, com o tráfego geral de Santa Lúcia [caindo aproximadamente 60% em relação à semana anterior](https://radar.cloudflare.com/explorer?dataSet=netflows&amp;loc=LC&amp;dt=2026-06-21_2026-06-27&amp;timeCompare=1#result) durante o período da interrupção.

### O Radar continua monitorando interrupções

O segundo trimestre de 2026 registrou interrupções na Internet decorrentes de uma ampla variedade de causas, incluindo condições climáticas severas, terremoto, quedas de energia, interrupções ordenadas por governos, danos à infraestrutura de nuvem, rompimento de cabos e uma configuração incorreta de DNSSEC. Como esses eventos demonstram, a internet depende de um conjunto complexo de sistemas inter-relacionados, e uma falha em qualquer um deles pode resultar em perda de conectividade.

A equipe do Cloudflare Radar está constantemente monitorando as interrupções na internet, compartilhando nossas observações no [Central de interrupções do Cloudflare Radar](https://radar.cloudflare.com/outage-center), por meio das mídias sociais e em posts no [blog.cloudflare.com](http://blog.cloudflare.com). Siga-nos nas redes sociais em [@CloudflareRadar](https://twitter.com/CloudflareRadar) (X), [noc.social/@cloudflareradar](https://noc.social/@cloudflareradar) (Mastodon) e [radar.cloudflare.com](http://radar.cloudflare.com) (Bluesky).

]]>01KYVEFXN9RMEK2R3WA4ZAB8TJComemorando 12 anos do projeto Galileohttps://blog.cloudflare.com/pt-br/celebrating-12-years-of-project-galileo/ Thu, 18 Jun 2026 13:00:00 GMTPara marcar o 12º aniversário do Projeto Galileo, a Cloudflare publicou seu primeiro relatório abrangente analisando os ataques cibernéticos contra a sociedade civil.ImpactoProjeto GalileoHá doze anos, neste mês, a Cloudflare lançou um projeto ambicioso baseado em uma ideia simples: as pessoas não deveriam ser desconectadas da internet só porque alguém mais poderoso discorda delas. Hoje, o [projeto Galileo](https://www.cloudflare.com/galileo/) oferece acesso gratuito a serviços de segurança cibernética para mais de 3.400 sites pertencentes a jornalistas, defensores dos direitos humanos e outras organizações sem fins lucrativos em 120 países. [Continuamos](https://blog.cloudflare.com/protecting-free-expression-online/) acreditando que uma internet melhor é aquela em que qualquer pessoa com uma ideia possa alcançar um público global. 

Todos os anos, no aniversário do projeto Galileo, anunciamos novos produtos, programas e parcerias estratégicas. Para celebrar nosso 12º aniversário este ano, estamos publicando [nosso primeiro relatório abrangente](https://cfl.re/cyberattacks-against-civil-society-project-galileo-anniversary-report) sobre ataques cibernéticos direcionados à sociedade civil, divulgando [estudos de caso](https://www.cloudflare.com/project-galileo-case-studies/) que exploram as necessidades de segurança de 16 participantes do projeto Galileo e anunciando novos parceiros do projeto.

### Apresentamos um novo relatório anual sobre ataques cibernéticos contra a sociedade civil global

Como o projeto Galileo inclui agora 3.400 domínios pertencentes a organizações em mais de 120 países, a Cloudflare tem acesso a dados exclusivos sobre ameaças, ataques e tendências cibernéticas direcionadas à sociedade civil, um pilar fundamental da democracia global. Além disso, como a rede da Cloudflare abrange mais de 335 cidades em 125 países e mais de 20% da web está por trás dela, também conseguimos comparar os ataques direcionados à sociedade civil com aqueles que visam a internet de forma mais ampla. O relatório completo pode ser acessado [aqui](https://cfl.re/cyberattacks-against-civil-society-project-galileo-anniversary-report).

Os dados deste ano demonstram que as organizações da sociedade civil foram visadas com mais frequência, e muitas vezes com mais intensidade, do que outros usuários da internet. Os ataques cibernéticos muitas vezes coincidiram com momentos críticos no trabalho da sociedade civil, como a publicação de relatórios investigativos ou a realização de defesa pública. Nossas principais constatações incluem: 

  * Os ataques de DDoS foram a ameaça cibernética mais comum contra a sociedade civil. Sua característica definidora foi a duração, com alguns se estendendo por dias e semanas.
  * Grupos da sociedade civil enfrentaram tentativas de exploração de vulnerabilidades em seus sites a uma taxa sete vezes maior do que outros clientes da Cloudflare. As organizações de mídia foram afetadas de forma desproporcional.
  * Jornalistas que atuam no exílio enfrentaram uma taxa de tráfego malicioso quase quatro vezes maior do que a de organizações jornalísticas em geral. 
  * Quase 10% de todos os e-mails processados pela Cloudflare para a sociedade civil continham possível material de phishing. 



Concluímos nosso relatório com uma chamada à ação: garantir segurança cibernética simples e acessível para todos, ampliar a transparência sobre ataques cibernéticos e interrupções na internet e incorporar IA e proteções pós-quânticas em ferramentas de segurança por padrão. Esperamos que este relatório sirva como um recurso para a sociedade civil, formuladores de políticas e o público em geral que buscam entender e responder a ataques cibernéticos. Planejamos publicá-lo anualmente, o que nos permitirá comparar as tendências de ameaças cibernéticas ao longo do tempo. 

Além do relatório, a Cloudflare divulgou os seguintes [estudos de caso](https://www.cloudflare.com/project-galileo-case-studies/) qualitativos que contextualizam as necessidades de segurança de cada organização.

Organização| Descrição| País/Região de operação  
---|---|---  
SHARE Foundation| Organização sem fins lucrativos que defende a privacidade, a liberdade de expressão e outros direitos digitais.| Sérvia   
Hledaczvirat| Plataforma/banco de dados on-line para encontrar animais de estimação perdidos, conectando proprietários a abrigos de animais.| Checa, República  
Iran Watch / The Wisconsin Project| Projeto de pesquisa que acompanha as capacidades bélicas do Irã e questões de não proliferação, conduzido pelo Wisconsin Project on Nuclear Arms Control. | Estados Unidos   
Bulletin of the Atomic Scientists| Organização de mídia sem fins lucrativos que cobre risco nuclear, mudanças climáticas e tecnologia disruptiva. | Estados Unidos  
The Real Meteorologic Society| Sociedade para a ciência do clima e do tempo, que apoia a pesquisa em meteorologia, educação e acreditação profissional.| Reino Unido  
Project Ainita| Coletivo de engenharia que desenvolve ferramentas e pesquisas para organizações de direitos humanos, advogados e ativistas que operam em ambientes de alto risco.| Global  
Ukraine War Archive| Arquivo digital que documenta e preserva evidências de crimes de guerra e eventos da guerra entre a Rússia e a Ucrânia. | Ucrânia  
Our World in Data| Pesquisa e publicação de dados sobre questões globais como pobreza, saúde e clima. | Reino Unido   
Hague Institute for Innovation of Law| Centro de estudos e ação focado em sistemas de justiça acessíveis aos usuários e na resolução de problemas de justiça para pessoas em todo o mundo. | Países Baixos   
Center for American Progress| Centro de pesquisa e defesa de políticas públicas progressistas.| Estados Unidos  
Sea Shepherd Brasil| Capítulo brasileiro da Sea Shepherd, organização de conservação marinha que protege a vida selvagem e os ecossistemas oceânicos. | Brasil  
elTOQUE| Veículo de mídia digital independente cobrindo Cuba, incluindo notícias, economia e rastreamento de taxas de câmbio. | Global  
Humanitix| Plataforma de emissão de ingressos sem fins lucrativos que doa taxas de reserva para instituições de caridade de educação e saúde infantil. | Austrália   
Organized Crime and Corruption Reporting Project (OCCRP)| Rede global de jornalismo investigativo que expõe o crime organizado e a corrupção. | Países Baixos  
Activist Rights| Recurso de informações legais para ativistas sobre seus direitos e riscos legais durante protestos e campanhas. | Austrália  
China Digital Times| Site de notícias bilíngue cobrindo censura, direitos humanos e política na China. | Estados Unidos   
  
### Boas-vindas aos novos parceiros 

O projeto Galileo conta com seus 59 parceiros da sociedade civil para ser um sucesso. Cada organização que se inscreve no programa é analisada e aprovada por um desses parceiros. Esses grupos oferecem seu tempo e experiência, muitas vezes analisando várias inscrições por dia, para ajudar a garantir que nossos serviços cheguem às organizações que merecem. 

Ao longo do tempo, esses relacionamentos não apenas ajudaram a transformar o projeto Galileo no programa que é hoje, como também lançaram iniciativas totalmente novas, como nossa parceria de segurança de e-mail com a [Protect.ngo](https://protect.ngo/) (antigo CyberPeace Institute) ou nosso trabalho de apoio à medição da internet em escolas públicas por meio do [projeto Giga](https://www.cloudflare.com/press/press-releases/2025/cloudflare-partners-with-giga-to-accelerate-school-connectivity-worldwide/) da UNICEF.

Por vários anos, um dos objetivos do projeto Galileo tem sido alcançar mais organizações em regiões fora da América do Norte e da Europa. Parte desse esforço tem sido a participação em eventos regionais como a RightsCon na Costa Rica (2023) e em Taiwan (2025) para falar diretamente com organizações locais de direitos digitais. Também demos as boas-vindas a novos parceiros que trazem suas próprias redes e comunidades ativas para o programa. Por exemplo, no ano passado, anunciamos dois novos parceiros na região Ásia-Pacífico: a EngageMedia e a OpenCulture Foundation.

Devido aos novos serviços [que adicionamos recentemente](https://blog.cloudflare.com/ai-crawl-control-for-project-galileo/) ao projeto Galileo para ajudar organizações de notícias locais a proteger seu conteúdo contra crawlers de IA, o foco de nossa parceria este ano foram os grupos que atendem a jornalistas. Para isso, temos o orgulho de anunciar três novos parceiros:

Organização| Descrição| País/Região de operação  
---|---|---  
International Center for Journalists| Organização sem fins lucrativos focada na promoção de um jornalismo independente de alta qualidade. Oferece treinamento, parcerias, orientação e apoio financeiro a jornalistas e é especializada em ajudá-los a utilizar as tecnologias digitais. | Com sede nos Estados Unidos e apoiando jornalistas em mais de 180 países.  
Media Cluster Norway| Centro de inovação focado em tecnologia de mídia de última geração. Oferece espaços de pesquisa colaborativa, oportunidades de financiamento, incubação de negócios e eventos de rede para mais de 100 criadores e redações locais. | Noruega   
NGO-ISAC| Rede sem fins lucrativos focada em proteger a sociedade civil contra ameaças à segurança cibernética. Fornece inteligência contra ameaças, coordenação defensiva, treinamento e suporte à sua rede de mais de mil organizações sem fins lucrativos. | Estados Unidos   
  
### Continuar a proteger a sociedade civil em todo o mundo 

O novo relatório, os estudos de caso e os novos parceiros de hoje visam alcançar o objetivo fundamental do projeto Galileo: garantir que os ataques cibernéticos não silenciem as organizações que atuam em áreas vulneráveis e essenciais, como jornalismo e direitos humanos. 

Quando olhamos para o futuro, continuamos comprometidos em encontrar novas maneiras de expandir nossas proteções para grupos em risco em todo o mundo. Se sua organização busca proteção do projeto Galileo, acesse[ cloudflare.com/galileo](https://www.cloudflare.com/galileo/).

]]>1kBoofDb8dfLiYnekjlUaXApresentamos a pilha do Cloudflare One: implantação orientada por agenteshttps://blog.cloudflare.com/pt-br/cloudflare-one-stack/ Wed, 17 Jun 2026 13:00:00 GMTA pilha do Cloudflare One é uma biblioteca de habilidades de agentes que oferece a qualquer agente de IA o conhecimento necessário para planejar, implantar e gerenciar um ambiente Zero Trust, sem necessidade de chamadas de migração.AgentesCloudflare OneZero TrustAdotar ou migrar para uma arquitetura de rede Zero Trust pode ser uma tarefa complexa. Antes mesmo de qualquer alteração em uma política, as equipes precisam se lembrar de como sua rede está estruturada: quais aplicativos existem, seus mecanismos de autenticação e autorização, como o tráfego flui entre eles e quaisquer suposições feitas pela arquitetura atual. Esse processo prático exige que os profissionais decifrem a intenção por trás de cada política de segurança e roteamento em vigor.

Hoje, estamos lançando a pilha do Cloudflare One, um [conjunto de habilidades](https://github.com/cloudflare/skills) que você concede ao seu agente para configurar, implantar e gerenciar seu ambiente Zero Trust. Este kit de ferramentas foi projetado para ajudar a automatizar o processo de aprendizado de um conjunto de segurança totalmente novo e mapear o seu conjunto existente para a Cloudflare.

A Cloudflare já trabalhou com milhares de clientes exatamente nesse processo. Essa experiência repetida gerou conhecimento sobre onde as migrações encontram dificuldades, quais perguntas surgem com frequência e o que é necessário para avançar. A pilha do Cloudflare One reúne esse conhecimento e o torna mais acessível do que nunca. 

### A lacuna de agentes na segurança de rede

As equipes já estão usando agentes para escrever códigos, fazer triagem de alertas e automatizar fluxos de trabalho. As organizações estão solicitando cada vez mais as ferramentas fornecidas pela Cloudflare para ajudar os agentes a executar os fluxos de trabalho de segurança. Por si só, os agentes não são treinados nas nuances da topologia de rede específica de uma organização ou nas configurações de um fornecedor.

Ao fornecer orientação prescritiva e autoritativa, as organizações podem adicionar esse contexto ao kit de ferramentas existente para fazer melhor uso dos produtos de segurança que já estão implantando.

A Cloudflare é há muito tempo o fornecedor SASE mais fácil de implantar do mercado. A pilha estende essa filosofia aos agentes: ela fornece a eles o contexto, as ferramentas e o raciocínio estruturado de que precisam para operar em sua infraestrutura de segurança.

## O que é a pilha do Cloudflare One?

A pilha do Cloudflare One é [uma coleção de habilidades](https://github.com/cloudflare/skills) que podem ser usadas com qualquer agente. Como acontece com [qualquer habilidade](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), você pode usá-las de forma autônoma, em camadas em seu próprio contexto ou criar ferramentas por cima. Ela foi desenvolvida especificamente para ajudar os profissionais de segurança em todo o ciclo de vida de avaliação, implantação e gerenciamento do [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).

A pilha foi construída sintetizando o conhecimento selecionado manualmente de funcionários com dezenas de milhares de horas de experiência trabalhando com clientes em produtos Cloudflare One. Ela contém ferramentas para planejar, gerenciar e implementar a infraestrutura de segurança de usuários e agentes na Cloudflare. Ela também contém lógica escolhida a dedo para migrar de fornecedores legados, como [Zscaler](https://blog.cloudflare.com/descaler-program/) e Palo Alto Networks.

Quando usada em conjunto com o [servidor MCP em modo de código da Cloudflare](https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/), a pilha fornece aos agentes uma interface tipada para a API da Cloudflare. Os agentes podem consultar sua conta ativa, inspecionar configurações e fazer alterações por meio de um conjunto selecionado de fluxos de trabalho recomendados pela Cloudflare, em vez de chamadas de API ad hoc.

## O que está incluído na pilha?

A pilha do Cloudflare One é enviada como dois arquivos de habilidades leves: cloudflare-one e cloudflare-one-migration. Juntos, eles abrangem a migração, a criação de uma implementação, o gerenciamento e a solução de problemas de sua implantação do Cloudflare One:

  * **Acesso remoto e substituição de VPN** com o Cloudflare Access
  * **Segurança de usuários, redes, dispositivos e dados** com o Cloudflare Gateway
  * **Conectividade** com o Cloudflare Tunnel, Cloudflare Mesh e Cloudflare WAN
  * **Orientação sobre migração** com detalhes explícitos para migrar de outros fornecedores de SASE
  * **Interpretação e geração de diagramas de rede** , para que você possa visualizar as alterações propostas para sua rede de uma forma fácil de entender para você e sua equipe
  * **Tradução de conceitos de fornecedores** , que mapeia os conceitos entre fornecedores de SASE para reduzir a barreira na avaliação e troca de provedores
  * **Solução de problemas e operações** , com o kit de ferramentas Digital Experience Monitoring (DEX) e recomendações de regras automatizadas



## Como funciona

A pilha está disponível no repositório [Cloudflare Skills](https://github.com/cloudflare/skills). Todos os arquivos de habilidades contêm conhecimento estruturado, árvores de decisão e definições de ferramentas que os agentes carregam automaticamente quando o contexto corresponde. Forneça isso ao seu agente e deixe que ele ajude você a definir, configurar e gerenciar seu ambiente Zero Trust:

A habilidade cloudflare-one abrange orientações gerais sobre produtos. Por exemplo, se você perguntar a um agente a melhor maneira de substituir sua infraestrutura de VPN pelo Cloudflare Tunnel ou Cloudflare Mesh, a habilidade sabe como:

  1. Fazer inventário de aplicativos de VPN existentes e identificar qual modelo de conectividade cada um requer
  2. Mapear cada aplicativo para a primitiva Cloudflare apropriada, aplicativo Access auto-hospedado, serviço conectado ao Tunnel ou segmento de rede conectado ao Mesh
  3. Gerar uma sequência de implantação recomendada que minimize as interrupções durante a transição
  4. Produzir um resumo da configuração que sua equipe possa analisar antes de fazer qualquer alteração



A habilidade cloudflare-one-migration abrange a tradução de fornecedor para fornecedor. Por exemplo, se você solicitar a um agente que migre seus aplicativos do Zscaler Private Access para o Cloudflare Access, a habilidade saberá como:

  1. Mapear definições de aplicativos do Zscaler para definições de aplicativos do Cloudflare Access
  2. Transformar grupos de usuários e políticas do Zscaler em políticas do Cloudflare Access
  3. Usar a API da Cloudflare para criar os recursos equivalentes em sua conta
  4. Gerar um resumo do que foi migrado e do que requer análise manual



A lógica de migração na pilha é a mesma usada nos programas [Descaler](https://blog.cloudflare.com/descaler-program/) e [Deskope](https://blog.cloudflare.com/deskope-program-and-asdp-for-descaler/) da Cloudflare. Esses programas já migraram clientes corporativos do Zscaler e do Netskope para o Cloudflare One em horas, em vez de meses. A pilha disponibiliza esse recurso para qualquer cliente ou parceiro, a qualquer momento, sem precisar esperar por um agendamento prévio.

### Mais maneiras de usar a pilha

A pilha do Cloudflare One também pode:

  * Recomendar regras de segurança com base no tráfego observado em sua conta ativa
  * Migrar automaticamente seus aplicativos do Zscaler Private Access existentes para aplicativos auto-hospedados do Cloudflare Access
  * Investigar anomalias em logs HTTP de seu gateway seguro da web e criar regras para resolver os problemas que os usuários estão enfrentando
  * Gerar relatórios sobre a estabilidade de usuários com o kit de ferramentas DEX e tomar medidas para melhorar a latência de usuários em cenários importantes



Seja carregando a habilidade de um agente ou criando ferramentas personalizadas por cima, a pilha do Cloudflare One lida com todos esses casos de uso e muito mais.

## Para parceiros também

Embora isso simplifique o gerenciamento contínuo para clientes que já adotaram o conjunto de produtos Cloudflare One, também é uma ferramenta para a rede de parceiros da Cloudflare. Os parceiros podem usá-la para ajudar seus clientes a implantar mais rapidamente, gerenciar com mais eficiência, solucionar problemas com maior precisão e resolver problemas com mais facilidade.

## O que vem a seguir

Você pode começar a usar a pilha do Cloudflare One hoje mesmo. Para aproveitar ao máximo a pilha, combine-a com o [servidor MCP em modo de código](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode) da Cloudflare. O servidor MCP dá ao seu agente acesso em tempo real à API da Cloudflare por meio de uma interface única compactada que mantém as credenciais de autenticação fora do contexto do modelo. 

A pilha do Cloudflare One continuará a se expandir de acordo com a evolução dos produtos Cloudflare One. Novas habilidades para fontes de migração adicionais e fluxos de trabalho de solução de problemas mais avançados já estão em desenvolvimento.

À medida que aprendemos mais sobre como os clientes e parceiros utilizam esses arquivos de habilidades, planejamos desenvolver ferramentas mais robustas em torno dessas habilidades. Se você é cliente ou parceiro e quer compartilhar feedback sobre o que a pilha deve abordar a seguir, entre em contato com sua equipe de conta ou abra uma solicitação no repositório.

]]>1LDBKUul6cfW72f1DQaLyEProjeto Glasswing: o que o Mythos nos mostrouhttps://blog.cloudflare.com/pt-br/cyber-frontier-models/ Mon, 18 May 2026 06:00:00 GMTNas últimas semanas, utilizamos o Mythos e outros LLMs focados em segurança para analisar códigos ativos em partes críticas de nossa infraestrutura. Compartilhamos o que observamos, os pontos fortes e fracos dos modelos e o que precisa existir em torno deles para que tudo isso possa escalar.AgentesAIAutomaçãoCustomer ZeroEngenhariaGerenciamento de riscoInteligência contra ameaçasLLMOperações de ameaçasSegurançaNos últimos meses, testamos vários LLMs focados em segurança em nossa própria infraestrutura. Esses LLMs ajudam a identificar possíveis vulnerabilidades em nossos próprios sistemas, para que possamos corrigi-las e também nos mostram o que os invasores podem fazer com os modelos mais recentes.

Nenhum desses LLMs atraiu mais atenção do que o Mythos Preview, da Anthropic. Há algumas semanas, fomos convidados a usar o Mythos Preview como parte do [projeto Glasswing](https://www.anthropic.com/glasswing). Rapidamente o direcionamos para mais de cinquenta dos nossos próprios repositórios, para ver o que ele encontraria e entender como funciona. 

Este post compartilha o que observamos, os pontos fortes e fracos dos modelos e como a arquitetura e os processos em torno deles precisam ser alterados para que possam ser usados em larga escala.

## O que mudou com o Mythos Preview

O Mythos Preview é um verdadeiro avanço, e é importante afirmar isso claramente antes de qualquer outra coisa. Já faz algum tempo que executamos modelos em nosso código e o salto do que era possível com os modelos de fronteira de uso geral anteriores e o que o Mythos Preview faz hoje não é apenas um refinamento do que existia antes.

É um tipo diferente de ferramenta que realiza um tipo diferente de trabalho, e isso dificulta uma comparação direta com os modelos anteriores. Então, em vez de tentar comparar o Mythos Preview com modelos de fronteira de uso geral, é mais útil descrever o que ele realmente pode fazer, e dois recursos se destacaram no trabalho que realizamos com o Mythos Preview:

  * **Construção de cadeia de exploração -** Um ataque real raramente usa apenas uma falha. Ele encadeia várias primitivas de ataque pequenas em uma exploração funcional. Por exemplo, pode transformar uma falha de uso após liberação em uma primitiva de leitura e gravação arbitrária, desviar o fluxo de controle e usar sequências de programação orientada a retorno (ROP) para assumir controle total de um sistema. O Mythos Preview pode usar várias dessas primitivas e avaliar como combiná-las em uma prova funcional. A justificativa que ele apresenta ao longo do processo parece mais o trabalho de um pesquisador sênior do que a saída de um scanner automatizado.
  * **Geração de provas -** Encontrar uma falha e provar que ela é explorável são coisas diferentes, e o Mythos Preview pode fazer ambos. Ele escreve um código que aciona a falha suspeita, compila esse código em um ambiente de teste e o executa. Se o programa fizer o que o modelo esperava, essa é a prova. Caso contrário, o modelo lê a falha, ajusta sua hipótese e tenta novamente. O ciclo é tão importante quanto as falhas encontradas, porque uma suspeita de falha sem uma prova funcional é mera especulação, e o Mythos Preview preenche essa lacuna por conta própria.



Parte do que descrevemos acima não é exclusividade do Mythos Preview. Quando executamos outros modelos de fronteira no mesmo harness, eles encontraram um número considerável das mesmas falhas subjacentes e, em alguns casos, também avançaram mais do que esperávamos na parte de raciocínio. Onde eles falharam foi na integração das informações. Um modelo identificou uma falha interessante, escreveu uma descrição detalhada de sua importância e, em seguida, parou, deixando a cadeia real incompleta e a questão da explorabilidade em aberto. O que mudou com o Mythos Preview é que agora um modelo pode pegar essas falhas de baixa gravidade (que tradicionalmente ficariam invisíveis em uma lista de pendências) e encadeá-las em uma única exploração mais grave.

## Recusas do modelo em pesquisas legítimas de vulnerabilidades

O modelo Mythos Preview fornecido pela Anthropic, como parte do projeto Glasswing, não possuía as proteções adicionais que estão presentes em modelos geralmente disponíveis (como o Opus 4.7 ou o GPT-5.5).

Apesar disso, o modelo recusa organicamente certas solicitações. Assim como as capacidades cibernéticas que o tornam útil para a busca de vulnerabilidades, o modelo possui suas próprias salvaguardas emergentes que, às vezes, o levam a recusar solicitações legítimas de pesquisa de segurança. Mas, como descobrimos, essas recusas orgânicas não são consistentes. A mesma tarefa, formulada de maneira diferente ou apresentada em um contexto diferente, pode produzir resultados completamente diferentes, como ilustrado nos exemplos abaixo.

_Exemplo do Mythos Preview recusando a criação de uma prova de conceito funcional_

Por exemplo, o modelo inicialmente se recusou a fazer pesquisa de vulnerabilidades em um projeto, mas concordou em realizar a mesma pesquisa no mesmo código após uma alteração não relacionada no ambiente do projeto. Nada sobre o código que estava sendo analisado havia mudado.   
  
Em outro caso, o modelo encontrou e confirmou várias falhas sérias de memória em uma base de código, e então se recusou a escrever uma demonstração de exploração. A mesma solicitação, estruturada de maneira diferente, obteve uma resposta diferente, e até mesmo a mesma solicitação pode produzir resultados diferentes em execuções distintas devido à natureza probabilística do modelo. Tarefas semanticamente equivalentes podem produzir resultados opostos dependendo de como e quando são apresentadas ao modelo.

Isso é importante porque, embora as recusas/salvaguardas orgânicas do modelo sejam reais, elas não são consistentes o suficiente para servirem como uma barreira de segurança completa por si só. É precisamente por isso que qualquer modelo de fronteira cibernética capaz, em disponibilidade geral no futuro, deve incluir salvaguardas adicionais além desse comportamento básico, tornando-o apropriado para uso mais amplo fora de um contexto de pesquisa controlado como o Projeto Glasswing.

## O problema da relação sinal-ruído

Uma das partes mais difíceis da triagem de vulnerabilidades de segurança é decidir quais falhas são reais, quais são exploráveis e quais precisam ser corrigidas imediatamente. Esse já era um problema complexo mesmo antes da era da IA. Os scanners de vulnerabilidades com IA e o código gerado por IA pioraram a situação, e na Cloudflare criamos várias etapas de pós-validação para lidar com isso.

Dois fatores dominam a taxa de ruído:

  * **Linguagem de programação** \- C e C++ oferecem controle direto de memória e, com isso, classes de falhas - estouro de buffer, leituras e gravações fora dos limites - que linguagens com segurança de memória, como Rust, eliminam em tempo de compilação. Constatamos de forma consistente mais falsos positivos em projetos escritos em linguagens sem segurança de memória.
  * **Viés do modelo** \- Um bom pesquisador humano informa o que descobriu e o grau de confiança em suas descobertas. Os modelos não. Peça a um modelo para encontrar falhas, e ele as encontrará, mesmo que o código não tenha nenhuma. As descobertas retornam com ressalvas como "possivelmente", "potencialmente" ou "em teoria", e as descobertas com ressalvas superam em muito as descobertas concretas. Esse é um viés razoável para uma ferramenta exploratória. É um viés desastroso para uma fila de triagem, onde cada descoberta especulativa consome atenção humana e tokens para ser descartada, e esse custo se acumula ao longo de milhares de descobertas.



O Mythos Preview representa uma clara melhoria nesse aspecto, principalmente em sua capacidade de encadear primitivas, combinando múltiplas vulnerabilidades em uma prova de conceito funcional em vez de relatá-las isoladamente. Uma descoberta que chega com uma prova de conceito é uma descoberta sobre a qual você pode agir, e isso significa muito menos tempo gasto perguntando "isso é real mesmo?".

Nossos harnesses são deliberadamente ajustados para gerar excesso de alertas, assim conseguimos enxergar mais coisas (e deixar passar menos), embora isso também traga muito mais ruído. Mas no momento da triagem, o resultado do Mythos Preview tem uma qualidade visivelmente superior: menos descobertas com ressalvas, etapas de reprodução mais claras e menos trabalho para chegar a uma decisão de corrigir ou descartar.

## Por que apontar um agente de codificação genérico para um repositório não funciona

Quando começamos a pesquisa de vulnerabilidades assistida por IA no ano passado, nosso instinto foi o óbvio: apontar um agente genérico de codificação para um repositório arbitrário e pedir que ele descobrisse vulnerabilidades. Essa abordagem funciona, no sentido de que o modelo produzirá descobertas, mas não funciona para produzir uma cobertura significativa de uma base de código real e identificar descobertas valiosas. Há duas razões principais para isso:

  * **Contexto -** Os agentes de codificação são ajustados para um fluxo de trabalho específico: criar um recurso, corrigir uma falha, escrever uma reestruturação. Eles ingerem muito código-fonte, mantêm uma única hipótese por vez e iteram sobre ela. Esse formato é exatamente o errado para a pesquisa de vulnerabilidades, que é restrita e paralela por natureza. Um pesquisador humano escolhe um aspecto específico para analisar e o investiga minuciosamente. Esse aspecto pode ser um único recurso complexo, transições entre limites de segurança ou uma classe de vulnerabilidade específica, como injeções de comando, em que a entrada do invasor acaba sendo executada como um comando de shell. Em seguida, repetem o processo para um recurso, limite de segurança ou classe de vulnerabilidade diferente, milhares de vezes em todo o código-fonte. Uma única sessão de agente (mesmo com subagentes) em um repositório de cem mil linhas pode cobrir, talvez, um décimo de um por cento da superfície de forma útil antes que a janela de contexto do modelo se preencha e a compactação entre em ação, possivelmente descartando descobertas anteriores que seriam relevantes.
  * **Capacidade de processamento -** Um agente de fluxo único executa uma tarefa por vez, mas bases de código reais precisam de muitas hipóteses contra muitos componentes simultaneamente, com a capacidade de se expandir ainda mais quando algo interessante surge. Você pode exigir mais de um único agente, mas, em algum momento, você deixa de ser limitado pelo modelo e passa a ser limitado pela forma da própria interação. Usar o modelo diretamente em um agente de codificação é adequado para investigação manual quando um pesquisador já tem uma pista e deseja uma segunda opinião. No entanto, é a ferramenta errada para alcançar alta cobertura. Uma vez que aceitamos isso, paramos de tentar fazer o Mythos Preview executar a tarefa errada e começamos a construir o harness em torno dele.



## O que um harness realmente corrige

Quatro lições surgiram ao executar o trabalho em escala, e cada uma apontou para a necessidade de um harness que gerencie a execução geral:

  * **Escopo restrito produz descobertas melhores -** Dizer ao modelo "Encontre vulnerabilidades neste repositório" faz com que ele se disperse. Dizer a ele "Procure injeção de comando nesta função específica, com este limite de confiança sobre ela, aqui está o documento de arquitetura e aqui está a cobertura anterior dessa área" faz com que ele execute algo muito mais próximo do que um pesquisador realmente faria.
  * **Revisão adversarial reduz o ruído -** Adicionar um segundo agente entre a descoberta inicial e a fila, um com um prompt diferente, um modelo diferente e sem a capacidade de gerar suas próprias descobertas, captura muito do ruído que o primeiro agente perderia se apenas verificasse seu próprio trabalho. Acontece que colocar dois agentes em desacordo deliberado é muito mais eficaz do que apenas dizer a um agente para ter cuidado.
  * **Dividir a cadeia entre agentes produz um raciocínio melhor -** Perguntar "Este código está com falhas?" e "Um invasor pode realmente acessar essa falha de fora do sistema?" são duas perguntas diferentes, e o modelo se sai melhor em cada uma delas quando feitas separadamente, pois cada pergunta é mais específica do que a versão combinada.
  * **Tarefas paralelas específicas superam um único agente exaustivo -** A cobertura melhora quando vários agentes trabalham em perguntas com escopo restrito e eliminamos as duplicatas dos resultados posteriormente, em vez de pedir a um único agente que seja exaustivo.



Cada uma dessas observações diz respeito ao comportamento do modelo e, juntas, descrevem algo que não é mais uma interface de chat. É um harness que ajuda a alcançar os resultados finais. Os primeiros passos para construir um harness são simples, pois você pode pedir ao modelo para ajudar, que foi o que fizemos. Usamos o Mythos Preview para desenvolver, adaptar e aprimorar nossos harnesses originais para se adequar aos seus pontos fortes.  
  
Um exemplo de como um harness é na prática é descrito abaixo.

## Nosso harness de descoberta de vulnerabilidades

Veja como é o nosso harness de descoberta de vulnerabilidades, etapa por etapa. Ele foi utilizado para analisar o código ativo em nosso tempo de execução, caminho de dados na borda, pilha de protocolos, plano de controle e nos projetos de código aberto dos quais dependemos.

## O que isso significa para as equipes de segurança

A reação mais forte ao Mythos Preview de outros líderes de segurança tem sido sobre rapidez — escanear mais rápido, corrigir mais rápido, ciclo de resposta mais curto. Mais de uma equipe com que conversamos agora opera com um SLA de duas horas desde a divulgação da CVE até a correção em produção. O instinto é compreensível: quando o tempo do invasor diminui, o do defensor também precisa se diminuir. Ser mais rápido não será suficiente, e acreditamos que muitas equipes estão prestes a gastar muito tempo, esforço e dinheiro aprendendo isso da maneira mais difícil.

Corrigir mais rapidamente não altera a estrutura do pipeline que produz a correção. Se os testes de regressão levam um dia, não é possível alcançar um SLA de duas horas sem pular essa etapa, e as falhas que você lança quando pula os testes de regressão tendem a ser piores do que as falhas que estava tentando corrigir. Aprendemos algo parecido quando tentamos deixar o modelo gerar suas próprias correções e vimos algumas serem implementadas corrigindo a falha original, enquanto silenciosamente estragavam outra coisa da qual o código dependia.

A questão mais complexa é como deve ser a arquitetura em torno da vulnerabilidade. O princípio é dificultar a exploração para um invasor mesmo quando existe uma falha, de modo que o intervalo entre a divulgação de uma vulnerabilidade e sua correção seja menos relevante. Isso significa defesas que ficam na frente do aplicativo e impedem que a falha seja explorada. Significa projetar o aplicativo de modo que uma falha em uma parte do código não permita que um invasor tenha acesso a outras partes. Significa poder implementar uma correção em todos os locais onde o código está sendo executado simultaneamente, em vez de esperar que equipes individuais o implantem. 

Reconhecemos também que esse tema tem dois lados. As mesmas capacidades que nos ajudaram a encontrar falhas em nosso próprio código, em mãos erradas, podem acelerar os ataques contra todos os aplicativos na internet. A Cloudflare está à frente de milhões desses aplicativos, e os princípios arquitetônicos descritos acima são exatamente aqueles que nossos produtos são projetados para aplicar em nome dos clientes. Compartilharemos mais sobre o que isso significa para os clientes nas próximas semanas.

Se sua equipe realiza um trabalho semelhante e gostaria de trocar experiências, entre em contato conosco pelo endereço [security-ai-research@cloudflare.com](mailto:security-ai-research@cloudflare.com).

_Nossa pesquisa com o Mythos Preview foi conduzida em um ambiente controlado, utilizando nosso próprio código. Todas as vulnerabilidades identificadas durante esse trabalho foram triadas, validadas e corrigidas quando necessário, seguindo o processo formal de gerenciamento de vulnerabilidades da Cloudflare._

_Este trabalho foi um esforço de equipe. Agradecemos a Albert Pedersen, Craig Strubhart, Dan Jones, Irtefa Fairuz, Martin Schwarzl e Rohit Chenna Reddy por suas contribuições para a pesquisa, engenharia e análise deste post no blog._

]]>xrcYtr7kU54LNDB8MEmQYDesenvolvendo para o futurohttps://blog.cloudflare.com/pt-br/building-for-the-future/ Thu, 07 May 2026 20:15:12 GMTEsta tarde, enviamos o seguinte e-mail para nossa equipe global. Um dos nossos valores fundamentais na Cloudflare é a transparência, e acreditamos que é importante que vocês ouçam isso diretamente de nós porque é um momento importante na Cloudflare. A equipeEsta tarde, enviamos o seguinte e-mail para nossa equipe global. Um dos nossos valores fundamentais na Cloudflare é a transparência, e acreditamos que é importante que vocês ouçam isso diretamente de nós porque é um momento importante na Cloudflare. 

> _Equipe,_

> _Estamos escrevendo para informar você diretamente que tomamos a decisão de reduzir a força de trabalho da Cloudflare em mais de 1.100 funcionários globalmente._

> _A forma como trabalhamos na Cloudflare mudou fundamentalmente. Não apenas construímos e vendemos ferramentas e plataformas de IA, somos nosso cliente mais exigente. O uso de IA pela Cloudflare aumentou mais de 600% nos últimos três meses. Funcionários de toda a empresa, desde a engenharia até o RH, finanças e marketing, realizam milhares de sessões com agentes de IA todos os dias para concluir seu trabalho. Isso significa que devemos ser intencionais em como arquitetamos nossa empresa para a era da IA agêntica, a fim de potencializar o valor que entregamos aos nossos clientes e honrar nossa missão de ajudar a construir uma internet melhor para todos, em qualquer lugar._

> _Hoje é um dia difícil. Infelizmente, esta decisão significa dizer adeus a colegas que contribuíram significativamente para nossa missão e para transformar a Cloudflare em uma das empresas de maior sucesso do mundo. Queremos deixar claro que esta decisão não reflete o trabalho ou o talento individual daqueles que estão nos deixando. Em vez disso, estamos repensando todos os processos internos, equipes e funções em toda a empresa. As ações de hoje não são um exercício de redução de custos ou uma avaliação do desempenho individual. Elas representam a definição, pela Cloudflare, de como uma empresa de primeira classe e de alto crescimento opera e cria valor na era da IA agêntica_

>  _Este é um momento que precisamos assumir como fundadores e líderes da empresa. Matthew enviou pessoalmente todas as cartas de oferta que fizemos. É uma prática pela qual ele sempre teve grande apreço, pois representava nosso crescimento e o incrível talento que se juntava à nossa missão. Não nos pareceu certo que esta mensagem viesse de alguém além de nós dois. Em vez de enviar avisos aos poucos através dos gerentes, enviaremos e-mails para todos os funcionários._

> _Dentro da próxima hora, todos os membros da nossa equipe global receberão um e-mail nosso esclarecendo como essa mudança os afeta. Para aqueles que estão saindo hoje, enviaremos esta atualização tanto para seus endereços pessoais e da Cloudflare, para garantir que recebam a informação imediatamente._

> _É importante para nós tratar os membros da equipe que estão saindo de maneira adequada e de uma forma que supere o que já vimos em outras empresas. Acreditamos que agir com empatia não significa evitar decisões difíceis, mas sim como tratamos as pessoas quando essas decisões são tomadas. Se pedimos à nossa equipe que seja de primeira classe, temos a obrigação recíproca de sermos de primeira classe na forma como os tratamos. Estamos combinando a objetividade dessas medidas com pacotes de indenização que são líderes no setor. Os pacotes para os funcionários que deixarem a empresa incluirão o equivalente ao seu salário-base integral até o final de 2026. A cobertura de saúde é diferente ao redor do mundo e, se você estiver nos Estados Unidos, continuaremos a oferecer suporte até o final do ano. Também estamos concedendo ações aos membros da equipe que deixarem a empresa até 15 de agosto, para que recebam ações mesmo após a data de desligamento E, se os membros da equipe que deixarem a empresa ainda não tiverem atingido o período mínimo de aquisição de ações (primeiro ano de trabalho), vamos isentá-los desse período e conceder ações proporcionais até agosto também._

> _Pedimos à equipe que fizesse isso apenas uma vez, por mais difícil que seja hoje. Não queremos fazer isso novamente em um futuro próximo. Ao tomarmos medidas decisivas agora, proporcionamos clareza imediata aos que estão saindo e protegemos a estabilidade da equipe que permanece. Estamos implementando essas mudanças agora porque cortes menores e repetidos ou prolongar uma reorganização por vários trimestres gera incerteza emocional para os funcionários e impede nosso crescimento. É a coisa certa a fazer; é a coisa honesta a fazer; e reflete os valores da empresa que continuamos a construir._

> _A Cloudflare começou como uma empresa nativa digital, criada em nuvem. Isso nos permitiu alcançar e ultrapassar empresas que tinham uma vantagem de anos ou décadas, mas que foram prejudicadas por sistemas e processos obsoletos. Agora que nos tornamos líderes, não podemos nos acomodar com os fluxos de trabalho e estruturas organizacionais que funcionavam ontem. Temos certeza de que nossa organização reformulada será ainda mais ágil e inovadora à medida que continuamos a construir o futuro._

> _Àqueles que estão nos deixando: vocês ajudaram a construir a base sólida sobre a qual a Cloudflare se ergue hoje. Temos o máximo respeito pelo seu trabalho e gratidão pelo impacto que vocês causaram. Temos certeza de que vocês encontrarão outras grandes oportunidades e construirão muitas outras empresas de sucesso no futuro, levando consigo um conjunto único de habilidades adquiridas enquanto construíam a Cloudflare._

> _A transparência é um princípio fundamental na Cloudflare, e era importante que vocês soubessem disso por nós primeiro. Realizaremos nossa teleconferência de resultados às 14h PT, quando compartilharemos mais informações. Também planejamos abordar os anúncios de hoje ao vivo com a equipe em nossa reunião geral._

> _Não é um dia fácil, mas é a decisão certa. Nossa missão de ajudar a construir uma internet melhor é mais importante agora do que nunca, e ainda há muito trabalho a ser feito._

]]>4XKENJm0fq33smsBSmUIc5O "Code Orange: Fail Small" está concluído. O resultado é uma rede da Cloudflare mais fortehttps://blog.cloudflare.com/pt-br/code-orange-fail-small-complete/ Fri, 01 May 2026 21:07:30 GMTConcluímos um esforço enorme de engenharia para tornar nossa infraestrutura mais resiliente. Por meio de novas ferramentas como Snapstone e o Engineering Codex, implementamos mudanças de configuração mais seguras e automatizamos práticas recomendadas para evitar incidentes futuros.Código LaranjaInterrupçãoPost MortemNos últimos dois trimestres e pouco, realizamos um intenso esforço de engenharia, internamente conhecido como “[Code Orange: Fail Small](https://blog.cloudflare.com/fail-small-resilience-plan/)”, focado em tornar a infraestrutura da Cloudflare mais resiliente, segura e confiável para todos os nossos clientes.

No início deste mês, a equipe da Cloudflare concluiu este trabalho.

Embora aprimorar a resiliência nunca será um "trabalho concluído" e sempre será uma prioridade máxima em todo nosso ciclo de desenvolvimento, agora finalizamos o trabalho que teria evitado as interrupções globais de [18 de novembro de 2025](https://blog.cloudflare.com/18-november-2025-outage/) e [5 de dezembro de 2025](https://blog.cloudflare.com/5-december-2025-outage/).

Este trabalho se concentrou em diversas áreas-chave: alterações de configuração mais seguras, redução do impacto de falhas e revisão de nossos procedimentos de emergência e gerenciamento de incidentes. Também introduzimos medidas para impedir desvios e regressões ao longo do tempo e fortalecemos a maneira como nos comunicamos com nossos clientes durante uma interrupção.

Aqui, explicamos detalhadamente o que lançamos e o que isso significa para você.

### Alterações de configuração mais seguras

 _**O que isso significa para você** : na maioria dos casos, as mudanças internas de configuração da Cloudflare não chegam mais à nossa rede instantaneamente, em vez disso, são implementadas de forma progressiva, com monitoramento da integridade em tempo real. Isso permite que nossas ferramentas de observabilidade detectem problemas e revertam erros antes que eles afetem seu tráfego._

Para detectar implantações possivelmente perigosas antes que cheguem à produção, identificamos pipelines de configuração de alto risco e criamos novas ferramentas para gerenciar melhor as alterações de configuração.

Para produtos que são executados em nossa rede, processando tráfego de clientes e recebendo alterações de configuração, não implantamos mais essas alterações instantaneamente em toda a rede. Em vez disso, as equipes relevantes adotaram uma metodologia de "implantação mediada por integridade", a mesma [que usamos quando lançamos software](https://blog.cloudflare.com/safe-change-at-any-scale/), para todas as implantações de configuração. Isso inclui, entre outros, as equipes de produto que foram diretamente afetadas pelos incidentes.

No centro disso está um novo componente interno que chamamos de Snapstone, que criamos para trazer implantação mediada por integridade para alterações de configuração. O Snapstone é um sistema que agrupa alterações de configuração em um pacote e então permite a liberação gradual da alteração de configuração com princípios de mediação de integridade. Antes do Snapstone, aplicar essa metodologia à configuração era possível, mas difícil. Exigia um esforço significativo de cada equipe e não era aplicada de forma consistente em toda a rede. O Snapstone preenche essa lacuna, oferecendo uma forma unificada de implementar por padrão implantação progressiva, monitoramento de integridade em tempo real e reversão automática para implantações de configuração.

O que torna o Snapstone extremamente poderoso é sua flexibilidade. Em vez de ser uma correção para falhas passadas específicas, o Snapstone permite que as equipes definam dinamicamente qualquer unidade de configuração que precisa de mediação de integridade, seja um arquivo de dados, como o que causou a [interrupção de 18 de novembro](https://blog.cloudflare.com/18-november-2025-outage/), ou um indicador de controle em nosso sistema de configuração global como o envolvido na [interrupção de 5 de dezembro](https://blog.cloudflare.com/5-december-2025-outage/). As equipes criam essas unidades de configuração sob demanda, e o Snapstone garante a implantação segura em todos os lugares onde são usadas.

Isso nos proporciona algo que não tínhamos antes: quando uma análise de risco ou experiência operacional identifica um padrão de configuração perigoso, a correção é simples: trazê-lo para o Snapstone, e o padrão de configuração herda imediatamente a implantação segura. 

### Reduzir o impacto das falhas

 _**O que isso significa para você** : caso um problema seja detectado em nossa rede, nossos sistemas agora falham de forma mais controlada. Isso reduz drasticamente o raio de impacto em potencial, garantindo que seu tráfego seja entregue mesmo nos piores cenários._

As equipes de produtos revisaram cuidadosamente, de forma manual e por meio de programação, os modos de falha em potencial para produtos críticos para o atendimento do tráfego de clientes. As equipes removeram dependências de tempo de execução não essenciais e implementaram modos de falha melhores. Agora, usaremos a última configuração válida conhecida, sempre que possível ("falha obsoleta"), e, caso isso não seja possível, revisamos cada caso de falha e implementamos "falha aberta" ou "falha fechada", dependendo se o atendimento do tráfego com funcionalidade reduzida é preferível ao não atendimento.

Vejamos um exemplo de como isso funciona. A nossa interrupção de novembro de 2025 foi causada por uma falha na implementação do nosso classificador de aprendizado de máquina para detecção do Bot Management. De acordo com nossos novos procedimentos, se fossem gerados novamente dados que nosso sistema não pudesse ler, ele se recusaria a usar a configuração atualizada e, em vez disso, usaria a configuração antiga. Se a configuração antiga não estivesse disponível por algum motivo, ele entraria em "falha aberta" para garantir a continuidade do tráfego de produção dos clientes, o que é um resultado muito melhor do que tempo de inatividade.

Como resultado, se a mesma alteração no Bot Management, que causou a falha em novembro, fosse implementada agora, o sistema detectaria a falha em um estágio inicial da implantação, antes que ela afetasse mais do que uma pequena porcentagem do tráfego.

Também começamos a segmentar ainda mais nosso sistema, para que cópias independentes dos serviços sejam executadas para diferentes grupos de tráfego. A Cloudflare já utiliza esses grupos de clientes para mitigar o raio de impacto com técnicas de gerenciamento de tráfego e esse trabalho adicional de segmentação de processos oferece um poderoso recurso de confiabilidade para nós no futuro. 

Por exemplo, o sistema de tempo de execução do Workers é segmentado em vários serviços independentes que lidam com diferentes grupos de tráfego, com um deles lidando apenas com o tráfego de nossos clientes gratuitos. As alterações são implantadas nesses segmentos com base nos grupos de clientes, começando pelos clientes gratuitos. Também estamos enviando atualizações com mais rapidez e frequência para os segmentos menos críticos e em um ritmo mais lento para os segmentos mais críticos.

Como resultado, se uma alteração fosse implementada no sistema de tempo de execução do Workers e interrompesse o tráfego, agora, ela afetaria apenas uma pequena porcentagem de nossos clientes gratuitos antes de ser detectada e revertida automaticamente.

Continuando com o exemplo do sistema de tempo de execução do Workers, em um período de sete dias no início deste mês, o processo de implementação foi acionado mais de cinquenta vezes. É possível observar como cada um deles acontece em "ondas", à medida que a alteração se propaga para a borda, frequentemente em paralelo com as versões subsequentes e anteriores:

Estamos trabalhando para estender esse padrão de implantação para muitos dos nossos sistemas no futuro.

### Revisão dos procedimentos de emergência e de gerenciamento de incidentes

 _**O que isso significa para você?** : se ocorrer um incidente, temos as ferramentas e equipes necessárias para nos comunicar com mais clareza e resolvê-lo rapidamente, minimizando o tempo de inatividade._

A Cloudflare é executada na Cloudflare. Usamos nossos próprios produtos Zero Trust para proteger nossa infraestrutura, mas isso cria uma dependência: se uma interrupção em toda a rede afetar essas ferramentas, perdemos os próprios caminhos necessários para corrigi-las. Antes da iniciativa Code Orange, nossos caminhos de emergência eram restritos a um pequeno grupo de pessoas e ofereciam acesso limitado às ferramentas. Precisávamos que essas ferramentas e caminhos ficassem disponíveis de forma mais ampla durante uma interrupção.

Para resolver isso, realizamos uma auditoria abrangente das ferramentas essenciais para a visibilidade do sistema, depuração e alterações na produção. Por fim, desenvolvemos caminhos de autorização de backup para 18 serviços principais, compatíveis com novos scripts de emergência e novos proxies.

Durante o programa Code Orange, passamos da teoria à prática. Após exercícios em equipes pequenas, realizamos um simulado com toda a equipe de engenharia em 7 de abril de 2026, envolvendo mais de 200 membros da equipe. Embora a automação mantenha esses caminhos funcionais, treinamentos como esses garantem que nossos engenheiros tenham a memória muscular necessária para usá-los sob pressão.

Esse esforço também concentra-se no fluxo de informações. Quando a visibilidade interna é interrompida, nossa resposta a incidentes fica mais lenta e nossa capacidade de comunicação com o mundo externo é prejudicada. Historicamente, observações técnicas feitas no calor do momento nem sempre se traduziram em atualizações claras para nossos clientes.

Para superar essa lacuna, criamos uma equipe de comunicação dedicada para trabalhar em conjunto com os responsáveis pela resposta a incidentes durante eventos críticos. Enquanto nossos engenheiros praticavam seus procedimentos de emergência, essa equipe usou o programa Code Orange para aprimorar a frequência e a clareza das atualizações para os clientes. Ao garantir que temos tanto as ferramentas para visualizar quanto a estrutura para comunicar, podemos resolver incidentes mais rapidamente e manter nossos clientes melhor informados.

### Codificamos nossas melhorias

 _**O que isso significa para você** : lembramos dos aprendizados com nossos incidentes e codificamos as soluções. Nossa rede se tornará cada vez mais resiliente._

Para evitar desvios e a reintrodução de regressões ao trabalho realizado como parte do Code Orange ao longo do tempo, a equipe criou um Codex interno que solidifica todas as nossas diretrizes em regras claras e concisas.

O Codex agora é obrigatório para todas as equipes de engenharia e produto e se tornou parte central dos procedimentos internos da Cloudflare. Suas regras são aplicadas por meio de revisões de código com IA que destacam automaticamente qualquer instância que possa divergir das diretrizes, exigindo revisões manuais adicionais. Isso é aplicado sem exceção a toda a nossa base de código. O objetivo é simples: criar uma memória institucional que se auto impõe.

As interrupções de novembro e dezembro compartilharam um modo de falha comum: código que supunha que as entradas seriam sempre válidas, sem degradação gradual quando essa suposição falhava. Um serviço Rust chamou `.unwrap()` em vez de resolver um erro. O código Lua indexou um objeto que não existia. Ambos os padrões podem ser evitados se as lições forem aprendidas e aplicadas.

O Codex faz parte da nossa resposta. É um repositório vivo de padrões de engenharia escritos por especialistas em domínios por meio do nosso processo Request For Comments (RFC), que são depois usados para criar regras práticas. As práticas recomendadas que antes existiam apenas na mente de engenheiros seniores, ou eram descobertas somente após um incidente, agora se tornam conhecimento compartilhado e acessível a todos. Cada regra segue um formato simples: "Se precisar de X, use Y", com um link para o RFC que explica o motivo.

Por exemplo, um RFC agora afirma: "Não use `.unwrap()`" fora de testes e `build.rs.`" Outro captura um princípio mais amplo: "Os serviços DEVEM validar se as dependências upstream estão em um estado esperado antes do processamento."

Se essas regras tivessem sido aplicadas antes, as interrupções de novembro e dezembro teriam sido solicitações de mesclagem rejeitadas em vez de incidentes globais.

Regras sem aplicação são sugestões. O Codex se integra a agentes com tecnologia de IA em todas as etapas do ciclo de vida do desenvolvimento de software, desde a revisão do projeto até a implantação e a análise de incidentes. Isso desloca a aplicação para a esquerda, de "interrupção global" para "solicitação de mesclagem rejeitada". O raio de impacto de uma violação diminui de milhões de solicitações afetadas para um único desenvolvedor recebendo feedback acionável antes mesmo de seu código chegar à produção.

O Codex é um documento vivo e será continuamente aprimorado ao longo do tempo. Especialistas da área escrevem RFCs para codificar as melhores práticas. Os incidentes revelam lacunas que se tornam novos RFCs. Cada RFC aprovado gera regras para o Codex. Essas regras alimentam os agentes que analisam a próxima solicitação de mesclagem. É um ciclo virtuoso: a expertise se transforma em padrões, os padrões se transformam em aplicação e a aplicação eleva o padrão para todos.

### Não se trata apenas de código: a comunicação é fundamental

 _**O que isso significa para você** : a transparência é importante para nós. Se algo der errado, nos comprometemos a informar você em todas as etapas, para que possa se concentrar no que é importante._

As interrupções globais nos fizeram revisar nossos principais processos e abordagens culturais, indo além da engenharia e do desenvolvimento de produtos. Como parte das iniciativas mais amplas do Code Orange, introduzimos objetivos de nível de serviço (SLOs) adicionais para todos os nossos serviços, implementamos um registro de alterações global, integramos todas as equipes ao nosso sistema de coordenação de manutenção e aprimoramos a transparência em toda a empresa sobre a lista de pendências de tickets de "prevenção" de incidentes.

Também fortalecemos a maneira como nos comunicamos com nossos clientes durante uma interrupção. Nosso objetivo é alertar você sobre um problema no momento em que o confirmamos, antes mesmo que você perceba. Quando você notar uma lentidão ou um erro, nosso objetivo é que já haja uma atualização disponível em suas notificações.

Durante um incidente ativo, agora fornecemos atualizações em intervalos previsíveis (por exemplo, a cada 30 ou 60 minutos), mesmo que a atualização seja simplesmente "Ainda estamos testando a correção. Nenhuma alteração nova ainda." Isso permite que você planeje seu dia em vez de ficar atualizando constantemente uma página de status.

Nosso trabalho não acaba quando o status volta ao normal. Fornecemos relatórios pós-incidente detalhados explicando o que aconteceu, por que aconteceu e as mudanças estruturais específicas que estamos implementando para garantir que isso não se repita.

### Essa iniciativa está concluída. Mas nosso trabalho em resiliência nunca termina.

Levamos os incidentes muito a sério e adotamos uma responsabilidade compartilhada em toda a organização Cloudflare, perguntando a cada equipe: O que poderia ter sido feito melhor? Isso orientou o trabalho que realizamos nos últimos dois trimestres.

Embora esse trabalho nunca termine de fato, estamos confiantes de que estamos em uma posição muito melhor e que a Cloudflare está muito mais forte por causa disso.

]]>6EfXlJEx6OJ21w9NlnS59DNosso compromisso contínuo com a privacidade no resolvedor de DNS público 1.1.1.1https://blog.cloudflare.com/pt-br/1111-privacy-examination-2026/ Wed, 01 Apr 2026 13:00:00 GMTHá oito anos, lançamos o 1.1.1.1 para criar uma internet mais rápida e privada. Hoje, compartilhamos os resultados do nossa verificação independente mais recente. O resultado: nossas proteções de privacidade estão funcionando exatamente como prometido.1.1.1.1DNSPrivacidadeServiços ao consumidorTransparênciaHá exatamente 8 anos, [lançamos o resolvedor de DNS público 1.1.1.1](https://blog.cloudflare.com/announcing-1111/), com a intenção de criar o resolvedor [mais rápido](https://www.dnsperf.com/#!dns-resolvers) do mundo e o mais privado. Sabíamos que a confiança é tudo para um serviço que lida com a "lista telefônica da internet". E é por isso que, no lançamento, assumimos um compromisso único de confirmar publicamente que estamos fazendo o que dissemos que faríamos com os dados pessoais. Em 2020, [contratamos uma empresa independente para verificar nosso trabalho](https://blog.cloudflare.com/announcing-the-results-of-the-1-1-1-1-public-dns-resolver-privacy-examination/), em vez de apenas pedir que você confie em nossa palavra. Manifestamos nossa intenção de atualizar essas verificações no futuro. Também solicitamos que outros provedores fizessem o mesmo, mas, até onde sabemos, nenhum outro grande resolvedor público teve suas práticas de privacidade de DNS examinadas de forma independente.

No momento da análise de 2020, o resolvedor 1.1.1.1 tinha menos de dois anos e o objetivo da verificação era provar que nossos sistemas cumpriram todos os compromissos que assumimos sobre como nosso resolvedor 1.1.1.1 funcionava, até mesmo compromissos que não afetavam os dados pessoais ou a privacidade do usuário. 

Desde então, a pilha de tecnologia da Cloudflare cresceu significativamente em escala e complexidade. Por exemplo, [desenvolvemos uma plataforma totalmente nova](https://blog.cloudflare.com/big-pineapple-intro/) que alimenta nosso resolvedor 1.1.1.1 e outros sistemas de DNS. Portanto, sentimos que era vital analisar nossos sistemas, e em particular nossos compromissos de privacidade do resolvedor 1.1.1.1, mais uma vez com uma análise rigorosa e independente. 

Hoje, compartilhamos os resultados de nossa mais recente verificação de privacidade realizada pela mesma empresa de contabilidade do grupo Big 4. Sua verificação independente está disponível em nossa [página de conformidade](https://www.cloudflare.com/trust-hub/compliance-resources/).

Após a conclusão do ano civil de 2024, iniciamos nosso processo abrangente de coleta e preparação de evidências para nossos auditores independentes. A verificação levou vários meses e exigiu que muitas equipes da Cloudflare fornecessem evidências de apoio de nossos controles de privacidade em ação. Após a conclusão da verificação dos auditores independentes, temos o prazer de compartilhar o relatório final, que garante que nossos compromissos foram cumpridos: nossos sistemas são tão privados quanto prometemos. Mais importante, **nossas principais garantias de privacidade para o resolvedor 1.1.1.1 permanecem inalteradas e são confirmadas pela análise independente:**

  * **A Cloudflare não vende ou compartilha dados pessoais de usuários de resolvedores públicos com terceiros nem usa dados pessoais do resolvedor público para enviar anúncios a qualquer usuário.**
  * **A Cloudflare apenas retém ou usa o que está sendo solicitado, não informações que identifiquem quem está solicitando.**
  * **Os endereços de IP de origem são anonimizados e excluídos em 25 horas.**



Também queremos ser transparentes sobre dois pontos. Primeiro: como explicamos em [nosso blog de 2020, que anunciava os resultados de nossa verificação anterior,](https://blog.cloudflare.com/announcing-the-results-of-the-1-1-1-1-public-dns-resolver-privacy-examination/) pacotes de rede amostrados aleatoriamente (no máximo 0,05% de todo o tráfego, incluindo o endereço de IP de consulta dos usuários do resolvedor público 1.1.1.1) são usados exclusivamente para solução de problemas de rede e mitigação de ataques.

Em segundo lugar, o escopo dessa verificação se concentra exclusivamente em nossos compromissos com a privacidade. Em 2020, nossa primeira verificação analisou todas as nossas declarações, não apenas nossos compromissos com a privacidade, mas nossa descrição de como lidaríamos com transações anonimizadas e dados de log de depuração (“logs do resolvedor público”) para o funcionamento legítimo do nosso resolvedor público e para fins de pesquisa. Com o tempo, nossos usos desses dados para impulsionar ferramentas como o [Cloudflare Radar](https://radar.cloudflare.com/), que foi lançado após nossa verificação inicial do 1.1.1.1, mudaram a forma como tratamos esses logs, embora isso não afete as informações pessoais ou a privacidade individual. 

[Como observamos na primeira análise, há 6 anos](https://blog.cloudflare.com/announcing-the-results-of-the-1-1-1-1-public-dns-resolver-privacy-examination/): nunca quisemos saber o que as pessoas fazem na internet e tomamos medidas técnicas para garantir que não saibamos. Na Cloudflare, acreditamos que a privacidade deve ser o padrão. Ao nos submetermos proativamente a essas verificações independentes, esperamos definir um padrão para o restante do setor. Acreditamos que cada usuário, esteja ele navegando na web diretamente ou implantando um agente de IA em seu nome, merece uma internet que não rastreie seus movimentos. Além disso, a Cloudflare mantém firmemente o compromisso em nossa [Política de Privacidade](https://www.cloudflare.com/privacypolicy/) de que não combinaremos nenhuma informação coletada de consultas de DNS ao resolvedor 1.1.1.1 com quaisquer outros dados da Cloudflare ou de terceiros de qualquer forma que possa ser usada para identificar usuários finais individuais.

Como sempre, agradecemos por confiar no 1.1.1.1 para ser sua porta de entrada para a internet. Detalhes da verificação de privacidade do resolvedor 1.1.1.1 e o relatório do nosso contador podem ser encontrados na [página de recursos de de certificações e conformidade](https://www.cloudflare.com/trust-hub/compliance-resources/) da Cloudflare. Visite [https://developers.cloudflare.com/1.1.1.1/](https://developers.cloudflare.com/1.1.1.1/) para saber mais sobre como começar a usar o resolvedor de DNS mais rápido da internet e que prioriza a privacidade. 

]]>VOddnCi9jbM6zHOay1HCNO Cloudflare One é o primeiro SASE que oferece criptografia pós-quântica moderna em toda a plataformahttps://blog.cloudflare.com/pt-br/post-quantum-sase/ Mon, 23 Feb 2026 06:00:00 GMTAtualizamos o Cloudflare One para ser compatível com a criptografia pós-quântica, implementando os esboços mais recentes do IETF para ML-KEM híbrido em nosso produto Cloudflare IPsec. Isso estende a criptografia pós-quântica a todas as principais vias de acesso e de saída do Cloudflare One.Cloudflare OneCriptografiaIPsecPós-quânticoZero TrustDurante a Security Week 2025, lançamos o primeiro[ Gateway seguro da web (SWG) pós-quântico nativo em nuvem do setor e uma solução Zero Trust](https://www.cloudflare.com/press/press-releases/2025/cloudflare-advances-industrys-first-cloud-native-quantum-safe-zero-trust/), um grande passo para proteger o tráfego de rede corporativo enviado de dispositivos de usuários finais para redes públicas e privadas.

Mas isso é apenas parte da equação. Para realmente proteger o futuro das redes corporativas, você precisa de um [Serviço de acesso seguro de norda (SASE)](https://www.cloudflare.com/learning/access-management/what-is-sase/) completo. 

Hoje, completamos a equação: o Cloudflare One é a primeira plataforma SASE a oferecer suporte à criptografia pós-quântica (PQ) compatível com os padrões modernos em nosso Gateway seguro da web, e em casos de uso de Zero Trust e redes de longa distância (WANs). Mais especificamente, o Cloudflare One agora oferece ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism) híbrido pós-quântico em todas as principais vias de acesso e de saída.

Para completar a equação, adicionamos suporte para criptografia pós-quântica ao nosso [Cloudflare IPsec](https://developers.cloudflare.com/magic-wan/reference/gre-ipsec-tunnels/) (nossa WAN como serviço nativa de nuvem) e ao [Cloudflare One Appliance](https://developers.cloudflare.com/magic-wan/configuration/connector/) (nosso dispositivo de WAN físico ou virtual que estabelece conexões Cloudflare IPsec). O Cloudflare IPsec usa o protocolo [IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/) para estabelecer túneis criptografados da rede de um cliente para a rede global da Cloudflare, enquanto o IP [Anycast](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/) é usado para rotear automaticamente esse túnel para o data center da Cloudflare mais próximo. O IPsec da Cloudflare simplifica a configuração e oferece alta disponibilidade. Se um data center específico se tornar indisponível, o tráfego será redirecionado automaticamente para o data center íntegro mais próximo. O Cloudflare IPsec é executado na escala de nossa rede global e oferece suporte entre sites em uma WAN, bem como conexões de saída para a internet.

A atualização do [Cloudflare One Appliance](https://developers.cloudflare.com/magic-wan/configuration/connector/) está em disponibilidade geral a partir da versão do dispositivo 2026.2.0. A atualização do [IPsec da Cloudflare](https://developers.cloudflare.com/magic-wan/reference/gre-ipsec-tunnels/) está em beta fechado, e você pode solicitar acesso adicionando seu nome à nossa [lista de beta fechado](https://www.cloudflare.com/security-week/pq-ipsec-beta/).

## Criptografia pós-quântica é importante agora

As ameaças quânticas não são um problema da "próxima década". Veja por que nossos clientes estão priorizando a [criptografia pós-quântica (PQC)](https://www.cloudflare.com/learning/ssl/quantum/what-is-post-quantum-cryptography/) hoje:

**O prazo está se aproximando.** No final de 2024, o Instituto Nacional de Padrões e Tecnologia (NIST) enviou um [sinal claro](https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8547.ipd.pdf) (que foi [repetido](https://www.bsi.bund.de/EN/Service-Navi/Presse/Pressemitteilungen/Presse2024/241127_Post-Quantum_Cryptography.html) por outras [agências](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines)): a era da criptografia clássica de chave pública está chegando ao fim. O NIST estabeleceu o prazo até 2030 para descontinuar o RSA e a Elliptic Curve Cryptography (ECC) e [fazer a transição para a PQC](https://www.cloudflare.com/pqc/), que não pode ser quebrada por computadores quânticos poderosos. As organizações que ainda não iniciaram sua migração correm o risco de ficar fora de conformidade e vulneráveis à medida que o prazo se aproxima.

**Historicamente, as atualizações têm sido complicadas.** Embora 2030 possa parecer distante, atualizar algoritmos criptográficos é notoriamente difícil. A história nos mostrou que a descontinuação da criptografia pode levar décadas. Encontramos exemplos de [problemas causados pelo MD5 vinte anos após sua descontinuação](https://blog.cloudflare.com/radius-udp-vulnerable-md5-attack/). Essa falta de agilidade criptográfica, a capacidade de trocar facilmente algoritmos criptográficos, é um grande gargalo. Ao integrar a criptografia PQ diretamente ao [Cloudflare One](https://www.cloudflare.com/zero-trust/), nossa plataforma SASE, oferecemos agilidade criptográfica integrada, simplificando a forma como as organizações oferecem acesso remoto e conectividade entre sites.

**Os dados podem já estar em risco.** Por fim, "colher agora, descriptografar depois" é uma ameaça presente e persistente, em que os invasores coletam tráfego de rede sensível hoje e o armazenam até que os computadores quânticos se tornem poderosos o suficiente para descriptografá-lo. Se seus dados tiverem uma vida útil de mais do que alguns anos (por exemplo, informações financeiras, dados de saúde, segredos de estado), eles já estão em risco, a menos que sejam protegidas pela criptografia PQ.

### As duas migrações no caminho para a segurança quântica: acordo de chaves e assinaturas digitais

A transição do tráfego de rede para a criptografia pós-quântica (PQC) requer uma revisão de dois fundamentos criptográficos: acordo de chaves e assinaturas digitais. 

**Migração 1: estabelecimento de chave.** O acordo de chaves permite que duas partes estabeleçam um segredo partilhado através de um canal inseguro. O segredo compartilhado é então usado para criptografar o tráfego de rede, resultando em criptografia pós-quântica. O setor convergiu amplamente para o ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism) como o protocolo padrão de acordo de chaves PQ. 

O ML-KEM foi amplamente adotado para uso em [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/), geralmente implantado junto com o clássico Elliptic Curve Diffie Hellman (ECDHE), onde a chave usada para criptografar o tráfego de rede é derivada da combinação dos resultados dos acordos de chaves ML-KEM e ECDHE. (Isto também é conhecido como “ML-KEM híbrido”). Mais de [60% do tráfego TLS gerado por humanos](https://radar.cloudflare.com/adoption-and-usage#post-quantum-encryption) para a rede da Cloudflare é atualmente protegido por ML-KEM híbrido. A transição para o ML-KEM híbrido foi bem-sucedida porque:

  * interrompe ataques de "colher agora, descriptografar depois"
  * não requer hardware especializado ou conectividade física especializada entre cliente e servidor, ao contrário de abordagens como [distribuição quântica de chaves (QKD)](https://blog.cloudflare.com/you-dont-need-quantum-hardware/)
  * tem [pouco impacto no desempenho](https://blog.cloudflare.com/you-dont-need-quantum-hardware/), mesmo para conexões TLS de curta duração



Como o ML-KEM é executado em _paralelo_ com o ECDHE clássico, não há redução na segurança e na conformidade em comparação com a abordagem ECDHE clássica. 

**Migração 2: assinaturas digitais.** Enquanto isso, as assinaturas digitais e os certificados protegem a autenticidade, impedindo que adversários ativos se passem pelo servidor para o cliente. Infelizmente, as assinaturas de PQ são atualmente maiores em tamanho do que os algoritmos de ECC clássicos, o que retarda sua adoção. Felizmente, a migração para assinaturas PQ é menos urgente, porque elas são projetadas para impedir adversários ativos armados com computadores quânticos poderosos, que ainda não são conhecidos. Assim, embora a Cloudflare esteja contribuindo ativamente para a padronização e implementação de assinaturas digitais PQ, a atualização atual do IPsec da Cloudflare se concentra na atualização do estabelecimento de chaves para o ML-KEM híbrido. 

A Agência de Segurança Cibernética e de Infraestrutura (CISA) dos EUA reconheceu a natureza dessas duas migrações em sua [publicação de janeiro de 2026](https://www.cisa.gov/resources-tools/resources/product-categories-technologies-use-post-quantum-cryptography-standards), “Product Categories for Technologies That Use Post-Quantum Cryptography Standards”.

## Inovar com o IPsec 

Para obter um SASE totalmente protegido com criptografia pós-quântica, atualizamos nossos produtos Cloudflare IPsec para oferecer suporte ao ML-KEM híbrido no protocolo IPsec.

A jornada da comunidade IPsec em direção à criptografia pós-quântica tem sido muito diferente da do TLS. O [TLS](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/) é o padrão de fato para criptografar o tráfego da internet pública na camada 4, por exemplo, de um navegador para uma [rede de distribuição de conteúdo (CDN)](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/), portanto, segurança e interoperabilidade entre fornecedores são prioridades em seu design. Enquanto isso, o IPsec é um protocolo de camada 3 que geralmente conecta dispositivos desenvolvidos pelo mesmo fornecedor (por exemplo, dois roteadores), portanto, historicamente, a interoperabilidade tem sido uma preocupação menor. Com isso em mente, vamos dar uma olhada na jornada do IPsec rumo ao futuro quântico. 

### Chaves pré-compartilhadas? Distribuição de chaves quânticas?

A [RFC 8784](https://datatracker.ietf.org/doc/html/rfc8784), publicada em maio de 2020, foi concebida como a atualização pós-quântica do IPsec Internet Key Exchange v2 (IKEv2), usado para estabelecer as chaves simétricas utilizadas na criptografia do tráfego de rede IPsec. A RFC 8784 sugere a utilização de chaves pré-compartilhadas (PSK) de longa duração ou distribuição quântica de chaves (QKD). Nenhuma dessas abordagens é muito aceitável.

A RFC 8784 propõe a combinação de uma PSK com uma chave derivada da Diffie Hellman Exchange (DHE), essencialmente executando a PSK em um modo híbrido com a DHE. Essa abordagem protege contra invasores do tipo "colher agora, descriptografar depois", mas não oferece [sigilo de encaminhamento](https://blog.cloudflare.com/staying-on-top-of-tls-attacks/#forward-secrecy) contra adversários quânticos. 

O [sigilo de encaminhamento](https://blog.cloudflare.com/staying-on-top-of-tls-attacks/#forward-secrecy) é um requisito padrão dos protocolos de acordo de chaves. Ele garante que um sistema permaneça seguro mesmo se a chave de longa duração for vazada. A abordagem PSK na RFC 8784 é vulnerável a um adversário do tipo "colher agora, descriptografar depois" que também obtém uma cópia da PSK de longa duração e pode descriptografar o tráfego no futuro (quebrando o acordo de chaves DHE) assim que computadores quânticos poderosos estiverem disponíveis.

Para resolver este problema de sigilo de encaminhamento, a RFC 8.784 pode ser usada para combinar a chave da DHE clássica com uma chave gerada recentemente derivada de um protocolo de QKD.

A QKD usa a mecânica quântica para estabelecer uma chave criptográfica secreta e compartilhada entre duas partes. É importante ressaltar que para a QKD funcionar, as partes devem ter hardware especializado ou estar conectadas por uma conexão física dedicada. Esta é uma [limitação significativa](https://blog.cloudflare.com/you-dont-need-quantum-hardware/), tornando a QKD inútil para casos de uso comuns da Internet, como conectar um laptop a um servidor distante por Wi-Fi. Essas limitações também são o motivo pelo qual nunca investimos na implantação da QKD para o Cloudflare IPsec. A [Agência de Segurança Nacional (NSA)](https://www.nsa.gov/Cybersecurity/Quantum-Key-Distribution-QKD-and-Quantum-Cryptography-QC/) dos EUA, o [BSI da Alemanha](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Quantentechnologien-und-Post-Quanten-Kryptografie/quantentechnologien-und-post-quanten-kryptografie_node.html) e o [Centro Nacional de Segurança Cibernética do Reino Unido](https://www.ncsc.gov.uk/whitepaper/quantum-security-technologies) também alertaram contra confiar apenas na QKD.

### Mas e quanto à interoperabilidade? 

A [RFC 9370](https://datatracker.ietf.org/doc/html/rfc9370) foi lançada em maio de 2023, especificando o uso de um acordo de chaves híbrido em vez de PSK ou QKD. Mas, diferentemente do TLS, que só é compatível com o uso de ML-KEM pós-quântico em paralelo com a DHE clássica, esse padrão IPsec permite o uso de até _sete acordos de chaves diferentes para serem executados simultaneamente_ em paralelo com a Diffie Helman clássica. Além disso, não especifica detalhes sobre quais devem ser esses acordos-chave, deixando a cargo dos fornecedores a escolha de seus algoritmos e implementações. A Palo Alto Networks, por exemplo, levou isso a sério e criou suporte para mais de [sete conjuntos de cifras de PQC diferentes](https://docs.paloaltonetworks.com/compatibility-matrix/reference/supported-cipher-suites/cipher-suites-supported-in-pan-os-11-2/cipher-suites-supported-in-pan-os-11-2-ipsec) em seu next generation firewall (NGFW), a maioria dos quais não interopera com outros fornecedores e alguns dos quais ainda não foram padronizados pelo NIST.

Ao longo dos anos, o TLS foi na direção oposta, reduzindo o número de conjuntos de cifras registrados de centenas no TLS 1.2 para cerca de cinco no TLS 1.3. Essa filosofia de reduzir o "inchaço do conjunto de cifras" também está alinhada com o [SP 800 52](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf) do NIST de 2019. A justificativa para reduzir o "inchaço do conjunto de cifras" inclui: 

  * Interoperabilidade aprimorada entre fornecedores e regiões
  * Menor risco de ataques que exploram versões mais fracas do conjunto de cifras 
  * Menor risco de problemas de segurança devido a configurações incorretas
  * Menor risco de falhas de implementação, reduzindo o tamanho da base de código.



É por isso que inicialmente não criamos compatibilidade com a RFC 9370. 

### Padrões que, finalmente, estão no caminho certo

É também por isso que ficamos animados quando a comunidade IPsec apresentou o [draft-ietf-ipsecme-ikev2-mlkem](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/). Este internet-draft padroniza a troca de PQ para IPsec da mesma forma que a troca de chaves PQ tem sido amplamente implantada para TLS: ML-KEM híbrido. A nova versão preliminar preenche as lacunas da RFC 9370, especificando como executar o ML-KEM como troca de chaves adicional em paralelo com a Diffie-Hellman clássica no IKEv2. 

Agora que essa especificação está disponível, avançamos na compatibilidade com o IPsec pós-quântico em nossos produtos Cloudflare IPsec. 

## O Cloudflare IPsec agora é pós-quântico

O Cloudflare IPsec é uma solução WAN de [rede como serviço](https://www.cloudflare.com/learning/network-layer/network-as-a-service-naas/) que substitui arquiteturas de rede privada legadas conectando data centers, filiais e VPCs em nuvem à rede Anycast global da Cloudflare. 

Com o Cloudflare IPsec, a rede da Cloudflare atua como o [IKEv2](https://datatracker.ietf.org/doc/html/rfc5996) Responder, aguardando solicitações de conexão de um iniciador de IPsec, que é um dispositivo conector de filiais na rede do cliente. O Cloudflare IPsec é compatível com sessões IPsec iniciadas por conectores de filiais que incluem nosso próprio Cloudflare One Appliance, além de conectores de filiais de um [conjunto diversificado de fornecedores](https://developers.cloudflare.com/magic-wan/reference/device-compatibility/), incluindo Cisco, Juniper, Palo Alto Networks, Fortinet, Aruba e outros.

Implementamos o suporte híbrido de produção ML-KEM no Cloudflare IPsec IKEv2 Responder, conforme especificado em [draft-ietf-ipsecme-ikev2-mlkem](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/). O esboço requer uma primeira troca de chaves para ser executada usando uma troca de chaves Diffie Helman clássica. A chave derivada é usada para criptografar uma segunda troca de chaves que é executada usando ML-KEM. Por fim, as chaves derivadas das duas trocas são combinadas e o resultado é usado para proteger o tráfego do plano de dados no modo IPsec ESP (Encapsulating Security Payload). O modo ESP usa criptografia simétrica e, portanto, já é seguro em relação ao quântico sem nenhuma atualização adicional. Testamos nossa implementação em relação ao IPsec Initiator na implementação de referência [strongswan](https://strongswan.org/).

Você pode ver o conjunto de cifras usado na negociação IKEv2 visualizando os [logs do Cloudflare IPsec](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ipsec_logs/).

Optamos por implementar o ML-KEM híbrido em vez do ML-KEM "puro", ou seja, apenas ML-KEM sem DHE executada em paralelo, por dois motivos. Em primeiro lugar, usamos ML-KEM híbrido em todos os nossos outros produtos da Cloudflare, já que essa é a abordagem adotada em toda a comunidade TLS. Em segundo lugar, ele fornece uma segurança reforçada: o ML-KEM fornece proteção contra ataques quânticos "colher agora, descriptografar depois", enquanto a DHE fornece um algoritmo testado e comprovado contra adversários não quânticos.

### Um convite à interoperabilidade

O valor total desta implementação pode ser alcançado apenas por meio da interoperabilidade. Por esse motivo, estamos convidando outros fornecedores que estão desenvolvendo compatibilidade com IPsec Initiators em seus conectores de filiais, conforme [draft-ietf-ipsecme-ikev2-mlkem](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/), para testar nossa implementação do Cloudflare IPsec. Os clientes da Cloudflare que desejam testar a interoperabilidade com conectores de filiais de terceiros enquanto estamos no beta fechado podem [se inscrever aqui](https://www.cloudflare.com/security-week/pq-ipsec-beta/). Planejamos lançar a disponibilidade geral e desenvolver a interoperabilidade com outros fornecedores à medida que mais deles começarem a ficar on-line com compatibilidade com [draft-ietf-ipsecme-ikev2-mlkem](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/).

### Hardware seguro em relação ao quântico: o Cloudflare One Appliance

Muitos de nossos clientes adquirem seus conectores de filiais (hardware ou virtualizados) da Cloudflare, em vez de um fornecedor terceirizado. É por isso que o [Cloudflare One Appliance](https://developers.cloudflare.com/magic-wan/configuration/connector/), nosso dispositivo plug-and-play que conecta sua rede local ao Cloudflare One, também foi atualizado com criptografia pós-quântica.

O Cloudflare One Appliance não usa o IKEv2 para acordos de chaves ou estabelecimento de sessões, optando, em vez disso, por confiar no TLS. O dispositivo inicia periodicamente um handshake TLS com a borda da Cloudflare, compartilha um segredo simétrico sobre a conexão TLS resultante e, em seguida, injeta esse segredo simétrico na camada ESP do IPsec, que criptografa e autentica o tráfego do plano de dados IPsec. Esse design nos permitiu evitar a criação de lógica do IKEv2 Initiator e facilita a manutenção do conector usando nossas bibliotecas TLS existentes. 

Assim, atualizar o Cloudflare One Appliance para criptografia PQ foi apenas uma questão de atualizar o TLS 1.2 para o TLS 1.3 com ML-KEM híbrido, algo que fizemos muitas vezes em diferentes produtos na Cloudflare. 

### Como faço para ativar essa opção? E quanto custa?

Como sempre, essa atualização para o Cloudflare IPsec não tem nenhum custo extra para nossos clientes. Como acreditamos que uma internet segura e privada deve ser acessível a todos, estamos em uma missão de incluir a PQC em todos os nossos [produtos](https://blog.cloudflare.com/post-quantum-cryptography-ga/), sem [hardware especializado](https://blog.cloudflare.com/you-dont-need-quantum-hardware/), e sem [custo adicional](https://blog.cloudflare.com/post-quantum-crypto-should-be-free/) para nossos clientes e usuários finais.

Os clientes que usam o Cloudflare One Appliance obtiveram essa atualização para a PQC na versão 2026.2.0 (lançada em 11/02/2026). A atualização é implementada automaticamente (sem necessidade de ação do cliente) de acordo com a janela de interrupção configurada para cada dispositivo.

Para clientes que usam o Cloudflare IPsec com dispositivos de conexão de filiais de outro fornecedor, a interoperabilidade ocorrerá assim que o suporte para o [draft-ietf-ipsecme-ikev2-mlkem](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) estiver on-line. [Você também pode entrar em contato conosco](https://www.cloudflare.com/security-week/pq-ipsec-beta/) diretamente para obter acesso ao beta fechado e solicitar que interoperemos com o conector de filiais de um fornecedor específico.

## O panorama completo: SASE pós-quântico

A proposta de valor para um SASE pós-quântico é clara: as organizações podem obter proteção imediata de ponta a ponta para seu tráfego de rede privada enviando-o por meio de túneis protegidos por ML-KEM híbrido. Isso protege o tráfego de ataques do tipo "colher agora, descriptografar depois", mesmo que os aplicativos individuais na rede corporativa ainda não tenham sido atualizados para a PQC.

O diagrama acima mostra como o ML-KEM híbrido pós-quântico é oferecido em várias configurações de rede do Cloudflare One. Ele inclui as seguintes vias de acesso:

  * sem cliente ([TLS 1.3 com ML-KEM híbrido](https://blog.cloudflare.com/post-quantum-zero-trust/) [supondo que o navegador seja compatível com ML-KEM híbrido])
  * Cloudflare One Client ([MASQUE sobre TLS 1.3 com ML-KEM híbrido](https://blog.cloudflare.com/post-quantum-warp/) iniciado pelo cliente do dispositivo)
  * via de acesso ao Cloudflare IPsec (conforme descrito neste blog)



e as seguintes vias de saída:

  * Via de saída do Cloudflare Tunnel ([TLS 1.3 com túnel ML-KEM híbrido](https://blog.cloudflare.com/post-quantum-tunnel/) iniciado pelo cliente do dispositivo cloudflared)
  * Via de saída do Cloudflare IPsec (conforme descrito neste blog)



O diagrama abaixo destaca um exemplo de configuração de rede que usa a via de acesso do Cloudflare One Client para conectar um dispositivo a um servidor atrás de uma via de saída do Cloudflare One Appliance. O dispositivo do usuário final se conecta à rede da Cloudflare (link 1) usando [MASQUE com ML-KEM híbrido](https://blog.cloudflare.com/post-quantum-warp/). Em seguida, o tráfego viaja pela rede global da Cloudflare por meio de TLS 1.3 com ML-KEM híbrido (link 2). Em seguida, o tráfego sai da rede da Cloudflare por meio de um link Cloudflare IPsec pós-quântico (link 3) que termina em um dispositivo Cloudflare One Appliance. Por fim, ele se conecta a um servidor dentro do ambiente do cliente. O tráfego é protegido por criptografia pós-quântica enquanto viaja pela internet pública, mesmo que o próprio servidor não seja compatível com a criptografia pós-quântica.

Por fim, observamos que o tráfego que acessa o Cloudflare One e, em seguida, sai para a internet pública também pode ser protegido por nosso [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tls-decryption/#post-quantum-support) pós-quântico, nosso Gateway seguro da web (SWG). Aqui está um diagrama mostrando como o SWG funciona:

Conforme discutido em [um post anterior no blog](https://blog.cloudflare.com/post-quantum-zero-trust/#quantum-safe-swg-end-to-end-pqc-for-access-to-third-party-web-applications), nosso SWG já é compatível com o ML-KEM híbrido no tráfego do SWG para o servidor de origem (desde que a origem seja compatível com o ML-KEM híbrido) e no tráfego do cliente para o SWG (se o cliente for compatível com o ML-KEM híbrido, que é o caso da maioria dos navegadores modernos). É importante ressaltar que qualquer tráfego que acesse o SWG por meio de um dispositivo que tenha o Cloudflare One Client instalado ainda está protegido com ML-KEM híbrido, mesmo que o próprio navegador web ainda não seja compatível com criptografia pós-quântica. Isso se deve ao [túnel MASQUE pós-quântico](https://blog.cloudflare.com/post-quantum-warp/) que o Cloudflare One Client estabelece para a rede global da Cloudflare. O mesmo se aplica ao tráfego que acessa o SWG por meio de um túnel Cloudflare IPsec pós-quântico.

Em resumo, o Cloudflare One agora oferece criptografia pós-quântica em nossas vias de acesso e de saída TLS, MASQUE e IPsec, para tráfego de rede privada e para o tráfego que sai para a Internet pública por meio de nosso SWG. 

## O futuro está seguro em relação ao quântico

Ao completar a equação SASE pós-quântica com o Cloudflare IPsec e o Cloudflare One Appliance, estendemos a criptografia pós-quântica a todas as nossas principais vias de acesso e de saída. Escolhemos intencionalmente o caminho da interoperabilidade e da simplicidade, a abordagem híbrida ML-KEM que o IETF e o NIST defenderam, em vez de prender nossos clientes em implementações proprietárias, "inchaço do conjunto de cifras" ou atualizações de hardware desnecessárias. 

Esta é a promessa do Cloudflare One, uma plataforma SASE que não é apenas mais rápida e confiável do que as arquiteturas legadas que substitui, mas que fornece criptografia pós-quântica. Seja para proteger o navegador de um funcionário remoto ou um link de data center de vários gigabits, agora você pode fazer isso com a confiança de que seus dados estão protegidos contra ataques de "colher agora, descriptografar depois" e outras ameaças futuras. 

[Inscreva-se aqui](https://www.cloudflare.com/lp/pqc/) para obter uma demonstração completa de nossos recursos pós-quânticos na plataforma SASE Cloudflare One, ou [registre-se aqui](https://www.cloudflare.com/security-week/pq-ipsec-beta/) para entrar na lista do beta fechado do Cloudflare IPsec. Temos orgulho de liderar o setor nesta nova era da criptografia e convidamos você a se juntar a nós na construção de uma internet escalável, compatível com padrões e pós-quântica.

]]>4R1725ncbcxxmKyZueXmhwCódigo Laranja: Falhe Pequeno — nosso plano de resiliência após os incidentes recenteshttps://blog.cloudflare.com/pt-br/fail-small-resilience-plan-uk-ua/ Fri, 19 Dec 2025 22:35:30 GMTDeclaramos o "Código Laranja: Falhe Pequeno" para que todos na Cloudflare se concentrem em um conjunto de fluxos de trabalho de alta prioridade com um objetivo simples: garantir que a causa das nossas duas últimas interrupções globais nunca mais aconteça.Código LaranjaInterrupçãoPost MortemEm [18 de novembro de 2025](https://blog.cloudflare.com/18-november-2025-outage/), a rede da Cloudflare apresentou falhas significativas no fornecimento de tráfego de rede por aproximadamente duas horas e dez minutos. Quase três semanas depois, em [5 de dezembro de 2025](https://blog.cloudflare.com/5-december-2025-outage/), houve uma nova falha em fornecer tráfego para 28% dos aplicativos em nossa rede por cerca de 25 minutos

Publicamos posts de blog detalhados sobre os dois incidentes após a ocorrência, mas sabemos que precisamos nos esforçar mais para reconquistar a confiança de vocês. Hoje, estamos compartilhando detalhes sobre o trabalho em andamento na Cloudflare para evitar que interrupções como essas voltem a acontecer.

Nosso plano se chama “**Código Laranja: Falhe Pequeno** ” e reflete nosso objetivo de tornar a rede mais resiliente a erros ou falhas que possam levar a uma grande interrupção. Um "Código Laranja" significa que o trabalho nesse projeto tem prioridade. Para fins de contexto, declaramos um “Código Laranja” na Cloudflare [uma vez](https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/), após outro grande incidente que exigiu prioridade máxima de todos na empresa. Entendemos que os eventos recentes exigem a mesma atenção. O Código Laranja é a nossa forma de possibilitar que isso aconteça, permitindo que as equipes trabalhem de forma multifuncional conforme necessário para realizar o trabalho, enquanto pausam outras atividades.

O trabalho do Código Laranja está organizado em três áreas principais:

  * Exigir implementações controladas para qualquer alteração de configuração propagada na rede, da mesma forma que fazemos atualmente para lançamentos de binários de software.
  * Revisar, aprimorar e testar os modos de falha de todos os sistemas que lidam com o tráfego de rede para garantir que apresentem um comportamento bem definido em todas as condições, incluindo estados de erro inesperados.
  * Alterar nossos procedimentos internos de emergência* e remover dependências circulares para que nós e nossos clientes possamos agir rapidamente e acessar todos os sistemas sem problemas durante um incidente.



Esses projetos proporcionarão melhorias iterativas à medida que avançam, em vez de uma mudança radical ao final. Cada atualização individual contribuirá para maior resiliência na Cloudflare. Ao final, esperamos que a rede da Cloudflare seja muito mais resiliente, inclusive para problemas como aqueles que desencadearam os incidentes globais que tivemos nos últimos dois meses.

Entendemos que esses incidentes são problemáticos para nossos clientes e para a internet como um todo. Estamos profundamente constrangidos. É por isso que este trabalho é a prioridade número um para todos aqui na Cloudflare.

_***** Os procedimentos de emergência na Cloudflare permitem que certos indivíduos elevem seus privilégios, sob certas circunstâncias, para realizar ações urgentes e resolver cenários de alta gravidade._

## O que deu errado?

No primeiro incidente, usuários que visitavam o site de um cliente na Cloudflare visualizaram páginas de erro que indicavam que a Cloudflare não podia fornecer uma resposta à solicitação deles. No segundo caso, viram páginas em branco.

Ambas as interrupções seguiram um padrão semelhante. Nos momentos que antecederam cada incidente, uma alteração de configuração foi implantada instantaneamente em nossos data centers em centenas de cidades ao redor do mundo.

A alteração de novembro foi uma atualização automática do nosso classificador Bot Management. Executamos diversos modelos de inteligência artificial que aprendem com o tráfego que flui em nossa rede para criar detecções que identificam bots. Atualizamos constantemente esses sistemas para nos mantermos à frente de agentes mal-intencionados que tentam burlar nossa proteção de segurança e alcançar os sites dos clientes.

Durante o incidente de dezembro, enquanto tentávamos proteger nossos clientes de uma vulnerabilidade na popular estrutura de código aberto React, implementamos uma alteração em uma ferramenta de segurança utilizada por nossos analistas de segurança para aprimorar as assinaturas. Assim como a urgência das novas atualizações de gerenciamento de bots, precisávamos nos antecipar aos invasores que queriam explorar a vulnerabilidade. Essa alteração desencadeou o início do incidente.

O padrão expôs uma lacuna grave na forma como implantamos as alterações de configuração na Cloudflare, em comparação com a forma como lançamos as atualizações de software. Quando lançamos atualizações de versão de software, fazemos isso de forma controlada e monitorada. Para cada nova versão binária, a implantação deve concluir várias etapas com sucesso antes de poder atender ao tráfego mundial. Inicialmente, a implementação é feita no tráfego de funcionários, antes de implementarmos gradualmente a alteração para porcentagens crescentes de clientes em todo o mundo, começando com usuários gratuitos. Se detectarmos uma anomalia em qualquer fase, poderemos reverter a versão sem qualquer intervenção humana.

Essa metodologia não foi aplicada a alterações de configuração. Ao contrário do lançamento do software principal que alimenta nossa rede, quando fazemos alterações de configuração, estamos modificando os valores de como esse software se comporta. Podemos fazer isso instantaneamente. Também concedemos esse poder aos nossos clientes: se você fizer uma alteração em uma configuração na Cloudflare, ela se propagará globalmente em segundos.

Embora essa velocidade traga vantagens, ela também acarreta riscos que precisamos mitigar. Os dois últimos incidentes demonstraram que precisamos tratar qualquer alteração aplicada à forma como servimos o tráfego em nossa rede com o mesmo nível de cautela testada que aplicamos às alterações no próprio software.

## Vamos alterar a forma como implementamos as atualizações de configuração na Cloudflare

Nossa capacidade de implementar alterações de configuração globalmente em segundos foi o ponto fundamental em comum entre os dois incidentes. Em ambos os eventos, uma configuração incorreta derrubou a rede em segundos.

A introdução de implementações controladas da nossa configuração, assim como **_já fazemos_** para as versões de software, é o fluxo de trabalho mais importante do nosso plano Código Laranja.

As alterações de configuração na Cloudflare se propagam para a rede muito rapidamente. Quando um usuário cria um novo registro de DNS ou cria uma nova regra de segurança, ele atinge 90% dos servidores na rede em segundos. Isso é alimentado por um componente de software que chamamos internamente de Quicksilver.

O Quicksilver também é utilizado para qualquer alteração de configuração solicitada pelas nossas próprias equipes. A velocidade é um recurso: podemos reagir e atualizar globalmente o comportamento da nossa rede com muita rapidez. No entanto, em ambos os incidentes, isso causou uma alteração radical que se propagou para toda a rede em segundos, em vez de passar por gateways para testá-la.

Embora a capacidade de implementar alterações em nossa rede de forma quase instantânea seja útil em muitos casos, ela raramente é necessária. Estamos trabalhando para tratar a configuração da mesma forma que tratamos o código: introduzindo implementações controladas no Quicksilver para qualquer alteração de configuração.

Lançamos atualizações de software em nossa rede várias vezes ao dia por meio do que chamamos de sistema de Implantação Mediada por Saúde (HMD). Nessa estrutura, cada equipe da Cloudflare que possui um serviço (um componente de software implementado em nossa rede) deve definir as métricas que indicam se uma implementação foi bem-sucedida ou falhou, o plano de implementação e as medidas a serem tomadas caso não tenha havido sucesso.

Serviços diferentes terão variáveis ligeiramente diferentes. Alguns podem precisar de tempos de espera maiores antes de prosseguir para mais data centers, enquanto outros podem ter tolerâncias menores para taxas de erro, mesmo que isso cause sinais de falsos positivos.

Após a implantação, nosso kit de ferramentas HMD começa a progredir cuidadosamente de acordo com o plano, monitorando cada etapa antes de prosseguir. Se alguma etapa falhar, a reversão será iniciada automaticamente e a equipe poderá ser notificada, se necessário.

Ao final do Código Laranja, as atualizações de configuração seguirão o mesmo processo. Esperamos que isso nos permita detectar rapidamente os tipos de problemas que ocorreram nestes dois últimos incidentes, muito antes que se tornem problemas generalizados.

## Como abordaremos os modos de falha entre os serviços?

Embora estejamos otimistas de que um melhor controle sobre as alterações de configuração detectará mais problemas antes que se tornem incidentes, sabemos que erros podem e vão ocorrer. Nos dois incidentes, erros em uma parte da nossa rede tornaram-se problemas na maior parte da nossa pilha de tecnologia, incluindo o plano de controle que os clientes utilizam para configurar a forma como usam a Cloudflare.

Precisamos pensar em implementações cuidadosas e graduais, não apenas em termos de progressão geográfica (expandindo para mais dos nossos data centers) ou em termos de progressão da população (expandindo para funcionários e tipos de clientes). Também precisamos planejar implantações mais seguras que contenham falhas de progressão de serviço (que se propagam de um produto, como nosso serviço Bot Management, para um não relacionado, como nosso painel).

Para isso, estamos revisando os contratos de interface entre todos os produtos e serviços críticos que compõem nossa rede para garantir que vamos: a) **presumir que ocorrerão falhas** entre cada interface e b) lidar com essas falhas **da maneira mais razoável possível**. 

Voltando à falha do nosso serviço Bot Management, havia pelo menos duas interfaces importantes onde, se tivéssemos presumido que a falha iria acontecer, poderíamos ter lidado com ela de maneira adequada, de tal forma que seria improvável que qualquer cliente fosse impactado. A primeira era a interface que leu o arquivo de configuração corrompido Em vez de entrarmos em pânico, deveria haver um conjunto sensato de padrões validados que teriam permitido que o tráfego passasse pela nossa rede, enquanto teríamos, na pior das hipóteses, perdido o ajuste fino em tempo real que alimenta nossos modelos de aprendizado de máquina para detecção de bots.  
  
A segunda interface era entre o software principal que executa nossa rede e o próprio módulo do Bot Management. No caso de falha do nosso módulo do Bot Management (como ocorreu), não deveríamos ter descartado o tráfego por padrão. Em vez disso, poderíamos ter proposto, mais uma vez, um padrão mais sensato que permitisse a passagem do tráfego com uma classificação aceitável.

## Como podemos resolver emergências mais rapidamente?

Durante os incidentes, levamos muito tempo para resolver o problema. Em ambos os casos, a situação foi agravada pelos nossos sistemas de segurança, que impediram os membros da equipe de acessar as ferramentas necessárias para solucionar o problema. Além disso, em alguns casos, as dependências circulares nos atrasaram, pois alguns sistemas internos também ficaram indisponíveis.

Como uma empresa de segurança, todas as nossas ferramentas estão protegidas por camadas de autenticação com controles de acesso granulares para garantir a segurança dos dados de clientes e impedir o acesso não autorizado. Essa é a atitude correta, mas, ao mesmo tempo, nossos processos e sistemas atuais nos atrasaram quando a velocidade era uma prioridade máxima

As dependências circulares também afetaram a experiência do cliente. Por exemplo, durante o incidente de 18 de novembro, o Turnstile, nossa solução de bot sem CAPTCHA, ficou indisponível. Como usamos o Turnstile no fluxo de login do painel da Cloudflare, os clientes que não tinham sessões ativas ou tokens de serviço de API não conseguiram iniciar sessão na Cloudflare no momento em que mais precisavam para fazer alterações críticas.

Nossa equipe vai revisar e aprimorar todos os procedimentos e a tecnologia de emergência para garantir que, quando necessário, possamos acessar as ferramentas certas o mais rápido possível, mantendo nossos requisitos de segurança. Isso inclui revisar e remover dependências circulares, ou ser capaz de "contorná-las" rapidamente caso haja um incidente. Também aumentaremos a frequência dos nossos exercícios de treinamento para que os processos sejam bem compreendidos por todas as equipes antes de qualquer possível cenário de desastre no futuro. 

## Quando vamos terminar?

Embora não tenhamos abordado neste artigo todo o trabalho que está sendo realizado internamente, os fluxos de trabalho detalhados acima descrevem as principais prioridades nas quais as equipes devem se concentrar. Cada um desses fluxos de trabalho corresponde a um plano detalhado que atinge quase todas as equipes de produto e engenharia da Cloudflare. Temos muito trabalho a fazer.

Até o final do 1º trimestre, e em grande parte antes disso, nós vamos:

  * Garantir que todos os sistemas de produção sejam cobertos por Implantações Mediadas por Saúde (HMD) para gerenciamento de configuração.
  * Atualizar nossos sistemas para aderir aos modos de falha adequados para cada conjunto de produtos.
  * Garantir que tenhamos processos implementados para que as pessoas certas tenham o acesso certo para fornecer a remediação adequada durante uma emergência.



Alguns desses objetivos serão contínuos. Sempre precisaremos lidar melhor com as dependências circulares à medida que lançamos novos softwares. Nossos procedimentos de emergência precisarão ser atualizados para refletir como nossa tecnologia de segurança muda ao longo do tempo.

Falhamos com nossos usuários e com a internet como um todo nestes dois últimos incidentes. Temos trabalho a fazer para corrigir isso. Planejamos compartilhar atualizações conforme esse trabalho avança e agradecemos as perguntas e o feedback que recebemos dos nossos clientes e parceiros

]]>1kqIUPPp2ZuAxjAi7f6FWaCódigo Laranja: Falhe Pequeno — nosso plano de resiliência após os incidentes recenteshttps://blog.cloudflare.com/pt-br/fail-small-resilience-plan/ Fri, 19 Dec 2025 22:35:30 GMTDeclaramos o "Código Laranja: Falhe Pequeno" para que todos na Cloudflare se concentrem em um conjunto de fluxos de trabalho de alta prioridade com um objetivo simples: garantir que a causa das nossas duas últimas interrupções globais nunca mais aconteça.Código LaranjaInterrupçãoPost MortemEm [18 de novembro de 2025](https://blog.cloudflare.com/18-november-2025-outage/), a rede da Cloudflare apresentou falhas significativas no fornecimento de tráfego de rede por aproximadamente duas horas e dez minutos. Quase três semanas depois, em [5 de dezembro de 2025](https://blog.cloudflare.com/5-december-2025-outage/), houve uma nova falha em fornecer tráfego para 28% dos aplicativos em nossa rede por cerca de 25 minutos

Publicamos posts de blog detalhados sobre os dois incidentes após a ocorrência, mas sabemos que precisamos nos esforçar mais para reconquistar a confiança de vocês. Hoje, estamos compartilhando detalhes sobre o trabalho em andamento na Cloudflare para evitar que interrupções como essas voltem a acontecer.

Nosso plano se chama “**Código Laranja: Falhe Pequeno** ” e reflete nosso objetivo de tornar a rede mais resiliente a erros ou falhas que possam levar a uma grande interrupção. Um "Código Laranja" significa que o trabalho nesse projeto tem prioridade. Para fins de contexto, declaramos um “Código Laranja” na Cloudflare [uma vez](https://blog.cloudflare.com/major-data-center-power-failure-again-cloudflare-code-orange-tested/), após outro grande incidente que exigiu prioridade máxima de todos na empresa. Entendemos que os eventos recentes exigem a mesma atenção. O Código Laranja é a nossa forma de possibilitar que isso aconteça, permitindo que as equipes trabalhem de forma multifuncional conforme necessário para realizar o trabalho, enquanto pausam outras atividades.

O trabalho do Código Laranja está organizado em três áreas principais:

  * Exigir implementações controladas para qualquer alteração de configuração propagada na rede, da mesma forma que fazemos atualmente para lançamentos de binários de software.
  * Revisar, aprimorar e testar os modos de falha de todos os sistemas que lidam com o tráfego de rede para garantir que apresentem um comportamento bem definido em todas as condições, incluindo estados de erro inesperados.
  * Alterar nossos procedimentos internos de emergência* e remover dependências circulares para que nós e nossos clientes possamos agir rapidamente e acessar todos os sistemas sem problemas durante um incidente.



Esses projetos proporcionarão melhorias iterativas à medida que avançam, em vez de uma mudança radical ao final. Cada atualização individual contribuirá para maior resiliência na Cloudflare. Ao final, esperamos que a rede da Cloudflare seja muito mais resiliente, inclusive para problemas como aqueles que desencadearam os incidentes globais que tivemos nos últimos dois meses.

Entendemos que esses incidentes são problemáticos para nossos clientes e para a internet como um todo. Estamos profundamente constrangidos. É por isso que este trabalho é a prioridade número um para todos aqui na Cloudflare.

_***** Os procedimentos de emergência na Cloudflare permitem que certos indivíduos elevem seus privilégios, sob certas circunstâncias, para realizar ações urgentes e resolver cenários de alta gravidade._

## O que deu errado?

No primeiro incidente, usuários que visitavam o site de um cliente na Cloudflare visualizaram páginas de erro que indicavam que a Cloudflare não podia fornecer uma resposta à solicitação deles. No segundo caso, viram páginas em branco.

Ambas as interrupções seguiram um padrão semelhante. Nos momentos que antecederam cada incidente, uma alteração de configuração foi implantada instantaneamente em nossos data centers em centenas de cidades ao redor do mundo.

A alteração de novembro foi uma atualização automática do nosso classificador Bot Management. Executamos diversos modelos de inteligência artificial que aprendem com o tráfego que flui em nossa rede para criar detecções que identificam bots. Atualizamos constantemente esses sistemas para nos mantermos à frente de agentes mal-intencionados que tentam burlar nossa proteção de segurança e alcançar os sites dos clientes.

Durante o incidente de dezembro, enquanto tentávamos proteger nossos clientes de uma vulnerabilidade na popular estrutura de código aberto React, implementamos uma alteração em uma ferramenta de segurança utilizada por nossos analistas de segurança para aprimorar as assinaturas. Assim como a urgência das novas atualizações de gerenciamento de bots, precisávamos nos antecipar aos invasores que queriam explorar a vulnerabilidade. Essa alteração desencadeou o início do incidente.

O padrão expôs uma lacuna grave na forma como implantamos as alterações de configuração na Cloudflare, em comparação com a forma como lançamos as atualizações de software. Quando lançamos atualizações de versão de software, fazemos isso de forma controlada e monitorada. Para cada nova versão binária, a implantação deve concluir várias etapas com sucesso antes de poder atender ao tráfego mundial. Inicialmente, a implementação é feita no tráfego de funcionários, antes de implementarmos gradualmente a alteração para porcentagens crescentes de clientes em todo o mundo, começando com usuários gratuitos. Se detectarmos uma anomalia em qualquer fase, poderemos reverter a versão sem qualquer intervenção humana.

Essa metodologia não foi aplicada a alterações de configuração. Ao contrário do lançamento do software principal que alimenta nossa rede, quando fazemos alterações de configuração, estamos modificando os valores de como esse software se comporta. Podemos fazer isso instantaneamente. Também concedemos esse poder aos nossos clientes: se você fizer uma alteração em uma configuração na Cloudflare, ela se propagará globalmente em segundos.

Embora essa velocidade traga vantagens, ela também acarreta riscos que precisamos mitigar. Os dois últimos incidentes demonstraram que precisamos tratar qualquer alteração aplicada à forma como servimos o tráfego em nossa rede com o mesmo nível de cautela testada que aplicamos às alterações no próprio software.

## Vamos alterar a forma como implementamos as atualizações de configuração na Cloudflare

Nossa capacidade de implementar alterações de configuração globalmente em segundos foi o ponto fundamental em comum entre os dois incidentes. Em ambos os eventos, uma configuração incorreta derrubou a rede em segundos.

A introdução de implementações controladas da nossa configuração, assim como **_já fazemos_** para as versões de software, é o fluxo de trabalho mais importante do nosso plano Código Laranja.

As alterações de configuração na Cloudflare se propagam para a rede muito rapidamente. Quando um usuário cria um novo registro de DNS ou cria uma nova regra de segurança, ele atinge 90% dos servidores na rede em segundos. Isso é alimentado por um componente de software que chamamos internamente de Quicksilver.

O Quicksilver também é utilizado para qualquer alteração de configuração solicitada pelas nossas próprias equipes. A velocidade é um recurso: podemos reagir e atualizar globalmente o comportamento da nossa rede com muita rapidez. No entanto, em ambos os incidentes, isso causou uma alteração radical que se propagou para toda a rede em segundos, em vez de passar por gateways para testá-la.

Embora a capacidade de implementar alterações em nossa rede de forma quase instantânea seja útil em muitos casos, ela raramente é necessária. Estamos trabalhando para tratar a configuração da mesma forma que tratamos o código: introduzindo implementações controladas no Quicksilver para qualquer alteração de configuração.

Lançamos atualizações de software em nossa rede várias vezes ao dia por meio do que chamamos de sistema de Implantação Mediada por Saúde (HMD). Nessa estrutura, cada equipe da Cloudflare que possui um serviço (um componente de software implementado em nossa rede) deve definir as métricas que indicam se uma implementação foi bem-sucedida ou falhou, o plano de implementação e as medidas a serem tomadas caso não tenha havido sucesso.

Serviços diferentes terão variáveis ligeiramente diferentes. Alguns podem precisar de tempos de espera maiores antes de prosseguir para mais data centers, enquanto outros podem ter tolerâncias menores para taxas de erro, mesmo que isso cause sinais de falsos positivos.

Após a implantação, nosso kit de ferramentas HMD começa a progredir cuidadosamente de acordo com o plano, monitorando cada etapa antes de prosseguir. Se alguma etapa falhar, a reversão será iniciada automaticamente e a equipe poderá ser notificada, se necessário.

Ao final do Código Laranja, as atualizações de configuração seguirão o mesmo processo. Esperamos que isso nos permita detectar rapidamente os tipos de problemas que ocorreram nestes dois últimos incidentes, muito antes que se tornem problemas generalizados.

## Como abordaremos os modos de falha entre os serviços?

Embora estejamos otimistas de que um melhor controle sobre as alterações de configuração detectará mais problemas antes que se tornem incidentes, sabemos que erros podem e vão ocorrer. Nos dois incidentes, erros em uma parte da nossa rede tornaram-se problemas na maior parte da nossa pilha de tecnologia, incluindo o plano de controle que os clientes utilizam para configurar a forma como usam a Cloudflare.

Precisamos pensar em implementações cuidadosas e graduais, não apenas em termos de progressão geográfica (expandindo para mais dos nossos data centers) ou em termos de progressão da população (expandindo para funcionários e tipos de clientes). Também precisamos planejar implantações mais seguras que contenham falhas de progressão de serviço (que se propagam de um produto, como nosso serviço Bot Management, para um não relacionado, como nosso painel).

Para isso, estamos revisando os contratos de interface entre todos os produtos e serviços críticos que compõem nossa rede para garantir que vamos: a) **presumir que ocorrerão falhas** entre cada interface e b) lidar com essas falhas **da maneira mais razoável possível**. 

Voltando à falha do nosso serviço Bot Management, havia pelo menos duas interfaces importantes onde, se tivéssemos presumido que a falha iria acontecer, poderíamos ter lidado com ela de maneira adequada, de tal forma que seria improvável que qualquer cliente fosse impactado. A primeira era a interface que leu o arquivo de configuração corrompido Em vez de entrarmos em pânico, deveria haver um conjunto sensato de padrões validados que teriam permitido que o tráfego passasse pela nossa rede, enquanto teríamos, na pior das hipóteses, perdido o ajuste fino em tempo real que alimenta nossos modelos de aprendizado de máquina para detecção de bots.  
  
A segunda interface era entre o software principal que executa nossa rede e o próprio módulo do Bot Management. No caso de falha do nosso módulo do Bot Management (como ocorreu), não deveríamos ter descartado o tráfego por padrão. Em vez disso, poderíamos ter proposto, mais uma vez, um padrão mais sensato que permitisse a passagem do tráfego com uma classificação aceitável.

## Como podemos resolver emergências mais rapidamente?

Durante os incidentes, levamos muito tempo para resolver o problema. Em ambos os casos, a situação foi agravada pelos nossos sistemas de segurança, que impediram os membros da equipe de acessar as ferramentas necessárias para solucionar o problema. Além disso, em alguns casos, as dependências circulares nos atrasaram, pois alguns sistemas internos também ficaram indisponíveis.

Como uma empresa de segurança, todas as nossas ferramentas estão protegidas por camadas de autenticação com controles de acesso granulares para garantir a segurança dos dados de clientes e impedir o acesso não autorizado. Essa é a atitude correta, mas, ao mesmo tempo, nossos processos e sistemas atuais nos atrasaram quando a velocidade era uma prioridade máxima

As dependências circulares também afetaram a experiência do cliente. Por exemplo, durante o incidente de 18 de novembro, o Turnstile, nossa solução de bot sem CAPTCHA, ficou indisponível. Como usamos o Turnstile no fluxo de login do painel da Cloudflare, os clientes que não tinham sessões ativas ou tokens de serviço de API não conseguiram iniciar sessão na Cloudflare no momento em que mais precisavam para fazer alterações críticas.

Nossa equipe vai revisar e aprimorar todos os procedimentos e a tecnologia de emergência para garantir que, quando necessário, possamos acessar as ferramentas certas o mais rápido possível, mantendo nossos requisitos de segurança. Isso inclui revisar e remover dependências circulares, ou ser capaz de "contorná-las" rapidamente caso haja um incidente. Também aumentaremos a frequência dos nossos exercícios de treinamento para que os processos sejam bem compreendidos por todas as equipes antes de qualquer possível cenário de desastre no futuro. 

## Quando vamos terminar?

Embora não tenhamos abordado neste artigo todo o trabalho que está sendo realizado internamente, os fluxos de trabalho detalhados acima descrevem as principais prioridades nas quais as equipes devem se concentrar. Cada um desses fluxos de trabalho corresponde a um plano detalhado que atinge quase todas as equipes de produto e engenharia da Cloudflare. Temos muito trabalho a fazer.

Até o final do 1º trimestre, e em grande parte antes disso, nós vamos:

  * Garantir que todos os sistemas de produção sejam cobertos por Implantações Mediadas por Saúde (HMD) para gerenciamento de configuração.
  * Atualizar nossos sistemas para aderir aos modos de falha adequados para cada conjunto de produtos.
  * Garantir que tenhamos processos implementados para que as pessoas certas tenham o acesso certo para fornecer a remediação adequada durante uma emergência.



Alguns desses objetivos serão contínuos. Sempre precisaremos lidar melhor com as dependências circulares à medida que lançamos novos softwares. Nossos procedimentos de emergência precisarão ser atualizados para refletir como nossa tecnologia de segurança muda ao longo do tempo.

Falhamos com nossos usuários e com a internet como um todo nestes dois últimos incidentes. Temos trabalho a fazer para corrigir isso. Planejamos compartilhar atualizações conforme esse trabalho avança e agradecemos as perguntas e o feedback que recebemos dos nossos clientes e parceiros

]]>DMVZ2E5NT13VbQvP1hUNjAnálise anual de 2025 do Cloudflare Radar: a ascensão da IA, o pós-quântico e os ataques de DDoS recordeshttps://blog.cloudflare.com/pt-br/radar-2025-year-in-review/ Mon, 15 Dec 2025 14:00:00 GMTApresentamos nossa 6ª Análise anual de tendências e padrões da internet observados em todo o mundo, revelando as disrupções, avanços e métricas que definiram 2025. AIAnálise do anoInterrupçãoQualidade da internetRadarSegurançaTendênciasTendências da internetTráfego da internetChegou a [Análise anual de 2025 do Cloudflare Radar](https://radar.cloudflare.com/year-in-review/2025/): nossa sexta análise anual das tendências e padrões da internet que observamos ao longo do ano, com base na ampla visão de rede da Cloudflare.

Nossa visão é única, graças à [rede](https://cloudflare.com/network) global da Cloudflare, presente em 330 cidades em mais de 125 países/regiões, que processa em média mais de 81 milhões de solicitações HTTP por segundo, com picos de mais de 129 milhões de solicitações HTTP por segundo em nome de milhões de ativos web de clientes, além de responder a aproximadamente 67 milhões de consultas de DNS ([autoritativo + resolvedor](https://www.cloudflare.com/learning/dns/dns-server-types/)) por segundo. O [Cloudflare Radar](https://radar.cloudflare.com/) utiliza os dados gerados por esses serviços web e DNS, combinados com outros conjuntos de dados complementares, para fornecer insights quase em tempo real sobre [tráfego](https://radar.cloudflare.com/traffic), [bots](https://radar.cloudflare.com/bots), [segurança](https://radar.cloudflare.com/security/), [conectividade](https://radar.cloudflare.com/quality) e padrões e tendências de [DNS](https://radar.cloudflare.com/dns) que observamos na internet. 

Nossa [Análise anual do Radar](https://radar.cloudflare.com/year-in-review/2025/) utiliza essa capacidade de observação e, em vez de uma visão em tempo real, oferece uma retrospectiva de 2025: incorporando tabelas, gráficos e mapas interativos que permitem explorar e comparar tendências e medições selecionadas ano a ano e em todas as regiões, bem como compartilhar e incorporar gráficos da Análise anual. 

A Análise anual de 2025 está organizada em seis seções: [Tráfego](https://radar.cloudflare.com/year-in-review/2025#internet-traffic-growth), [IA](https://radar.cloudflare.com/year-in-review/2025#robots-txt), [Adoção e uso](https://radar.cloudflare.com/year-in-review/2025#ios-vs-android), [Conectividade](https://radar.cloudflare.com/year-in-review/2025#internet-outages), [Segurança](https://radar.cloudflare.com/year-in-review/2025#mitigated-traffic) e [Segurança de e-mail](https://radar.cloudflare.com/year-in-review/2025#malicious-emails), com dados que abrangem o período de 1º de janeiro a 2 de dezembro de 2025. Para garantir a consistência, mantivemos as metodologias subjacentes inalteradas em relação aos cálculos dos anos anteriores. Também incorporamos diversos novos conjuntos de dados este ano, incluindo várias métricas relacionadas à IA, [atividade global de testes de velocidade](https://radar.cloudflare.com/year-in-review/2025#speed-tests) e [progressão de tamanho de DDOS hipervolumétrico](https://radar.cloudflare.com/year-in-review/2025#ddos-attacks). As tendências para 200 países/regiões estão disponíveis no microsite. Locais menores ou menos populosos foram excluídos devido a dados insuficientes. Algumas métricas são mostradas apenas mundialmente e não são exibidas se um país/região for selecionado. 

Neste post, destacamos as principais constatações e observações interessantes das principais seções do microsite Análise anual e publicamos novamente um _post no blog sobre os_[ serviços mais populares da internet](https://blog.cloudflare.com/radar-2025-year-in-review-internet-services/) que explora especificamente as tendências vistas nos [principais serviços da internet](https://radar.cloudflare.com/year-in-review/2025#internet-services).

Recomendamos que você visite o [microsite Análise Anual de 2025](https://radar.cloudflare.com/year-in-review/2025/) para explorar os conjuntos de dados e métricas com mais detalhes, incluindo aqueles para seu país/região para ver como eles mudaram desde 2024 e como se comparam a outras áreas de interesse. 

Esperamos que você considere a Análise anual uma ferramenta perspicaz e poderosa para explorar as disrupções, os avanços e as métricas que definiram a internet em 2025. 

Vamos começar.

## Principais conclusões

### Aceleração

  * O tráfego global da internet cresceu 19% em 2025, com aumento significativo a partir de agosto. ➜
  * Os dez principais serviços de internet mais populares apresentaram algumas mudanças em relação ao ano anterior, enquanto vários novos participantes surgiram nas listas de categorias. ➜
  * O tráfego da Starlink dobrou em 2025, incluindo o tráfego de mais de 20 novos países/regiões. ➜
  * O Googlebot foi novamente responsável pelo maior volume de tráfego de solicitações para a Cloudflare em 2025, ao rastrear milhões de sites de clientes da Cloudflare para indexação de pesquisa e treinamento de IA. ➜
  * A parcela do tráfego da web gerado por humanos com criptografia pós-quântica aumentou para 52%. ➜
  * O Googlebot foi responsável por mais de um quarto do tráfego de bots verificados. ➜



### AI

  * O volume de rastreamento do Googlebot, com sua função dupla, superou em muito o de outros bots e crawlers de IA. ➜
  * O rastreamento de "ação do usuário" de IA aumentou mais de 15 vezes em 2025 ➜
  * Enquanto outros bots de IA representaram 4,2% do tráfego de solicitações HTML, o Googlebot sozinho representou 4,5%. ➜
  * A Anthropic teve a maior proporção entre rastreamento e indicação entre as principais plataformas de IA e pesquisa. ➜
  * Os crawlers de IA foram os agentes de usuário totalmente bloqueados encontrados com maior frequência em arquivos robots.txt. ➜
  * No Workers AI, o modelo llama-3-8b-instruct da Meta foi o mais popular, e a geração de texto foi o tipo de tarefa mais popular. ➜



### Adoção e uso

  * Os dispositivos iOS geraram 35% do tráfego de dispositivos móveis globalmente e mais da metade do tráfego de dispositivos em muitos países. ➜
  * A participação global de solicitações da web que utilizam HTTP/3 e HTTP/2 aumentou ligeiramente em 2025. ➜
  * Bibliotecas e estruturas baseadas em JavaScript continuam sendo ferramentas essenciais para a criação de sites. ➜
  * Um quinto das chamadas de API automatizadas foram feitas por clientes baseados no Go. ➜
  * O Google continua sendo o principal mecanismo de busca, com Yandex, Bing e DuckDuckGo como concorrentes distantes. ➜
  * O Chrome continua sendo o navegador líder em todas as plataformas e sistemas operacionais, exceto no iOS, onde o Safari detém a maior participação. ➜



### Conectividade

  * Quase metade das 174 principais interrupções na internet observadas em todo o mundo em 2025 foram causadas por interrupções regionais e nacionais da conectividade à internet determinadas por governos. ➜
  * Globalmente, menos de um terço das solicitações de pilha dupla foram feitas por IPv6, enquanto na Índia, mais de dois terços foram. ➜
  * Os países europeus apresentaram algumas das maiores velocidades de download, todas acima de 200 Mbps. A Espanha permaneceu consistentemente entre os principais locais em todas as métricas de qualidade da internet medidas. ➜
  * Londres e Los Angeles foram pontos de destaque para a atividade de teste de velocidade da Cloudflare em 2025. ➜
  * Mais da metade do tráfego de solicitações vem de dispositivos móveis em 117 países/regiões. ➜



### Segurança

  * 6% do tráfego global na rede da Cloudflare foi mitigado pelos nossos sistemas, seja como possivelmente malicioso ou por motivos definidos pelo cliente. ➜
  * 40% do tráfego de bots global teve origem nos Estados Unidos, sendo que o Amazon Web Services e o Google Cloud foram responsáveis por um quarto desse tráfego. ➜
  * No ano de 2025, as organizações do setor de “Pessoas e Sociedade” foram as mais visadas. ➜
  * A segurança do roteamento, medida como a participação em rotas RPKI válidas e no espaço de endereços de IP coberto, apresentou melhorias contínuas ao longo de 2025. ➜
  * Os tamanhos dos ataques de DDoS hipervolumétricos aumentaram significativamente ao longo do ano. ➜
  * Mais de 5% das mensagens de e-mail analisadas pela Cloudflare foram consideradas maliciosas. ➜
  * Links enganosos, fraude de identidade e falsificação de marca foram os tipos mais comuns de ameaças encontrados em mensagens de e-mail maliciosas. ➜
  * Quase todas as mensagens de e-mail dos domínios de nível superior .christmas e .lol foram consideradas spam ou maliciosas. ➜



## Tendências de tráfego

### O tráfego global da internet cresceu 19% em 2025, com aumento significativo a partir de agosto

Para determinar as tendências de tráfego ao longo do tempo para a Análise anual, usamos o volume médio de tráfego diário (excluindo tráfego de bots) durante a segunda semana completa do calendário (12 a 18 de janeiro) de 2025 como nossa linha de base. (A segunda semana do calendário é usada para dar tempo para que as pessoas voltem às suas rotinas "normais" de escola e trabalho após as festas de fim de ano). A alteração percentual mostrada no gráfico de tendências de tráfego é calculada em relação ao valor da linha de base. Ela não representa o volume absoluto de tráfego para um país/região. A linha de tendência representa uma média de sete dias, que é usada para suavizar as mudanças bruscas observadas nos dados com granularidade diária. 

O crescimento do tráfego em 2025 parece ter ocorrido em várias fases. Em média, o tráfego manteve-se relativamente estável até meados de abril, geralmente dentro de alguns pontos percentuais do valor da linha de base. No entanto, observou-se um crescimento em maio, atingindo aproximadamente 5% acima da linha de base, mantendo-se na faixa de +4% a 7% até meados de agosto. Foi nesse período que o crescimento acelerou, subindo de forma constante durante setembro, outubro e novembro, [atingindo um pico de crescimento de 19%](https://radar.cloudflare.com/year-in-review/2025#internet-traffic-growth) no ano. Impulsionada por um aumento no final de novembro, a taxa de crescimento de 2025 é cerca de 10% superior ao crescimento de 17% observado em 2024. Em [anos anteriores](https://blog.cloudflare.com/radar-2024-year-in-review/#global-internet-traffic-grew-17-2-in-2024), também observamos uma aceleração do crescimento do tráfego no segundo semestre, embora, entre 2022 e 2024, essa aceleração tenha começado em julho. Não está claro por que o crescimento deste ano parece ter sofrido um atraso de várias semanas.

_Tendências de tráfego da internet em 2025, mundialmente_

[ Botsuana](https://radar.cloudflare.com/year-in-review/2025/bw#internet-traffic-growth) teve o maior pico de crescimento, atingindo 298% acima da linha de base em 8 de novembro, e terminando o período com 295% acima da linha de base. (Mais sobre o que explica esse crescimento na seção Starlink abaixo). Botsuana e [Sudão](https://radar.cloudflare.com/year-in-review/2025/sd#internet-traffic-growth) foram os únicos países/regiões a registrar um aumento de tráfego de mais do que o dobro ao longo do ano, embora alguns outros tenham experimentado picos de aumento superiores a 100% em algum momento durante o ano.

_Tendências de tráfego da internet em 2025, Botsuana_

O impacto de interrupções prolongadas da internet também é claramente visível nos gráficos. Por exemplo, em 29 de outubro, o governo da [Tanzânia](https://radar.cloudflare.com/year-in-review/2025/tz#internet-traffic-growth) impôs uma interrupção da internet em resposta aos protestos do dia das eleições. Essa interrupção durou apenas um dia, mas outra ocorreu de 30 de outubro a 3 de novembro. Embora o tráfego no país tenha aumentado mais de 40% acima da linha de base antes das interrupções, a interrupção acabou reduzindo o tráfego em mais de 70% abaixo da linha de base, uma rápida inversão. O tráfego se recuperou rapidamente após a conectividade ser restaurada. Um padrão semelhante foi observado na [Jamaica](https://radar.cloudflare.com/year-in-review/2025/jm#internet-traffic-growth), onde o tráfego da internet aumentou antes da chegada do [furacão Melissa](https://x.com/CloudflareRadar/status/1983188999461319102?s=20), em 28 de outubro, e caiu significativamente depois que a tempestade causou quedas de energia e danos à infraestrutura na ilha. O tráfego começou a se recuperar após a passagem da tempestade, retornando a um nível ligeiramente acima da linha de base no início de dezembro.

_Tendências de tráfego da internet em 2025, Tanzânia_

 _Tendências de tráfego da internet em 2025, Jamaica_

### Os dez principais serviços de internet mais populares apresentaram algumas mudanças em relação ao ano anterior, enquanto as listas de categorias registraram diversas novas entradas.

Para a Análise anual, analisamos o período acumulado de 11 meses. Além de uma lista classificada como “geral”, também classificamos os serviços em nove categorias, com base na análise de dados de consulta anonimizados de tráfego para o nosso [Resolvedor de DNS público 1.1.1.1](https://1.1.1.1/dns) provenientes de milhões de usuários em todo o mundo. Para os fins dessas classificações, os domínios que pertencem a um único serviço de internet são agrupados.

Google e Facebook mais uma vez ocuparam os dois primeiros lugares entre os [dez principais](https://radar.cloudflare.com/year-in-review/2025/#internet-services). Embora os outros membros da lista dos dez principais tenham permanecido consistentes com as classificações de 2024, houve algumas mudanças no meio da lista. Microsoft, Instagram e YouTube tiveram alta; o Amazon Web Services (AWS) caiu uma posição, enquanto o TikTok caiu quatro posições.

_Principais serviços de internet em 2025, mundialmente._

Entre os serviços de IA generativa, o ChatGPT/OpenAI continuou no topo da lista. Mas houve mudanças em outras categorias, destacando a natureza dinâmica do setor. Os serviços que subiram na classificação incluem Perplexity, Claude/Anthropic e GitHub Copilot. As novas entradas nos dez principais de 2025 incluem Google Gemini, Windsurf AI, Grok/xAI e DeepSeek.

_Principais serviços de IA generativa em 2025, no mundo todo_

Outras categorias também tiveram movimentações em suas listas. A Shopee (“a principal plataforma de compras on-line de comércio eletrônico no sudeste asiático e em Taiwan”) é uma nova participante na lista de comércio eletrônico, e a HBO Max ingressou na classificação de streaming de vídeo. Essas classificações por categoria, bem como as tendências observadas em serviços específicos, são exploradas com mais detalhes em [outro post do blog](https://blog.cloudflare.com/radar-2025-year-in-review-internet-services/).

Além disso, este ano, também estamos fornecendo os principais insights sobre serviços de internet em nível de país/região para as categorias geral, IA generativa, mídia social e mensagens. (Em 2024, compartilhamos apenas da categoria geral).

### O tráfego da Starlink dobrou em 2025, incluindo o tráfego de mais de 20 novos países/regiões

O serviço de internet via satélite Starlink da SpaceX continua a ser uma opção popular para levar conectividade a áreas não atendidas ou mal atendidas, bem como a usuários em [aviões](https://starlink.com/business/aviation) e [barcos](https://starlink.com/business/maritime). Analisamos os volumes agregados de tráfego de solicitações associados ao [sistema autônomo](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/) primário da Starlink ([AS14593](https://radar.cloudflare.com/as14593)) para acompanhar o crescimento do uso do serviço ao longo de 2025. O volume de solicitações mostrado na linha de tendência do gráfico representa uma média móvel de sete dias. 

Globalmente, o [tráfego da Starlink](https://radar.cloudflare.com/year-in-review/2025/#starlink-traffic-trends) continuou a apresentar um crescimento consistente ao longo de 2025, com um aumento de 2,3 vezes no volume total de solicitações durante o ano. Observamos um crescimento rápido do tráfego quando o serviço Starlink se torna disponível em um país/região, e essa tendência continua em 2025. 

 _Crescimento do tráfego da Starlink em todo o mundo em 2025_

Foi exatamente isso que observamos nos mais de 20 novos países/regiões onde a [@Starlink](https://x.com/starlink) anunciou disponibilidade: em questão de dias, o tráfego da Starlink nesses locais aumentou rapidamente. Isso incluiu [Armênia](https://radar.cloudflare.com/year-in-review/2025/am#starlink-traffic-trends), [Níger](https://radar.cloudflare.com/year-in-review/2025/ne#starlink-traffic-trends), [Sri Lanka](https://radar.cloudflare.com/year-in-review/2025/lk#starlink-traffic-trends) e [São Martinho](https://radar.cloudflare.com/year-in-review/2025/sx#starlink-traffic-trends).

Também observamos o tráfego da Starlink de vários locais que atualmente não estão [marcados para disponibilidade do serviço](https://starlink.com/map). No entanto, existem prefixos IPv4 e/ou IPv6 associados a esses países no [geofeed publicado](https://geoip.starlinkisp.net/feed.csv) da Starlink. Dada a capacidade dos usuários da Starlink de usar o serviço (e o equipamento) em [roaming](https://starlink.com/roam), esse tráfego provavelmente vem de usuários em roaming nessas áreas.

_Crescimento do tráfego da Starlink no Níger em 2025_

Dos países/regiões onde o serviço estava ativo antes de 2025, [Benin](https://radar.cloudflare.com/year-in-review/2025/bj#starlink-traffic-trends), [Timor-Leste](https://radar.cloudflare.com/year-in-review/2025/tl#starlink-traffic-trends) e [Botsuana](https://radar.cloudflare.com/year-in-review/2025/bw#starlink-traffic-trends) tiveram alguns dos maiores crescimentos de tráfego, de 51 vezes, 19 vezes e 16 vezes, respectivamente. A disponibilidade do serviço Starlink em [Benin](https://x.com/Starlink/status/1720438167944499638) foi anunciada pela primeira vez em novembro de 2023, em [Timor-Leste](https://x.com/Starlink/status/1866631930902622360) em dezembro de 2024 e em [Botsuana](https://x.com/Starlink/status/1828840132688130322) em agosto de 2024.

_Crescimento do tráfego da Starlink em Botsuana, em 2025_

Serviços semelhantes, como [Amazon Leo](https://leo.amazon.com/), [Eutelsat Konnect](https://www.eutelsat.com/satellite-services/tv-internet-home/satellite-internet-home-business-konnect) e o [Qianfan](https://en.wikipedia.org/wiki/Qianfan) da China, continuam a aumentar suas constelações de satélites e a se aproximar da disponibilidade comercial. Esperamos analisar o crescimento do tráfego nesses serviços no futuro também.

### O Googlebot foi novamente responsável pelo maior volume de tráfego de solicitações para a Cloudflare em 2025, ao rastrear milhões de sites de clientes da Cloudflare para indexação de pesquisa e treinamento de IA.

Para analisar o tráfego agregado de solicitações que a Cloudflare observou em 2025 de toda a internet IPv4, podemos usar uma [curva de Hilbert](https://en.wikipedia.org/wiki/Hilbert_curve), que nos permite visualizar uma sequência de endereços de IPv4 em um padrão bidimensional que mantém os endereços de IP próximos uns dos outros, tornando-os [úteis](https://xkcd.com/195/) para mapear o espaço de endereços de IPv4 da internet. Na [visualização](https://radar.cloudflare.com/year-in-review/2025/#ipv4-traffic-distribution), agregamos os endereços IPv4 em prefixos [/20](https://www.ripe.net/about-us/press-centre/IPv4CIDRChart_2015.pdf), o que significa que, no nível de zoom mais alto, cada quadrado representa o tráfego de 4.096 endereços IPv4. Esse nível de agregação mantém a quantidade de dados usada para a visualização gerenciável. Veja o [post no blog Análise anual de 2024](https://blog.cloudflare.com/radar-2024-year-in-review/#googlebot-was-responsible-for-the-highest-volume-of-request-traffic-to-cloudflare-in-2024-as-it-retrieved-content-from-millions-of-cloudflare-customer-sites-for-search-indexing) para obter mais detalhes sobre a visualização.

Pelo terceiro ano consecutivo, o bloco de endereços de IP com o maior volume de solicitações para a Cloudflare em 2025 foi o [66.249.64.0/20](https://radar.cloudflare.com/routing/prefix/66.249.64.0/20) do Google, [um dos vários](https://developers.google.com/static/search/apis/ipranges/googlebot.json) usados pelo web crawler [Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot) para recuperar conteúdo para indexação de pesquisas e treinamento de IA. O fato de um bloco de endereços IP do Googlebot ter figurado novamente como a principal fonte de tráfego de requisições não é surpreendente, considerando o número de ativos da web na rede da Cloudflare e a intensa atividade de rastreamento do Googlebot. O prefixo do Googlebot foi responsável por quase quatro vezes mais tráfego de solicitações IPv4 do que a segunda maior fonte de tráfego, 146.20.240.0/20, que faz parte de um [bloco maior de espaço de endereço IPv4 anunciado pela Rackspace Hosting](https://radar.cloudflare.com/routing/prefix/146.20.0.0/16). Como provedora de nuvem e hospedagem, a Rackspace oferece suporte a diversos tipos de clientes e aplicativos. Portanto, a origem do tráfego observado para a Cloudflare é desconhecida.

_Visualização ampliada da curva de Hilbert mostrando o bloco de endereços que gerou o maior volume de solicitações em 2025_

Este ano, adicionamos a capacidade de pesquisar um sistema autônomo (ASN) à visualização, permitindo que você veja a abrangência da distribuição dos endereços IP de um provedor de rede no universo IPv4. 

Um exemplo é o AS16509 (AMAZON-02, usado com o AWS), que mostra os resultados das aquisições da Amazon de [grandes quantidades de espaço de endereços IPv4](https://toonk.io/aws-and-their-billions-in-ipv4-addresses/index.html) ao longo dos anos. Outro exemplo é o AS7018 (ATT-INTERNET4, AT&T), que é um dos maiores [anunciantes de espaço de endereços IPv4 nos Estados Unidos](https://radar.cloudflare.com/routing/us#ases-registered-in-united-states). Grande parte do tráfego deste número de sistema autônomo vem do [12.0.0.0/8,](https://radar.cloudflare.com/routing/prefix/12.0.0.0/8) um bloco de mais de 16 milhões de endereços IPv4 que [pertence à AT&T desde 1983.](https://wq.apnic.net/apnic-bin/whois.pl?searchtext=12.147.5.178)

_Curva de Hilbert exibindo os blocos de endereços IPv4 do AS7018 que enviaram tráfego para a Cloudflare em 2025_

### A parcela do tráfego da web gerado por humanos com criptografia pós-quântica aumentou para 52%

"[Pós-quântico](https://en.wikipedia.org/wiki/Post-quantum_cryptography)" refere-se a um conjunto de técnicas criptográficas desenvolvidas para proteger dados criptografados contra ataques do tipo ["Colher agora, descriptografar depois",](https://en.wikipedia.org/wiki/Harvest_now,_decrypt_later) realizados por adversários capazes de capturar e armazenar dados hoje para descriptografá-los no futuro com computadores quânticos suficientemente avançados. A equipe de pesquisa da Cloudflare [trabalha com criptografia pós-quântica desde 2017](https://blog.cloudflare.com/sidh-go/) e publica regularmente [atualizações](https://blog.cloudflare.com/pq-2025/) sobre o estado da internet pós-quântica.

Depois de observar [um crescimento significativo em 2024](https://radar.cloudflare.com/year-in-review/2024#post-quantum-encryption), a participação global do [tráfego com criptografia pós-quântica](https://radar.cloudflare.com/year-in-review/2025/#post-quantum-encryption) quase dobrou ao longo de 2025, passando de 29% no início do ano para 52% no início de dezembro. 

 _Crescimento do tráfego TLS 1.3 com criptografia pós-quântica em 2025, mundialmente_

Vinte e oito países/regiões viram sua participação no tráfego com criptografia pós-quântica mais que dobrar ao longo do ano, incluindo um crescimento significativo em [Porto Rico](https://radar.cloudflare.com/year-in-review/2025/pr#post-quantum-encryption) e [Kuwait](https://radar.cloudflare.com/year-in-review/2025/kw#post-quantum-encryption). A participação do Kuwait quase triplicou, de 13% para 37%, e a participação de Porto Rico aumentou de 20% para 49%. 

Esses três países estavam entre outros que que apresentaram um crescimento significativo na participação de mercado em meados de setembro, [coincidindo com](https://9to5mac.com/2025/09/09/apple-announces-ios-26-release-date-september-15/) o lançamento de atualizações do sistema operacional da Apple, nas quais “ _as conexões protegidas por TLS[ vão anunciar automaticamente o suporte para troca de chaves híbridas e seguras em relação ao quântico](https://support.apple.com/en-us/122756) no TLS 1.3_”. No Kuwait e em Porto Rico, mais da metade do tráfego de solicitações é proveniente de dispositivos móveis, e aproximadamente metade também vem de dispositivos iOS em ambos os locais. Portanto, não é surpreendente que essa atualização de software tenha resultado em um aumento significativo na participação do tráfego com pós-quântico.

_Crescimento do tráfego TLS 1.3 com criptografia pós-quântica em 2025, Porto Rico_

Assim, a parcela do tráfego com criptografia pós-quântica de dispositivos iOS da Apple [aumentou significativamente em setembro](https://radar.cloudflare.com/explorer?dataSet=http&groupBy=post_quantum&filters=botClass%253DLIKELY_HUMAN%252Cos%253DiOS&dt=2025-09-01_2025-09-28) após o lançamento oficial do iOS 26. Apenas [quatro dias após o lançamento](https://x.com/CloudflareRadar/status/1969159602999640535?s=20), a participação global de solicitações com suporte a criptografia pós-quântica de dispositivos iOS cresceu de pouco menos de 2% para 11%. Até o [início de dezembro](https://radar.cloudflare.com/explorer?dataSet=http&groupBy=post_quantum&filters=deviceType%253DMobile%252Cos%253DiOS%252CbotClass%253DLikely_Human&dt=2025-12-01_2025-12-07), mais de 25% das solicitações de dispositivos iOS usavam criptografia pós-quântica.

### O Googlebot foi responsável por mais de um quarto do tráfego de bots verificados.

O novo [Diretório de Bots](https://radar.cloudflare.com/bots/directory?kind=all) no Cloudflare Radar fornece uma grande quantidade de informações sobre [bots verificados](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) e [agentes assinados](https://developers.cloudflare.com/bots/concepts/bot/signed-agents/), incluindo seus operadores, categorias e agentes de usuário associados, links para documentação e tendências de tráfego. Os bots verificados devem estar em conformidade com um [conjunto de requisitos](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/policy/) além de serem verificados por meio do [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) ou da [validação de IP](https://developers.cloudflare.com/bots/reference/bot-verification/ip-validation/). Um agente assinado é controlado por um usuário final e um agente de assinatura verificado de sua implementação de [Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) e deve estar em conformidade com um [conjunto de requisitos](https://developers.cloudflare.com/bots/concepts/bot/signed-agents/policy/) separado.

O [Googlebot](https://radar.cloudflare.com/bots/directory/google) é usado para rastrear o conteúdo de sites para indexação de pesquisa e treinamento de IA, e foi, de longe, [o bot mais ativo observado pela Cloudflare](https://radar.cloudflare.com/year-in-review/2025/#per-bot-traffic) ao longo de 2025. O período de maior atividade foi entre meados de fevereiro e meados de julho, atingindo o pico em meados de abril, e foi responsável por mais de 28% do tráfego proveniente de bots verificados. Outros bots operados pelo Google que foram responsáveis por volumes consideráveis de tráfego incluem o [Google AdsBot](https://radar.cloudflare.com/bots/directory/googleads) (utilizado para monitorar sites onde anúncios do Google são exibidos), o [Google Image Proxy](https://radar.cloudflare.com/bots/directory/googleimageproxy) (utilizado para recuperar e armazenar em cache imagens incorporadas em mensagens de e-mail) e o [GoogleOther](https://radar.cloudflare.com/bots/directory/google-other) (utilizado por diversas equipes de produto para buscar conteúdo acessível publicamente em sites).

O [GPTBot](https://radar.cloudflare.com/bots/directory/gptbot) da OpenAI, que rastreia conteúdo para treinamento de IA, foi o segundo bot mais ativo, originando cerca de 7,5% do tráfego de bots verificados, com atividade de rastreamento bastante volátil durante o primeiro semestre do ano. O [Bingbot](https://radar.cloudflare.com/bots/directory/bing) da Microsoft rastreia o conteúdo de sites para indexação de pesquisa e treinamento de IA, gerando 6% do tráfego de bots verificados ao longo do ano e demonstrando uma atividade relativamente estável. 

 _Tendências de tráfego de bots verificados em 2025, no mundo todo_

Os crawlers de mecanismos de busca e os crawlers de IA são as duas categorias de bots verificados mais ativas, com padrões de tráfego que se assemelham aos principais bots nessas categorias, incluindo o GoogleBot e o GPTBot da OpenAI. [Os crawlers de mecanismos de busca](https://radar.cloudflare.com/bots/directory?category=SEARCH_ENGINE_CRAWLER&kind=all) foram responsáveis por 40% do tráfego de bots verificados, enquanto os [crawlers de IA](https://radar.cloudflare.com/bots/directory?category=AI_CRAWLER&kind=all) geraram metade disso (20%). [Os bots de otimização para mecanismos de busca](https://radar.cloudflare.com/bots/directory?category=SEARCH_ENGINE_OPTIMIZATION&kind=all) também estiveram bastante ativos, representando mais de 13% das solicitações provenientes de bots verificados.

_Tendências de tráfego de bots verificadas por categoria em 2025, mundialmente_

## Insights sobre IA

##  O volume de rastreamento do Googlebot, com sua dupla finalidade, superou em muito o de outros bots e crawlers de IA.

Em setembro, um [post de blog](https://blog.cloudflare.com/building-a-better-internet-with-responsible-ai-bot-principles/) da Cloudflare apresentou uma proposta de princípios para bots de IA responsáveis, um dos quais era: “Os bots de IA devem ter uma finalidade distinta e declará-la”. Na [visão geral de práticas recomendadas para bots de IA](https://radar.cloudflare.com/ai-insights#ai-bot-best-practices) no Radar, observamos que vários operadores de bots têm crawlers com dupla finalidade, incluindo Google e Microsoft.

Como o [Googlebot](https://radar.cloudflare.com/bots/directory/google) rastreia tanto para indexação de mecanismos de busca quanto para treinamento de IA, nós o incluímos na [visão geral de crawlers de IA](https://radar.cloudflare.com/year-in-review/2025/#ai-bot-and-crawler-traffic) deste ano. Em 2025, seu volume de rastreamento superou em muito o de outros bots de IA líderes. O tráfego de solicitações começou a aumentar em meados de fevereiro, atingindo o pico no final de abril, e depois diminuiu lentamente até o final de julho. Depois disso, cresceu gradualmente até o final do ano. O [Bingbot](https://radar.cloudflare.com/bots/directory/bing) também tem tem uma dupla finalidade semelhante, embora seu volume de rastreamento seja uma fração do do Googlebot. A atividade de rastreamento do Bingbot apresentou uma tendência geralmente crescente ao longo do ano.

_Tendências de tráfego de crawlers de IA em 2025, mundialmente_

O [GPTBot](https://radar.cloudflare.com/bots/directory/gptbot) da OpenAI é usado para rastrear conteúdo que pode ser usado no treinamento dos modelos de base de IA generativa da OpenAI. Sua atividade de rastreamento apresentou bastante volatilidade ao longo do ano, atingindo seus níveis mais altos em junho, mas terminou novembro ligeiramente acima dos níveis de rastreamento observados no início do ano. 

O volume de rastreamento do [ChatGPT-User](https://radar.cloudflare.com/bots/directory/chatgpt-user) da OpenAI, que visita páginas web quando os usuários fazem perguntas ao ChatGPT ou a um CustomGPT, apresentou um crescimento constante ao longo do ano, com um padrão de uso semanal tornando-se mais evidente a partir de meados de fevereiro, sugerindo um aumento do uso em escolas e no local de trabalho. Os picos de volume de solicitações foram até 16 vezes maiores do que no início do ano. Uma queda na atividade também foi evidente no período de junho a agosto, quando muitos estudantes estavam fora da escola e muitos profissionais estavam de férias. 

O [OAI-SearchBot](https://radar.cloudflare.com/bots/directory/oai-searchbot), que é usado para vincular e exibir sites nos resultados de pesquisa nos recursos de pesquisa do ChatGPT, observou um crescimento gradual na atividade de rastreamento até agosto, com vários picos de tráfego em agosto e setembro, antes de aumentar de forma mais agressiva em outubro, com um volume máximo de solicitações durante um pico no final de outubro, aproximadamente 5 vezes maior do que no início do ano.

_Tendências de tráfego de crawlers da OpenAI em 2025, mundialmente_

O rastreamento do ClaudeBot da Anthropic praticamente dobrou no primeiro semestre do ano, mas diminuiu gradualmente durante o segundo semestre, retornando a um nível aproximadamente 10% superior ao do início do ano. O tráfego de rastreamento do PerplexityBot da Perplexity cresceu lentamente durante janeiro e fevereiro, mas observou um grande aumento na atividade de meados de março até abril. Depois disso, o crescimento foi mais gradual até outubro, antes de observar um aumento significativo novamente em novembro, terminando cerca de 3,5 vezes maior do que no início do ano.

_Tendências de tráfego do ClaudeBot em 2025, mundialmente_

 _Tendências de tráfego do PerplexityBot em 2025, mundialmente_

O Bytespider da ByteDance, um dos principais crawlers de IA de 2024, apresentou um volume de rastreamento inferior ao de vários outros bots de treinamento, e sua atividade diminuiu ao longo do ano, continuando o declínio observado no ano anterior.

### O rastreamento de "ação do usuário" de IA aumentou mais de 15 vezes em 2025

A maioria dos rastreamentos de bots de IA é realizada para uma destas três [finalidades](https://radar.cloudflare.com/year-in-review/2025/#ai-crawler-traffic-by-purpose): treinamento, que coleta conteúdo de sites para o treinamento de modelos de IA; busca, que indexa o conteúdo de sites para a funcionalidade de busca disponível em plataformas de IA; e ação do usuário, que visita sites em resposta a perguntas de usuários feitas a um chatbot. Observe que o rastreamento para pesquisa também pode incluir o rastreamento para [Geração Aumentada de Recuperação (RAG)](https://developers.cloudflare.com/ai-search/concepts/what-is-rag/), que permite que um proprietário de conteúdo traga seus próprios dados para a geração de LLMs sem treinar ou ajustar um modelo novamente. (Uma quarta finalidade “não declarada” captura o tráfego de bots de IA cujo objetivo de rastreamento é incerto ou desconhecido).

O rastreamento para o treinamento de modelos é responsável pela grande maioria do tráfego de crawlers de IA, chegando a ser de 7 a 8 vezes maior que o rastreamento de pesquisa e 32 vezes maior que o rastreamento de ação do usuário em picos. O volume de tráfego para treinamento é fortemente influenciado pelo GPTBot da OpenAI e, portanto, seguiu um padrão muito semelhante ao longo do ano.

O rastreamento para pesquisa atingiu seu pico em meados de março, quando caiu aproximadamente 40%. Depois disso, o crescimento voltou a ser mais gradual, embora tenha terminado o período analisado um pouco abaixo de 10% em relação ao início do ano.

O rastreamento de ação do usuário começou 2025 com o menor volume de rastreamento entre as três finalidades definidas, mas mais do que dobrou entre janeiro e fevereiro. Dobrou novamente no início de março e, a partir daí, continuou a crescer ao longo do ano, aumentando mais de 21 vezes de janeiro até o início de dezembro. Esse crescimento corresponde precisamente às tendências de tráfego observadas para o bot ChatGPT-User da OpenAI.

_Tendências de tráfego de crawlers de ação do usuário em 2025, mundialmente_

### Enquanto outros bots de IA representaram 4,2% do tráfego de solicitações HTML, o Googlebot representou 4,5% sozinho.

Os bots de IA têm aparecido frequentemente nas notícias em 2025, à medida que os proprietários de conteúdo expressam preocupações sobre a quantidade de tráfego que eles geram, especialmente porque grande parte desse tráfego [não se traduz em](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/) usuários finais sendo redirecionados para os sites de origem. Para entender melhor o impacto da atividade de rastreamento de bots de IA, em comparação com bots não IA e o uso da web por humanos, analisamos o tráfego de solicitações de conteúdo HTML em toda a base de clientes da Cloudflare e o [classificamos](https://radar.cloudflare.com/year-in-review/2025/#ai-traffic-share) como proveniente de humanos, bots de IA ou outros tipos de bots “não IA”. (Observe que, como estamos nos concentrando apenas no conteúdo HTML, as participações de bots e de humanos no tráfego será diferente da mostrada no Radar, que analisa o tráfego de solicitações para todos os tipos de conteúdo). Como o Googlebot rastreia de forma tão ativa e tem dupla finalidade, separamos sua participação nesta análise.

Ao longo de 2025, descobrimos que o tráfego de bots de IA representou, em média, 4,2% das solicitações HTML. Essa participação variou bastante ao longo do ano, caindo para apenas 2,4% no início de abril e atingindo o máximo de 6,4% no final de junho.

Nesse sentido, os bots não IA começaram 2025 responsáveis por metade das solicitações de páginas HTML, sete pontos percentuais acima do tráfego gerado por humanos. Essa diferença chegou a 25 pontos percentuais nos primeiros dias de junho. No entanto, essas participações de tráfego começaram a se aproximar a partir de meados de junho e, a partir de 11 de setembro, entraram em um período em que a participação do tráfego HTML gerado por humanos às vezes superou a de bots não IA. Em 2 de dezembro, o tráfego humano gerou 47% das solicitações HTML e os bots não IA, 44%.

O Googlebot é um crawler particularmente voraz e, este ano, originou 4,5% das solicitações HTML, uma participação ligeiramente maior do que os bots de IA em conjunto. Começando o ano com pouco menos de 2,5%, sua participação aumentou rapidamente nos quatro meses seguintes, atingindo um pico de 11% no final de abril. Posteriormente, recuou para o ponto de partida nos meses seguintes e, em seguida, cresceu novamente durante o segundo semestre do ano, terminando com uma participação de 5%. Essa mudança na participação reflete, em grande parte, a atividade de rastreamento do Googlebot, conforme discutido acima.

_Participação no tráfego HTML por tipo de bot em 2025, mundialmente_

### A Anthropic teve a maior proporção entre rastreamento e indicação entre as principais plataformas de IA e pesquisa

Em 1º de julho, [lançamos no Radar a métrica de proporção entre rastreamento e indicação](https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/) para acompanhar a frequência com que uma determinada IA ou plataforma de pesquisa envia tráfego a um site em relação à frequência com que rastreia esse site. Uma proporção alta significa muito rastreamento por IA sem o envio de humanos reais para um site.

Essa métrica pode ser volátil, com os valores mudando diariamente conforme a atividade de rastreamento e o tráfego de referência se alteram. Essa [métrica compara](https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar/#how-does-this-measurement-work) o número total de solicitações de agentes de usuário relevantes associados a uma determinada plataforma de pesquisa ou IA, onde a resposta foi Content-type: text/html, com o número total de solicitações de conteúdo HTML em que o cabeçalho Referer continha um nome de host associado a uma determinada plataforma de pesquisa ou IA. 

A Anthropic teve as maiores [proporções entre rastreamento e indicação este ano](https://radar.cloudflare.com/year-in-review/2025/#crawl-refer-ratio), chegando a 500.000:1, embora tenham sido bastante irregulares de janeiro a maio. Tanto a magnitude quanto a natureza irregular da métrica provavelmente se devem ao baixo tráfego de referência durante esse período. Depois disso, as proporções se tornaram mais consistentes, mas permaneceram mais altas do que as outras, variando de aproximadamente 25.000:1 a aproximadamente 100.000:1.

As proporções da OpenAI ao longo do tempo foram bastante irregulares, chegando a atingir 3.700:1 em março. Essas oscilações podem ser atribuídas à estabilização da atividade de rastreamento do GPTBot, juntamente com o aumento do uso da funcionalidade de pesquisa do ChatGPT, que inclui links para os sites de origem em suas respostas. Os usuários que seguem esses links aumentam as contagens do Referer, possivelmente diminuindo a proporção. (Considerando que o tráfego de rastreamento não estivesse aumentando em uma taxa semelhante ou superior).

O Perplexity apresentou as menores proporções entre rastreamento e indicação entre as principais plataformas de IA, começando o ano abaixo de 100:1 antes de atingir um pico acima de 700:1 no final de março, coincidindo com um pico no tráfego de rastreamento do PerplexityBot. Após o pico inicial, os valores máximos da proporção geralmente permaneceram abaixo de 400:1 e abaixo de 200:1 a partir de setembro.

Entre as plataformas de busca, a proporção da Microsoft exibiu inesperadamente um padrão semanal cíclico, atingindo seus níveis mais baixos às quintas-feiras e atingindo o pico aos domingos. Os valores máximos da proporção geralmente variaram de 50:1 a 70:1 ao longo do ano. Começando o ano com pouco mais de 3:1, a proporção entre rastreamento e indicação do Google aumentou de forma constante até abril, chegando a 30:1. Após atingir o pico, houve uma queda um tanto irregular até meados de julho, retornando a 3:1, embora tenha aumentado gradualmente no segundo semestre de 2025. A proporção do DuckDuckGo permaneceu abaixo de 1:1 durante os três primeiros trimestres de 2025, mas apresentou um salto repentino para 1,5:1 em meados de outubro e se manteve elevada durante o restante do período.

_Proporção entre rastreamento e indicação de plataformas de IA e pesquisa em 2025, mundialmente_

### Os crawlers de IA foram os agentes de usuário totalmente bloqueados encontrados com maior frequência em arquivos robots.txt.

O arquivo robots.txt, formalmente definido na [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) como o Protocolo de Exclusão de Robôs, é um arquivo de texto que os proprietários de conteúdo podem usar para sinalizar aos web crawlers quais partes de um site os crawlers podem acessar, usando diretivas para permitir ou bloquear explicitamente que crawlers de IA e de pesquisa acessem todo o site ou apenas partes dele. As diretivas dentro do arquivo funcionam como um sinal de “proibida a entrada” e não fornecem nenhum controle de acesso formal. Dito isto, o recurso [robots.txt gerenciado](https://blog.cloudflare.com/control-content-use-for-ai-training/#putting-up-a-guardrail-with-cloudflares-managed-robots-txt) da Cloudflare atualiza automaticamente o arquivo robots.txt existente de um site ou cria um arquivo robots.txt no site, que inclui diretivas solicitando que os operadores de bots de IA populares não usem o conteúdo para treinamento de modelos de IA. Além disso, nossos recursos do [AI Crawl Control](https://blog.cloudflare.com/ai-audit-enforcing-robots-txt/) podem rastrear violações das diretivas do robots.txt de um site e dar ao proprietário do site a capacidade de bloquear solicitações do agente de usuário infrator.

No Cloudflare Radar, fornecemos [insights](https://radar.cloudflare.com/ai-insights#ai-user-agents-found-in-robotstxt) sobre o número de arquivos robots.txt encontrados entre nossos 10 mil [domínios](https://radar.cloudflare.com/domains) principais e a disposição total/parcial das diretivas permitir e bloquear encontradas nos arquivos para agentes de usuário de crawlers selecionados. (Neste contexto, “completo” refere-se a diretivas que se aplicam a todo o site, e “parcial” refere-se a diretivas que se aplicam a caminhos ou tipos de arquivo específicos). [No microsite Análise anual](https://radar.cloudflare.com/year-in-review/2025/#robots-txt), mostramos como a disposição dessas diretivas mudou ao longo de 2025.

Os agentes de usuário com o maior número de diretivas totalmente bloqueadas são aqueles associados a crawlers de IA, incluindo GPTBot, ClaudeBot e [CCBot](https://www.theatlantic.com/technology/2025/11/common-crawl-ai-training-data/684567/). As diretivas para os crawlers Googlebot e Bingbot, usados tanto para indexação de pesquisa quanto para treinamento de IA, tenderam fortemente para o bloqueio parcial, provavelmente com foco no isolamento de endpoints de login e outras áreas não relacionadas ao conteúdo de um site. Para esses dois bots, as diretivas aplicadas a todo o site representaram uma pequena fração do número total de diretivas de bloqueio observadas ao longo do ano. 

 _Diretivas de bloqueio do robots.txt por agente de usuário_

O número de diretivas de permissão explícitas encontradas nos arquivos robots.txt descobertos representou uma fração das diretivas de bloqueio observadas, provavelmente porque "permitir" é a política padrão quando não há diretivas específicas. O Googlebot teve o maior número de diretivas de permissão explícitas, embora mais da metade delas fossem permissões parciais. Diretivas de permissão direcionadas a crawlers de IA foram encontradas em menos domínios, com diretivas direcionadas aos crawlers da OpenAI tendendo mais para permissões completas explícitas. 

O [Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended) é um token de agente de usuário que os editores da web podem usar para gerenciar se o conteúdo que o Google rastreia em seus sites pode ser usado para treinar [modelos do Gemini](https://deepmind.google/models/gemini/) ou para fornecer conteúdo do site a partir do índice de pesquisa do Google para o Gemini, e o número de diretivas de permissão direcionadas a ele triplicou durante o ano. A maioria permitia acesso parcial no início do ano, enquanto o final do ano apresentou um número maior de diretivas que permitiam explicitamente o acesso total ao site do que aquelas que permitiam acesso a apenas parte do conteúdo do site. 

 _Diretivas de permissão do robots.txt por agente de usuário_

### No Workers AI, o modelo llama-3-8b-instruct da Meta foi o mais popular, e a geração de texto foi o tipo de tarefa mais popular

O cenário de modelos de IA está evoluindo rapidamente, com os provedores lançando regularmente modelos mais poderosos, capazes de tarefas como geração de texto e imagens, reconhecimento de fala e classificação de imagens. A Cloudflare trabalha em estreita colaboração com fornecedores de modelos de IA para garantir que [o Workers AI seja compatível com esses modelos](https://developers.cloudflare.com/workers-ai/models/) o mais rápido possível após o lançamento. Recentemente, [adquirimos a Replicate](https://blog.cloudflare.com/replicate-joins-cloudflare/) para expandir significativamente nosso catálogo de modelos compatíveis. Em [fevereiro de 2025](https://blog.cloudflare.com/expanded-ai-insights-on-cloudflare-radar/#popularity-of-models-and-tasks-on-workers-ai), introduzimos visibilidade no Radar sobre a popularidade dos [modelos](https://radar.cloudflare.com/ai-insights/#workers-ai-model-popularity) compatíveis disponíveis publicamente, bem como os tipos de [tarefas](https://radar.cloudflare.com/ai-insights/#workers-ai-task-popularity) que esses modelos executam, com base na participação nas contas dos clientes. 

[Ao longo do ano](https://radar.cloudflare.com/year-in-review/2025/#workers-ai-model-and-task-popularity), o modelo [llama-3-8b-instruct](https://developers.cloudflare.com/workers-ai/models/llama-3-8b-instruct/) da Meta dominou, com uma participação nas contas (36,3%) mais de três vezes maior que as dos modelos seguintes mais populares, o [whisper](https://developers.cloudflare.com/workers-ai/models/whisper/) da OpenAI (10,1%) e o [stable-diffusion-xl-base-1.0](https://developers.cloudflare.com/workers-ai/models/stable-diffusion-xl-base-1.0/) da Stability AI (9,8%). Tanto a Meta quanto a BAAI (Academia de Inteligência Artificial de Pequim) tinham vários modelos entre os dez principais, e os dez modelos principais detinham uma participação de 89% nas contas, com o restante distribuído por uma longa lista de outros modelos.

_Modelos mais populares no Workers AI em 2025, mundialmente_

A popularidade das tarefas foi impulsionada em grande parte pelos principais modelos, com a geração de texto, a conversão de texto em imagem e o reconhecimento automático de fala liderando a lista. A geração de texto foi utilizada por 48,2% nas contas de clientes do Workers AI, quase quatro vezes mais do que a conversão de texto em imagem (12,3%) e o reconhecimento automático de fala (11,0%) 

 _Tarefas mais populares no Workers AI em 2025, mundialmente_

## O que está sendo rastreado

Além da análise do ano até o momento mostrada acima, apresentamos abaixo análises pontuais do que está sendo rastreado. Observe que esses insights não estão incluídos no microsite da Análise anual.

### Rastreamento por região geográfica

Na seção de IA da Análise anual, analisamos o tráfego global de bots e crawlers de IA, sem considerar a geografia associada à conta proprietária do conteúdo rastreado. Se detalharmos geograficamente, usando dados de outubro de 2025, e observarmos quais bots geram mais tráfego de rastreamento para sites de clientes com endereço de faturamento em uma determinada região geográfica, descobrimos que o Googlebot representa entre 35% e 55% do tráfego de crawlers em cada região.

O GPTBot da OpenAI ou o Bingbot da Microsoft são os segundos mais ativos, com participações de rastreamento de 13% a 14%. Nas economias desenvolvidas da América do Norte, Europa e Oceania, o Bingbot mantém uma liderança sólida sobre os crawlers de IA. No entanto, para sites localizados em mercados de rápido crescimento na América do Sul e na Ásia, o GPTBot tem uma vantagem menor sobre o Bingbot.

Região geográfica| Principais crawlers  
---|---  
América do Norte| Googlebot (45.5%)  
Bingbot (14,0%)Meta-ExternalAgent (7.7%)  
América do Sul| Googlebot (44.2%)  
GPTBot (13,8%)  
Bingbot (13,5%)  
Europa| Googlebot (48.6%)  
Bingbot (13,2%)  
GPTBot (10,8%)  
Ásia| Googlebot (39.0%)  
GPTBot (14,0%)  
Bingbot (12,6%)  
África| Googlebot (35.8%)  
Bingbot (13,7%)  
GPTBot (13,1%)  
Oceania| Googlebot (54.2%)  
Bingbot (13,8%)  
GPTBot (6,6%)  
  
### Rastreamento por setor

Ao analisar a atividade de crawlers de IA por setor de clientes durante outubro de 2025, descobrimos que os setores de varejo e software de computador atraíram consistentemente a maior parte do tráfego de crawlers de IA, representando juntos pouco mais de 40% de toda a atividade.

Outros dez principais representaram parcelas bem menores da atividade de rastreamento. Esses dez setores principais representaram pouco menos de 70% do rastreamento, com o restante distribuído por uma longa lista de outros setores.

_Participação do setor na atividade de rastreamento de IA, outubro de 2025_

## Adoção e uso

### Os dispositivos iOS geraram 35% do tráfego de dispositivos móveis globalmente e mais da metade do tráfego de dispositivos em muitos países

Os dois principais sistemas operacionais para dispositivos móveis em todo o mundo são o [iOS da Apple](https://en.wikipedia.org/wiki/IOS) e o [Android do Google](https://en.wikipedia.org/wiki/Android_\(operating_system\)). Ao analisar as informações no cabeçalho [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) incluído em cada solicitação da web, podemos calcular a distribuição do tráfego por sistema operacional do cliente ao longo do ano. Os dispositivos Android geram a maior parte do tráfego de dispositivos móveis globalmente, devido à ampla distribuição de preços, formatos e recursos desses dispositivos.

Globalmente, a [participação do tráfego do iOS](https://radar.cloudflare.com/year-in-review/2025/#ios-vs-android) cresceu ligeiramente [em relação ao ano anterior](https://blog.cloudflare.com/radar-2024-year-in-review/#globally-nearly-one-third-of-mobile-device-traffic-was-from-apple-ios-devices-android-had-a-90-share-of-mobile-device-traffic-in-29-countries-regions-peak-ios-mobile-device-traffic-share-was-over-60-in-eight-countries-regions), um aumento de dois pontos percentuais, para 35% em 2025. Analisando os principais países com participação no tráfego de iOS, [Mônaco](https://radar.cloudflare.com/year-in-review/2025/mc#ios-vs-android) teve a maior participação, de 70%. O iOS foi responsável por 50% ou mais do tráfego de dispositivos móveis em um total de 30 países/regiões, incluindo [Dinamarca](https://radar.cloudflare.com/year-in-review/2025/dk#ios-vs-android) (65%), [Japão](https://radar.cloudflare.com/year-in-review/2025/jp#ios-vs-android) (57%) e [Porto Rico](https://radar.cloudflare.com/year-in-review/2025/pr#ios-vs-android) (52%).

_Distribuição do tráfego de dispositivos móveis por sistema operacional em 2025, mundialmente_

Em países/regiões com maior uso do Android, as participações foram significativamente maiores. Vinte e sete tiveram adoção do Android acima de 90% em 2025, com [Papua-Nova Guiné](https://radar.cloudflare.com/year-in-review/2025/pg#ios-vs-android) liderando com 97%. [Sudão](https://radar.cloudflare.com/year-in-review/2025/sd#ios-vs-android), [Malauí](https://radar.cloudflare.com/year-in-review/2025/mw#ios-vs-android), [Bangladesh](https://radar.cloudflare.com/year-in-review/2025/bd#ios-vs-android) e [Etiópia](https://radar.cloudflare.com/year-in-review/2025/et#ios-vs-android) também registraram uma participação do Android de 95% ou mais. O Android foi responsável por 50% ou mais do tráfego de dispositivos móveis em 175 países/regiões, com as [Bahamas](https://radar.cloudflare.com/year-in-review/2025/bs#ios-vs-android) ocupando a última posição dessa lista, com 51%. 

 _Distribuição do uso de iOS e Android em 2025_

### As participações de solicitações da web globais que usam HTTP/3 e HTTP/2 aumentaram ligeiramente em 2025

HTTP (protocolo de transferência de hipertexto) é o protocolo que faz a web funcionar. Nos últimos 30 anos ou mais, ele passou por diversas revisões importantes. A primeira versão padronizada, [HTTP/1.0](https://datatracker.ietf.org/doc/html/rfc1945), foi adotada em 1996, o [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc2616.html) em 1999 e o [HTTP/2](https://www.rfc-editor.org/rfc/rfc7540.html) em 2015. O [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html), padronizado em 2022, marcou uma atualização significativa, executado sobre um novo protocolo de transporte conhecido como [QUIC](https://blog.cloudflare.com/the-road-to-quic/). Usar o QUIC como seu transporte subjacente permite que o [HTTP/3](https://www.cloudflare.com/learning/performance/what-is-http3/) estabeleça conexões mais rapidamente, além de oferecer um desempenho aprimorado ao mitigar os efeitos da perda de pacotes e das alterações na rede. Como também fornece criptografia por padrão, o uso do HTTP/3 mitiga o risco de ataques. 

[Globalmente em 2025](https://radar.cloudflare.com/year-in-review/2025/#http-versions), 50% das solicitações para a Cloudflare foram feitas via HTTP/2, 29% via HTTP/1.x e os 21% restantes via HTTP/3. Essas participações permaneceram praticamente inalteradas [desde 2024](https://radar.cloudflare.com/year-in-review/2024#http-versions). O HTTP/2 e o HTTP/3 ganharam apenas frações de ponto percentual este ano.

_Distribuição do tráfego por versão HTTP em 2025, mundialmente_

Geograficamente, o uso de HTTP/3 parece estar aumentando e se espalhando. No ano passado, notamos que observamos oito países/regiões enviando mais de um terço de suas solicitações via HTTP/3. Em 2025, 15 países/regiões enviaram mais de um terço das solicitações por HTTP/3. A Geórgia, com uma taxa de adoção de 38%, excedeu por pouco a taxa máxima de adoção de 37% registrada em Reunião em 2024. (Analisando [dados históricos](https://radar.cloudflare.com/adoption-and-usage/ge?dateStart=2025-01-01&dateEnd=2025-12-02), a Geórgia [começou o ano](https://radar.cloudflare.com/adoption-and-usage/ge?dateStart=2025-01-01&dateEnd=2025-01-07) em torno de 46% de adoção de HTTP/3, mas caiu no primeiro semestre do ano antes de se estabilizar). A Armênia teve o maior aumento na adoção de HTTP/3 em relação ao ano anterior, saltando de 25% para 37%. 

Sete países/regiões apresentaram níveis gerais de uso de HTTP/3 abaixo de 10% devido aos altos níveis de tráfego HTTP/1.x originado por bots. Isso inclui Hong Kong, Dominica, Cingapura, Irlanda, Irã, Seicheles e Gibraltar. 

### Bibliotecas e estruturas baseadas em JavaScript continuam sendo ferramentas essenciais para a criação de sites

Para criar um site moderno, os desenvolvedores precisam integrar de forma competente uma coleção crescente de bibliotecas e estruturas com ferramentas e plataformas de terceiros. Todos esses componentes devem funcionar em conjunto para garantir uma experiência do usuário de alto desempenho, rica em recursos e sem problemas. Assim como nos anos anteriores, usamos o [URL Scanner do Cloudflare Radar](https://radar.cloudflare.com/scan) para analisar sites associados aos [5 mil principais domínios](https://radar.cloudflare.com/domains) para identificar as [tecnologias e serviços mais populares](https://radar.cloudflare.com/year-in-review/2025/#website-technologies) usados em onze categorias. 

O [jQuery](https://jquery.com/) se auto descreve como uma biblioteca JavaScript rápida, pequena e rica em recursos, e nossa análise constatou sua presença em 8 vezes mais sites do que o [Slick](https://kenwheeler.github.io/slick/), uma biblioteca JavaScript utilizada para exibir carrosséis de imagens. O [React](https://react.dev/) permaneceu a principal estrutura JavaScript utilizada para construir interfaces web, presente em duas vezes mais sites analisados do que o [Vue.js](https://vuejs.org/). PHP, Node.js e Java continuaram sendo as linguagens/tecnologias de programação mais populares, mantendo uma liderança expressiva sobre outras linguagens, incluindo Ruby, Python, Perl e C.

_Principais tecnologias de sites, categoria de bibliotecas JavaScript em 2025_

O [WordPress](https://wordpress.org/) continuou sendo o sistema de gerenciamento de conteúdo (CMS) mais popular, embora sua participação nos sites verificados tenha diminuído para 47%, com a diferença distribuída entre os ganhos observados por vários concorrentes. [HubSpot](https://www.hubspot.com/) e [Marketo](https://business.adobe.com/products/marketo.html) continuaram sendo as principais plataformas de automação de marketing, com uma participação combinada 10% maior em relação ao ano anterior. Entre as ferramentas de teste A/B, a participação do [VWO](https://vwo.com/) cresceu oito pontos percentuais em relação ao ano anterior, ampliando sua liderança sobre o [Optimizely](https://www.optimizely.com/), enquanto o [Google Optimize](https://support.google.com/analytics/answer/12979939?hl=en), que foi descontinuado em setembro de 2023, viu sua participação cair de 14% para 4%.

### Um quinto das chamadas de API automatizadas foram feitas por clientes baseados no Go

As interfaces de programação de aplicativos (APIs) são a base dos sites dinâmicos modernos e dos aplicativos nativos e baseados na web. Esses sites e aplicativos dependem muito de chamadas de API automatizadas para fornecer informações personalizadas. Ao analisar o tráfego da web protegido e entregue pela Cloudflare, podemos identificar as chamadas feitas aos endpoints de API. Ao aplicar heurísticas a essas chamadas relacionadas à API, que não foram feitas por uma pessoa usando um navegador ou aplicativo móvel nativo, podemos identificar as [principais linguagens usadas para criar clientes de API](https://radar.cloudflare.com/year-in-review/2025/#api-client-language-popularity).

Em 2025, 20% das chamadas de API automatizadas foram feitas por clientes baseados em Go, representando um crescimento significativo em relação à participação de 12% do Go em 2024. A participação do Python também aumentou em relação ao ano anterior, passando de 9,6% para 17%. O Java saltou para o terceiro lugar, atingindo uma participação de 11,2%, contra 7,4% em 2024. O [Node.js](http://node.js), a segunda linguagem mais popular do ano passado, viu sua participação cair para apenas 8,3% em 2025, o que o empurrou para o quarto lugar, enquanto o .NET permaneceu na última posição das cinco primeiras, caindo para apenas 2,3%.

_Linguagens automatizadas mais populares de clientes de API em 2025_

### O Google continua sendo o principal mecanismo de busca, com Yandex, Bing e DuckDuckGo como concorrentes distantes

A Cloudflare está em uma posição única para avaliar a [participação de mercado dos mecanismos de busca](https://radar.cloudflare.com/year-in-review/2025/#search-engine-market-share), pois protegemos sites e aplicativos de milhões de clientes. Para tanto, desde o quarto trimestre de 2021, temos publicado [relatórios](https://radar.cloudflare.com/reports) trimestrais sobre esses dados. Usamos o [cabeçalho Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) HTTP para identificar o mecanismo de busca que envia tráfego para sites e aplicativos de clientes, e apresentar os dados de participação de mercado como um agregado geral, bem como divididos por tipo de dispositivo e sistema operacional. (As informações sobre o tipo de dispositivo e o sistema operacional são baseadas nos cabeçalhos de solicitação HTTP [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) e [Client Hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints)).

Globalmente, o Google foi o que mais direcionou tráfego para sites protegidos e entregues pela Cloudflare, com uma participação de quase 90% em 2025. Os outros mecanismos de busca entre os cinco primeiros incluem Bing (3,1%), Yandex (2,0%), Baidu (1,4%) e DuckDuckGo (1,2%). Analisando as tendências ao longo do ano, o Yandex caiu de uma participação de 2,5% em maio para 1,5% em julho, enquanto o Baidu cresceu de 0,9% em abril para 1,6% em junho.

_Participação geral no mercado de mecanismos de busca em todo o mundo em 2025._

Os usuários da Yandex estão baseados principalmente na [Rússia](https://radar.cloudflare.com/year-in-review/2025/ru#search-engine-market-share), onde a plataforma doméstica detém uma participação de mercado de 65%, quase o dobro da do Google, com 34%. Na [República Tcheca](https://radar.cloudflare.com/year-in-review/2025/cz#search-engine-market-share), os usuários preferem o Google (84%), mas a participação de 7,7% do mecanismo de busca local Seznam é um desempenho notável em comparação com os mecanismos de busca em segundo lugar em outros países. 

 _Participação geral no mercado de mecanismos de busca em 2025, República Tcheca_

No tráfego de sistemas “desktop” agregado globalmente, a participação de mercado do Google cai para cerca de 80%, enquanto a do Bing sobe para quase 11%. Isso provavelmente se deve ao domínio contínuo de mercado dos sistemas baseados em Windows. No Windows, o Google responde por apenas 76% do tráfego, enquanto o Bing responde por cerca de 14%. No tráfego de dispositivos móveis, o Google detém quase 93% da participação de mercado, com a mesma participação observada para o tráfego de dispositivos Android e iOS.

_Participação geral de mercado de mecanismos de busca em 2025, sistemas baseados em Windows_

Para obter detalhes adicionais, incluindo mecanismos de busca agregados em "Outros", consulte os [relatórios de referência de mecanismos de busca](https://radar.cloudflare.com/reports/search-engines) trimestrais no Cloudflare Radar.

### O Chrome continua sendo o navegador líder em todas as plataformas e sistemas operacionais, exceto no iOS, onde o Safari detém a maior participação

A Cloudflare também está em uma posição única para medir a [participação de mercado dos navegadores](https://radar.cloudflare.com/year-in-review/2025/#browser-market-share), e publicamos [relatórios](https://radar.cloudflare.com/reports) trimestrais sobre o assunto há vários anos. Para identificar o navegador e o sistema operacional associado que fazem as solicitações de conteúdo, usamos informações dos cabeçalhos HTTP [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) e [Client Hints](https://developer.mozilla.org/en-US/docs/Web/HTTP/Client_hints). Apresentamos os dados de participação de mercado dos navegadores como um agregado geral, bem como divididos por tipo de dispositivo e sistema operacional. Observe que as participações dos navegadores disponíveis em computadores e dispositivos móveis, como o Chrome ou o Safari, são apresentadas de forma agregada.

Globalmente, dois terços do tráfego de solicitações para a Cloudflare vieram do Chrome em 2025, semelhante à sua participação no ano anterior. O Safari, disponível exclusivamente para dispositivos Apple, foi o segundo navegador mais popular, com uma participação de mercado de 15,4%. Em seguida, vieram o Microsoft Edge (7,4%), o Mozilla Firefox (3,7%) e o Samsung Internet (2,3%). 

 _Participação geral no mercado de navegadores em 2025, mundialmente_

Na [Rússia](https://radar.cloudflare.com/year-in-review/2025/ru#browser-market-share), o Chrome continua sendo o mais popular, com uma participação de 44%. No entanto, o navegador doméstico Yandex Browser uma sólida segunda posição, com uma participação de mercado de 33%, em comparação com as participações abaixo de 10% do Safari, Edge e Opera. Curiosamente, em junho, o Yandex Browser superou o Chrome por um ponto percentual (39% contra 38%), antes de perder uma parcela significativa do mercado para o Chrome ao longo do ano.

_Participação geral no mercado de navegadores em 2025, Rússia_

Como navegador padrão no iOS, o Safari é de longe o navegador mais popular nesses dispositivos, com uma participação de mercado de 79%, quatro vezes superior à quota de 19% do Chrome. Menos de 1% das solicitações vêm do DuckDuckGo, Firefox e QQ Browser (desenvolvido na China pela Tencent). Em contraste, no Android, 85% das solicitações são do Chrome, enquanto o Samsung Internet, fornecido pelo fabricante, ocupa um distante segundo lugar, com uma participação de 6,6%. O Huawei Browser, outro navegador fornecido pelo fornecedor, está em terceiro lugar com apenas 1%. E, apesar de ser o navegador padrão no Windows, a participação de 19% do Edge é insignificante em comparação com o Chrome, que lidera com 69% de participação nesse sistema operacional.

_Participação geral no mercado de navegadores web em 2025, dispositivos iOS_

Para obter mais detalhes, incluindo navegadores agregados em "Outros", consulte os [relatórios de participação de navegadores no mercado](https://radar.cloudflare.com/reports/browser) trimestrais no Cloudflare Radar.

## Conectividade

### Quase metade das 174 principais interrupções na internet observadas em todo o mundo em 2025 foram causadas por interrupções regionais e nacionais da conectividade à internet determinadas por governos

As interrupções na internet continuam sendo uma ameaça constante e o impacto em potencial dessas interrupções continua crescendo, pois podem levar a perdas econômicas, interrupção de serviços educacionais e governamentais e comunicação limitada. Durante 2025, abordamos interrupções significativas na internet e suas causas associadas em nossos posts de resumo trimestrais ([1º trimestre](https://blog.cloudflare.com/q1-2025-internet-disruption-summary/), [2º trimestre](https://blog.cloudflare.com/q2-2025-internet-disruption-summary/), [3º trimestre](https://blog.cloudflare.com/q3-2025-internet-disruption-summary/)), bem como posts independentes cobrindo as principais interrupções em [Portugal e Espanha](https://blog.cloudflare.com/how-power-outage-in-portugal-spain-impacted-internet/) e [Afeganistão](https://blog.cloudflare.com/nationwide-internet-shutdown-in-afghanistan/). A [Central de interrupções do Cloudflare Radar](https://radar.cloudflare.com/outage-center) rastreia essas interrupções na internet e usa os dados de tráfego da Cloudflare para obter insights sobre seu escopo e duração.

Quase metade das [interrupções observadas](https://radar.cloudflare.com/year-in-review/2025/#internet-outages) este ano estavam relacionadas a interrupções da internet com o objetivo de impedir fraudes em provas acadêmicas. Países como [Iraque,](https://x.com/CloudflareRadar/status/1930310203083210760) [Síria](https://x.com/CloudflareRadar/status/1952002641896288532) e [Sudão](https://blog.cloudflare.com/q3-2025-internet-disruption-summary/#sudan) implementaram novamente interrupções regulares de várias horas ao longo de várias semanas durante os períodos de provas. Outras interrupções determinadas por governos na [Líbia](https://x.com/CloudflareRadar/status/1924531952993841639) e na [Tanzânia](https://x.com/CloudflareRadar/status/1983502557868666900) foram implementadas em resposta a protestos e agitação civil, enquanto no [Afeganistão](https://blog.cloudflare.com/nationwide-internet-shutdown-in-afghanistan/), o Talibã ordenou a interrupção da conectividade à internet por fibra ótica em várias províncias como parte de um esforço para “evitar a imoralidade”.

Os cortes de cabos, que afetam a infraestrutura de fibra óptica submarina e doméstica, também foram uma das principais causas de interrupções da internet em 2025. Esses cortes resultaram em provedores de rede em países/regiões, incluindo os [Estados Unidos](https://blog.cloudflare.com/q3-2025-internet-disruption-summary/#texas-united-states), [África do Sul](https://blog.cloudflare.com/q3-2025-internet-disruption-summary/#south-africa), [Haiti](https://blog.cloudflare.com/q2-2025-internet-disruption-summary/#digicel-haiti), [Paquistão](https://blog.cloudflare.com/q3-2025-internet-disruption-summary/#pakistan-united-arab-emirates) e [Hong Kong](https://x.com/CloudflareRadar/status/1910709632756019219), que sofreram interrupções de serviço que duraram de algumas horas a vários dias. Outras interrupções notáveis incluem uma causada por um [incêndio](https://bsky.app/profile/radar.cloudflare.com/post/3ltf6jtxd5s2p) em um edifício de telecomunicações no Cairo, Egito, que interrompeu a conectividade com a internet em vários provedores de serviços durante vários dias, e outra na [Jamaica](https://x.com/CloudflareRadar/status/1983188999461319102), onde os danos causados pelo furacão Melissa resultaram em uma diminuição do tráfego da internet na ilha por mais de uma semana.

Na [linha do tempo](https://radar.cloudflare.com/year-in-review/2025#internet-outages) do microsite Análise anual, passar o mouse sobre um ponto exibe informações sobre essa interrupção, e clicar nele leva a insights adicionais.

_Mais de 170 grandes interrupções na internet foram observadas em todo o mundo durante 2025_

### Globalmente, menos de um terço das solicitações de pilha dupla foram feitas por IPv6, enquanto na Índia, mais de dois terços foram

O espaço de endereços IPv4 disponível está praticamente esgotado [há uma década ou mais](https://ipv4.potaroo.net/), embora soluções como a [Tradução de Endereços de Rede (NAT)](https://en.wikipedia.org/wiki/Network_address_translation) tenham permitido que os provedores de rede ampliassem os recursos limitados do IPv4. Isso contribuiu em parte para retardar a adoção do [IPv6](https://www.rfc-editor.org/rfc/rfc1883), projetado em meados da década de 1990 como um protocolo sucessor do IPv4, e oferece um espaço de endereços expandido destinado a suportar melhor o crescimento esperado no número de dispositivos conectados à internet.

Por quase 15 anos, a Cloudflare tem sido uma defensora ativa e expressiva do IPv6, lançando soluções como o [Gateway IPv6 automático](https://blog.cloudflare.com/introducing-cloudflares-automatic-ipv6-gatewa/) em 2011, que possibilitou a compatibilidade com o IPv6 gratuita para todos os nossos clientes, e a [compatibilidade com o IPv6 por padrão para todos os nossos clientes](https://blog.cloudflare.com/i-joined-cloudflare-on-monday-along-with-5-000-others) em 2014. Simplificando, a compatibilidade do lado do servidor é apenas metade do que é necessário para impulsionar a adoção do IPv6, porque as conexões do usuário final também precisam ser compatíveis. Ao agregar e analisar a versão do IP usada para as solicitações feitas à Cloudflare ao longo do ano, podemos obter informações sobre a distribuição do tráfego entre IPv6 e IPv4.

[Globalmente](https://radar.cloudflare.com/year-in-review/2025/#ipv6-adoption), 29% das solicitações compatíveis com IPv6 (“[pilha dupla](https://www.techopedia.com/definition/19025/dual-stack-network)”) foram feitas por IPv6, um aumento de um ponto percentual em relação a [28% em 2024](https://radar.cloudflare.com/year-in-review/2024#ipv6-adoption). A Índia novamente liderou a lista com uma taxa de adoção do IPv6 de 67%, seguida por apenas três outros países/regiões ([Malásia](https://radar.cloudflare.com/year-in-review/2025/my#ipv6-adoption), [Arábia Saudita](https://radar.cloudflare.com/year-in-review/2025/sa#ipv6-adoption) e [Uruguai](https://radar.cloudflare.com/year-in-review/2025/uy#ipv6-adoption)) que também fizeram mais da metade dessas solicitações por meio do IPv6, o mesmo que no ano passado. Alguns dos maiores ganhos foram observados em [Belize](https://radar.cloudflare.com/year-in-review/2025/bz#ipv6-adoption), que cresceu de 4,3% para 24% em relação ao ano anterior, e no [Catar](https://radar.cloudflare.com/year-in-review/2025/qa#ipv6-adoption), que viu sua adoção quase dobrar, atingindo 33% em 2025. Infelizmente, alguns países/regiões ainda estão atrás dos líderes, com 94 registrando taxas de adoção abaixo de 10%, incluindo [Rússia](https://radar.cloudflare.com/year-in-review/2025/ru#ipv6-adoption) (8,6%), [Irlanda](https://radar.cloudflare.com/year-in-review/2025/ie#ipv6-adoption) (6,5%) e [Hong Kong](https://radar.cloudflare.com/year-in-review/2025/hk#ipv6-adoption) (3,0%). Ainda mais atrás estão os 20 países/regiões com taxas de adoção abaixo de 1%, incluindo [Tanzânia](https://radar.cloudflare.com/year-in-review/2025/tz#ipv6-adoption) (0,9%), [Síria](https://radar.cloudflare.com/year-in-review/2025/sy#ipv6-adoption) (0,3%) e [Gibraltar](https://radar.cloudflare.com/year-in-review/2025/gi#ipv6-adoption) (0,1%).

_Distribuição do tráfego por versão de IP em 2025, mundialmente_

 _Os cinco principais países em adoção de IPv6 em 2025_

### Os países europeus apresentaram algumas das maiores velocidades de download, todas acima de 200 Mbps. A Espanha permaneceu consistentemente entre os principais locais em todas as métricas de qualidade da internet medidas

Na última década, recorremos aos testes de velocidade da internet para diversas finalidades: verificar a honestidade de nossos provedores de serviço, solucionar problemas de conexão ou exibir velocidades de download particularmente altas nas redes sociais. Na verdade, nos acostumamos a focar nas velocidades de download como a principal medida da qualidade de uma conexão. Embora seja uma métrica absolutamente importante, para casos de uso cada vez mais populares, como videoconferência, streaming ao vivo e jogos on-line, altas velocidades de upload e baixa latência também são essenciais. No entanto, mesmo quando os provedores de internet oferecem níveis de serviço que incluem altas velocidades simétricas e menor latência, a adesão do consumidor costuma ser mista devido ao custo, disponibilidade ou outros problemas.

Os testes em [speed.cloudflare.com](https://speed.cloudflare.com/) medem as velocidades de download e upload, bem como a latência com e sem carga. Ao agregar os resultados de [testes realizados em todo o mundo durante 2025](https://radar.cloudflare.com/year-in-review/2025/#internet-quality), podemos obter uma perspectiva por país/região sobre os valores médios dessas métricas de [qualidade de conexão](https://developers.cloudflare.com/radar/glossary/#connection-quality), bem como insights sobre a distribuição das medições.

A Europa esteve bem representada entre os que apresentaram as maiores velocidades médias de download em 2025. [Espanha](https://radar.cloudflare.com/year-in-review/2025/es#internet-quality), [Hungria](https://radar.cloudflare.com/year-in-review/2025/hu#internet-quality), [Portugal](https://radar.cloudflare.com/year-in-review/2025/pt#internet-quality), [Dinamarca](https://radar.cloudflare.com/year-in-review/2025/dk#internet-quality), [Romênia](https://radar.cloudflare.com/year-in-review/2025/ro#internet-quality) e [França](https://radar.cloudflare.com/year-in-review/2025/fr#internet-quality) ficaram todos entre os dez principais, com a Espanha e a Hungria apresentando velocidades médias de download acima de 300 Mbps. A média da Espanha aumentou 25 Mbps desde 2024, enquanto o aumento da Hungria foi de 46 Mbps. Enquanto isso, os países asiáticos apresentaram muitas das maiores velocidades médias de upload, com [Coreia do Sul](https://radar.cloudflare.com/year-in-review/2025/kr#internet-quality), [Macau,](https://radar.cloudflare.com/year-in-review/2025/mo#internet-quality) [Cingapura](https://radar.cloudflare.com/year-in-review/2025/sg#internet-quality) e [Japão](https://radar.cloudflare.com/year-in-review/2025/jp#internet-quality) entre os dez principais, todos com médias superiores a 130 Mbps.

Mas a Espanha também liderou a lista na métrica de upload, com 206 Mbps, um aumento de 13 Mbps em relação a 2024. A forte presença do país em ambas as métricas de velocidade pode ser atribuída ao [“UNICO-Broadband”](https://commission.europa.eu/projects/unico-broadband_en), uma “ _chamada de projetos de operadoras de telecomunicações visando a implantação de infraestrutura de banda larga de alta velocidade capaz de fornecer serviços com velocidades simétricas de pelo menos 300 Mbps, escaláveis para 1 Gbps_ ”, que visava cobrir 100% da população em 2025.

_Países/regiões com as maiores velocidades de download em 2025, mundialmente_

Conforme mencionado acima, conexões de baixa latência são necessárias para proporcionar aos usuários uma boa experiência de [jogos](https://www.screenbeam.com/wifihelp/wifibooster/how-to-reduce-latency-or-lag-in-gaming-2/#:~:text=Latency%20is%20measured%20in%20milliseconds,%2C%2020%2D40ms%20is%20optimal.) e [videoconferências/streaming](https://www.haivision.com/glossary/video-latency/#:~:text=Low%20latency%20is%20typically%20defined,and%20streaming%20previously%20recorded%20events.). A [métrica de latência](https://blog.cloudflare.com/introducing-radar-internet-quality-page/#connection-speed-quality-data-is-important) pode ser dividida em latência carregada e ociosa. A primeira mede a latência em uma conexão carregada, onde a largura de banda está sendo consumida ativamente, enquanto a segunda mede a latência em uma conexão "ociosa", quando não há outro tráfego de rede presente. (Essas definições são da perspectiva do aplicativo de teste de velocidade). 

Em 2025, vários países europeus estavam entre aqueles com as menores latências ociosas e carregadas. Para a latência ociosa média, a [Islândia](https://radar.cloudflare.com/year-in-review/2025/is#internet-quality) registrou o menor valor, com 13 ms, apenas 2 ms melhor que a [Moldávia](https://radar.cloudflare.com/year-in-review/2025/md#internet-quality). Além destes dois, [Portugal](https://radar.cloudflare.com/year-in-review/2025/pt#internet-quality), [Espanha](https://radar.cloudflare.com/year-in-review/2025/es#internet-quality) e [Hungria](https://radar.cloudflare.com/year-in-review/2025/hu#internet-quality) também ficaram entre os dez principais, todos com latência ociosa média abaixo de 20 ms. A Moldávia liderou a lista de países/regiões com a menor latência carregada média, com 73 ms. Hungria, Espanha, [Bélgica](https://radar.cloudflare.com/year-in-review/2025/be#internet-quality), Portugal, [Eslováquia](https://radar.cloudflare.com/year-in-review/2025/sk#internet-quality) e [Eslovênia](https://radar.cloudflare.com/year-in-review/2025/si#internet-quality) também integraram os dez principais, todos com latência carregada média, abaixo de 100 ms.

_Latência ociosa/carregada medida, Moldávia_

### Londres e Los Angeles foram pontos de destaque para a atividade de teste de velocidade da Cloudflare em 2025

Como discutimos acima, o teste de velocidade em [speed.cloudflare.com](http://speed.cloudflare.com) mede as velocidades de conexão e a latência de um usuário. Analisamos os resultados agregados desses testes, destacando os países/regiões com os melhores resultados. No entanto, também nos perguntamos sobre a atividade de testes em todo o mundo. Onde os usuários estão mais preocupados com a qualidade da conexão e com que frequência realizam testes? [Uma nova visualização animada da Análise anual ilustra a atividade de teste de velocidade](https://radar.cloudflare.com/year-in-review/2025/#speed-tests), agregada semanalmente.

Os dados são agregados em nível regional e a atividade associada é plotada no mapa com círculos dimensionados com base no número de testes realizados a cada semana. Observe que os locais com menos de 100 testes de velocidade por semana não foram plotados. Analisando o volume de testes ao longo do ano, as regiões metropolitanas de Londres e Los Angeles foram as mais ativas, assim como Tóquio, Hong Kong e diversas cidades dos EUA.

Ao animar o gráfico para visualizar as mudanças ao longo do ano, observa-se diversos picos semanais no volume de testes. Isso inclui a área de Nairobi, no Quênia, durante o período de sete dias com término em 10 de junho; a área de Teerã, no Irã, no período que terminou em 29 de julho; diversas áreas na Rússia, no período que terminou em 5 de agosto; e a área de Karnataka, na Índia, no período que terminou em 28 de outubro. Não está claro o que causou esses aumentos no volume de testes. A [Central de interrupções do Cloudflare Radar](https://radar.cloudflare.com/outage-center?dateStart=2025-01-01&dateEnd=2025-12-02) não mostra nenhuma interrupção observada na internet que afete essas áreas nesses horários, portanto, é improvável que sejam assinantes testando a restauração da conectividade.

_Atividade do teste de velocidade da Cloudflare por local em 2025_

### Mais da metade do tráfego de solicitações vem de dispositivos móveis em 117 países/regiões

Para o bem ou para o mal, ao longo do último quarto de século, os dispositivos móveis se tornaram parte indispensável da vida cotidiana. A adoção varia em todo o mundo. Estatísticas do [Banco Mundial](https://blogs.worldbank.org/en/voices/Mobile-phone-ownership-is-widespread-Why-is-digital-inclusion-still-lagging) mostram vários países/regiões com taxas de propriedade de telefones celulares acima de 90%, enquanto em vários outros, as taxas estão abaixo de 10%, em outubro de 2025. Em alguns países/regiões, os dispositivos móveis se conectam à internet principalmente através de Wi-Fi, enquanto outros países/regiões são "mobile first", onde os serviços 4G/5G são o principal meio de acesso à internet.

As informações contidas no cabeçalho [User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) incluído em cada solicitação à Cloudflare nos permitem categorizá-lo como proveniente de um dispositivo móvel, desktop ou outro tipo de dispositivo. [A agregação dessa categorização globalmente em 2025](https://radar.cloudflare.com/year-in-review/2025/#mobile-vs-desktop) revelou que 43% das solicitações foram feitas por dispositivos móveis, um aumento em relação aos [41% em 2024](https://radar.cloudflare.com/year-in-review/2024#mobile-vs-desktop). O restante veio de dispositivos "clássicos" como notebooks e desktops. Semelhante a uma observação [feita no ano passado](https://blog.cloudflare.com/radar-2024-year-in-review/#41-3-of-global-traffic-comes-from-mobile-devices-in-nearly-100-countries-regions-the-majority-of-traffic-comes-from-mobile-devices), essas participações no tráfego estavam em linha com as medidas nos relatórios da Análise anual desde 2022, sugerindo que o uso de dispositivos móveis atingiu um "estado de estabilidade".

Em 117 países/regiões, mais da metade das solicitações vieram de dispositivos móveis, com destaque para o [Sudão](https://radar.cloudflare.com/year-in-review/2025/sd#mobile-vs-desktop) e o [Malawi](https://radar.cloudflare.com/year-in-review/2025/mw#mobile-vs-desktop) com 75% e 74%, respectivamente. Outros cinco países/regiões africanos, [Eswatini (Suazilândia)](https://radar.cloudflare.com/year-in-review/2025/sz#mobile-vs-desktop), [Iêmen](https://radar.cloudflare.com/year-in-review/2025/ye#mobile-vs-desktop), [Botsuana](https://radar.cloudflare.com/year-in-review/2025/bw#mobile-vs-desktop), [Moçambique](https://radar.cloudflare.com/year-in-review/2025/mz#mobile-vs-desktop) e [Somália](https://radar.cloudflare.com/year-in-review/2025/so#mobile-vs-desktop), também tiveram participações de solicitações móveis acima de 70% em 2025, em consonância com a [alta taxa de propriedade de telefones celulares](https://voxdev.org/topic/understanding-mobile-phone-and-internet-use-across-world) na região. Entre os países/regiões com baixa participação no tráfego de dispositivos móveis, [Gibraltar](https://radar.cloudflare.com/year-in-review/2025/gi#mobile-vs-desktop) foi o único abaixo de 10% (5,1%), e apenas outros seis registraram menos de um quarto das solicitações de dispositivos móveis. Isto é menos do que em [2024](https://radar.cloudflare.com/year-in-review/2024#mobile-vs-desktop), quando uma dúzia de países/regiões apresentava uma participação de dispositivos móveis abaixo de 25%.

_Distribuição do tráfego por tipo de dispositivo em 2025, mundialmente_

 _Distribuição global do tráfego por tipo de dispositivo em 2025._

## Segurança

### 6% do tráfego global na rede da Cloudflare foi mitigado pelos nossos sistemas, seja como possivelmente malicioso ou por motivos definidos pelo cliente

A Cloudflare mitiga automaticamente o tráfego de ataque direcionado a sites e aplicativos de clientes, utilizando técnicas de mitigação de [DDoS](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) ou [regras gerenciadas do firewall de aplicativos web (WAF)](https://developers.cloudflare.com/waf/managed-rules/), protegendo-os de diversas ameaças representadas por agentes maliciosos. Também permitimos que os clientes mitiguem o tráfego, mesmo que não seja malicioso, usando técnicas como [limitação de taxa](https://developers.cloudflare.com/waf/rate-limiting-rules/) de solicitações ou [bloqueio de todo o tráfego de um determinado local](https://developers.cloudflare.com/waf/tools/ip-access-rules/). A necessidade de fazer isso pode ser motivada por requisitos regulatórios ou da empresa. Analisamos a parcela geral do tráfego para a rede da Cloudflare ao longo de 2025 que foi mitigada por qualquer motivo, bem como a parcela que foi bloqueada como um ataque de DDoS ou pelas regras gerenciadas do WAF.

Este ano, [6,2% do tráfego global foi mitigado](https://radar.cloudflare.com/year-in-review/2025/#mitigated-traffic), uma queda de um quarto de ponto percentual [em relação a 2024](https://radar.cloudflare.com/year-in-review/2024#mitigated-traffic). 3,3% do tráfego foi mitigado como ataque de DDoS ou por regras gerenciadas, um aumento de um décimo de ponto percentual em relação ao ano anterior. Mitigações gerais foram aplicadas a mais de 10% do tráfego proveniente de mais de 30 países/regiões, enquanto 14 países/regiões tiveram mitigações de DDoS/WAF aplicadas a mais de 10% do tráfego de origem. Ambas as contagens apresentaram queda em comparação com 2024. 

A Guiné Equatorial apresentou as maiores participações de tráfego mitigado, com 40% mitigado de forma geral e 29% com mitigações de DDoS/WAF aplicadas. Essas participações cresceram no ano passado, de 26% (geral) e 19% (DDoS/WAF). Em contraste, Dominica apresentou as menores participações de tráfego mitigado, com apenas 0,7% do tráfego mitigado, com mitigações de DDoS/WAF aplicadas a somente 0,1%.

O grande aumento no tráfego mitigado observado em julho no gráfico abaixo deve-se a uma campanha de ataque de DDoS muito grande que teve como alvo principal um único domínio de cliente da Cloudflare.

_Tendências de tráfego mitigado em 2025, mundialmente_

### 40% do tráfego de bots global teve origem nos Estados Unidos, sendo que o Amazon Web Services e o Google Cloud foram responsáveis por um quarto desse tráfego

Um [bot](https://developers.cloudflare.com/bots/concepts/bot/) é um aplicativo de software programado para executar determinadas tarefas, e a Cloudflare usa [heurísticas](https://blog.cloudflare.com/bots-heuristics/) avançadas para diferenciar o tráfego de bots do tráfego humano, [classificando](https://developers.cloudflare.com/bots/concepts/bot-score/) cada solicitação de acordo com a probabilidade de se originar de um bot ou de um usuário humano. Ao monitorar o tráfego suspeito de ser de bots, os proprietários de sites e aplicativos podem detectar e, se necessário, bloquear atividades possivelmente maliciosas. No entanto, nem todos os bots são maliciosos. Os bots também podem ser úteis, e a Cloudflare mantém um [diretório de bots verificados](https://radar.cloudflare.com/bots/directory?kind=all) que inclui aqueles usados para [indexação de mecanismos de busca](https://radar.cloudflare.com/bots/directory?category=SEARCH_ENGINE_CRAWLER&kind=all), [verificação de segurança](https://radar.cloudflare.com/bots/directory?category=SECURITY&kind=all) e [monitoramento de sites/aplicativos](https://radar.cloudflare.com/bots/directory?category=MONITORING_AND_ANALYTICS&kind=all). Independentemente da intenção, analisamos [a origem do tráfego de bots em 2025](https://radar.cloudflare.com/year-in-review/2025/#bot-traffic-sources), usando o endereço de IP de uma solicitação para identificar a rede ([sistema autônomo](https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/)) e o país/região associados ao bot que fez a solicitação. 

Globalmente, dez países/regiões principais representaram 71% do tráfego de bots observado. Quarenta por cento originou-se dos Estados Unidos, muito à frente da participação de 6,5% da Alemanha. A participação dos EUA aumentou mais de cinco pontos percentuais [em relação a 2024](https://radar.cloudflare.com/year-in-review/2024#bot-traffic-sources), enquanto a participação da Alemanha caiu uma fração de ponto percentual. Os demais países entre os dez principais contribuíram com percentuais de tráfego de bots inferiores a 5% em 2025.

_Distribuição global do tráfego de bots por país/região de origem em 2025_

Ao analisar o tráfego de bots por rede, constatamos que as plataformas em nuvem continuaram entre as principais origens. Isso se deve a uma série de fatores, incluindo a facilidade de uso de ferramentas automatizadas para provisionar rapidamente recursos de computação, seu custo relativamente baixo, sua presença geográfica amplamente distribuída e a conectividade de alta largura de banda das plataformas com a internet. 

Dois sistemas autônomos associados ao Amazon Web Services representaram um total de 14,4% do tráfego de bots observado, e dois associados ao Google Cloud foram responsáveis por um total de 9,7% do tráfego de bots. Em seguida, veio o Microsoft Azure, que originou 5,5% do tráfego de bots. As participações das três plataformas aumentaram em comparação com 2024. Essas plataformas em nuvem têm uma forte presença regional de data centers em muitos dos dez países/regiões principais. Em outras partes do mundo, os provedores de telecomunicações locais frequentemente representaram a maior parte do tráfego de bots automatizado observado nesses países/regiões.

_Distribuição global do tráfego de bots por rede de origem em 2025_

### No ano de 2025, as organizações da vertical de “Pessoas e Sociedade” foram as mais visadas

Os invasores estão constantemente mudando suas táticas e alvos, diversificando suas estratégias na tentativa de evitar a detecção ou com base nos danos que pretendem causar. Eles podem tentar causar danos financeiros a empresas, visando sites de comércio eletrônico durante períodos de grande movimento, fazer declarações políticas atacando sites relacionados ao governo ou à sociedade civil, ou tentar derrubar oponentes atacando um servidor de jogos. Para identificar atividades de ataque direcionadas ao setor durante 2025, analisamos o tráfego mitigado para clientes que tinham um setor e uma vertical associados em seu registro de cliente. O tráfego mitigado foi agregado semanalmente por país/região de origem em 17 setores visados.

As organizações da vertical "Pessoas e Sociedade" foram as [mais visadas ao longo do ano](https://radar.cloudflare.com/year-in-review/2025/#most-attacked-industries), com 4,4% do tráfego global direcionado à vertical mitigado. Os clientes classificados como “Pessoas e Sociedade” incluem instituições religiosas, organizações sem fins lucrativos, organizações cívicas e sociais e bibliotecas. A vertical iniciou o ano com menos de 2% do tráfego mitigado, mas observou um aumento para 10% na semana de 5 de março e um crescimento para mais de 17% até o final do mês. Outras ondas de ataque direcionadas a esses sites ocorreram no final de abril (chegando a 19,1%) e no início de julho (chegando a 23,2%). Muitas dessas organizações são protegidas pelo Projeto Galileo da Cloudflare, e [este post no blog](https://blog.cloudflare.com/celebrating-11-years-of-project-galileo-global-impact/) detalha os ataques e ameaças que elas enfrentaram em 2024 e 2025.

O setor de jogos/apostas, a [vertical mais visada no ano passado](https://radar.cloudflare.com/year-in-review/2024#most-attacked-industries), viu sua participação em ataques mitigados cair mais da metade em relação ao ano anterior, para apenas 2,6%. Embora se possa esperar que os ataques direcionados a sites de apostas atinjam um pico durante grandes eventos desportivos como o Super Bowl e o March Madness, essa tendência não se verificou, uma vez que a participação de ataques atingiu um pico de 6,5% na semana de 5 de março, um mês após o Super Bowl e algumas semanas antes do início do March Madness.

_Participação global do tráfego mitigado por setor em 2025, visão resumida_

### A segurança do roteamento, medida como a participação em rotas RPKI válidas e no espaço de endereços de IP coberto, apresentou melhorias contínuas ao longo de 2025

O [Border Gateway Protocol (BGP)](https://www.cloudflare.com/learning/security/glossary/what-is-bgp/) é o protocolo de roteamento central da internet, permitindo que o tráfego flua entre a origem e o destino através da comunicação de rotas entre as redes. No entanto, como depende da confiança entre redes conectadas, informações incorretas compartilhadas entre pares (intencionalmente ou não) podem enviar tráfego para o lugar errado, possivelmente para [sistemas controlados por um invasor](https://blog.cloudflare.com/bgp-leaks-and-crypto-currencies/). Para resolver isso, o [Resource Public Key Infrastructure (RPKI)](https://blog.cloudflare.com/rpki/) foi desenvolvido como um método criptográfico de assinatura de registros que associa um anúncio de rota BGP ao número correto do sistema autônomo (AS) de origem para garantir que as informações compartilhadas vieram originalmente de uma rede autorizada. A Cloudflare há muito tempo defende a segurança de roteamento, sendo inclusive participante fundadora do [MANRS CDN and Cloud Programme](https://www.internetsociety.org/news/press-releases/2020/leading-cdn-and-cloud-providers-join-manrs-to-improve-routing-security/) e fornecendo uma [ferramenta pública](https://isbgpsafeyet.com/) que permite aos usuários testar se seu provedor de internet implementou o BGP com segurança. 

Analisamos os dados disponíveis na [página de roteamento](https://radar.cloudflare.com/routing) do Cloudflare Radar para determinar a participação das [rotas válidas do RPKI](https://rpki.readthedocs.io/en/latest/about/help.html) e como essa participação mudou ao longo de 2025, bem como determinar a [participação do espaço de endereços de IP coberto por rotas válidas](https://radar.cloudflare.com/year-in-review/2025/#routing-security). Esta última métrica é notável porque um anúncio de rota cobrindo uma grande quantidade de espaço de endereços de IP (milhões de endereços IPv4) tem um impacto potencial maior do que um anúncio que abrange um pequeno bloco de espaço de endereços de IP (centenas de endereços IPv4).

Começamos 2025 com 50% de rotas IPv4 válidas, crescendo para 53,9% até 2 de dezembro. A proporção de rotas IPv6 válidas aumentou para 60,1%, um aumento de 4,7 pontos percentuais. Observando a participação global do espaço de endereços de IP coberto por rotas válidas, o IPv4 aumentou para 48,5%, um aumento de três pontos percentuais. A participação do espaço de endereços IPv6 coberto por rotas válidas caiu ligeiramente para 61,6%. Embora a variação anual dessas métricas esteja desacelerando, fizemos progressos significativos nos últimos cinco anos. Desde o início de 2020, a participação de rotas RPKI válidas IPv4 e o espaço de endereços IPv4 aumentaram aproximadamente três vezes.

_Participação global de entradas de roteamento válidas do RPKI por versão IP em 2025_

 _Participação no espaço de endereços IP anunciado globalmente coberto por rotas RPKI válidas em 2025_

[ Barbados](https://radar.cloudflare.com/year-in-review/2025/bb#routing-security) apresentou o maior crescimento na participação de rotas IPv4 válidas, aumentando de 2,2% para 20,8%. Analisando as rotas IPv6 válidas, o [Mali](https://radar.cloudflare.com/year-in-review/2025/ml#routing-security) teve o crescimento de participação mais significativo em 2025, passando de 10,0% para 58,3%. 

Barbados também apresentou o maior aumento na participação do espaço IPv4 coberto por rotas válidas, saltando de apenas 2,0% para 18,6%. Em relação ao espaço de endereços IPv6, tanto o [Tajiquistão](https://radar.cloudflare.com/year-in-review/2025/tj#routing-security) quanto a [Dominica](https://radar.cloudflare.com/year-in-review/2025/dm#routing-security) passaram de praticamente não ter espaço coberto por rotas válidas no início do ano para 5,5% e 3,5%, respectivamente. 

### Os tamanhos dos ataques de DDoS hipervolumétricos aumentaram significativamente ao longo do ano 

Em nossa série de relatórios trimestrais sobre DDoS ([1º trimestre](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/), [2º trimestre](https://blog.cloudflare.com/ddos-threat-report-for-2025-q2/), [3º trimestre](https://blog.cloudflare.com/ddos-threat-report-2025-q3/)), destacamos o aumento na frequência e no tamanho de ataques hipervolumétricos na camada de rede direcionados a clientes da Cloudflare e à infraestrutura da Cloudflare. Definimos um “ataque hipervolumétrico na camada de rede” como aquele que opera nas camadas 3 e 4 e que atinge um pico de mais de um terabit por segundo (1 Tbps) ou mais de um bilhão de pacotes por segundo (1 Bpps). Esses relatórios fornecem uma perspectiva trimestral, mas também queríamos [mostrar uma visão da atividade ao longo do ano](https://radar.cloudflare.com/year-in-review/2025/#ddos-attacks) para entender quando os invasores estão mais ativos e como os tamanhos dos ataques aumentaram ao longo do tempo. 

Analisando a atividade de ataques hipervolumétricos em 2025, em termos de Tbps, julho registrou o maior número desses ataques, com mais de 500, enquanto fevereiro apresentou o menor número, com pouco mais de 150. A intensidade dos ataques permaneceu geralmente abaixo de 5 Tbps, embora um ataque de 10 Tbps bloqueado no final de agosto fosse um prenúncio do que estava por vir. Este ataque foi o primeiro de uma campanha de ataques de mais de 10 Tbps que ocorreu durante a primeira semana de setembro, precedendo uma série de ataques de mais de 20 Tbps durante a última semana do mês. No início de outubro, foram observados vários ataques hipervolumétricos cada vez maiores, com o maior do mês [atingindo um pico de 29,7 Tbps](https://blog.cloudflare.com/ddos-threat-report-2025-q3/#aisuru-breaking-records-with-ultrasophisticated-hyper-volumetric-ddos-attacks). No entanto, esse recorde foi logo superado, quando um ataque no início de novembro atingiu 31,4. Tbps.

Em termos de Bpps, a atividade de ataques volumétricos foi muito menor, com novembro registrando o maior número (mais de 140), enquanto apenas três foram observados em fevereiro e junho. A intensidade dos ataques ao longo do ano geralmente se manteve abaixo de 4 Bpps até o final de agosto, embora uma sucessão de ataques cada vez maiores tenha sido observada nos meses seguintes, atingindo o pico em outubro. Embora a intensidade da maioria dos mais de 110 ataques bloqueados em outubro tenha ficado abaixo de 5 Bpps, um ataque de 14 Bpps observado durante o mês foi o maior ataque hipervolumétrico em termos de pacotes por segundo bloqueado durante o ano, superando outros cinco ataques recordes consecutivos ocorridos em setembro.

_Picos de tamanho de ataques de DDoS em 2025_

## Email security

### Mais de 5% das mensagens de e-mail analisadas pela Cloudflare foram consideradas maliciosas

[Estatísticas recentes](https://www.signite.io/emails-are-still-king) indicam que o e-mail continua sendo o principal canal de comunicação para contatos comerciais externos, apesar do crescente uso corporativo de aplicativos de colaboração/mensagens. Devido ao seu amplo uso corporativo, os invasores ainda o consideram um ponto de entrada atraente para as redes corporativas. As ferramentas de IA generativa [facilitam a criação](https://blog.cloudflare.com/dispelling-the-generative-ai-fear-how-cloudflare-secures-inboxes-against-ai-enhanced-phishing/) de e-mails maliciosos altamente direcionados, que se fazem passar de forma convincente por marcas confiáveis ou remetentes legítimos (como executivos corporativos), mas contêm links enganosos, anexos perigosos ou outros tipos de ameaças. O [Cloudflare Email Security](https://www.cloudflare.com/zero-trust/products/email-security/) protege os clientes contra ataques baseados em e-mail, inclusive aqueles realizados por meio de mensagens de e-mail maliciosas direcionadas. 

Em 2025, uma [média de 5,6% dos e-mails analisados pela Cloudflare foram considerados maliciosos](https://radar.cloudflare.com/year-in-review/2025/#malicious-emails). A participação de mensagens processadas pelo Cloudflare Email Security que foram consideradas maliciosas geralmente variou entre 4% e 6% durante a maior parte do ano. Nossos dados mostram um aumento na proporção de e-mails maliciosos a partir de outubro, provavelmente devido a um sistema de classificação aprimorado implementado pelo Cloudflare Email Security. 

 _Tendências de participação global de e-mails maliciosos em 2025_

### Links enganosos, fraude de identidade e falsificação de marca foram os tipos mais comuns de ameaças encontrados em mensagens de e-mail maliciosas

Os links enganosos foram a [principal categoria de ameaças de e-mail maliciosos em 2025](https://radar.cloudflare.com/year-in-review/2025/#top-email-threats), encontrados em 52% das mensagens, um aumento em relação aos [43% de 2024](https://radar.cloudflare.com/year-in-review/2024#top-email-threats). Como o texto de exibição de um hiperlink em HTML pode ser definido arbitrariamente, os invasores podem fazer com que um URL pareça estar vinculado a um site benigno quando, na verdade, ele está realmente vinculado a um recurso malicioso que pode ser usado para roubar credenciais de login ou baixar malware. A proporção de e-mails processados que continham links fraudulentos atingiu 70% no final de abril e, novamente, em meados de novembro.

A fraude de identidade ocorre quando um invasor envia um e-mail alegando ser outra pessoa. Isso pode ser feito usando domínios que parecem semelhantes ou que são falsificados, ou ainda, usar truques com nomes de exibição para parecer que vêm de um domínio confiável. A falsificação de marca é uma forma de fraude de identidade em que um invasor envia uma mensagem de phishing se passando por uma empresa ou marca conhecida. A falsificação de marca também pode usar a falsificação de nome de exibição ou de domínio. A fraude de identidade (38%) e a falsificação de marca (32%) representaram ameaças crescentes em 2025, em comparação com 35% e 23% em 2024, respectivamente. Ambas observaram um aumento em meados de novembro.

_Tendências das categorias de ameaça de e-mail em 2025, mundialmente_

### Quase todas as mensagens de e-mail dos domínios de nível superior .christmas e .lol foram consideradas spam ou maliciosas

Além de fornecer informações sobre tráfego, distribuição geográfica e certificados digitais para domínios de nível superior (TLDs) como [.com](https://radar.cloudflare.com/tlds/com) ou [.us](https://radar.cloudflare.com/tlds/us), o Cloudflare Radar também fornece insights sobre os [TLDs “mais violados”](https://radar.cloudflare.com/security/email#most-abused-tlds), aqueles cujos domínios, segundo nossa avaliação, são responsáveis pela maior parte dos e-mails maliciosos e spam analisados pelo Cloudflare Email Security. A análise é baseada no TLD do domínio de envio, encontrado no cabeçalho "De:" de uma mensagem de e-mail. Por exemplo, se uma mensagem veio de sender@example.com, então example.com é o domínio de envio e .com é o TLD associado. Para a Análise anual, incluímos apenas TLDs dos quais observamos uma média mínima de 30 mensagens por hora.

Com base nas [mensagens analisadas ao longo de](https://radar.cloudflare.com/year-in-review/2025/#most-abused-tlds) 2025, constatamos que[.christmas](https://radar.cloudflare.com/tlds/christmas) e [.lol](https://radar.cloudflare.com/tlds/lol) foram os TLDs mais violados, com 99,8% e 99,6% das mensagens desses TLDs, respectivamente, classificadas como spam ou maliciosas. Ordenando a lista de TLDs pela participação de e-mails maliciosos, [.cfd](https://radar.cloudflare.com/tlds/cfd) e [.sbs](https://radar.cloudflare.com/tlds/sbs) apresentaram mais de 90% dos e-mails analisados classificados como maliciosos. O TLD [.best](https://radar.cloudflare.com/tlds/best) apresentou o pior desempenho em termos de participação de spam, com 69% das mensagens de e-mail classificadas como tal.

_TLDs que originaram a maior porcentagem total de e-mails maliciosos e spam em 2025_

## Conclusão

Embora a internet e a web continuem a evoluir e mudar ao longo do tempo, parece que algumas das principais métricas se tornaram bastante estáveis. No entanto, esperamos que outras métricas, como as que rastreiam as tendências de IA, mudem ao longo dos próximos anos, à medida que esse espaço evolui rapidamente. 

Recomendamos que você visite o [microsite Análise anual do Cloudflare Radar de 2025](https://radar.cloudflare.com/year-in-review/2025) e explore as tendências para o seu país/região, e considere como elas afetam sua organização ao planejar para 2026. Você também pode obter insights quase em tempo real sobre muitas dessas métricas e tendências no [Cloudflare Radar](https://radar.cloudflare.com/). E, como mencionado acima, para obter informações sobre os principais serviços de internet em várias categorias do setor e países/regiões, recomendamos que você leia o [post no blog da Análise anual complementar](https://blog.cloudflare.com/radar-2025-year-in-review-internet-services/).

Em caso de dúvidas, entre em contato com a equipe do Cloudflare Radar em [radar@cloudflare.com](mailto:radar@cloudflare.com) ou nas redes sociais em [@CloudflareRadar](https://twitter.com/CloudflareRadar) (X), [https://noc.social/@cloudflareradar](https://noc.social/@cloudflareradar) (Mastodon) e [radar.cloudflare.com](https://bsky.app/profile/radar.cloudflare.com) (Bluesky).

## Agradecimentos

É preciso um esforço conjunto para que nossa Análise anual aconteça, desde a agregação e análise dos dados, até a criação do microsite e o desenvolvimento do conteúdo associado. Gostaria de agradecer aos membros da equipe que contribuíram para o esforço deste ano, em especial a: Jorge Pacheco, Sabina Zejnilovic, Carlos Azevedo, Mingwei Zhang, Sofia Cardita (análise de dados); André Páscoa, Nuno Pereira (desenvolvimento de front-end); João Tomé (serviços mais populares da internet); David Fidalgo, Janet Villarreal e a equipe de internacionalização (traduções); Jackie Dutton, Kari Linder, Guille Lasarte (Comunicações); Laurel Wamsley (edição do blog); e Paula Tavares (gerenciamento de engenharia), bem como a outros colegas da Cloudflare pelo apoio e assistência.

]]>2Mp06VKep73rBpdUmywpQ2Interrupção da Cloudflare em 5 de dezembro de 2025https://blog.cloudflare.com/pt-br/5-december-2025-outage/ Fri, 05 Dec 2025 00:00:00 GMTA Cloudflare sofreu uma interrupção significativa de tráfego em 5 de dezembro de 2025, começando aproximadamente às 8h47 UTC. O incidente durou aproximadamente 25 minutos até a resolução. Lamentamos o impacto causado aos nossos clientes e à internet. O incidente não foi causado por um ataque, mas sim por alterações de configuração aplicadas para mitigar uma vulnerabilidade recente que afeta componentes do Servidor React em todo o setor.InterrupçãoPost MortemEm 5 de dezembro de 2025, às 08:47 UTC (todos os horários neste blog são UTC), uma parte da rede da Cloudflare começou a apresentar falhas significativas. O incidente foi resolvido às 09:12 (aproximadamente 25 minutos de impacto total), quando todos os serviços foram totalmente restaurados.

Um subconjunto de clientes foi afetado, representando aproximadamente 28% de todo o tráfego HTTP atendido pela Cloudflare. Vários fatores precisaram se combinar para que um cliente individual fosse afetado, conforme descrito abaixo.

O problema não foi causado, direta ou indiretamente, por um ataque cibernético aos sistemas da Cloudflare ou atividade maliciosa de qualquer natureza. Em vez disso, ele foi acionado por alterações feitas em nossa lógica de análise de corpo ao tentar detectar e mitigar uma vulnerabilidade do setor [divulgada esta semana](https://blog.cloudflare.com/waf-rules-react-vulnerability/) nos componentes do Servidor React.

Qualquer interrupção de nossos sistemas é inaceitável e sabemos que decepcionamos a internet novamente após o incidente de 18 de novembro. Na próxima semana, vamos publicar detalhes sobre o trabalho que estamos realizando para evitar que esses tipos de incidentes ocorram.

### O que ocorreu

O gráfico abaixo mostra os erros HTTP 500 fornecidos pela nossa rede durante o período do incidente (linha vermelha na parte inferior), em comparação com o tráfego total da Cloudflare não afetado (linha verde na parte superior).

O firewall de aplicativos web (WAF) da Cloudflare oferece aos clientes proteção contra conteúdos maliciosos, permitindo que sejam detectados e bloqueados. Para fazer isso, o proxy da Cloudflare armazena o conteúdo do corpo da solicitação HTTP em buffer na memória para análise. Anteriormente, o tamanho do buffer era definido em 128 KB.

Como parte do nosso trabalho contínuo para proteger os clientes que usam o React contra uma vulnerabilidade crítica, a [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182), começamos a implementar um aumento no tamanho do nosso buffer para 1 MB, o limite padrão permitido pelos aplicativos Next.js. Nosso objetivo era garantir que o maior número possível de clientes estivesse protegido.

Essa primeira mudança estava sendo implementada usando nosso sistema de implantação gradual. Durante o lançamento, notamos que nossa ferramenta interna de teste WAF não era compatível com o tamanho do buffer aumentado. Como essa ferramenta de teste interno não era necessária naquele momento e não influenciava o tráfego de clientes, fizemos uma segunda alteração para desligá-la.

Essa segunda alteração de desligar nossa ferramenta de teste WAF foi feita usando o sistema de configuração global. Esse sistema não realiza implementações graduais, mas propaga as alterações em segundos para todo o conjunto de servidores em nossa rede e está em análise [após a interrupção ocorrida no dia 18 de novembro](https://blog.cloudflare.com/18-november-2025-outage/). 

Infelizmente, na versão FL1 do nosso proxy, sob certas circunstâncias, a segunda alteração de desativar nossa ferramenta de teste de regras WAF causou um estado de erro que resultou no fornecimento de códigos de erro HTTP 500 pela nossa rede.

Assim que a alteração se propagou para nossa rede, a execução de código em nosso proxy FL1 provocou uma falha em nosso módulo de regras, o que levou à seguinte exceção em Lua: 

resultando na emissão de erros de código HTTP 500.

O problema foi identificado logo após a aplicação da alteração e foi revertido às 09h12. Depois disso, todo o tráfego voltou a ser atendido corretamente.

Os clientes que tinham seus ativos da web atendidos por nosso proxy FL1 mais antigo **E** que tinham o conjunto de regras gerenciadas da Cloudflare implantado foram afetados. Todas as solicitações para sites neste estado retornaram um erro HTTP 500, com a pequena exceção de alguns endpoints de teste, como `/cdn-cgi/trace`.

Os clientes que não tiham a configuração acima aplicada não foram afetados. O tráfego de clientes atendido pela China network também não foi impactado.

### O erro de tempo de execução

O sistema de conjuntos de regras da Cloudflare consiste em conjuntos de regras que são avaliadas para cada solicitação que entra em nosso sistema. Uma regra consiste em um filtro, que seleciona algum tráfego, e uma ação que aplica um efeito a esse tráfego. As ações típicas são “`block`”, “`log`”, ou “`skip`”. Outro tipo de ação é “`execute`”,que é usada para acionar a avaliação de outro conjunto de regras.

Nosso sistema de registro de logs interno usa este recurso para avaliar novas regras antes de disponibilizá-las ao público. Um conjunto de regras de nível superior executa outro conjunto de regras que contém regras de teste. Eram estas regras de teste que estávamos tentando desativar.

Temos um subsistema killswitch (bloqueio de rede) como parte do sistema de conjunto de regras, projetado para permitir a desativação rápida de uma regra com comportamento inadequado. Esse sistema killswitch recebe informações do nosso sistema de configuração global, mencionado nas seções anteriores. Já utilizamos esse sistema killswitch em diversas ocasiões para mitigar incidentes e possuímos um Procedimento Operacional Padrão bem definido, que foi seguido neste incidente.

No entanto, nunca aplicamos um killswitch a uma regra com a ação de "`execute`". Quando o killswitch foi aplicado, o código ignorou corretamente a avaliação da ação de execução e não avaliou o subconjunto de regras apontado por ela. No entanto, um erro foi encontrado durante o processamento dos resultados gerais da avaliação do conjunto de regras:

Este código espera que, se o conjunto de regras tiver a action="execute", o objeto "rule_result.execute" exista. No entanto, como a regra foi ignorada, o objeto "rule_result.execute" não existia e Lua retornou um erro devido à tentativa de buscar um valor em um valor nulo.

Este é um erro simples no código, que permaneceu sem ser detectado por muitos anos. Esse tipo de erro de erro de código é evitado por linguagens com sistemas de tipos fortes. Em nossa substituição desse código no novo proxy FL2, escrito em Rust, o erro não ocorreu.

### E quanto às mudanças implementadas após o incidente de 18 de novembro de 2025?

Duas semanas atrás, em 18 de novembro de 2025, fizemos uma alteração não relacionada que causou um incidente de disponibilidade semelhante porém [mais prolongado](https://blog.cloudflare.com/18-november-2025-outage/). Em ambos os casos, uma implementação para ajudar a mitigar um problema de segurança para nossos clientes se propagou por toda a nossa rede e causou erros para quase toda a nossa base de clientes.

Após o incidente, conversamos diretamente com centenas de clientes e compartilhamos nossos planos de implementar mudanças para evitar que atualizações isoladas causem um impacto generalizado como este. Acreditamos que essas mudanças teriam ajudado a evitar o impacto do incidente de hoje, mas, infelizmente, ainda não as implantamos por completo.

Sabemos que é decepcionante que esse trabalho ainda não tenha sido concluído. Ele continua sendo nossa prioridade número um em toda a organização. Em particular, os projetos descritos abaixo devem ajudar a conter o impacto desses tipos de mudanças:

  * **Implementações e controle de versão aprimorados** : assim como implementamos software gradualmente com validação de integridade rigorosa, os dados usados para resposta rápida a ameaças e configuração geral precisam ter os mesmos recursos de segurança e mitigação de explosões. Isso inclui validação de integridade e recursos de reversão rápida, entre outras coisas.
  * **Recursos de break glass otimizados:** garantem que as operações críticas ainda possam ser realizadas diante de tipos adicionais de falhas. Isso se aplica tanto aos serviços internos quanto a todos os métodos padrão de interação com o plano de controle da Cloudflare, utilizados por todos os clientes da Cloudflare.
  * **Tratamento de erros "Fail-Open":** como parte do esforço de resiliência, estamos substituindo a lógica de falha rígida aplicada incorretamente em todos os componentes críticos do plano de dados da Cloudflare. Se um arquivo de configuração estiver corrompido ou fora do intervalo (por exemplo, excedendo os limites de recursos), o sistema registrará o erro e retornará a um estado válido conhecido ou permitirá o tráfego sem pontuação, em vez de descartar as solicitações. Alguns serviços provavelmente oferecerão ao cliente a opção de fail-open ou fail-closed em determinados cenários. Isso incluirá recursos de prevenção de desvios para garantir que seja aplicado continuamente.



Antes do final da próxima semana, publicaremos uma análise detalhada de todos os projetos de resiliência em andamento, incluindo os listados acima. Enquanto esse trabalho estiver em andamento, estamos bloqueando todas as alterações em nossa rede para garantir que tenhamos sistemas de mitigação e reversão melhores antes de começarmos novamente.

Esse tipo de incidente, e a frequência com que ocorreram, é inaceitável para uma rede como a nossa. Em nome da equipe da Cloudflare, gostaríamos de nos desculpar pelo impacto e transtorno causados aos nossos clientes e à internet como um todo.

### Cronograma

Horário (UTC)| Status| Descrição  
---|---|---  
08:47| Início do INCIDENTE| Alteração de configuração implantada e propagada para a rede  
08:48| Impacto total| Alteração totalmente propagada  
08:50| INCIDENTE Declarado| Alertas automatizados  
09:11| Alteração Revertida| Alteração de configuração revertida e propagação iniciada  
09:12| Fim do INCIDENTE| Reversão totalmente propagada. Todo o tráfego foi restaurado.  
]]>7lRsBDx09Ye8w2dhpF0YcRelatório sobre ameaças de DDoS do terceiro trimestre de 2025 da Cloudflare, incluindo a Aisuru, o ápice das botnetshttps://blog.cloudflare.com/pt-br/ddos-threat-report-2025-q3/ Wed, 03 Dec 2025 14:00:00 GMTBoas-vindas à vigésima terceira edição do Relatório trimestral sobre ameaças de DDoS da Cloudflare. Este relatório oferece uma análise abrangente do cenário de ameaças em evolução dos ataques de negação de serviço distribuída (DDoS), com base em dados da rede da Cloudflare. Nesta edição, nos concentramos no terceiro trimestre de 2025.DDoSRelatórios de DDoSBoas-vindas à vigésima terceira edição do Relatório trimestral sobre ameaças de DDoS da Cloudflare. Este relatório oferece uma análise abrangente do cenário de ameaças em evolução de [ataques de negação de serviço distribuída (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) com base em dados da [rede da Cloudflare](https://www.cloudflare.com/network/). Nesta edição, nos concentramos no terceiro trimestre de 2025.

O terceiro trimestre de 2025 foi marcado pela botnet Aisuru, com um enorme exército estimado entre 1 e 4 milhões de hosts infectados em todo o mundo. A Aisuru lançou ataques de DDoS hipervolumétricos que rotineiramente ultrapassavam 1 terabit por segundo (Tbps) e 1 bilhão de pacotes por segundo (Bpps). O número desses ataques aumentou 54% em relação ao trimestre anterior, com uma média de 14 ataques hipervolumétricos diariamente. A escala foi sem precedentes, com ataques atingindo picos de 29,7 Tbps e 14,1 Bpps.

## Principais insights

Além da Aisuru, outros insights importantes neste relatório incluem:

  1. O tráfego de ataques de DDoS contra empresas de IA aumentou até 347% mês a mês em setembro de 2025, à medida que a preocupação pública e a revisão regulatória da IA aumentam. 
  2. A escalada das tensões comerciais entre a UE e a China sobre minerais de terras raras e tarifas de veículos elétricos coincide com um aumento significativo nos ataques de DDoS contra a indústria de mineração, minerais e metais, bem como a indústria automotiva no terceiro trimestre de 2025.
  3. No geral, no terceiro trimestre de 2025, as defesas autônomas da Cloudflare bloquearam um total de 8,3 milhões de ataques de DDoS. Isso é uma média de quase 3.780 ataques de DDoS por hora. O número de ataques de DDoS cresceu 15% em relação ao trimestre anterior e 40% em termos anuais. 



## Ataques de DDoS em números

Até agora em 2025, e com um trimestre inteiro até o final do ano, a Cloudflare já mitigou 36,2 milhões de ataques de DDoS. Isso corresponde a 170% dos ataques de DDoS que a Cloudflare mitigou ao longo de 2024. 

No terceiro trimestre de 2025, a Cloudflare detectou e mitigou automaticamente 8,3 milhões de ataques de DDoS, representando um aumento de 15% no trimestre e 40% em relação ao ano anterior.

Os ataques de DDoS na camada de rede, que representaram 71% dos ataques de DDoS no terceiro trimestre de 2025, ou 5,9 milhões de ataques de DDoS, aumentaram 87% em relação ao trimestre anterior e 95% em relação ao ano anterior. No entanto, os ataques de DDoS por HTTP, que representaram apenas 29% dos ataques de DDoS no terceiro trimestre de 2025, ou 2,4 milhões de ataques de DDoS, diminuíram 41% em relação ao trimestre anterior e 17% em relação ao ano anterior.

No terceiro trimestre de 2025, a Cloudflare mitigou uma média de 3.780 ataques de DDoS a cada hora.

## A Aisuru quebra recordes com ataques de DDoS ultrassofisticados e hipervolumétricos

**Força disruptiva**

A Aisuru visou provedores de telecomunicações, [empresas de jogos](https://www.cloudflare.com/gaming/), provedores de hospedagem e [serviços financeiros](https://www.cloudflare.com/banking-and-financial-services/), para citar alguns. Também causou “interrupções colaterais generalizadas na internet [nos EUA]”, conforme [relatado por Krebs on Security](https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/), simplesmente devido à quantidade de tráfego de botnets roteado pelos provedores de internet (ISPs). 

Pense nisso. Se o tráfego de ataque da Aisuru pode interromper partes da infraestrutura da internet dos EUA quando os referidos provedores de internet nem eram o alvo do ataque, imagine o que ele pode fazer quando for voltado diretamente a provedores de internet desprotegidos ou insuficientemente protegidos, [infraestrutura crítica](https://www.cloudflare.com/the-net/government/critical-infrastructure/), [serviços de saúde](https://www.cloudflare.com/healthcare/), serviços de emergência e sistemas militares. 

**Estatísticas de botnets para alugar e DDoS**

"Partes" da Aisuru são oferecidas por distribuidores como botnets para alugar, permitindo que qualquer pessoa cause caos em nações inteiras ao paralisar redes de backbone e saturar links de internet, interrompendo milhões de usuários e prejudicando o acesso a serviços essenciais, tudo por um custo de algumas centenas a alguns milhares de dólares americanos. 

Desde o início de 2025, a Cloudflare já mitigou 2.867 ataques da Aisuru. Somente no terceiro trimestre, a Cloudflare mitigou 1.304 ataques volumétricos lançados pela Aisuru. Isso representa um aumento de 54% no trimestre. Isso inclui os ataques de DDoS de 29,7 Tbps e de 14,1 Bpps que quebraram o recorde mundial. 

O ataque de 29,7 Tbps foi um ataque de carpet bombing de UDP, bombardeando uma média de 15 mil portas de destino por segundo. O ataque distribuído randomizou vários atributos de pacotes na tentativa de escapar das defesas, mas os sistemas de mitigação da Cloudflare detectaram e mitigaram todos os ataques, inclusive este, de forma totalmente autônoma. Leia mais sobre [Como a Cloudflare mitiga ataques de DDoS hipervolumétricos](https://blog.cloudflare.com/how-cloudflare-auto-mitigated-world-record-3-8-tbps-ddos-attack/#how-cloudflare-defends-against-large-attacks).

## Características do ataque

Embora a maioria dos ataques de DDoS seja relativamente pequena, no terceiro trimestre, a quantidade de ataques de DDoS que excederam 100 milhões de pacotes por segundo (Mpps) aumentou 189% em relação ao trimestre anterior. Da mesma forma, os ataques que excedem 1 Tbps aumentaram 227% no trimestre. Na camada HTTP, quatro em cada cem ataques excederam um milhão de solicitações por segundo. 

Além disso, a maioria, 71%, dos ataques de DDoS por HTTP e 89% dos ataques na camada de rede, termina em menos de 10 minutos. Isso é rápido demais para qualquer ser humano ou serviço sob demanda reagir. Um ataque curto pode durar apenas alguns segundos, mas a disrupção que ele causa pode ser grave, e a recuperação leva muito mais tempo. A equipe operacional e a de engenharia ficam presas a um processo complexo e de várias etapas para colocar sistemas críticos novamente on-line, verificar a consistência dos dados em sistemas distribuídos e restaurar serviços seguros e confiáveis para os clientes. 

O impacto dos ataques de DDoS de curta duração, sejam eles hipervolumétricos ou não, pode se estender muito além da duração do ataque.

## Principais origens de ataques

Sete das dez principais origens são locais na Ásia, com a Indonésia na liderança. A Indonésia é a maior origem de ataques de DDoS e foi classificada como número um no mundo por um ano inteiro (desde o terceiro trimestre de 2024). Mesmo antes disso, a Indonésia sempre esteve nas principais listas de origens de ataques. No segundo trimestre de 2024, a Indonésia foi a segunda maior origem, depois de subir das classificações mais baixas nos trimestres e anos anteriores.

Para ilustrar a ascensão da Indonésia como um hub de DDoS, em apenas cinco anos (desde o terceiro trimestre de 2021), a porcentagem de solicitações de ataques de DDoS por HTTP originadas na Indonésia aumentou impressionantes 31.900%. 

## Setores mais atacados

**Os atacantes de DDoS visam minerais de terras raras**

Os ataques de DDoS contra a indústria de mineração, minerais e metais aumentaram significativamente no terceiro trimestre de 2025, quando a [25ª cúpula comercial União Europeia–China](https://www.consilium.europa.eu/en/press/press-releases/2025/07/24/25th-eu-china-summit-eu-press-release/) viu tensões crescentes sobre tarifas de veículos elétricos (EV), exportações de terras raras e questões de segurança cibernética, de acordo com vários veículos de notícias. A [BBC](https://www.bbc.co.uk/news/articles/clyxk4ywppzo) informou que “a China também aumentou os controles de exportação de terras raras e minerais críticos”. No geral, o setor de mineração, minerais e metais subiu 24 posições na classificação global, tornando-se o 49º setor mais atacado do mundo.

O setor automotivo teve o maior aumento nos ataques de DDoS, subindo 62 posições em apenas um trimestre, tornando-se o sexto setor mais atacado no mundo. As empresas de cibersegurança também registraram um aumento significativo nos ataques de DDoS. O setor de segurança cibernética subiu 17 posições, tornando-se o 13º setor mais atacado do mundo.

**Ataques de DDoS contra IA disparam 347%**

Em setembro de 2025, uma[ pesquisa do Tony Blair Institute](https://www.theguardian.com/technology/2025/sep/22/more-britons-view-ai-as-economic-risk-than-opportunity-tony-blair-thinktank-finds?utm_source=chatgpt.com) mostrou que os britânicos veem a IA mais como um risco econômico do que uma oportunidade, gerando grandes manchetes sobre automação e confiança. A[ Comissão de Direito do Reino Unido](https://www.localgovernmentlawyer.co.uk/governance/396-governance-news/62164-law-commission-to-review-public-sector-use-of-ai-in-automated-decisions?utm_source=chatgpt.com) lançou uma análise sobre o uso da IA no governo, tornando este um mês de destaque para a ética da IA, regulamentação e adoção de IA generativa. Em setembro de 2025, a Cloudflare também observou picos mensais de até 347% no tráfego de ataques de DDoS por HTTP contra empresas de IA generativa (com base em uma amostra dos principais serviços de IA generativa).

**Os 10 principais**

No terceiro trimestre de 2025, tecnologia da informação e serviços liderou a lista como o setor mais atacado, seguido por telecomunicações e jogos e apostas. Notavelmente, o setor automotivo subiu dramaticamente 62 posições no trimestre. Mídia, produção e publicação também tiveram um forte aumento, precedido pelo setor de bancos e serviços financeiros, o [setor de varejo](https://www.cloudflare.com/retail/) e o setor de eletrônicos de consumo.

## Principais locais atacados

Há uma correlação direta entre eventos geopolíticos e a atividade de ataques de DDoS.

**Parem os saques!**

"Lootuvaifi" (Parem os saques!) em maldívio**,** tornou-se o grito de guerra nos [protestos maldívios de 2025](https://en.wikipedia.org/wiki/2025_Maldivian_protests), quando os manifestantes foram às ruas para protestar contra a "corrupção governamental percebida e o retrocesso democrático", culminando com o projeto de lei da mídia que "acaba com a liberdade de expressão", que o [Human Rights Chief da ONU](https://www.ohchr.org/en/press-releases/2025/09/un-human-rights-chief-calls-repeal-new-media-law-maldives) disse que "prejudicará seriamente a liberdade de imprensa e o direito à liberdade de expressão do povo das Maldivas se não for retirado". Os protestos maldivos de 2025 foram acompanhados por uma enxurrada de ataques de DDoS. Da mesma forma, as Maldivas foram o país que viu o maior aumento nos ataques de DDoS. No terceiro trimestre de 2025, as Maldivas subiram 125 posições, tornando-se o 38º país mais atacado do mundo.

**"Bloquear tudo"**

O [movimento de protesto nacional](https://www.reuters.com/world/europe/block-everything-protests-sweep-across-france-scores-arrested-2025-09-10/), "Bloquear tudo", ou "Bloquons Tout" em francês, foi lançado por sindicatos franceses em setembro de 2025 para se opor ao governo do presidente Macron devido às novas medidas de austeridade, mudanças no sistema de pensões e aumento do custo de vida. Enquanto os sindicatos pediam greves coordenadas e bloqueios de transporte para paralisar o país, agentes de ameaças cibernéticas visaram sites e serviços de internet franceses com ondas de ataques de DDoS. A França saltou 65 posições na comparação trimestral, tornando-se o 18º país mais atacado do mundo. 

**“Traçar a linha vermelha para Gaza em Bruxelas”**

Aumentos nos ataques de DDoS foram observados juntamente com protestos em mais países. Por exemplo, a [Bélgica](https://www.euronews.com/2025/09/07/tens-of-thousands-of-protesters-draw-the-red-line-for-gaza-in-brussels) saltou 63 lugares, tornando-se o 74º país mais atacado do mundo, quando “dezenas de milhares de manifestantes traçaram a linha vermelho para Gaza em Bruxelas.”

**Os 10 principais**

No terceiro trimestre de 2025, a China continuou a ser o país mais atacado, seguida pela Turquia, em segundo, e a Alemanha, em terceiro lugar. As mudanças mais notáveis neste trimestre foram o aumento dos ataques de DDoS contra os Estados Unidos, que subiram 11 posições, tornando-se o quinto país mais atacado. As Filipinas tiveram o maior aumento entre os 10 primeiros, saltaram 20 posições.

## Vetores de ataque 

**Ataques DDoS na camada de rede**

A quantidade de [ataques de DDoS UDP](https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack/), parcialmente alimentada pelos ataques da Aisuru, aumentou 231% em relação ao trimestre anterior, tornando-se o principal vetor de ataque na camada de rede. [As inundações de DNS](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) ficaram em segundo lugar, [as inundações SYN](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/) em terceiro e [as inundações ICMP](https://www.cloudflare.com/learning/ddos/ping-icmp-flood-ddos-attack/) em quarto, respondendo por pouco mais da metade de todos os ataques de DDoS na camada de rede.

Embora quase dez anos tenham se passado desde sua primeira grande estreia, os ataques de DDoS da Mirai ainda são bastante comuns. Quase dois em cada cem ataques de DDoS na camada de rede são lançados por permutações da [botnet Mirai](https://www.cloudflare.com/learning/ddos/glossary/mirai-botnet/).

**Ataques DDoS por HTTP**

Quase 70% dos ataques de DDoS por HTTP se originaram de [botnets](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-botnet/) já conhecidos pela Cloudflare. Isso reflete um dos benefícios que nossos clientes obtêm ao usar a Cloudflare. Quando uma botnet ataca um dos milhões de clientes da Cloudflare, todos ficam automaticamente protegidos contra essa botnet.

Cerca de 20% dos ataques de DDoS por HTTP se originaram de navegadores falsos ou sem interface gráfica, ou incluíram atributos HTTP suspeitos. Cerca de 10% dos restantes foram uma combinação de [inundações genéricas](https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack/), solicitações incomuns, ataques de estouro de cache e ataques direcionados a endpoints de login.

## Por que as soluções legadas de DDoS não são mais suficientes

Entramos em uma era em que os ataques de DDoS cresceram rapidamente em sofisticação e tamanho, além de tudo que poderíamos imaginar alguns anos atrás. Muitas organizações enfrentam desafios para acompanhar este cenário de ameaças em evolução. 

As organizações que dependem de dispositivos de mitigação no local ou de soluções de centros de depuração sob demanda podem se beneficiar ao revisar sua estratégia de defesa, considerando o cenário atual de ameaças.

A Cloudflare, com sua [vasta rede global](https://www.cloudflare.com/network/) e [sistemas autônomos de mitigação de DDoS](https://developers.cloudflare.com/ddos-protection/about/), está comprometida em fornecer[ proteção contra DDoS gratuita e não medida](https://www.cloudflare.com/ddos/) a todos os clientes, independentemente do tamanho, duração ou quantidade de ataques de DDoS que eles enfrentam.

]]>1lRRUtB2DMN3pPhk7yfeSMInterrupção da Cloudflare em 18 de novembro de 2025https://blog.cloudflare.com/pt-br/18-november-2025-outage/ Tue, 18 Nov 2025 00:00:00 GMTA Cloudflare sofreu uma interrupção de serviço em 18 de novembro de 2025. A interrupção foi causada por uma falha na lógica de geração de um arquivo de recurso do Bot Management, afetando vários serviços da Cloudflare. Bot ManagementInterrupçãoPost MortemEm 18 de novembro de 2025, às 11h20 UTC (todos os horários neste blog são UTC), a rede da Cloudflare começou a apresentar falhas significativas no fornecimento de tráfego de rede principal. Isso foi mostrado aos usuários da internet que tentavam acessar os sites de nossos clientes como uma página de erro, indicando uma falha na rede da Cloudflare. 

**O problema não foi causado, direta ou indiretamente, por um ataque cibernético ou atividade maliciosa de qualquer natureza.** Ele foi desencadeado por uma alteração nas permissões de um dos nossos sistemas de banco de dados, que fez com que o banco de dados enviasse várias entradas para um “arquivo de recursos” usado pelo nosso sistema do Bot Management. Esse arquivo de recursos, por sua vez, dobrou de tamanho. O arquivo de recursos, maior que o esperado, foi então propagado para todas as máquinas que compõem nossa rede.

O software executado nessas máquinas para rotear o tráfego em nossa rede lê esse arquivo de recursos para manter nosso sistema do Bot Management atualizado com as ameaças em constante mudança. O software tinha um limite no tamanho do arquivo de recursos que era inferior ao seu tamanho duplicado. Isso fez com que o software falhasse.

Depois de suspeitarmos inicialmente que os sintomas que estávamos observando eram causados por um ataque de DDoS em hiperescala, identificamos corretamente o problema principal e conseguimos interromper a propagação do arquivo de recursos maior do que o esperado e substituí-lo por uma versão anterior do arquivo. O tráfego principal estava fluindo normalmente às 14h30. Trabalhamos nas horas seguintes para mitigar o aumento da carga em várias partes de nossa rede à medida que o tráfego voltava a ficar on-line. Às 17h06, todos os sistemas da Cloudflare funcionavam normalmente.

Lamentamos o impacto causado aos nossos clientes e à internet em geral. Dada a importância da Cloudflare no ecossistema da internet, qualquer interrupção de qualquer um de nossos sistemas é inaceitável. O fato de ter havido um período em que nossa rede não conseguiu rotear o tráfego é profundamente lamentável para todos os membros de nossa equipe. Sabemos que decepcionamos vocês hoje.

Esta publicação é um relato detalhado do que aconteceu exatamente e de quais sistemas e processos falharam. É também o começo, embora não o fim, do que planejamos fazer para garantir que uma interrupção como esta não volte a acontecer.

## A interrupção

O gráfico abaixo mostra o volume de códigos de status HTTP de erro 5xx fornecidos pela rede da Cloudflare. Normalmente, esse valor deveria ser muito baixo, e era assim até o início da interrupção. 

O volume anterior a 11h20 é a linha de base esperada de erros 5xx observados em nossa rede. O pico e as flutuações subsequentes mostram que nosso sistema está falhando devido ao carregamento do arquivo de recursos incorreto. O que é notável é que o nosso sistema se recuperou durante um período. Este foi um comportamento muito incomum para um erro interno.

A explicação era de que o arquivo estava sendo gerado a cada cinco minutos por uma consulta executada em um cluster de banco de dados da ClickHouse, o qual estava sendo atualizado gradualmente para melhorar o gerenciamento de permissões. Dados incorretos eram gerados somente se a consulta fosse executada em uma parte do cluster que tivesse sido atualizada. Como resultado, a cada cinco minutos, havia a chance de um conjunto de arquivos de configuração, bom ou ruim, ser gerado e rapidamente propagado pela rede.

Essa flutuação tornou obscuro o que estava acontecendo, já que o sistema inteiro se recuperava e falhava novamente, porque arquivos de configuração, às vezes bons, às vezes ruins, eram distribuídos para a nossa rede. Inicialmente, isso nos levou a acreditar que isso poderia ser causado por um ataque. Ao final, cada nó do ClickHouse gerava o arquivo de configuração incorreto e a flutuação se estabilizou no estado de falha.

Os erros continuaram até que o problema subjacente fosse identificado e resolvido, a partir das 14h30. Resolvemos o problema interrompendo a geração e propagação do arquivo de recursos defeituoso e inserindo manualmente um arquivo funcional conhecido na fila de distribuição de arquivo de recursos. E, em seguida, forçamos a reinicialização do nosso proxy principal.

A cauda longa remanescente no gráfico acima refere-se à nossa equipe reiniciando os serviços restantes que entraram em um estado inadequado, com o volume de código de erro 5xx retornando ao normal às 17h06.

Os seguintes serviços foram afetados:

Serviço/produto| Descrição do impacto  
---|---  
Serviços de CDN e segurança principais| Códigos de status HTTP 5xx. A captura de tela na parte superior deste post mostra uma página de erro típica exibida aos usuários finais.  
Turnstile| Falha ao carregar o Turnstile.  
Workers KV| O Workers KV retornou um nível significativamente elevado de erros HTTP 5xx, pois as solicitações ao gateway "front-end" do KV falharam devido a falha do proxy principal  
Painel| Embora o painel estivesse operacional na maior parte do tempo, a maioria dos usuários não conseguiu fazer login devido à indisponibilidade do Turnstile na página de login.  
Segurança de e-mail| Embora o processamento e a distribuição de e-mails não tenham sido afetados, observamos uma perda temporária de acesso a uma fonte de reputação de IP, o que reduziu a precisão da detecção de spam e impediu o acionamento de algumas detecções de idade de domínio recente. Não foi observado nenhum impacto crítico para os clientes. Também vimos falhas em algumas ações de movimentação automática. Todas as mensagens afetadas foram revisadas e corrigidas.  
Access| As falhas de autenticação foram generalizadas para a maioria dos usuários, começando no início do incidente e continuando até que o rollback fosse iniciado às 13h05. As sessões existentes do Access não foram afetadas.  
Todas as tentativas de autenticação com falha resultaram em uma página de erro, o que significa que nenhum desses usuários chegou ao aplicativo de destino enquanto a autenticação falhava. Os logins bem-sucedidos durante este período foram registrados corretamente durante este incidente.   
Qualquer tentativa de atualização da configuração do Access naquele momento teria falhado completamente ou se propagado muito lentamente. Todas as atualizações de configuração foram recuperadas.  
  
Além de retornar erros HTTP 5xx, observamos aumentos significativos na latência das respostas da nossa CDN durante o período de impacto. Isso ocorreu devido ao alto consumo de CPU pelos nossos sistemas de depuração e observabilidade, que aprimoram automaticamente o processo de detecção de erros não detectados com informações adicionais de depuração.

## Como a Cloudflare processa as solicitações e o que deu errado hoje

Cada solicitação para a Cloudflare segue um caminho bem definido através da nossa rede. Pode ser proveniente de um navegador carregando uma página da web, um aplicativo móvel chamando uma API ou tráfego automatizado de outro serviço. Essas solicitações terminam primeiro em nossa camada HTTP e TLS, depois seguem para o nosso sistema proxy principal (que chamamos de FL, abreviação de "Frontline") e, finalmente, passam pelo Pingora, que realiza pesquisas de cache ou busca dados na origem, se necessário.

Anteriormente, compartilhamos mais detalhes sobre como o proxy principal funciona [aqui](https://blog.cloudflare.com/20-percent-internet-upgrade/.). 

À medida que uma solicitação passa pelo proxy principal, executamos os vários produtos de segurança e desempenho disponíveis em nossa rede. O proxy aplica a configuração e as definições exclusivas de cada cliente, desde a aplicação das regras do WAF e a proteção contra DDoS até o roteamento do tráfego para a plataforma para desenvolvedores e o R2. Ele realiza isso por meio de um conjunto de módulos específicos de domínio que aplicam as regras de configuração e política ao tráfego que transita pelo nosso proxy.

Um desses módulos, o Bot Management, foi a causa da interrupção de hoje. 

O [Bot Management](https://www.cloudflare.com/application-services/products/bot-management/) da Cloudflare inclui, entre outros sistemas, um modelo de aprendizado de máquina que usamos para gerar pontuações de bots para cada solicitação que percorre nossa rede. Nossos clientes usam classificações de bots para controlar quais bots têm permissão para acessar seus sites ou não.

O modelo recebe como entrada um arquivo de configuração de "recurso". Nesse contexto, um recurso é uma característica individual usada pelo modelo de aprendizado de máquina para fazer uma previsão sobre se a solicitação foi automatizada ou não. O arquivo de configuração de recursos é uma coleção de recursos individuais.

Este arquivo de recursos é atualizado a cada poucos minutos e publicado em toda a nossa rede, permitindo-nos reagir a variações nos fluxos de tráfego na internet. Isso nos permite reagir a novos tipos de bots e novos ataques de bots. Portanto, é crucial que a implementação seja frequente e rápida, pois os agentes mal-intencionados alteram suas táticas com agilidade.

Uma mudança no comportamento subjacente da consulta ClickHouse (explicado abaixo) que gera este arquivo resultou em um grande número de linhas "feature" duplicadas Isso alterou o tamanho do arquivo de configuração de recursos, que anteriormente tinha tamanho fixo, fazendo com que o módulo de bots acionasse um erro.

Como resultado, o sistema proxy principal que lida com o processamento de tráfego para nossos clientes retornou códigos de erro HTTP 5xx para qualquer tráfego que dependesse do módulo de bots. Isso também afetou o Workers KV e o Access, que dependem do proxy principal.

Sem relação com este incidente, estávamos e estamos atualmente migrando nosso tráfego de clientes para uma nova versão do nosso serviço de proxy, conhecido internamente como [FL2](https://blog.cloudflare.com/20-percent-internet-upgrade/). Ambas as versões foram afetadas pelo problema, embora o impacto observado tenha sido diferente.

Clientes implantados no novo mecanismo de proxy FL2 observaram erros HTTP 5xx. Os clientes que utilizam nosso antigo mecanismo de proxy, conhecido como FL, não observaram erros, mas as pontuações de bots não foram geradas corretamente, resultando em todo o tráfego recebendo uma pontuação de bots igual a zero. Os clientes que tinham regras implementadas para bloquear bots observaram um grande número de falsos positivos. Os clientes que não estavam utilizando a nossa pontuação de bots em suas regras não notaram nenhum impacto.

Outro sintoma aparente que observamos nos fez suspeitar de um possível ataque: a página de status da Cloudflare ficou fora do ar. Essa página é hospedada completamente fora da infraestrutura da Cloudflare, sem nenhuma dependência da plataforma. Embora tenha se revelado uma coincidência, isso levou alguns membros da equipe, que diagnosticavam o problema, a acreditar que um invasor poderia estar visando tanto nossos sistemas quanto nossa página de status. Naquele momento, os visitantes da página de status se deparavam com a seguinte mensagem de erro:

Na sala de chat interna sobre incidentes, estávamos preocupados que isso pudesse ser a continuação da recente onda de [ataques de DDoS](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/defending-the-cloud-azure-neutralized-a-record-breaking-15-tbps-ddos-attack/4470422) [da Aisuru](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) de alto volume:

### A alteração no comportamento das consultas

Mencionei acima que uma alteração no comportamento da consulta subjacente resultou em um grande número de linhas duplicadas no arquivo de recursos. O sistema de banco de dados em questão utiliza o software ClickHouse.

Para fins de contexto, é útil saber como as consultas distribuídas do ClickHouse funcionam. Um cluster do ClickHouse consiste em vários fragmentos. Para consultar dados de todos os fragmentos, temos as chamadas tabelas distribuídas (alimentadas pelo mecanismo de tabela `Distributed`) em um banco de dados chamado `default`. O mecanismo Distributed consulta as tabelas subjacentes em um banco de dados `r0`. As tabelas subjacentes são onde os dados são armazenados em cada fragmento de um cluster do ClickHouse.

As consultas para as tabelas distribuídas são executadas por meio de uma conta de sistema compartilhada. Como parte dos esforços para melhorar a segurança e a confiabilidade de nossas consultas distribuídas, estamos trabalhando para que elas sejam executadas sob as contas de usuário iniciais.

Antes de hoje, os usuários do ClickHouse viam apenas as tabelas no banco de dados `default` ao consultar os metadados das tabelas do sistema do ClickHouse, como `system.tables` ou `system.columns`.

Como os usuários já têm acesso implícito às tabelas subjacentes em `r0`, fizemos uma alteração às 11h05 para tornar esse acesso explícito, para que os usuários também possam ver os metadados dessas tabelas. Ao garantir que todas as subconsultas distribuídas possam ser executadas sob o usuário inicial, os limites de consulta e as concessões de acesso podem ser avaliados de maneira mais precisa, evitando que uma subconsulta inadequada de um usuário afete outros.

A alteração explicada acima permitiu que todos os usuários acessassem metadados precisos sobre as tabelas às quais têm acesso. Infelizmente, no passado foram feitas suposições de que a lista de colunas retornada por uma consulta como esta incluiria apenas o banco de dados “`default`”:

`SELECT  
name,  
type  
FROM system.columns  
WHERE  
table = 'http_requests_features'  
order by name;`

Observe como a consulta não filtra o nome do banco de dados. Com a nossa implementação gradual das concessões explícitas para os usuários de um determinado cluster do ClickHouse, após a alteração às 11h05, a consulta acima começou a retornar “duplicatas” de colunas, porque estas eram para tabelas subjacentes armazenadas no banco de dados r0.

Infelizmente, este foi o tipo de consulta realizada pela lógica de geração do arquivo de recursos do Bot Management para construir cada “recurso” de entrada para o arquivo mencionado no início desta seção. 

A consulta acima retornou uma tabela de colunas como a exibida (exemplo simplificado).

No entanto, como parte das permissões adicionais que foram concedidas ao usuário, a resposta agora continha todos os metadados do esquema `r0`, efetivamente mais que dobrando as linhas na resposta e, em última instância, afetando o número de linhas (ou seja, recursos) na saída do arquivo final. 

### Pré-alocação de memória

Cada módulo em execução em nosso serviço de proxy possui uma série de limites para evitar o consumo irrestrito de memória e pré-alocar memória como uma otimização de desempenho. Nesse caso específico, o sistema do Bot Management tem um limite para o número de recursos de aprendizado de máquina que podem ser utilizados em tempo de execução. Atualmente, esse limite está definido em 200, bem acima do nosso uso atual de cerca de 60 recursos. Novamente, o limite existe porque, por motivos de desempenho, nós pré-alocamos memória para os recursos.

Quando o arquivo corrompido com mais de 200 recursos foi propagado para nossos servidores, esse limite foi atingido, resultando em um colapso do sistema. O código FL2 Rust que realiza a verificação e foi a origem do erro não tratado é exibido abaixo:

Isso resultou no seguinte colapso, que por sua vez resultou em um erro 5xx:

`thread fl2_worker_thread panicked: called Result::unwrap() on an Err value`

### Outro impacto durante o incidente

Outros sistemas que dependem de nosso proxy principal foram afetados durante o incidente. Isso incluiu o Workers KV e o Cloudflare Access. A equipe conseguiu reduzir o impacto nesses sistemas às 13h04, quando uma correção foi aplicada no Workers KV para contornar o proxy principal. Posteriormente, todos os sistemas downstream que dependem do Workers KV (como o próprio Access) observaram uma taxa de erros reduzida. 

O painel da Cloudflare também foi afetado devido ao uso interno do Workers KV e à implantação do Cloudflare Turnstile como parte do nosso fluxo de login.

O Turnstile foi afetado por essa interrupção, resultando na impossibilidade de clientes sem uma sessão ativa no painel de controle acessarem o sistema. Isso se refletiu em uma disponibilidade reduzida durante dois períodos: das 11h30 às 13h10 e entre 14h40 e 15h30, conforme mostrado no gráfico abaixo.

568 / 5.000O primeiro período, das 11h30 às 13h10, foi devido ao impacto no Workers KV, do qual algumas funções do plano de controle e do painel dependem. O sistema foi restaurado às 13h10, quando o Workers KV contornou o sistema proxy principal.O segundo período de impacto no painel ocorreu após a restauração dos dados de configuração do recurso. Um acúmulo de tentativas de login começou a sobrecarregar o painel. Esse acúmulo, em combinação com as tentativas de reenvio, resultou em latência elevada, reduzindo a disponibilidade do painel. O ajuste da simultaneidade no plano de controle restabeleceu a disponibilidade por volta das 15h30.

## Etapas de correção e acompanhamento

Agora que nossos sistemas estão on-line novamente e funcionando normalmente, já começamos a trabalhar em como fortalecê-los contra falhas como esta no futuro. Em particular, estamos:

  * Reforçando a segurança da ingestão de arquivos de configuração gerados pela Cloudflare da mesma forma que faríamos com entradas geradas por usuários
  * Habilitando mais interruptores globais para recursos
  * Eliminando a possibilidade de que despejos de memória ou outros relatórios de erro sobrecarreguem os recursos do sistema
  * Revisando os modos de falha para identificar condições de erro em todos os módulos principais do proxy.



Hoje foi a pior interrupção da Cloudflare [desde 2019](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/). Tivemos interrupções que tornaram nosso [painel indisponível](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/). Algumas que fizeram com que [novos recursos](https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/) não ficassem disponíveis por um período de tempo. Mas, nos últimos 6 anos ou mais, não tivemos outra interrupção que tenha feito com que a maior parte do tráfego principal parasse de fluir através da nossa rede.

Uma interrupção como a de hoje é inaceitável. Arquitetamos nossos sistemas para serem altamente resilientes a falhas, para garantir que o tráfego continue sempre fluindo. No passado, as interrupções sempre nos levaram a construir sistemas novos e mais resilientes.

Em nome de toda a equipe da Cloudflare, gostaria de pedir desculpas pelo transtorno que causamos à internet hoje. 

Horário (UTC)| Status| Descrição  
---|---|---  
11:05| Normal.| Alteração de controle de acesso ao banco de dados implantada.  
11:28| O impacto começa.| A implantação atinge os ambientes dos clientes. Os primeiros erros foram observados no tráfego HTTP dos clientes.  
11:32 - 13:05| A equipe investigou os níveis elevados de tráfego e erros no serviço Workers KV.  
  
| O sintoma inicial pareceu ser uma taxa de resposta degradada do Workers KV, causando impacto downstream em outros serviços da Cloudflare.  
Mitigações, como manipulação de tráfego e limitação de contas, foram tentadas para trazer o serviço Workers KV de volta aos níveis operacionais normais.  
O primeiro teste automatizado detectou o problema às 11h31 e a investigação manual começou às 11h32. A chamada de incidente foi criada às 11h35.  
13:05| Implementado o bypass do Workers KV e Cloudflare Access. Impacto reduzido.| Durante a investigação, utilizamos bypasses internos para o Workers KV e o Cloudflare Access, de modo que eles retornassem a uma versão anterior do nosso proxy principal. Embora o problema também estivesse presente em versões anteriores do nosso proxy, o impacto era menor, como descrito abaixo.  
13:37| O trabalho concentrou-se na reversão do arquivo de configuração do Bot Management para uma versão válida conhecida mais recente.| Estávamos confiantes de que o arquivo de configuração do Bot Management foi o gatilho para o incidente. As equipes trabalharam em maneiras de reparar o serviço em vários fluxos de trabalho, sendo o fluxo de trabalho mais rápido a restauração de uma versão anterior do arquivo.  
14:24| A criação e propagação de novos arquivos de configuração do Bot Management foram interrompidas.| Identificamos que o módulo do Bot Management era a origem dos erros 500 e que estes foram causados por um arquivo de configuração inválido. Interrompemos a implantação automática de novos arquivos de configuração do Bot Management.  
14:24| Teste do novo arquivo concluído.| Observamos uma recuperação bem-sucedida utilizando a versão antiga do arquivo de configuração e, em seguida, focamos em acelerar a correção globalmente.  
14h30| Impacto principal resolvido. Os serviços afetados downstream começaram a observar menos erros.| Um arquivo de configuração do Bot Management correto foi implementado globalmente e a maioria dos serviços começou a operar corretamente.  
17:06| Todos os serviços foram resolvidos. O impacto termina.| Todos os serviços downstream foram reiniciados e todas as operações foram totalmente restauradas.  
]]>oVEUcpjyyDA8DSSXiE7E6Interrupção da Cloudflare em 18 de novembro de 2025https://blog.cloudflare.com/pt-br/18-november-2025-outage-uk-ua/ Tue, 18 Nov 2025 00:00:00 GMTA Cloudflare sofreu uma interrupção de serviço em 18 de novembro de 2025. A interrupção foi causada por uma falha na lógica de geração de um arquivo de recurso do Bot Management, afetando vários serviços da Cloudflare. Bot ManagementInterrupçãoPost MortemEm 18 de novembro de 2025, às 11h20 UTC (todos os horários neste blog são UTC), a rede da Cloudflare começou a apresentar falhas significativas no fornecimento de tráfego de rede principal. Isso foi mostrado aos usuários da internet que tentavam acessar os sites de nossos clientes como uma página de erro, indicando uma falha na rede da Cloudflare. 

**O problema não foi causado, direta ou indiretamente, por um ataque cibernético ou atividade maliciosa de qualquer natureza.** Ele foi desencadeado por uma alteração nas permissões de um dos nossos sistemas de banco de dados, que fez com que o banco de dados enviasse várias entradas para um “arquivo de recursos” usado pelo nosso sistema do Bot Management. Esse arquivo de recursos, por sua vez, dobrou de tamanho. O arquivo de recursos, maior que o esperado, foi então propagado para todas as máquinas que compõem nossa rede.

O software executado nessas máquinas para rotear o tráfego em nossa rede lê esse arquivo de recursos para manter nosso sistema do Bot Management atualizado com as ameaças em constante mudança. O software tinha um limite no tamanho do arquivo de recursos que era inferior ao seu tamanho duplicado. Isso fez com que o software falhasse.

Depois de suspeitarmos inicialmente que os sintomas que estávamos observando eram causados por um ataque de DDoS em hiperescala, identificamos corretamente o problema principal e conseguimos interromper a propagação do arquivo de recursos maior do que o esperado e substituí-lo por uma versão anterior do arquivo. O tráfego principal estava fluindo normalmente às 14h30. Trabalhamos nas horas seguintes para mitigar o aumento da carga em várias partes de nossa rede à medida que o tráfego voltava a ficar on-line. Às 17h06, todos os sistemas da Cloudflare funcionavam normalmente.

Lamentamos o impacto causado aos nossos clientes e à internet em geral. Dada a importância da Cloudflare no ecossistema da internet, qualquer interrupção de qualquer um de nossos sistemas é inaceitável. O fato de ter havido um período em que nossa rede não conseguiu rotear o tráfego é profundamente lamentável para todos os membros de nossa equipe. Sabemos que decepcionamos vocês hoje.

Esta publicação é um relato detalhado do que aconteceu exatamente e de quais sistemas e processos falharam. É também o começo, embora não o fim, do que planejamos fazer para garantir que uma interrupção como esta não volte a acontecer.

## A interrupção

O gráfico abaixo mostra o volume de códigos de status HTTP de erro 5xx fornecidos pela rede da Cloudflare. Normalmente, esse valor deveria ser muito baixo, e era assim até o início da interrupção. 

O volume anterior a 11h20 é a linha de base esperada de erros 5xx observados em nossa rede. O pico e as flutuações subsequentes mostram que nosso sistema está falhando devido ao carregamento do arquivo de recursos incorreto. O que é notável é que o nosso sistema se recuperou durante um período. Este foi um comportamento muito incomum para um erro interno.

A explicação era de que o arquivo estava sendo gerado a cada cinco minutos por uma consulta executada em um cluster de banco de dados da ClickHouse, o qual estava sendo atualizado gradualmente para melhorar o gerenciamento de permissões. Dados incorretos eram gerados somente se a consulta fosse executada em uma parte do cluster que tivesse sido atualizada. Como resultado, a cada cinco minutos, havia a chance de um conjunto de arquivos de configuração, bom ou ruim, ser gerado e rapidamente propagado pela rede.

Essa flutuação tornou obscuro o que estava acontecendo, já que o sistema inteiro se recuperava e falhava novamente, porque arquivos de configuração, às vezes bons, às vezes ruins, eram distribuídos para a nossa rede. Inicialmente, isso nos levou a acreditar que isso poderia ser causado por um ataque. Ao final, cada nó do ClickHouse gerava o arquivo de configuração incorreto e a flutuação se estabilizou no estado de falha.

Os erros continuaram até que o problema subjacente fosse identificado e resolvido, a partir das 14h30. Resolvemos o problema interrompendo a geração e propagação do arquivo de recursos defeituoso e inserindo manualmente um arquivo funcional conhecido na fila de distribuição de arquivo de recursos. E, em seguida, forçamos a reinicialização do nosso proxy principal.

A cauda longa remanescente no gráfico acima refere-se à nossa equipe reiniciando os serviços restantes que entraram em um estado inadequado, com o volume de código de erro 5xx retornando ao normal às 17h06.

Os seguintes serviços foram afetados:

Serviço/produto| Descrição do impacto  
---|---  
Serviços de CDN e segurança principais| Códigos de status HTTP 5xx. A captura de tela na parte superior deste post mostra uma página de erro típica exibida aos usuários finais.  
Turnstile| Falha ao carregar o Turnstile.  
Workers KV| O Workers KV retornou um nível significativamente elevado de erros HTTP 5xx, pois as solicitações ao gateway "front-end" do KV falharam devido a falha do proxy principal  
Painel| Embora o painel estivesse operacional na maior parte do tempo, a maioria dos usuários não conseguiu fazer login devido à indisponibilidade do Turnstile na página de login.  
Segurança de e-mail| Embora o processamento e a distribuição de e-mails não tenham sido afetados, observamos uma perda temporária de acesso a uma fonte de reputação de IP, o que reduziu a precisão da detecção de spam e impediu o acionamento de algumas detecções de idade de domínio recente. Não foi observado nenhum impacto crítico para os clientes. Também vimos falhas em algumas ações de movimentação automática. Todas as mensagens afetadas foram revisadas e corrigidas.  
Access| As falhas de autenticação foram generalizadas para a maioria dos usuários, começando no início do incidente e continuando até que o rollback fosse iniciado às 13h05. As sessões existentes do Access não foram afetadas.  
Todas as tentativas de autenticação com falha resultaram em uma página de erro, o que significa que nenhum desses usuários chegou ao aplicativo de destino enquanto a autenticação falhava. Os logins bem-sucedidos durante este período foram registrados corretamente durante este incidente.   
Qualquer tentativa de atualização da configuração do Access naquele momento teria falhado completamente ou se propagado muito lentamente. Todas as atualizações de configuração foram recuperadas.  
  
Além de retornar erros HTTP 5xx, observamos aumentos significativos na latência das respostas da nossa CDN durante o período de impacto. Isso ocorreu devido ao alto consumo de CPU pelos nossos sistemas de depuração e observabilidade, que aprimoram automaticamente o processo de detecção de erros não detectados com informações adicionais de depuração.

## Como a Cloudflare processa as solicitações e o que deu errado hoje

Cada solicitação para a Cloudflare segue um caminho bem definido através da nossa rede. Pode ser proveniente de um navegador carregando uma página da web, um aplicativo móvel chamando uma API ou tráfego automatizado de outro serviço. Essas solicitações terminam primeiro em nossa camada HTTP e TLS, depois seguem para o nosso sistema proxy principal (que chamamos de FL, abreviação de "Frontline") e, finalmente, passam pelo Pingora, que realiza pesquisas de cache ou busca dados na origem, se necessário.

Anteriormente, compartilhamos mais detalhes sobre como o proxy principal funciona [aqui](https://blog.cloudflare.com/20-percent-internet-upgrade/.). 

À medida que uma solicitação passa pelo proxy principal, executamos os vários produtos de segurança e desempenho disponíveis em nossa rede. O proxy aplica a configuração e as definições exclusivas de cada cliente, desde a aplicação das regras do WAF e a proteção contra DDoS até o roteamento do tráfego para a plataforma para desenvolvedores e o R2. Ele realiza isso por meio de um conjunto de módulos específicos de domínio que aplicam as regras de configuração e política ao tráfego que transita pelo nosso proxy.

Um desses módulos, o Bot Management, foi a causa da interrupção de hoje. 

O [Bot Management](https://www.cloudflare.com/application-services/products/bot-management/) da Cloudflare inclui, entre outros sistemas, um modelo de aprendizado de máquina que usamos para gerar pontuações de bots para cada solicitação que percorre nossa rede. Nossos clientes usam classificações de bots para controlar quais bots têm permissão para acessar seus sites ou não.

O modelo recebe como entrada um arquivo de configuração de "recurso". Nesse contexto, um recurso é uma característica individual usada pelo modelo de aprendizado de máquina para fazer uma previsão sobre se a solicitação foi automatizada ou não. O arquivo de configuração de recursos é uma coleção de recursos individuais.

Este arquivo de recursos é atualizado a cada poucos minutos e publicado em toda a nossa rede, permitindo-nos reagir a variações nos fluxos de tráfego na internet. Isso nos permite reagir a novos tipos de bots e novos ataques de bots. Portanto, é crucial que a implementação seja frequente e rápida, pois os agentes mal-intencionados alteram suas táticas com agilidade.

Uma mudança no comportamento subjacente da consulta ClickHouse (explicado abaixo) que gera este arquivo resultou em um grande número de linhas "feature" duplicadas Isso alterou o tamanho do arquivo de configuração de recursos, que anteriormente tinha tamanho fixo, fazendo com que o módulo de bots acionasse um erro.

Como resultado, o sistema proxy principal que lida com o processamento de tráfego para nossos clientes retornou códigos de erro HTTP 5xx para qualquer tráfego que dependesse do módulo de bots. Isso também afetou o Workers KV e o Access, que dependem do proxy principal.

Sem relação com este incidente, estávamos e estamos atualmente migrando nosso tráfego de clientes para uma nova versão do nosso serviço de proxy, conhecido internamente como [FL2](https://blog.cloudflare.com/20-percent-internet-upgrade/). Ambas as versões foram afetadas pelo problema, embora o impacto observado tenha sido diferente.

Clientes implantados no novo mecanismo de proxy FL2 observaram erros HTTP 5xx. Os clientes que utilizam nosso antigo mecanismo de proxy, conhecido como FL, não observaram erros, mas as pontuações de bots não foram geradas corretamente, resultando em todo o tráfego recebendo uma pontuação de bots igual a zero. Os clientes que tinham regras implementadas para bloquear bots observaram um grande número de falsos positivos. Os clientes que não estavam utilizando a nossa pontuação de bots em suas regras não notaram nenhum impacto.

Outro sintoma aparente que observamos nos fez suspeitar de um possível ataque: a página de status da Cloudflare ficou fora do ar. Essa página é hospedada completamente fora da infraestrutura da Cloudflare, sem nenhuma dependência da plataforma. Embora tenha se revelado uma coincidência, isso levou alguns membros da equipe, que diagnosticavam o problema, a acreditar que um invasor poderia estar visando tanto nossos sistemas quanto nossa página de status. Naquele momento, os visitantes da página de status se deparavam com a seguinte mensagem de erro:

Na sala de chat interna sobre incidentes, estávamos preocupados que isso pudesse ser a continuação da recente onda de [ataques de DDoS](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/defending-the-cloud-azure-neutralized-a-record-breaking-15-tbps-ddos-attack/4470422) [da Aisuru](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/) de alto volume:

### A alteração no comportamento das consultas

Mencionei acima que uma alteração no comportamento da consulta subjacente resultou em um grande número de linhas duplicadas no arquivo de recursos. O sistema de banco de dados em questão utiliza o software ClickHouse.

Para fins de contexto, é útil saber como as consultas distribuídas do ClickHouse funcionam. Um cluster do ClickHouse consiste em vários fragmentos. Para consultar dados de todos os fragmentos, temos as chamadas tabelas distribuídas (alimentadas pelo mecanismo de tabela `Distributed`) em um banco de dados chamado `default`. O mecanismo Distributed consulta as tabelas subjacentes em um banco de dados `r0`. As tabelas subjacentes são onde os dados são armazenados em cada fragmento de um cluster do ClickHouse.

As consultas para as tabelas distribuídas são executadas por meio de uma conta de sistema compartilhada. Como parte dos esforços para melhorar a segurança e a confiabilidade de nossas consultas distribuídas, estamos trabalhando para que elas sejam executadas sob as contas de usuário iniciais.

Antes de hoje, os usuários do ClickHouse viam apenas as tabelas no banco de dados `default` ao consultar os metadados das tabelas do sistema do ClickHouse, como `system.tables` ou `system.columns`.

Como os usuários já têm acesso implícito às tabelas subjacentes em `r0`, fizemos uma alteração às 11h05 para tornar esse acesso explícito, para que os usuários também possam ver os metadados dessas tabelas. Ao garantir que todas as subconsultas distribuídas possam ser executadas sob o usuário inicial, os limites de consulta e as concessões de acesso podem ser avaliados de maneira mais precisa, evitando que uma subconsulta inadequada de um usuário afete outros.

A alteração explicada acima permitiu que todos os usuários acessassem metadados precisos sobre as tabelas às quais têm acesso. Infelizmente, no passado foram feitas suposições de que a lista de colunas retornada por uma consulta como esta incluiria apenas o banco de dados “`default`”:

`SELECT  
name,  
type  
FROM system.columns  
WHERE  
table = 'http_requests_features'  
order by name;`

Observe como a consulta não filtra o nome do banco de dados. Com a nossa implementação gradual das concessões explícitas para os usuários de um determinado cluster do ClickHouse, após a alteração às 11h05, a consulta acima começou a retornar “duplicatas” de colunas, porque estas eram para tabelas subjacentes armazenadas no banco de dados r0.

Infelizmente, este foi o tipo de consulta realizada pela lógica de geração do arquivo de recursos do Bot Management para construir cada “recurso” de entrada para o arquivo mencionado no início desta seção. 

A consulta acima retornou uma tabela de colunas como a exibida (exemplo simplificado).

No entanto, como parte das permissões adicionais que foram concedidas ao usuário, a resposta agora continha todos os metadados do esquema `r0`, efetivamente mais que dobrando as linhas na resposta e, em última instância, afetando o número de linhas (ou seja, recursos) na saída do arquivo final. 

### Pré-alocação de memória

Cada módulo em execução em nosso serviço de proxy possui uma série de limites para evitar o consumo irrestrito de memória e pré-alocar memória como uma otimização de desempenho. Nesse caso específico, o sistema do Bot Management tem um limite para o número de recursos de aprendizado de máquina que podem ser utilizados em tempo de execução. Atualmente, esse limite está definido em 200, bem acima do nosso uso atual de cerca de 60 recursos. Novamente, o limite existe porque, por motivos de desempenho, nós pré-alocamos memória para os recursos.

Quando o arquivo corrompido com mais de 200 recursos foi propagado para nossos servidores, esse limite foi atingido, resultando em um colapso do sistema. O código FL2 Rust que realiza a verificação e foi a origem do erro não tratado é exibido abaixo:

Isso resultou no seguinte colapso, que por sua vez resultou em um erro 5xx:

`thread fl2_worker_thread panicked: called Result::unwrap() on an Err value`

### Outro impacto durante o incidente

Outros sistemas que dependem de nosso proxy principal foram afetados durante o incidente. Isso incluiu o Workers KV e o Cloudflare Access. A equipe conseguiu reduzir o impacto nesses sistemas às 13h04, quando uma correção foi aplicada no Workers KV para contornar o proxy principal. Posteriormente, todos os sistemas downstream que dependem do Workers KV (como o próprio Access) observaram uma taxa de erros reduzida. 

O painel da Cloudflare também foi afetado devido ao uso interno do Workers KV e à implantação do Cloudflare Turnstile como parte do nosso fluxo de login.

O Turnstile foi afetado por essa interrupção, resultando na impossibilidade de clientes sem uma sessão ativa no painel de controle acessarem o sistema. Isso se refletiu em uma disponibilidade reduzida durante dois períodos: das 11h30 às 13h10 e entre 14h40 e 15h30, conforme mostrado no gráfico abaixo.

568 / 5.000O primeiro período, das 11h30 às 13h10, foi devido ao impacto no Workers KV, do qual algumas funções do plano de controle e do painel dependem. O sistema foi restaurado às 13h10, quando o Workers KV contornou o sistema proxy principal.O segundo período de impacto no painel ocorreu após a restauração dos dados de configuração do recurso. Um acúmulo de tentativas de login começou a sobrecarregar o painel. Esse acúmulo, em combinação com as tentativas de reenvio, resultou em latência elevada, reduzindo a disponibilidade do painel. O ajuste da simultaneidade no plano de controle restabeleceu a disponibilidade por volta das 15h30.

## Etapas de correção e acompanhamento

Agora que nossos sistemas estão on-line novamente e funcionando normalmente, já começamos a trabalhar em como fortalecê-los contra falhas como esta no futuro. Em particular, estamos:

  * Reforçando a segurança da ingestão de arquivos de configuração gerados pela Cloudflare da mesma forma que faríamos com entradas geradas por usuários
  * Habilitando mais interruptores globais para recursos
  * Eliminando a possibilidade de que despejos de memória ou outros relatórios de erro sobrecarreguem os recursos do sistema
  * Revisando os modos de falha para identificar condições de erro em todos os módulos principais do proxy.



Hoje foi a pior interrupção da Cloudflare [desde 2019](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/). Tivemos interrupções que tornaram nosso [painel indisponível](https://blog.cloudflare.com/post-mortem-on-cloudflare-control-plane-and-analytics-outage/). Algumas que fizeram com que [novos recursos](https://blog.cloudflare.com/cloudflare-service-outage-june-12-2025/) não ficassem disponíveis por um período de tempo. Mas, nos últimos 6 anos ou mais, não tivemos outra interrupção que tenha feito com que a maior parte do tráfego principal parasse de fluir através da nossa rede.

Uma interrupção como a de hoje é inaceitável. Arquitetamos nossos sistemas para serem altamente resilientes a falhas, para garantir que o tráfego continue sempre fluindo. No passado, as interrupções sempre nos levaram a construir sistemas novos e mais resilientes.

Em nome de toda a equipe da Cloudflare, gostaria de pedir desculpas pelo transtorno que causamos à internet hoje. 

Horário (UTC)| Status| Descrição  
---|---|---  
11:05| Normal.| Alteração de controle de acesso ao banco de dados implantada.  
11:28| O impacto começa.| A implantação atinge os ambientes dos clientes. Os primeiros erros foram observados no tráfego HTTP dos clientes.  
11:32 - 13:05| A equipe investigou os níveis elevados de tráfego e erros no serviço Workers KV.  
  
| O sintoma inicial pareceu ser uma taxa de resposta degradada do Workers KV, causando impacto downstream em outros serviços da Cloudflare.  
Mitigações, como manipulação de tráfego e limitação de contas, foram tentadas para trazer o serviço Workers KV de volta aos níveis operacionais normais.  
O primeiro teste automatizado detectou o problema às 11h31 e a investigação manual começou às 11h32. A chamada de incidente foi criada às 11h35.  
13:05| Implementado o bypass do Workers KV e Cloudflare Access. Impacto reduzido.| Durante a investigação, utilizamos bypasses internos para o Workers KV e o Cloudflare Access, de modo que eles retornassem a uma versão anterior do nosso proxy principal. Embora o problema também estivesse presente em versões anteriores do nosso proxy, o impacto era menor, como descrito abaixo.  
13:37| O trabalho concentrou-se na reversão do arquivo de configuração do Bot Management para uma versão válida conhecida mais recente.| Estávamos confiantes de que o arquivo de configuração do Bot Management foi o gatilho para o incidente. As equipes trabalharam em maneiras de reparar o serviço em vários fluxos de trabalho, sendo o fluxo de trabalho mais rápido a restauração de uma versão anterior do arquivo.  
14:24| A criação e propagação de novos arquivos de configuração do Bot Management foram interrompidas.| Identificamos que o módulo do Bot Management era a origem dos erros 500 e que estes foram causados por um arquivo de configuração inválido. Interrompemos a implantação automática de novos arquivos de configuração do Bot Management.  
14:24| Teste do novo arquivo concluído.| Observamos uma recuperação bem-sucedida utilizando a versão antiga do arquivo de configuração e, em seguida, focamos em acelerar a correção globalmente.  
14h30| Impacto principal resolvido. Os serviços afetados downstream começaram a observar menos erros.| Um arquivo de configuração do Bot Management correto foi implementado globalmente e a maioria dos serviços começou a operar corretamente.  
17:06| Todos os serviços foram resolvidos. O impacto termina.| Todos os serviços downstream foram reiniciados e todas as operações foram totalmente restauradas.  
]]>5EiRG3zMkhArZzOpaq4wgTO impacto da violação do Salesloft Drift na Cloudflare e em nossos clienteshttps://blog.cloudflare.com/pt-br/response-to-salesloft-drift-incident/ Tue, 02 Sep 2025 17:10:00 GMTUm agente de ameaça, GRUB1, explorou a integração do agente de chat Drift da Salesloft e a Salesforce para acesso não autorizado às instâncias do Salesforce da Cloudflare e de muitas outras empresas.Post MortemNa semana passada, a Cloudflare foi notificada de que nós (e nossos clientes) fomos afetados pela violação Salesloft Drift. Devido a essa violação, alguém externo à Cloudflare obteve acesso à nossa instância do Salesforce, que utilizamos para suporte ao cliente e gestão de casos internos de clientes, e a alguns dos dados que ela contém. A maioria dessas informações é de contato de clientes e dados básicos de casos de suporte, mas algumas interações de suporte ao cliente podem revelar informações sobre a configuração de um cliente e conter informações confidenciais, como tokens de acesso. Considerando que os dados dos casos de suporte do Salesforce contêm o conteúdo dos tickets de suporte com a Cloudflare, qualquer informação que um cliente possa ter compartilhado com a Cloudflare em nosso sistema de suporte, incluindo logs, tokens ou senhas, deve ser considerada comprometida, e recomendamos fortemente que você troque quaisquer credenciais que possa ter compartilhado conosco por meio deste canal. 

Como parte de nossa resposta a esse incidente, realizamos nossa própria busca nos dados comprometidos para procurar tokens ou senhas e encontramos 104 tokens de API da Cloudflare. Não identificamos nenhuma atividade suspeita associada a esses tokens, mas todos eles foram trocados, por precaução. Todos os clientes cujos dados foram comprometidos nessa violação foram informados diretamente pela Cloudflare.

Nenhum serviço da Cloudflare ou infraestrutura foi comprometido como resultado dessa violação.

Somos responsáveis pela escolha das ferramentas que utilizamos para apoiar nossos negócios. Essa violação decepcionou nossos clientes. Por isso, pedimos sinceras desculpas. O restante deste blog fornece um cronograma e informações detalhados sobre como investigamos essa violação.

## A violação Salesloft Drift

Na semana passada, a Cloudflare tomou conhecimento de atividades suspeitas em nossa instância do Salesforce e descobriu que nós, assim como centenas de outras empresas, nos tornamos alvo de um agente de ameaça que conseguiu exfiltrar com sucesso os campos de texto de casos de suporte de nossa instância do Salesforce. Nossa equipe de segurança iniciou imediatamente uma investigação, cortou o acesso do agente da ameaça e tomou uma série de medidas, detalhadas abaixo, para proteger nosso ambiente. Estamos escrevendo este blog para detalhar o que aconteceu, como respondemos e ajudar nossos clientes e outras pessoas a entenderem como se proteger desse incidente.

A Cloudflare utiliza o Salesforce para acompanhar quem são nossos clientes e como eles utilizam nossos serviços, e o utilizamos como uma ferramenta de suporte para interagir com nossos clientes. Um detalhe importante a ser compreendido como parte deste incidente é que o agente da ameaça acessou apenas dados em "casos" do Salesforce, que podem ser criados quando os membros da equipe de vendas e suporte da Cloudflare precisam comentar entre si, internamente, a fim de dar suporte aos nossos clientes. Eles também são criados quando os clientes interagem com o suporte da Cloudflare. A Salesforce tinha uma integração com o chatbot Salesloft Drift, que a Cloudflare usava para oferecer a qualquer pessoa que visitasse nosso site uma maneira de entrar em contato conosco.

Como a Salesloft [anunciou](https://trust.salesloft.com/?uid=Drift%2FSalesforce+Security+Update), um agente de ameaça violou seus sistemas. Como parte da violação, o agente de ameaça conseguiu obter credenciais OAuth associadas à integração do agente de chat Salesloft Drift com a Salesforce, a fim de exfiltrar dados das instâncias da Salesforce de clientes da Salesloft. Nossa investigação revelou que isso fazia parte de um ataque sofisticado à cadeia de suprimentos, direcionado a integrações de terceiros entre empresas, afetando centenas de organizações globalmente que eram clientes da Salesloft. A [Cloudforce One](https://www.cloudflare.com/en-au/application-services/products/cloudforceone/), a equipe de inteligência contra ameaças e pesquisa da Cloudflare, classificou o ator da ameaça avançada como **GRUB1**. Divulgações adicionais do [Grupo de inteligência contra ameaças do Google ](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift)alinhadas com a atividade que observamos em nosso ambiente.

Nossa investigação revelou que o agente da ameaça comprometeu e exfiltrou dados de nossa instância do Salesforce entre 12 e 17 de agosto de 2025, após a observação de reconhecimento inicial em 9 de agosto de 2025. Uma análise detalhada confirmou que a exposição foi limitada aos objetos de casos do Salesforce, que consistem principalmente em tickets de suporte ao cliente e seus dados associados em nossa instância do Salesforce. Esses objetos de casos contêm informações de contato de clientes relacionadas aos casos de suporte, linhas de assunto dos casos e corpo da correspondência dos casos, mas _não_ incluem anexos aos casos. A Cloudflare não solicita nem exige que os clientes compartilhem segredos, credenciais ou chaves de API em casos de suporte. No entanto, em alguns cenários de solução de problemas, os clientes podem colar chaves, logs ou outras informações confidenciais nos campos de texto dos casos. Qualquer coisa compartilhada por meio desse canal agora deve ser considerada comprometida.

Acreditamos que esse incidente não foi um evento isolado, mas que o agente da ameaça pretendia coletar credenciais e informações de clientes para ataques futuros. Considerando que centenas de organizações foram afetadas por esse comprometimento do Drift, suspeitamos que o agente da ameaça usará essas informações para lançar ataques direcionados contra clientes nas organizações afetadas. 

Esta postagem fornece uma linha do tempo do ataque, detalha nossa resposta e propõe recomendações de segurança para ajudar outras organizações a mitigar ameaças semelhantes.

_Ao longo deste post do blog, todas as datas e horários estão em UTC._

## Resposta e remediação da Cloudflare

Quando a Salesforce e a Salesloft nos notificaram em 23 de agosto de 2025 que a integração do Drift havia sido violada em várias organizações, incluindo a Cloudflare, lançamos imediatamente uma resposta a incidentes de segurança em toda a empresa. Ativamos equipes multifuncionais, reunindo especialistas em Segurança, TI, Produto, Jurídico, Comunicações e liderança empresarial sob uma estrutura de comando de incidentes única e unificada.

Estabelecemos quatro fluxos de trabalho prioritários claros com o objetivo de proteger nossos clientes e a Cloudflare:

  1. **Contenção imediata da ameaça:** cortamos todo o acesso do agente da ameaça desativando a integração comprometida do Drift, realizamos análise forense para entender o escopo do comprometimento e eliminamos a ameaça ativa do nosso ambiente.
  2. **Proteger nosso ecossistema de terceiros** : desconectamos imediatamente todas as integrações de terceiros a partir do Salesforce. Emitimos novas credenciais para todos os serviços e implementamos um novo processo para trocá-las semanalmente.
  3. **Proteger a integridade de nossos sistemas mais amplos** : expandimos a troca de credenciais para todos os nossos serviços de internet e contas de terceiros como medida de precaução para evitar que o invasor use dados comprometidos para acessar outros sistemas da Cloudflare.
  4. **Análise de impacto no cliente:** analisamos os dados dos objetos de casos do Salesforce para identificar se os clientes poderiam estar comprometidos e para garantir que recebessem uma comunicação oportuna e precisa sobre a possível exposição.



## Linha do tempo do ataque e resposta da Cloudflare

Nossa investigação forense reconstruiu as atividades do agente da ameaça contra a Cloudflare, que ocorreram entre 9 e 17 de agosto de 2025. A seguir está um resumo cronológico das ações do agente da ameaça, incluindo o reconhecimento inicial antes do comprometimento inicial.

### 9 de agosto de 2025: primeiros sinais de reconhecimento

Às **11:51** , o GRUB1 tentou validar um token de API emitido pela Cloudflare para a API do Salesforce. O agente usou o Trufflehog (um popular scanner de segredos de código aberto) como seu User-Agent e enviou uma solicitação de verificação para `client/v4/user/tokens/verify`. A solicitação falhou com um `404 Not Found`, confirmando que o token era inválido. A origem deste token de API é incerta, ele pode ter sido obtido de várias origens, incluindo outros clientes da Drift que o GRUB1 pode ter comprometido antes da Cloudflare. 

### 12 de agosto de 2025: comprometimento inicial da Cloudflare

Às **22:14** , o GRUB1 obteve acesso à instância do Salesforce da Cloudflare usando uma credencial roubada utilizada pela integração do Salesloft. Usando essa credencial, o GRUB1 efetuou login no endereço de IP `44[.]215[.]108[.]109` e fez uma solicitação GET para o endpoint de API `/services/data/v58.0/sobjects/` . Essa ação pareceu enumerar todos os objetos em nosso ambiente do Salesforce, proporcionando ao agente da ameaça uma visão geral abrangente dos dados armazenados ali.

### 13 de agosto de 2025: expansão do reconhecimento

Um dia após a violação inicial, o agente da ameaça, GRUB1, lançou um ataque subsequente do mesmo endereço de IP, `44[.]215[.]108[.]109`. A partir das **19h33** , o agente da ameaça roubou dados de clientes dos objetos de casos do Salesforce. Primeiro, ele reexecutou uma enumeração de objetos para confirmar a estrutura dos dados e, em seguida, recuperou imediatamente o esquema dos objetos de caso usando o endpoint `/sobjects/Case/describe/`. Isso foi seguido por uma ampla consulta do Salesforce que enumerou campos do objeto de casos do Salesforce.

### 14 de agosto de 2025: compreendendo nosso ambiente Salesforce

O agente da ameaça, GRUB1, dedicou horas para realizar um reconhecimento abrangente da instância do Salesforce da Cloudflare a partir do endereço de IP `44[.]215[.]108[.]109`. Parece que o objetivo dele era desenvolver uma compreensão do nosso ambiente. Durante várias horas, ele executou uma série de consultas direcionadas:

  * **00:17 -** Ele mediu a escala da instância contando contas, contatos e usuários; 
  * **04:34 -** Análise de fluxos de trabalho de caso consultando CaseTeamMemberHistory; e 
  * **11:09 -** Confirmou que estava em um ambiente de produção ao identificar o objeto Organization. 



O agente da ameaça concluiu seu reconhecimento com consultas adicionais para entender como nosso sistema de suporte ao cliente opera, incluindo como os membros da equipe lidam com diferentes tipos de casos, como os casos são atribuídos e escalados, e como nossos processos de suporte funcionam, e, em seguida, consultou o endpoint /limits/ para conhecer os limites operacionais da API. As consultas executadas pelo GRUB1 forneceram a ele insights sobre seu nível de acesso, o tamanho dos objetos de casos e os limites precisos da API que precisava respeitar para evitar a detecção em nosso ambiente Salesforce.

### 16 de agosto de 2025: preparando para a operação

Após o reconhecimento em 14 de agosto de 2025, não observamos tráfego ou logins bem-sucedidos do agente da ameaça, GRUB1, por quase 48 horas. 

Ele retornou em 16 de agosto de 2025. Às **19h26** , o GRUB1 se conectou novamente à instância do Salesforce da Cloudflare com o endereço de IP `44[.]215[.]108[.]109` e, às **19h28** , executou uma única consulta final: `SELECT count() FROM Case`. Esta ação serviu como um "ensaio" final para verificar o tamanho exato do conjunto de dados que ele estava prestes a roubar, marcando o fim definitivo da fase de reconhecimento e preparando o terreno para o ataque principal. 

### 17 de agosto de 2025: exfiltração final e encobrimento

O GRUB1 iniciou a fase de exfiltração de dados mudando para uma nova infraestrutura, fazendo login às **11:11:23** do endereço de IP `208[.]68[.]36[.]90`. Depois de realizar uma verificação final no tamanho do objeto de caso, ele lançou um trabalho do Salesforce Bulk API 2.0 às **11:11:56**. Em pouco mais de três minutos, ele conseguiu exfiltrar um conjunto de dados contendo o texto dos casos de suporte, mas sem quaisquer anexos ou arquivos, em nossa instância do Salesforce. Às **11:15:42** , o GRUB1 tentou encobrir seus rastros excluindo o trabalho da API. Embora essa ação tenha ocultado a evidência principal, nossa equipe conseguiu reconstruir o ataque a partir dos logs residuais. 

Não observamos mais nenhuma atividade desse agente de ameaça após 17 de agosto de 2025.

### 20 de agosto de 2025: ação do fornecedor antes da notificação

A Salesloft revogou as conexões Drift-to-Salesforce em toda a sua base de clientes e publicou um aviso em seu site. Naquele momento, a Cloudflare ainda não havia sido notificada, e não tínhamos qualquer indicação de que essa ação do fornecedor pudesse estar relacionada ao nosso ambiente.

### 23 de agosto de 2025: notificações da Salesforce e da Salesloft para a Cloudflare

Nossa resposta a este incidente começou quando a Salesforce e a Salesloft nos notificaram sobre atividades incomuns relacionadas ao Drift. Implementamos prontamente as etapas de contenção recomendadas pelos fornecedores e os envolvemos para coletar informações. 

### 25 de agosto de 2025: a Cloudflare inicia a atividade de resposta

Em 25 de agosto, havíamos recebido informações adicionais sobre o incidente e intensificamos nossa resposta além das medidas de contenção inicialmente recomendadas pelo fornecedor. Iniciamos nossa própria investigação abrangente e esforço de remediação.

Nossa primeira prioridade foi cortar o acesso do GRUB1 na origem. Desativamos a conta de usuário do Drift, revogamos seu ID de cliente e segredos, e eliminamos completamente todo o software Salesloft e extensões de navegador dos sistemas da Cloudflare. Essa remoção abrangente mitigou o risco de o agente da ameaça reutilizar tokens comprometidos, recuperar acesso por meio de sessões obsoletas ou explorar extensões de software para persistência.  
  
Separadamente, ampliamos nossa revisão de segurança para incluir todos os serviços de terceiros conectados ao nosso ambiente Salesforce, trocando credenciais como medida de precaução para impedir qualquer possível movimento lateral do agente da ameaça. 

Como usamos o Salesforce como nossa principal ferramenta para gerenciar nossos dados de suporte ao cliente, havia o risco de que os clientes tivessem enviado segredos, senhas ou outros dados confidenciais em suas solicitações de atendimento ao cliente. Precisávamos entender qual material confidencial o invasor possuía agora. 

Imediatamente nos concentramos em saber se algum desses dados poderia ter sido usado para comprometer as contas, sistemas ou infraestrutura de nossos clientes. Examinamos os dados obtidos pelo agente da ameaça para verificar se continham credenciais expostas, já que os casos incluem campos de texto livre onde os clientes podem enviar tokens de API da Cloudflare, chaves ou logs para nossa equipe de suporte. Nossas equipes desenvolveram ferramentas de varredura personalizadas usando regex, entropia e técnicas de correspondência de padrões para detectar possíveis segredos da Cloudflare em grande escala. 

Nossa investigação confirmou que a exposição foi estritamente limitada ao texto livre em objetos de casos do Salesforce, e não a anexos ou arquivos. Os casos são utilizados pelas equipes de vendas e suporte para se comunicarem internamente sobre questões de suporte ao cliente e para se comunicarem diretamente com os clientes. Como resultado, esses objetos de casos continham apenas dados de texto consistindo em:

  * Linha de assunto do caso da Salesforce
  * O corpo do caso (texto livre que pode incluir qualquer correspondência, como chaves, segredos, etc., se fornecido pelo cliente à Cloudflare)
  * Informações de contato do cliente (por exemplo, nome da empresa, endereço de e-mail do solicitante, número de telefone, nome de domínio da empresa e país da empresa)



Essa conclusão foi validada por meio de analises extensivas de integrações, atividades de autenticação, telemetria de endpoints e logs de rede.

### 26 a 29 de agosto de 2025: escalar a resposta e medidas proativas

Embora as credenciais principais do Salesforce e do Salesloft já tivessem sido trocadas, nossa próxima etapa foi encerrar e restabelecer com segurança nossas integrações de terceiros. Começamos a reintegrar metodicamente os serviços encerrados, garantindo que cada um recebesse novas credenciais e se sujeitasse a controles de segurança mais rigorosos.

Enquanto isso, nossas equipes continuaram a analisar os dados que foram exportados. Com base na análise, triamos e validamos possíveis exposições, operando sob o princípio de que quaisquer dados que pudessem ter sido expostos foram examinados. Isso nos permitiu tomar medidas diretas ao trocar os tokens emitidos pela plataforma da Cloudflare imediatamente após a descoberta, um total de 104 tokens de API foram trocados. Nenhuma atividade suspeita foi identificada relacionada a esses tokens. 

### 2 de setembro de 2025: clientes notificados****

Com base na análise detalhada da Cloudflare, todos os clientes impactados foram formalmente notificados por e-mail e por avisos de banner em nosso painel com informações sobre o incidente e as próximas etapas recomendadas. 

## Recomendações para todas as organizações

Esse incidente destaca a necessidade crítica de maior vigilância na segurança de aplicativos SaaS e outras integrações de terceiros. Os dados comprometidos em centenas de empresas alvo desse ataque podem ser utilizados para lançar ataques adicionais. Recomendamos fortemente que todas as organizações adotem as seguintes medidas de segurança:

  * **Desconectar o Salesloft e seus aplicativos:** desconecte imediatamente todas as conexões do Salesloft do seu ambiente Salesforce e desinstale qualquer software ou extensões de navegador relacionados.
  * **Trocar credenciais:** redefina as credenciais de todos os aplicativos e integrações de terceiros conectados à sua instância do Salesforce. Troque quaisquer credenciais que possam ter sido compartilhadas com a Cloudflare anteriormente em um caso de suporte. Com base no escopo e na intenção desse ataque, também recomendamos trocar todas as credenciais de terceiros no seu ambiente, bem como quaisquer credenciais que possam ter sido incluídas em um chamado de suporte de qualquer outro fornecedor. 
  * **Implementar troca de credenciais frequente:** estabeleça um cronograma de troca regular para todas as chaves de API e outros segredos usados em suas integrações para reduzir a janela de exposição.
  * **Analisar dados de casos de suporte:** analise todos os dados de casos de suporte de clientes com seus provedores terceirizados para identificar quais informações confidenciais podem ter sido expostas. Procure por casos que contenham credenciais, chaves de API, detalhes de configuração ou outros dados confidenciais que os clientes possam ter compartilhado. Para clientes da Cloudflare especificamente: você pode acessar o histórico de casos de suporte através do painel da Cloudflare em Suporte > Suporte Técnico > Minhas Atividades, onde é possível filtrar casos ou usar o recurso "Baixar Casos" para realizar uma análise abrangente.
  * **Realizar análise forense:** **** analise logs de acesso e permissões de todas as integrações de terceiros e analise [os materiais públicos](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift) associados ao incidente Drift e realize uma análise de segurança de seu ambiente, conforme apropriado.
  * **Aplicar o princípio do menor privilégio:** audite todos os aplicativos de terceiros para garantir que operem com o nível mínimo de acesso (menor privilégio) necessário para sua função e assegure que contas de administrador não sejam usadas por fornecedores. Além disso, imponha controles rigorosos, como restrições de endereços de IP e vinculação de sessão, em todas as conexões de terceiros e business-to-business (B2B).
  * **Aprimorar o monitoramento e os controles:** implante monitoramento aprimorado para detectar anomalias, como grandes exportações de dados ou logins de locais desconhecidos. Embora capturar logs de terceiros para terceiros possa ser difícil, é imperativo que esses logs façam parte de suas equipes de operações de segurança.



## Indicadores de comprometimento

Abaixo estão as indicações de comprometimento (IOCs) que observamos do GRUB1. Estamos publicando tais indicações para que outras organizações, e especialmente aquelas que possam ter sido afetadas pela violação do Salesloft, possam pesquisar seus logs para confirmar se o mesmo agente da ameaça não acessou seus sistemas ou terceiros.

Indicador| Tipo| Descrição  
---|---|---  
208[.]68[.]36[.]90| IPV4| Infraestrutura baseada na DigitalOcean   
44[.]215[.]108[.]109| IPV4| Infraestrutura baseada na AWS   
TruffleHog| Agente de usuário| Ferramenta de varredura de segredos de código aberto  
Salesforce-Multi-Org-Fetcher/1.0| Agente de usuário| Cadeia de caracteres de agente de usuário vinculada a ferramentas maliciosas  
Salesforce-CLI/1.0| Agente de usuário| Interface de linha de comando (CLI) do Salesforce  
python-requests/2.32.4| Agente de usuário| Agente de usuário que pode indicar scripts personalizados   
Python/3.11 aiohttp/3.12.15| Agente de usuário| Agente de usuário que pode permitir várias chamadas de API em paralelo  
  
## Conclusão

Somos responsáveis pelas ferramentas que selecionamos e, quando essas ferramentas são comprometidas por agentes de ameaças sofisticados, assumimos as consequências. Nossa equipe respondeu ao aviso, e nossa investigação confirmou que o impacto foi estritamente limitado aos dados em objetos de casos do Salesforce, sem comprometimento de outros sistemas ou da infraestrutura da Cloudflare.

Dito isto, consideramos inaceitável o comprometimento de _quaisquer_ dados. Nossos clientes confiam seus dados, sua infraestrutura e sua segurança à Cloudflare. Por sua vez, às vezes confiamos em ferramentas de terceiros que precisam ser monitoradas e rigorosamente limitadas em relação ao que podem acessar. Somos responsáveis por isso. Decepcionamos nossos clientes. Por isso, pedimos sinceras desculpas.

À medida que as ferramentas de terceiros se integram cada vez mais aos dados corporativos internos em todo o setor, precisamos abordar cada nova ferramenta com um escrutínio cuidadoso. Este incidente afetou centenas de organizações através de um único ponto de integração, destacando os riscos interconectados no cenário tecnológico atual. Estamos comprometidos em desenvolver novos recursos para nos ajudar e ajudar nossos clientes na defesa contra tais ataques no futuro. Fique atento aos anúncios durante a Semana de Aniversário da Cloudflare no final deste mês.

Também estamos comprometidos em compartilhar inteligência contra ameaças e pesquisa com a comunidade de segurança em geral. Nas próximas semanas, nossa equipe, Cloudforce One, publicará um blog detalhado analisando as técnicas do GRUB1 para apoiar a comunidade mais ampla na defesa contra campanhas semelhantes.

## Cronograma detalhado do evento

A tabela a seguir oferece uma visão detalhada e cronológica das ações específicas do GRUB1 durante o incidente.

Data/Hora (UTC)| Descrição do evento  
---|---  
09-08-2025 11:51:13| O GRUB1 observou o uso do Truffug e tentou verificar um token em relação a uma instância de cliente da Cloudflare: cliente/v4/user/tokens/verify, e recebeu um erro 404 de 44[.]215[.]108[.]109  
12/08/2025 22:14:08| O GRUB1 fez login na instância do Salesforce da Cloudflare a partir de 44[.]215[.]108[.]109  
12/08/2025 22:14:09| O GRUB1 enviou uma solicitação GET para uma lista de objetos na instância do Salesforce da Cloudflare: /services/data/v58.0/sobjects/  
13/08/2025 19:33:02| O GRUB1 fez login na instância do Salesforce da Cloudflare a partir de 44[.]215[.]108[.]109  
13/08/2025 19:33:03| O GRUB1 enviou uma solicitação GET para uma lista de objetos na instância do Salesforce da Cloudflare: /services/data/v58.0/sobjects/  
13/08/2025 19:33:07 e 19:33:09| O GRUB1 enviou uma solicitação GET de informações de metadados para o caso na instância do Salesforce da Cloudflare: /services/data/v58.0/sobjects/Case/describe/  
13/08/2025 19:33:11| O GRUB1 foi observado pela primeira vez executando uma consulta Salesforce: uma consulta ampla contra o objeto de caso por 44[.]215[.]108[.]109. Isso produziu uma das primeiras e maiores respostas de dados, consistente com o reconhecimento por meio da recuperação de registros em massa  
14/08/2025 00:17:40| O GRUB1 lista os objetos disponíveis e conta os objetos “Account”, “Contact” and “User”.  
14/08/2025 00:17:47| O GRUB1 consultou a tabela Account na instância do Salesforce da Cloudflare: consulta “SELECT COUNT() FROM Account” na instância do Salesforce da Cloudflare  
14/08/2025 00:17:51| O GRUB1 consultou a tabela Contact na instância do Salesforce da Cloudflare: consulta "SELECT COUNT() FROM Contact" na instância do Salesforce da Cloudflare  
14/08/2025 00:18:00| O GRUB1 consultou a tabela User na instância do Salesforce da Cloudflare: consulta "SELECT COUNT() FROM User" na instância do Salesforce da Cloudflare  
14/08/2025 04:34:39| O GRUB1 consultou "CaseTeamMemberHistory” na instância do Salesforce da Cloudflare: “SELECT Id, IsDeleted, Name, CreatedDate, CreatedById, LastModifiedDate, LastModifiedById, SystemModstamp, LastViewedDate, LastReferencedDate, Case__c FROM CaseTeamMemberHistory__c LIMIT 5000”  
14/08/2025 11:09:14| O GRUB1 consultou a tabela Organization na instância do Salesforce da Cloudflare: “SELECT Id, Name, OrganizationType, InstanceName, IsSandbox FROM Organization LIMIT 1”  
14/08/2025 11:09:21| O GRUB1 consultou a tabela User na instância do Salesforce da Cloudflare: “SELECT Id, Username, Email, FirstName, LastName, Name, Title, CompanyName, Department, Division, Phone, MobilePhone, IsActive, LastLoginDate, CreatedDate, LastModifiedDate, TimeZoneSidKey, LocaleSidKey, LanguageLocaleKey, EmailEncodingKey FROM User WHERE IsActive = :x ORDER BY LastLoginDate DESC NULLS LAST LIMIT 20”  
14/08/2025 11:09:22| O GRUB1 enviou uma solicitação GET no LimitSnapshot na instância do Salesforce da Cloudflare: /services/data/v58.0/limits/  
16/08/2025 19:26:37| O GRUB1 fez login na instância do Salesforce da Cloudflare de 44[.]215[.]108[.]109  
16/08/2025 19:28:08| O GRUB1 consultou a tabela Cases na instância do Salesforce da Cloudflare: caso SELECT COUNT() FROM  
17/08/2025 11:11:23| O GRUB1 conectou na instância do Salesforce da Cloudflare de 208[.]68[.]36[.]90  
17/08/2025 11:11:55| O GRUB1 consultou a tabela Case na instância do Salesforce da Cloudflare: caso SELECT COUNT() FROM e  
17/08/2025 11:11:56 às 11:15:18| O GRUB1 aproveitou o Salesforce BulkAPI 2.0 de 208[.]68[.]36[.]90 para executar um trabalho para exfiltrar o objeto Cases   
17/08/2025 11:15:42| O GRUB1 aproveitou o Salesforce Bulk API 2.0 de 208[.]68[.]36[.]90 para excluir o trabalho executado recentemente usado para exfiltrar o objeto Cases  
]]>4769G2MCNVfvZe8a8Rr8bv
