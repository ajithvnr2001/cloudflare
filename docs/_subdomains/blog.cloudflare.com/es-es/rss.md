---
url: https://blog.cloudflare.com/es-es/rss/
title: Blog de Cloudflare
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:16:14.098155+00:00
---

# Blog de Cloudflare

> Source: https://blog.cloudflare.com/es-es/rss/

Blog de CloudflareAnálisis técnicos en profundidad, actualizaciones de productos y perspectivas de los equipos que ayudan a construir una Internet mejor.https://blog.cloudflare.com/es-es/ es-eshttps://blog.cloudflare.com/favicon.icoBlog de Cloudflarehttps://blog.cloudflare.com Thu, 08 Oct 2026 08:16:10 GMTInternet cuenta ahora con un nuevo públicohttps://blog.cloudflare.com/es-es/agentic-web/ Thu, 08 Oct 2026 07:19:00 GMTMás de la mitad del tráfico que llega a los sitios web alojados en Cloudflare ahora es automatizado, y los agentes de IA representan el crecimiento más rápido. Te ofrecemos las herramientas para que puedas ver quién visita tus sitios web, decidir a quién dejas entrar y cobrar por el acceso.AgentesAIAI Bots (ES)AI SearchSemana aniversarioDurante la mayor parte de su historia, Internet tenía un único público que pagaba las facturas: la gente. Leíamos los artículos, veíamos los anuncios y comprábamos las suscripciones. Los bots siempre han estado ahí, pero en su mayoría eran grandes operaciones automatizadas que no veían anuncios, no pagaban nada ni leían de forma significativa.

Eso está cambiando muy rápido. A finales de 2024, Cloudflare gestionaba una media de 63 millones de solicitudes HTTP _por segundo_. Hoy en día, esa cifra casi se ha duplicado hasta los 115 millones, con picos que superan los 150 millones. Durante el último año, las solicitudes diarias de los agentes de IA en nuestra red crecieron más de un 1700 %. Este año, por primera vez, más de la mitad del tráfico de Internet no era humano.

La web que usan los humanos no se ha reducido para dejarles espacio. Ha aparecido otro tipo de público: los agentes, programas que actúan en nombre de las personas. Se sitúan a medio camino entre los humanos y los bots tradicionales. No responden a los anuncios, pero normalmente hay una persona detrás de ellos con una tarea que cumplir. Para las empresas que aprenden a atenderlos y a sacarles partido, los agentes son un valor añadido. Para las que no lo hacen, son un lastre.

Lo que necesitan nuestros clientes no ha cambiado: que los vean, contar buenas historias, crear experiencias geniales y vender. Lo que sí ha cambiado es que ahora más de la mitad de tus visitantes son programas. Nuestra labor es ayudarte a atender a ambos públicos.

## Más tráfico, menos ingresos

Durante treinta años, la web funcionó con un único mecanismo: dejabas que los motores de búsqueda rastrearan tu sitio, ellos te enviaban visitas y tú convertías esas visitas en negocio. Que te encontraran y que te pagaran era lo mismo.

La IA ha hecho que este delicado equilibrio se rompa. Ahora, los motores de respuestas leen la página y le ofrecen al lector un resumen. Esto le cuesta ancho de banda a los sitios web sin que lleve a ningún humano a un sitio donde se generen anuncios o pagos. Las máquinas siguieron llegando, y la audiencia que pagaba por la web dejó de llegar a esos sitios. Algunas de las categorías más rastreadas, como el comercio minorista, el software informático, las tecnologías de la información y los servicios, y los servicios financieros, han visto cómo el tráfico humano se reducía hasta un 40 % en menos de un año.

El resultado es que los ingresos por solicitud están cayendo, mientras que los costes suben. Cada solicitud automatizada sigue consumiendo ancho de banda, recursos informáticos y capacidad de origen, y una parte cada vez mayor de esas solicitudes no genera ninguna visita, ninguna impresión publicitaria ni ninguna suscripción. Nuestro primer instinto fue bloquear todo el tráfico automatizado. El año pasado recomendamos bloquear los rastreadores de entrenamiento de IA en los nuevos dominios para que los propietarios de los sitios pudieran, al menos, negarse a que su contenido se utilizara para crear modelos. En la primavera de 2025, el 22 % de las solicitudes de los rastreadores que vimos eran para entrenamiento de IA (según el propósito declarado por los propios rastreadores). En junio de 2026, la cifra ya era del 52 %. El problema es que un "no" generalizado no es un enfoque lo suficientemente matizado para la economía de Internet que se está construyendo ahora mismo.

Existe la oportunidad de dar respuesta a los agentes. Si lo haces bien, estarás a la vanguardia de un nuevo modelo de negocio. Sin embargo, si lo haces mal, los resultados serán los mismos que los de generaciones de sitios web que se vieron perjudicados por los cambios en los algoritmos de los motores de búsqueda.

## Parte de ese tráfico es un cliente

Un agente que reserva una mesa, compara presupuestos de seguros o compra un conjunto de datos para un investigador es un cliente. Simplemente no es un cliente humano.

La parte del tráfico automatizado que crece más rápido ya no son los rastreadores. Son los agentes: software que recurre páginas en nombre de una persona, a menudo porque esa persona le ha preguntado algo a un asistente virtual. Ese tráfico de agentes sigue las rutinas humanas, con un ritmo semanal y un descenso durante las vacaciones de verano. Si rechazas a un agente, puede que estés rechazando a la persona que lo envió.

Los agentes también se comportan de forma diferente a los rastreadores de entrenamiento. Un rastreador de entrenamiento recopila tus páginas para crear un modelo. Un agente vuelve cada vez que alguien pregunta por ese contenido, por lo que este tráfico crece en función del número de preguntas que hace la gente, no de lo que publiques.

No puedes hacer negocios con un público al que no ves, al que no puedes distinguir, al que no puedes imponer condiciones y al que no puedes cobrar. Hasta hace poco, con la mayor parte del tráfico no humano de la web, ninguna de esas cuatro cosas era posible.

### Descubre quién visita realmente tu sitio

“Bot de IA” ya no significa nada útil. Lo que importa es lo que hace un bot. Las herramientas de Cloudflare **AI Crawl Control** , **Business Insights** y **BotBase** muestran a los propietarios de sitios quién está rastreando, qué recogen, qué devuelven y cuáles de tus URL son las que más les interesan.

El nombre de un bot solo tiene valor si puedes confiar en él. Con **Web Bot Auth** , los operadores como OpenAI, Google y AWS, firman criptográficamente las solicitudes de sus agentes, de modo que un sitio web puede distinguir un agente real de un suplantador sin tener que adivinarlo a partir de direcciones IP o cadenas de agente de usuario. Vemos más de 500 000 millones de solicitudes de bots verificadas cada semana.

### Define tus condiciones

En julio, sustituimos la única opción “bloquear bots de IA” por controles independientes[ de búsqueda, agente y entrenamiento](https://blog.cloudflare.com/content-independence-day-ai-options/), disponibles en todos los planes, incluido el gratuito. Los datos demostraron por qué era necesaria esa distinción. Menos del 1 % de los sitios en Cloudflare bloquean los rastreadores de búsqueda, mientras que el 17 % bloquea el entrenamiento. Los propietarios de los sitios nunca intentaron esconderse. Pero con el aumento del tráfico de agentes y las nuevas formas en que estos utilizan la información, de repente se encontraron sin transparencia ni control sobre cómo se utilizaba su contenido. Que los encuentren ya no garantiza que les paguen, y quieren que los encuentren sin que se aprovechen de ellos.

Esto resulta especialmente complicado en el caso de los rastreadores de uso mixto. Cuando un bot realiza tanto búsquedas como entrenamiento, rechazar uno significa rechazar el otro. El 15 de septiembre lanzamos[ la opción No permitir el entrenamiento de IA](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers/). Te mantiene indexado para las búsquedas, al tiempo que utiliza mecanismos específicos para rastreadores con el fin de indicar al operador que no utilice tus datos para el entrenamiento. Apple, Google y Microsoft se han comprometido a respetar esta medida.[ Cloudflare Radar](https://radar.cloudflare.com/ai-insights?cf_page=agentic-web%2F#ai-bot-transparency) también realiza un seguimiento público del comportamiento de los rastreadores.

Ahora, a los dominios nuevos se les muestran configuraciones recomendadas en función de cómo gana dinero el sitio, en lugar de qué software lo visita. En el caso de los sitios financiados por publicidad, puedes desactivar fácilmente el entrenamiento y bloquear agentes en las páginas que contienen anuncios, ya que un anuncio solo se paga cuando una persona lo ve. Puedes cambiar cualquiera de estos ajustes en cualquier momento.

### Obtén ingresos

En agosto de 2026, describimos[ la web agéntica que estamos creando](https://blog.cloudflare.com/the-agentic-internet/) como legible, visible, disponible y rentable. La última palabra, “rentable”, es la que determina si la web abierta puede autofinanciarse. La web necesita una forma de decir “ _sí, si pagas_ ” en lugar de un “ _sí_ ” o un “ _no_ ” binario.

El mercado de las licencias muestra tanto cuánta demanda hay como dónde están las carencias. Desde 2023 se han firmado más de 50 acuerdos entre editoriales y empresas de IA. Casi todos son a medida y bilaterales, entre grandes editoriales y grandes empresas de IA. Demuestran que el contenido tiene valor. Pero no llegan a la mayor parte de la web, ni a la mayoría de los compradores.

No todos los activos deberían venderse de la misma manera. El contenido y los conjuntos de datos de alto valor necesitan una red de confianza, en la que se identifique a los compradores y estos informen de cómo se ha utilizado la obra. Servicios como las API y las herramientas MCP no funcionan así: cada solicitud se considera un uso.

Por eso estamos creando una solución para ambos.

[**Pago por uso**](http://blog.cloudflare.com/pay-per-use?cf_page=agentic-web%2F) llega a los sitios web a los que las licencias directas no pueden llegar. La mayoría de los creadores de contenido nunca conseguirán un acuerdo a medida con cada empresa de IA, y ninguna empresa de IA puede negociar con millones de sitios web. El pago por uso es el puente. No cobra por el rastreo. Paga cuando el contenido se usa de verdad. Cada comprador es un rastreador verificado, que es lo que hace que esta red sea de confianza, y cada uno define qué cuenta como uso y cuánto pagará.

Los creadores de contenido ven la oferta, eligen si quieren participar y pueden darse de baja cuando ya no les convenga. El comprador informa de cada uso, Cloudflare comprueba esos informes, luego factura al comprador y paga al creador de contenido. Los informes son tan importantes como el pago. Los creadores ven qué se ha usado, cuándo y cuánto han ganado, y, cuando el comprador lo comunica, también reciben información sobre qué consultas han dado lugar a su trabajo. Los acuerdos de licencia rara vez muestran nada de eso. Esto crea un ciclo de retroalimentación: los creadores de contenido se enteran de lo que la gente realmente busca y, a partir de ahí, pueden decidir qué tratar, qué actualizar y qué poner a disposición de los agentes.

No habrá una única definición de “uso”. Un motor de búsqueda que cita una fuente, un agente de investigación que cita un extracto y un agente de compras que realiza una compra crean diferentes tipos de valor, y cada uno querrá su propio modelo de negocio. Los compradores pueden participar a través de múltiples modelos de negocio utilizando la misma infraestructura, sin necesidad de una nueva integración para los editores. Piensa en una revista especializada para ingenieros navales, con unos pocos miles de suscriptores y pocas perspectivas de un acuerdo de licencia de IA. Recibe un pago de cada empresa de IA participante que utilice su trabajo.

[**Monetization Gateway**](https://blog.cloudflare.com/monetization-gateway-beta) capta valor que nunca antes había tenido una forma de cambiar de manos. Las cuentas, las claves API y las suscripciones sirven para los clientes que ya conoces, no para un agente que solo quiere hacer una consulta en un servicio que nunca ha usado antes. Nuestra versión beta cerrada permite a los clientes de Cloudflare de Estados Unidos que cumplan los requisitos ponerle un precio a cualquier cosa que pase por nosotros, usando el lenguaje de reglas que ya conocen. Cuando una regla coincide, devolvemos un código de error HTTP 402 “Pago requerido” usando el protocolo abierto x402, y el agente paga directamente al vendedor.

Esto hace mucho más que recuperar ingresos perdidos. Los agentes son clientes por derecho propio: pagan por los datos, las API y las herramientas que usan, tanto si la solicitud es una compra completa como si es un paso dentro de una tarea más amplia.

Monetization Gateway establece precios por solicitud, por consulta o por token, a precios fijos o con un límite máximo. Una web de estadísticas deportivas que se financia con anuncios puede cobrar una pequeña cantidad cada vez que un agente pregunte “¿quién es el líder de la liga en asistencias?”. Cuando anunciamos Monetization Gateway, miles de vendedores se apuntaron a la lista de espera, y su petición más habitual fue “cobrad a los agentes, no a las personas”. Nosotros también somos nuestro primer cliente. AI Gateway de Cloudflare usa Monetization Gateway para que los agentes paguen por la inferencia, así detectamos los fallos antes que nuestros clientes.

Para los compradores, ambos productos son mejores que una página de bloqueo: acceso fiable y una forma de llegar a millones de sitios web en lugar de tener que gestionar un acuerdo de licencia o una clave de API cada vez. Cada solicitud de pago deja un recibo que muestra qué se ha comprado y que se ha pagado.

Tanto Pago por uso como Monetization Gateway son apuestas, creadas junto con los clientes a partir de elementos básicos comunes: identidad, medición, precios, liquidación y análisis. Funcionan juntos, así que un creador de contenido puede desactivar el entrenamiento, permitir la búsqueda, ganar dinero con las respuestas de IA y cobrar a los agentes por artículo desde un único panel de control. Los precios y la visibilidad aún no están resueltos, por eso ambos se lanzan en versión beta, moldeados por clientes reales y transacciones reales.

### Cada solicitud, más barata

El pago es la solución a la caída de los ingresos. El aumento de los costes es otro problema, y gran parte de él se debe simplemente al despilfarro. La mayoría de los rastreadores siguen descargando, una y otra vez, páginas diseñadas para personas, solo para extraer unos pocos párrafos de texto. Con demasiada frecuencia, los bots rastrean sitios que no han cambiado desde el último intento. Eso consume ancho de banda del sitio y recursos informáticos del rastreador, y ocurre antes incluso de que se escriba ninguna respuesta. Estamos trabajando con nuestros clientes y los rastreadores en herramientas que te ayudarán. Hoy mismo puedes ver el consumo de ancho de banda por operador en nuestro panel de control.

En julio, anunciamos un[ proyecto de investigación conjunto con OpenAI](https://www.cloudflare.com/press/press-releases/2026/cloudflare-announces-research-pilot-with-openai/?cf_page=agentic-web%2F), una iniciativa piloto pionera para explorar cómo los datos de la red global de Cloudflare pueden ayudar a los motores de búsqueda con IA a encontrar e indexar contenido relevante en la web abierta de forma más eficiente y eficaz. Tenemos previsto compartir nuestros resultados iniciales en las próximas semanas.

Para nuestros clientes, estamos lanzando herramientas y experiencias con un solo clic para que sus sitios web estén optimizados para este nuevo tipo de tráfico.[**** Markdown for Agents](https://blog.cloudflare.com/markdown-for-agents/) permite a los agentes leer una página sin el estilo adicional pensado para los ojos humanos, y[ WebMCP](https://blog.cloudflare.com/webmcp/) permite que un sitio web muestre las acciones directamente, en lugar de que los agentes tengan que adivinar qué botón pulsar.

## Por qué desarrollar en Cloudflare

Más del 20 % de la web está protegida por la red de Cloudflare, al igual que casi el 80 % de las principales empresas de IA. Vemos las dos caras de este mercado. Creamos las bases para la visibilidad, la identidad, los controles y la liquidación, y dejamos que el mercado decida qué cosas valen la pena.

El viejo modelo ya no existe, y el nuevo aún se está escribiendo. Juntos podemos dar forma a lo que venga después.

En una versión, unas pocas empresas controlan cómo los agentes encuentran cosas, demuestran quiénes son y pagan, y todos los demás pasan por ellas. En la otra, esos elementos son estándares abiertos que cualquiera puede implementar, y un sitio de cualquier tamaño puede establecer sus propias condiciones y cobrar. Nosotros preferimos esta última.

Por eso estas infraestructuras funcionan con estándares abiertos como x402 y Web Bot Auth, para que cualquiera pueda desarrollar sobre ellos. Los propietarios de dominios eligen sus propios proveedores de identidad, sus propios procesadores de pagos y sus propios socios agentes. Cloudflare es una opción, no la solución completa.

Durante décadas, la web la pagaban las personas que la visitaban. Ahora, el software que la visita en su nombre también puede pagar su parte.

]]>01M4D5J9H3WK5QD4N7SFTGVB85Creación de una autoridad de certificación poscuántica con los certificados de árbol de Merklehttps://blog.cloudflare.com/es-es/pq-ca-with-mtcs/ Thu, 08 Oct 2026 03:20:55 GMTDado que las firmas poscuánticas amenazan con sobrecargar los protocolos de enlace TLS y los registros de transparencia de certificados, los certificados de árbol de Merkle ofrecen un camino hacia una autenticación compacta y auditable. La nueva autoridad de certificación de Cloudflare ofrecerá emisión de MTC a escala.Certificate TransparencyCryptographyPost-QuantumSeguridadSemana aniversarioTLSCuando escribes una dirección en el navegador, ¿cómo sabes que te estás conectando a la página web correcta? La infraestructura de clave pública de la Web (Web PKI) es ese ecosistema complejo y distribuido de políticas, protocolos y operadores de infraestructura que te ayuda a confiar en que no te están redirigiendo a una página web incorrecta o maliciosa. En las últimas décadas, este ecosistema ha sufrido cambios importantes. Uno de ellos es la incorporación de la transparencia: el requisito, ahora obligatorio, de que todos los certificados se registren en registros públicos de transparencia de certificados. Ahora se enfrenta a otro reto: la inminente llegada de un ordenador cuántico, lo que nos ha llevado a dar el salto a la criptografía poscuántica (PQ) [para 2029](https://blog.cloudflare.com/post-quantum-roadmap/).

Esta transición no es sencilla: limitarse a incorporar la criptografía poscuántica en los certificados a escala de Internet provocaría una degradación inaceptable del rendimiento. Este momento exige un nuevo enfoque para la Web PKI, uno que nos permita tratar la transparencia como una propiedad propia en lugar de un complemento, y diseñar un nuevo sistema que escale las firmas poscuánticas de manera eficiente.

Tras obtener un amplio apoyo en todo el sector, los [certificados de árbol de Merkle](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/?cf_target_id=42E7E1D763C63E826F9E79E2C80FFC30) (MTC) se han perfilado como el camino a seguir. Este año, tras una exitosa [implementación experimental con Chrome](https://blog.cloudflare.com/bootstrap-mtc/), Cloudflare avanza a toda máquina con los MTC.

Tras el anuncio de hoy de que Cloudflare se convierte en una [autoridad de certificación (CA)](https://blog.cloudflare.com/cloudflare-certificate-authority/), nos complace compartir que esta CA admitirá la emisión de MTC, con el objetivo de incluirlos a principios de 2027 en el recién lanzado [almacén de raíces resistente a la computación poscuántica](https://googlechrome.github.io/chromerootprogram/index.html?cf_target_id=F4FF824C29C06E235EF2A30A35AA3B71) de Chrome. Como parte de nuestra misión de ayudar a mejorar Internet mejor, y siguiendo la tradición de Cloudflare de ofrecer la criptografía más sólida disponible [de forma gratuita](https://blog.cloudflare.com/post-quantum-crypto-should-be-free/), ofreceremos la emisión de MTC estándar sin coste alguno. Contar con una CA que admita tanto la emisión de certificados clásicos como de MTC nos permite establecer por defecto el método de autenticación más seguro disponible, proporcionando una ruta de actualización a PQ sencilla y eficaz para una gran parte de Internet.

## **El ecosistema de confianza actual**

Para entender cómo los MTC están cambiando las reglas del juego, empecemos por explicar un poco cómo funciona la confianza en la web hoy en día.

Por el lado del cliente, los navegadores —en este caso, los “clientes TLS”— mantienen programas raíz, que especifican un conjunto de políticas que las CA deben seguir para que se confíe en ellas. Por el lado del servidor, las CA son los guardianes de confianza: gestionan la infraestructura de emisión de certificados, donde validan la propiedad del dominio y certifican la vinculación entre un nombre de dominio y una clave pública que demuestra la propiedad de ese dominio.

Pero, ¿cómo comprobamos que las CA siguen las reglas? Aquí entra en juego la transparencia de certificados (CT), que hace que la emisión de certificados sea auditable públicamente. Cuando una CA emite un certificado, también debe enviarlo a al menos dos registros públicos. Cloudflare lleva gestionando la familia de registros de CT [Nimbus](https://blog.cloudflare.com/introducing-certificate-transparency-and-nimbus/) desde 2016 y, de cara al futuro, va a lanzar Raio, una nueva familia de [registros CT estáticos](https://blog.cloudflare.com/azul-certificate-transparency-log/).

Aunque el ecosistema de CT permite ver los certificados públicamente, eso no significa que estén emitidos correctamente o que sean seguros de usar. La monitorización ayuda en este sentido al comparar esos registros con lo que esperaban los propietarios de los dominios y al informar de actividades sospechosas. Cloudflare lanzó [la supervisión de la transparencia de certificados](https://blog.cloudflare.com/introducing-certificate-transparency-monitoring/) en 2019 y recientemente la ha puesto[ a disposición de todos](https://blog.cloudflare.com/certificate-transparency-monitoring-ga/). También publicamos mediciones a gran escala sobre certificados en la página de[ transparencia de certificados](https://radar.cloudflare.com/certificate-transparency?cf_page=pq-ca-with-mtcs%2F) de Radar (antes conocido como Merkle Town).

A medida que las organizaciones empiecen a actualizar sus servidores para usar la autenticación poscuántica, la supervisión de la transparencia de certificados cobrará aún más importancia a la hora de detectar posibles retrocesos poscuánticos. Los propietarios de dominios que hayan actualizado sus dominios a la autenticación poscuántica deberían supervisar los registros de CT en busca de certificados heredados emitidos de forma inesperada para evitar que los clientes caigan en una ruta de degradación maliciosa.

Parte del problema con el sistema actual es que la transparencia era un complemento, lo que provocaba problemas de escalabilidad. Los certificados suelen registrarse varias veces, en diferentes formatos, en múltiples registros, lo que obliga a los supervisores a descargar y procesar cada registro para no pasar por alto ninguna emisión. Esto puede resultar caro, lo que dificulta fomentar una amplia variedad de operadores de registros a escala de Internet. Según nuestras estimaciones, las firmas poscuánticas multiplicarán por 40 la cantidad de datos que deben almacenar los registros CT. Este reto de escalabilidad, y la consiguiente falta de alineación de incentivos, es el núcleo del problema de escalabilidad poscuántica.

## **El problema de escalabilidad poscuántica**

Hemos escrito mucho sobre los[ retos de escalar la criptografía poscuántica](https://blog.cloudflare.com/bootstrap-mtc/), pero en resumen: para permitir la autenticación de servidores a escala de Internet, la Web PKI debe autenticar aproximadamente 1000 millones de servidores TLS sin tener que precargar la clave pública de cada servidor en cada cliente. Tradicionalmente, las CA abordaban este problema utilizando cadenas de certificados como mecanismo de distribución de confianza. Pero con el tiempo, novedades como las comprobaciones de revocación de claves y la transparencia de certificados han añadido más claves públicas y firmas: cinco firmas y dos claves en un protocolo de enlace TLS típico. Las firmas poscuánticas son aproximadamente 40 veces más grandes que las clásicas, lo que genera una sobrecarga mayor que resultaría costosa de gestionar a gran escala para los clientes, las CA, los registros y los monitores.

Aquí es donde entran en juego los[ certificados de árbol de Merkle](https://datatracker.ietf.org/doc/draft-ietf-transcert-merkle-tree-certs) (MTC), un borrador de especificación del grupo de trabajo[ IETF PLANTS](https://datatracker.ietf.org/group/plants/about/) que describe una arquitectura para certificados poscuánticos compactos y eficientes. Los MTC agrupan los certificados en un árbol de Merkle de solo añadir, lo que permite a una CA firmar la raíz de ese árbol en lugar de muchos certificados individuales. Esto permite que los navegadores u otros clientes verifiquen un certificado mediante una prueba de inclusión compacta —una secuencia de hash criptográficos— comparándola con la raíz firmada del árbol, en lugar de validar cada certificado por separado. Una[ idea clave](https://datatracker.ietf.org/meeting/124/materials/slides-124-plants-solution-space-and-dispatched-work-00) detrás de los MTC es “no registres lo que emites, emite registrando”. Al unir la emisión y el registro, la transparencia se convierte en un requisito para el funcionamiento, en lugar de un complemento.

## **El papel de una autoridad de certificación en una PKI rediseñada**

Estamos desarrollando nuestra capacidad para emitir MTC como parte integral de la creación de una CA de Cloudflare. Eso significa estar al tanto de los nuevos requisitos del Programa de Raíces PQ y desarrollar una pila de software de emisión y replicación al mismo tiempo que creamos las instalaciones, las operaciones y las funciones de cumplimiento de una CA tradicional —¡nada fácil!

La ventaja es que podemos priorizar los requisitos y la arquitectura de esta nueva PKI poscuántica desde el primer día, construyendo nuestra infraestructura de una forma que se ajuste a los valores y a la red global de Cloudflare, con el objetivo de ser lo más transparentes posible al embarcarnos en este nuevo viaje.

Echemos un vistazo a la arquitectura actualizada para los MTC:

Si lo comparas con el ecosistema tradicional de las CA, verás que las responsabilidades de una CA siguen siendo prácticamente las mismas: validar el control de un dominio, vincularlo a una clave pública y emitir certificados. La principal diferencia es que, en el ecosistema MTC, en lugar de firmar los certificados directamente y luego registrarlos, la CA ahora mantiene un registro de transparencia respaldado por un árbol de Merkle, donde una prueba de inclusión que confirma que el certificado está efectivamente en el árbol sirve como ancla de confianza. Las CA también gestionarán _cofirmantes espejo_ que almacenan una copia de los registros de emisión, verificando su consistencia de “solo añadir” y garantizando la transparencia y disponibilidad de estos registros para el ecosistema en general.

### **Emisión de MTC**

Los MTC pueden presentarse en dos formas, ambas codificables en el formato de certificado X.509 que el software de cliente reconoce hoy en día, solo que con un algoritmo de firma “curioso”. En su forma _autónoma_ , el valor de la firma del certificado contiene una cabeza de árbol firmada conjuntamente de un registro de emisión y una prueba de inclusión (una secuencia de hash) que demuestra que el certificado está incluido en ese registro. Si los clientes pueden obtener las cabeceras de árbol firmadas conjuntamente fuera de banda (por ejemplo, a través de un mecanismo de actualización del navegador), el certificado se puede servir en formato _relativo a un hito_ , donde el valor de la firma consiste en la prueba de inclusión ligera, sin ninguna firma poscuántica pesada.

Para simplificar, echemos un vistazo a un ejemplo de emisión de certificados independientes. Cuando un sitio web quiere un certificado para su dominio, puede solicitarlo a una CA a través del protocolo ACME (Entorno Automatizado de Gestión de Certificados), que se encarga de las solicitudes de certificados, la validación del control del dominio y los flujos de trabajo de emisión. La infraestructura ACME de Cloudflare será una bifurcación de[ Boulder](https://github.com/letsencrypt/boulder), el software ACME ampliamente implantado y bien probado que utiliza Let’s Encrypt. Let's Encrypt está desarrollando activamente[ la compatibilidad con MTC](https://letsencrypt.org/2026/06/03/pq-certs) en Boulder, y tenemos pensado mantener nuestra propia bifurcación que incorpore estos cambios del proyecto original junto con modificaciones específicas de Cloudflare, contribuyendo al proyecto original siempre que sea posible.

Cuando la CA de MTC recibe una solicitud de emisión de certificado, el servidor ACME de la CA comprueba que el servidor controle realmente el dominio. Si se superan esas comprobaciones, la CA serializa esos datos y los añade a un registro de solo apéndice.

Tras añadir la entrada de MTC a su registro de emisión, la CA calcula el estado actualizado del registro y, a continuación, firma un punto de control sobre ese estado. Este punto de control certifica que la CA ha emitido todas las entradas incluidas en el árbol de Merkle del registro hasta ese momento.

A continuación, la CA envía el estado actualizado de su registro y el nuevo punto de control a un segundo firmante de confianza, que almacena de forma permanente una copia del registro de emisión de la CA y comprueba que cada nuevo estado sea de solo adición, coherente con el árbol anterior y esté correctamente formado. Esta firma adicional te da a ti, como cliente, y a los supervisores la confianza de que otra parte de confianza ha observado el mismo estado del registro y ha verificado que la CA no está mostrando visiones diferentes de las emisiones a distintas partes del ecosistema. También garantiza que los certificados emitidos estarán disponibles para su supervisión incluso si el registro de emisión de la CA no está disponible.

El[ borrador de la política del Programa de Raíces Resistentes al Cuántico de Chrome](https://googlechrome.github.io/chromerootprogram/cqrp/draft-policy/) exige al menos dos firmas conjuntas: una de un cofirmante espejo reconocido por Chrome y gestionado por una organización distinta, y otra de la propia CA MTC emisora. Por eso, gestionaremos servidores espejo para otras CA piloto y exigiremos al menos una firma conjunta independiente en los certificados que emitamos nosotros mismos.

Cloudflare implementará nuestro firmante espejo en[ Azul](https://github.com/cloudflare/azul), nuestro registro de transparencia de código abierto basado en Rust, y, para lograr la máxima interoperabilidad, implementará el protocolo[ tlog mirror de c2sp](http://c2sp.org/tlog-mirror).

Por último, tras recibir con éxito una firma conjunta de un firmante espejo, la CA genera un MTC con las firmas conjuntas, la clave pública del servidor y una prueba de inclusión. A continuación, envía ese MTC al servidor, ¡que ya podrá utilizarlo para TLS en adelante!

### **Entrega eficiente de firmas PQ: la optimización de los puntos de referencia**

Aunque los certificados independientes funcionan, siguen enviando grandes firmas PQ durante el protocolo de enlace TLS, lo que limita su eficiencia. Las verdaderas mejoras de rendimiento que aporta el diseño del MTC son los certificados relativos a puntos de referencia.

En lugar de enviar firmas conjuntas en cada certificado, las CA pueden designar como punto de referencia una secuencia de subárboles que cubran todos los certificados activos del registro, y distribuir esos subárboles (junto con los datos para autenticarlos) a los clientes a través de un servicio de actualización fuera de banda. Durante un protocolo de enlace TLS, la autenticación real con el servidor se produce cuando el navegador comprueba que los datos del certificado del servidor —incluidos su nombre de dominio y su clave pública— aparecen en un subárbol de confianza del registro de la CA. Si la prueba de inclusión vincula ese certificado a un punto de referencia firmado conjuntamente, y la clave pública demuestra entonces su posesión durante el protocolo de enlace TLS, el cliente sabe que se está comunicando con el servidor correcto.

Al transmitir periódicamente estas firmas y los metadatos del árbol a los clientes TLS fuera de banda, un pequeño conjunto de firmas por lotes de MTC puede cubrir de forma eficiente miles de millones de certificados emitidos por una CA determinada. Aunque los puntos de referencia son más eficientes a escala, no eliminan la necesidad de MTC independientes: los clientes pueden estar recién instalados, sin conexión o carecer de la actualización relevante del punto de referencia. Por eso es importante que los servidores mantengan un certificado de reserva independiente.

## **Los MTC en la práctica: resultados de nuestro experimento con Chrome**

Este año, hicimos un experimento con Chrome para comprobar si los MTC funcionaban entre un cliente y un servidor. Pusimos en marcha una “CA de arranque” (una CA falsa que simulaba el proceso de emisión) que emitía MTC respaldados por una cadena de certificados tradicional para una selección de dominios de Cloudflare en el plan gratuito de Cloudflare y los servimos al 50 % de los usuarios de Chrome Beta 146. A lo largo del experimento, servimos con éxito miles de millones de MTC.

En cuanto a TLS, descubrimos que el caso habitual es bastante eficiente: con un certificado relativo a un punto de referencia, el protocolo de enlace solo tiene que transmitir una clave pública, una firma y una prueba de inclusión de menos de 1 kB. En el experimento, recurrimos a la cadena de certificados tradicional en lugar de servir un certificado independiente en los casos en los que no pudimos negociar un certificado relativo a un punto de referencia con el cliente. En cuanto a CT, los MTC también cambian las propiedades de escalabilidad de la transparencia: el registro solo tiene que contener los hash de las claves públicas; no hay firmas por entrada, y la firma en la raíz del árbol cubre todo el registro. Esto evita la “explosión de certificados”, ya que el registro de emisión de la CA es la fuente de verdad para todos los certificados que emite la CA, y los usuarios del registro solo tienen que obtener una única copia de cada certificado.

El resultado: ¡los MTC realmente funcionan! En la mediana, el uso de un MTC es un 9 % más rápido con MTC de puntos de referencia que con una cadena de firmas clásica (aunque hay que reconocer que la mayor parte de esta mejora de rendimiento se debe a la eliminación de pasos intermedios). Y como hemos probado los MTC con firmas clásicas, esperamos una mejora aún mayor con las firmas poscuánticas. Satisfechos con estos resultados y con el nivel de colaboración intersectorial en torno a los MTC en el[ PLANTS WG](https://datatracker.ietf.org/wg/plants/documents/) de la IETF, empezamos a dar por concluido el experimento el mes pasado (agosto de 2026).

## **El futuro de los MTC**

Nos alegra mucho que nuestro experimento con Chrome haya demostrado que los MTC funcionan en la práctica, y nos hace especial ilusión poder emitir certificados como una CA de verdad.

Sin embargo, aún quedan cuestiones más amplias que solo podremos resolver llevando a cabo este gran experimento con todo el ecosistema PKI. ¿Podrán los supervisores independientes[ consultar y verificar](https://transparency.dev/summit2025/talks/verifiable-indexes.html) los registros de emisión de MTC a escala real? ¿Surgirán múltiples CA y firmantes conjuntos para que el sistema cuente con la diversidad necesaria para su resiliencia? ¿Cómo deberían los navegadores equilibrar las ventajas de rendimiento de los MTC compactos con puntos de referencia con las rutas alternativas necesarias para los clientes que no dispongan de puntos de referencia actualizados? Los MTC se han consolidado como el diseño de referencia para la autenticación poscuántica, pero demostrarlo a escala real de Internet requerirá la participación de un conjunto diverso de programas raíz, proveedores de navegadores, CA, servidores espejo, supervisores y la comunidad en general.

Consideramos un honor poder participar en esta nueva fase de la Web PKI y nos tomamos muy en serio la responsabilidad de gestionar la infraestructura de la CA. Las CA ocupan una posición privilegiada en el ecosistema de confianza: los navegadores, los propietarios de dominios y la gente de a pie confían en ellas para validar identidades correctamente, proteger las claves de firma, cumplir las políticas y funcionar de forma fiable. Antes de que los navegadores puedan confiar en la CA de Cloudflare para emitir MTC, tendremos que solicitar nuestra inclusión en el almacén raíz resistente a la computación cuántica de Chrome y someternos a un riguroso proceso de evaluación. Acogemos con agrado ese escrutinio y esperamos cumplir con los mismos altos estándares que cualquier otra CA a la que se le confíe la tarea de ayudar a proteger Internet. Esperamos que surjan otras CA para apoyar la adopción de los MTC, y estamos deseando colaborar con cualquier navegador que quiera implementar MTC.

]]>01M4CR05XDY2DRB8W02F06YMH1Cloudflare Impact alcanza los 100 millones de dólares en donacioneshttps://blog.cloudflare.com/es-es/100-million-donations/ Thu, 08 Oct 2026 02:57:53 GMTEsta semana, los programas Impact de Cloudflare alcanzarán los 100 millones de dólares en servicios donados. Este hito significa que miles de entidades, entre las que se incluyen periodistas, la sociedad civil, gobiernos estatales y locales, organismos electorales y colegios públicos, están a salvo de los ciberataques.ImpactoProyecto GalileoSemana aniversarioEsta semana, los programas Impact de Cloudflare alcanzarán los 100 millones de dólares en servicios donados. Es un hito importante, y estamos orgullosos de haberlo alcanzado porque significa que miles de organizaciones, como medios de comunicación, la sociedad civil, gobiernos estatales y locales, organismos electorales y colegios públicos, están protegidas contra los ciberataques.

Pero los programas Impact de Cloudflare nunca han tenido que ver con la filantropía. Son una parte fundamental de nuestro negocio y de nuestra misión, y siguen ayudando a guiar casi todo lo que hacemos.

Mientras celebramos este hito y nuestra semana del 16.º aniversario, queríamos repasar no solo cómo hemos llegado hasta aquí, sino también cómo nuestros programas Impact siguen creciendo y evolucionando para ayudar a quienes trabajan por el interés público.

## **Gratis** → Impact

Cloudflare empezó como un servicio gratuito. La idea original era ofrecer una versión básica de nuestros servicios a desarrolladores y pequeñas empresas de forma gratuita, y luego usar los datos sobre los ciberataques en sus sitios web para crear productos más sofisticados que pudiéramos vender.

Sin embargo, pronto descubrimos que algunos de nuestros clientes gratuitos no solo realizaban una labor esencial, como informar sobre la corrupción en África o sobre la invasión rusa de Crimea, sino que también sufrían algunos de los ataques más graves contra nuestra red. Darnos cuenta de eso cambió nuestra forma de ver nuestros servicios gratuitos. Nos comprometimos no solo a ofrecer nuestros servicios de forma gratuita para todo el mundo, sino también a hacer más por las organizaciones que son blanco de poderosos adversarios simplemente por prestar servicio al público.

Cloudflare lanzó el proyecto Galileo en 2014 para ofrecer servicios de seguridad más avanzados a personas y organizaciones importantes pero vulnerables en Internet, como periodistas, defensores de los derechos humanos y grupos de la sociedad civil. Hoy en día, el programa incluye más de 3500 dominios en más de 120 países. En 2025, Cloudflare bloqueó más de 38 500 millones de ataques DDoS, vulnerabilidades de sitios web, phishing por correo electrónico y otros ataques cibernéticos contra los participantes del proyecto Galileo, casi 105,4 millones por día.

Durante los últimos 12 años, Cloudflare ha seguido ampliando lo que ahora llamamos nuestros programas Impact. Aunque cada programa es único, nuestro objetivo es el mismo: apoyar a organizaciones e instituciones que prestan servicios públicos, particularmente a aquellas que de otro modo no tendrían acceso a los servicios de ciberseguridad necesarios. Por ejemplo:

  * El[ proyecto Athenian](https://www.cloudflare.com/athenian/) (2017): apoyo a los gobiernos estatales y locales en la organización de elecciones democráticas, lo que incluye más de 440 sitios web en 33 estados de Estados Unidos. Más tarde ampliamos ese programa fuera de Estados Unidos y ahora protegemos a organismos electorales en ocho países, entre ellos Canadá, Macedonia del Norte, Georgia y Moldavia.
  * [Cloudflare for Campaigns](https://www.cloudflare.com/campaigns/) (2020): colaboramos con[ Defending Digital Campaigns](https://defendcampaigns.org/) para ofrecer servicios gratuitos de ciberseguridad a los candidatos a cargos públicos, lo que ahora incluye más de 530 sitios web en todo Estados Unidos. 
  * Infraestructura crítica: ampliamos programas adicionales para ayudar a proteger las[ escuelas públicas](https://www.cloudflare.com/lp/cybersafe-schools/),[ la respuesta a la COVID-19](https://www.cloudflare.com/pt-br/fair-shot/),[ el Gobierno de Ucrania](https://blog.cloudflare.com/steps-taken-around-cloudflares-services-in-ukraine-belarus-and-russia/),[ las clínicas de salud pública](https://blog.cloudflare.com/heeding-the-call-to-support-australias-most-at-risk-entities/),[ las redes comunitarias](https://www.cloudflare.com/pangea/) y otros[ servicios esenciales](https://blog.cloudflare.com/project-safekeeping/).



Seguir ayudando a estas organizaciones a mantenerse en línea protegiendo sus sitios web y sus datos internos sigue siendo esencial. En 2026, Cloudflare publicó su primer[ informe anual sobre los ciberataques contra la sociedad civil](https://cf-assets.www.cloudflare.com/dzlvafdwdttg/5YmIHaAURvy8ZKjJ1CcQo6/1335a737054c44915ace715348e62697/BDES-9187_Cyberattacks_against_civil_society_Project_Galileo_Anniversary_Report.pdf), en el que se concluyó que las organizaciones de la sociedad civil son objeto de ataques con más frecuencia y mayor intensidad que otros clientes de Cloudflare. Por ejemplo, los participantes en el proyecto Galileo se enfrentaron a intentos de explotar vulnerabilidades de seguridad en sitios web a un ritmo más de siete veces superior al de un usuario medio. Cloudflare también va camino de duplicar con creces el número de solicitudes para el proyecto Galileo con respecto al año pasado.

Pero los programas Impact de Cloudflare nunca han sido estáticos. Evolucionan junto con nuestra empresa y nuestra tecnología, así como con las organizaciones a las que prestan servicio. Cada vez más, eso significa no solo defender a las organizaciones de interés público, sino también darles las herramientas para que se adapten y prosperen en la era de la IA. 

## **Perspectivas para el futuro**

A principios de septiembre de 2026, en un día lluvioso en Barcelona, Cloudflare coorganizó un hackatón. Dado que nuestra plataforma para desarrolladores es una parte muy importante de nuestro negocio, organizamos estos eventos con frecuencia. Pero este fue diferente. En lugar de una sala llena de ingenieros de software o fundadores de startups, fue la primera vez que celebramos un evento específico para periodistas.

_Hackatón de Media Party coorganizado por Cloudflare en el BIT Habitat de Barcelona (9 de septiembre de 2026)._

El evento formó parte de una conferencia de tres días organizada por[ Media Party](https://mediaparty.org/), una organización sin ánimo de lucro dedicada a la innovación de los medios a través de herramientas digitales. El[ evento](https://mediaparty.org/2026/09/09/inside-the-media-party-barcelona-hackathon-building-the-newsroom-tools-of-tomorrow/) se diseñó con el fin de reunir a periodistas, desarrolladores y expertos en estrategia para solucionar un único problema: cómo ayudar a las redacciones a adaptarse a un panorama informativo impulsado por la IA y en el que ya no se busca en los motores de búsqueda. El evento se centró en cuatro temas: la automatización de los flujos de trabajo, el periodismo agéntico, la verificación de contenidos sintéticos y la integridad de la información.

Cada equipo recibió acceso gratuito a la plataforma para desarrolladores de Cloudflare y la asistencia de ingenieros voluntarios de Cloudflare para ver qué podían desarrollar en un día. 

Cuatro equipos llegaron a la ronda final. El equipo ganador,[ AIdas](https://aidas-test.gazzetta.workers.dev/), creó una herramienta que ayuda a investigadores y periodistas a estudiar los sesgos de la IA en temas políticamente controvertidos, comparando cómo responden diferentes modelos de lenguaje de gran tamaño (LLM) a la misma pregunta y registrando sus respuestas como datos abiertos.

El hackatón fue solo una parte de una iniciativa más amplia de Cloudflare Impact para ir más allá de los servicios de ciberseguridad y ayudar a los grupos de interés público a adaptarse a un mundo en constante cambio:

  * **[Protección de las noticias locales frente a los bots de IA](https://blog.cloudflare.com/ai-crawl-control-for-project-galileo/):** el año pasado, Cloudflare ofreció acceso gratuito a nuestras herramientas de gestión de bots y control de rastreo por IA a los participantes del proyecto Galileo, entre los que se encontraban más de 750 periodistas, medios de comunicación independientes y organizaciones sin ánimo de lucro que apoyan la recopilación de noticias en todo el mundo. Estas herramientas ayudarán a estas organizaciones a entender y controlar cómo los rastreadores de IA acceden a su contenido, y a proteger sus reportajes contra el rastreo no autorizado.
  * **Startups sin ánimo de lucro:** el año pasado, durante la Semana aniversario, Cloudflare[ anunció](https://blog.cloudflare.com/expanding-startups-for-nonprofits/) que su programa de startups, que ofrece más de 250 000 dólares en créditos de Cloudflare, estaría disponible por primera vez para organizaciones sin ánimo de lucro. Esta semana anunciaremos las primeras 30 organizaciones aceptadas en el programa y cómo están ayudando a sus comunidades con herramientas creadas en nuestra plataforma para desarrolladores.
  * **Herramientas de automatización para los derechos humanos:** esta semana también anunciaremos tres nuevos proyectos que los ingenieros de Cloudflare han desarrollado utilizando nuestra plataforma para desarrolladores en colaboración con tres organizaciones líderes en derechos humanos, que abarcan temas como el seguimiento de la represión transnacional, la legislación y el desarrollo de políticas sobre derechos digitales, y la diligencia debida de las empresas en materia de derechos humanos.



En todas estas nuevas iniciativas, el objetivo sigue siendo el mismo: ayudar a las organizaciones que realizan una labor esencial a acceder a las herramientas y al apoyo que necesitan para seguir avanzando en sus misiones.

## **Únete a nosotros**

Tuve la oportunidad de reunirme con dos de los ingenieros de Cloudflare que se ofrecieron como voluntarios en el hackatón de Barcelona. Ambos me comentaron que una de las razones por las que vinieron a trabajar a Cloudflare fue el proyecto Galileo y la oportunidad de usar sus habilidades para ayudar a organizaciones que trabajan en sus comunidades. 

Fue un recordatorio importante de que los programas Impact de Cloudflare y nuestra misión no son solo cosas que hayamos hecho. Siguen dando forma a nuestra identidad, incluso a través de las personas que eligen venir a trabajar con nosotros. 

Si esto te suena como el tipo de trabajo que te gustaría hacer,[ únete a nosotros](https://www.cloudflare.com/careers/).

]]>01M4CPS4SC0JVTDZWPFG4AM9NFUna autoridad de certificación para toda la webhttps://blog.cloudflare.com/es-es/cloudflare-certificate-authority/ Thu, 08 Oct 2026 02:22:20 GMTDoce años después del lanzamiento de Universal SSL, Cloudflare ha solicitado convertirse en una autoridad de certificación. La combinación de una raíz consolidada, un enfoque que da prioridad al protocolo ACME y los certificados de árbol de Merkle (MTC) nos está permitiendo crear una autoridad de certificación poscuántica para la web abierta.CryptographyPost-QuantumSeguridadSemana aniversarioTLSHace doce años, durante la Semana aniversario 2014, [activamos Universal SSL](https://blog.cloudflare.com/introducing-universal-ssl/) y, de la noche a la mañana, casi duplicamos el número de sitios cifrados en la web, ofreciendo TLS gratis a todos los sitios que utilizaban Cloudflare, incluso a los que nunca nos habían pagado ni un céntimo. El cifrado dejó de ser una tarea cara y que requería mucho tiempo para convertirse en la opción predeterminada.

Con motivo de la Semana aniversario de este año, vamos a dar un paso más en ese camino. Llevamos más de una década siendo uno de los mayores consumidores de certificados de confianza pública en Internet, y nunca hemos emitido ni uno solo por nuestra cuenta. Eso va a cambiar. Cloudflare anuncia su intención de convertirse en una autoridad de certificación (CA) pública.

Hoy anunciamos los primeros hitos concretos de esta iniciativa. Hemos solicitado nuestra inclusión en los programas raíz de Chrome, Apple, Microsoft y Mozilla, y hemos firmado un acuerdo definitivo para adquirir una raíz consolidada y ampliamente reconocida de GlobalSign, de modo que podamos ofrecer certificados con el mayor alcance posible en dispositivos desde el mismo día en que empecemos a emitirlos. También anunciamos nuestros planes de convertirnos en una de las primeras CA en ofrecer certificados poscuánticos, con el objetivo de formar parte del [Programa de Raíz Resistente a la Computación Cuántica](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) de Chrome.

Todavía no estamos emitiendo certificados, y pasará un tiempo hasta que lo hagamos. Lo que sí estamos haciendo es comprometernos públicamente con este trabajo, compartir los hitos a medida que se vayan alcanzando y contarte exactamente en qué estamos trabajando, al tiempo que colaboramos con los programas raíz y otros miembros de la comunidad WebPKI para lograrlo.

## **Dos caminos hacia la confianza**

Una raíz nueva no resulta realmente útil hasta pasados varios años. Incluso después de que un programa raíz la acepte, esa raíz tiene que extenderse por todos los sistemas operativos, navegadores y dispositivos del mundo, y nunca llega al gran número de dispositivos que han dejado de recibir actualizaciones o que nunca las recibieron. Esa larga cola de clientes antiguos es de donde surge gran parte del tráfico de Internet a nivel mundial, y donde se concentran, en consecuencia, un montón de fallos que se podrían evitar. Creemos que todos los clientes se merecen el mayor nivel de seguridad posible, sin importar su fabricante, sistema operativo o cuánto tiempo haya pasado desde la última actualización.

Adquirir una raíz ya existente con un alto grado de cobertura en los almacenes de confianza de un conjunto diverso de clientes resuelve eso desde el primer día. La raíz actual de GlobalSign goza de confianza en navegadores, sistemas operativos y dispositivos desde 2012, y llega a clientes antiguos a los que una raíz nueva nunca llegaría. La nueva raíz que vamos a presentar para su inclusión en los programas de claves raíz está diseñada pensando en hacia dónde se dirige el ecosistema, incluyendo los programas que están empezando a limitar la antigüedad máxima de una raíz de confianza. La raíz consolidada nos permite llegar a los dispositivos del pasado. Las nuevas raíces nos dan solidez de cara a las políticas del futuro. Queremos ambas cosas para garantizar que los certificados emitidos por nuestra CA ofrezcan la mayor compatibilidad posible con los clientes.

## **Una nueva fuente de certificados gratuitos**

El modelo de certificados gratuitos y automatizados sustenta actualmente la mayor parte de la web cifrada, y gran parte de ella pasa por un operador extraordinario. Let's Encrypt emite del orden de diez millones de certificados al día, presta servicio a más de 500 millones de sitios y superó los 4000 millones de certificados activos en 2025. Es una de las mejores cosas que le han pasado a Internet en veinte años, y lo decimos como uno de sus mayores usuarios.

Ese éxito conlleva cierto riesgo sistémico: si la autoridad de certificación gratuita dominante tuviera una mala semana, gran parte de la web no tendría ninguna alternativa gratuita y automatizada comparable lista para asumir la carga. A nivel de paquete de certificados, hemos dedicado años a crear exactamente este tipo de redundancia para nuestros propios clientes. Cada certificado SSL Universal de Cloudflare ya viene con un certificado de respaldo, protegido con una clave independiente y emitido por una autoridad diferente, listo para activarse automáticamente si el principal llegara a ser revocado o se viera comprometido. Una CA pública es lo mismo, pero a la escala de todo Internet.

Para facilitar su adopción, daremos prioridad al Entorno de Gestión Automatizada de Certificados ([ACME](https://www.globalsign.com/en/acme-automated-certificate-management)), un protocolo estándar abierto ampliamente aceptado. La emisión y renovación automáticas a través de ACME serán la forma en que obtendrás un certificado de nuestra parte, lo que significa que cualquiera que ya esté apuntando a cualquier CA gratuita existente podrá pasarse a nuestro servicio simplemente cambiando la URL de un directorio, sin necesidad de herramientas nuevas ni de rediseñar nada.

## **Las previsiones de crecimiento de los certificados son enormes**

Cloudflare protege más del 20 % del tráfico global de solicitudes de Internet y gestiona el TLS para millones de dominios, para lo cual utiliza millones de certificados al año. Proporcionamos esos certificados a través de varias CA, con rutas principales y de respaldo para que los servicios de los clientes sigan funcionando incluso si las CA sufren interrupciones o se producen revocaciones.

Eso nos ha enseñado no solo cómo funciona el ecosistema WebPKI, sino también que, desde el punto de vista del usuario, a veces falla, y lo hemos aprendido por las malas. Nos hemos enfrentado a límites de tasa, casos extremos de validación, latencia en la revocación, construcción de cadenas y retrasos en la distribución de certificados raíz. Hemos vivido la rotación de las CA de los últimos años y la hemos notado a través de nuestros clientes. Sabemos cómo debe ser una emisión fiable desde fuera, porque el tiempo activo de nuestros clientes ha dependido de que seamos resilientes y reactivos cuando un emisor tiene un mal día.

Y a medida que el [periodo máximo de validez de los certificados vaya disminuyendo](https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/#ballot-contents) en los próximos años, aumente la actividad de los agentes y los certificados PQ se generalicen, esperamos que el número total de certificados de los que dependemos anualmente siga creciendo rápidamente, y no somos los únicos. No solo queremos resolver este problema por nosotros mismos, sino formar parte de la provisión de este servicio a Internet y asegurarnos de que la cadena de suministro de certificados para nuestros clientes cuente con aún más proveedores.

## **Diseño orientado a la resiliencia: transparencia y "fallos menores"**

Ahora que asumimos esta nueva responsabilidad de ser nuestra propia CA, nos comprometemos a crear la CA más fiable y resiliente posible. Queremos construir una autoridad de certificación cuya fiabilidad no dependa solo de evitar errores, sino que, al igual que con el resto de productos de Cloudflare, apueste por los “fallos menores” y limite el impacto de cualquier problema concreto.

Eso significa establecer procesos para diseñar y probar la recuperación antes de que se produzca cualquier incidente. Por ejemplo, haremos que la automatización de la renovación sea una condición para la emisión. Solo emitiremos certificados a clientes que admitan [ACME Renewal Information](https://www.rfc-editor.org/info/rfc9773/) (ARI), estandarizado en RFC 9773. Los suscriptores deben mantener una automatización que sondee nuestro punto final de renovación, actúe en las ventanas de renovación que publicamos e identifique el certificado que está reemplazando.

También estamos aprendiendo de lo que hemos observado durante los últimos 16 años. Hemos visto cómo algunas autoridades de certificación se han visto atrapadas entre revocar a tiempo y mantener en línea los sitios web de los suscriptores, porque demasiados de ellos no podían sustituir sus certificados con la suficiente rapidez. Cuando hay que retirar certificados, ya sea por un problema de cumplimiento normativo o por un incidente de seguridad, podemos adelantar los plazos de renovación de los certificados afectados, distribuir las sustituciones a lo largo del tiempo disponible y hacer un seguimiento de la emisión de los certificados de sustitución.

Esta es solo una de las muchas formas en las que pensamos mejorar. Seremos transparentes con nuestro proceso de emisión y nuestras operaciones, publicaremos compilaciones reproducibles del software que firma los certificados, certificaremos los módulos de seguridad de hardware que almacenan nuestras claves y mantendremos un panel de control público sobre el estado de la emisión y los incidentes. Las auditorías son puntuales y solo indican que una CA ha superado la prueba, no cómo funciona un martes cualquiera. Queremos que los programas raíz, los investigadores y los propietarios de sitios web normales puedan ver cómo opera realmente una CA moderna entre una auditoría y otra.

## **Una autoridad de certificación para la web poscuántica**

También queremos marcar el camino en cuanto al futuro de los certificados, no solo en su estado actual. Tenemos previsto ser una de las primeras CA en emitir certificados de árbol de Merkle (MTC) en producción, con los primeros certificados emitidos en el primer trimestre de 2027.

Los MTC son una forma nueva y mucho más compacta de ofrecer certificados de confianza pública, diseñados para un mundo poscuántico en el que las cadenas de certificados tradicionales crecen tanto que pueden saturar los protocolos de enlace TLS. Hemos defendido la [propuesta basada en estándares](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) para los MTC en el IETF, y a principios de este año, [Chrome señaló a los MTC](https://blog.google/security/cultivating-a-robust-and-efficient-quantum-safe-https/) como la vía preferida para la autenticación poscuántica. Emitirlos en entorno de producción nos permite proteger tanto a los clientes de Cloudflare como a Internet en general frente a la amenaza poscuántica, con un volumen real que respalda una transición que toda la web tiene que llevar a cabo. Hemos compartido mucha más información sobre los MTC y cómo será esta nueva Infraestructura de Clave Pública (PKI) de la web [en una entrada del blog sobre el tema](http://blog.cloudflare.com/pq-ca-with-mtcs).

No esperamos que esa transición sea repentina. Gran parte de Internet seguirá dependiendo de los certificados clásicos y de la WebPKI existente durante muchos años más. Pero a lo largo de ese periodo, esperamos que los MTC vayan ganando cada vez más cuota de emisión, y por eso estamos creando un servicio que haga ambas cosas. Al reunir los certificados clásicos y los certificados de árbol de Merkle bajo una misma CA, con un único ciclo de vida y un único conjunto de garantías, los clientes pueden adoptar la tecnología al ritmo que más les convenga y ayudar a la web a realizar la transición sin un cambio brusco. Los clientes no deberían tener que elegir un bando en una migración que durará varias décadas, gestionar dos sistemas ni reconstruir todo cuando cambie el equilibrio.

## **Como siempre, Cloudflare será el cliente cero**

Además de proporcionar paquetes de certificados a través de Universal SSL para nuestros clientes, Cloudflare consume certificados de muchas CA diferentes para gestionar nuestros sistemas y operaciones internas. Al igual que con nuestros otros productos, seremos el [cliente cero](https://www.cloudflare.com/the-net/top-of-mind-security/customer-zero/) de la nueva CA y sus certificados (tanto WebPKI como MTC), garantizando que todos los aspectos de los nuevos sistemas y procesos cumplan nuestros altos estándares internos y que la infraestructura de nuestra CA se ponga a prueba a escala Cloudflare.

## **¿Y después?**

Estamos tramitando el proceso de solicitud y aprobación con cada uno de los principales programas de claves raíz web. Estos procesos se llevan a cabo de forma abierta, y compartiremos más novedades a medida que avancen, hasta la llegada de los primeros certificados de árbol de Merkle a principios de 2027. Si quieres seguir este trabajo o ser uno de los primeros en usar un certificado de la CA de Cloudflare en el futuro, puedes [registrarte para recibir actualizaciones](http://cloudflare.com/resource/certificate-authority). Y si te apetece formar parte del desarrollo de esta nueva funcionalidad dentro de Cloudflare, [¡estamos contratando!](https://boards.greenhouse.io/cloudflare/jobs/8237801?gh_jid=8237801)

A medida que desarrollamos esta nueva funcionalidad, seguiremos colaborando estrechamente con la red de CA públicas asociadas en las que hemos confiado durante muchos años —¡16, de hecho!— mientras trabajamos juntos para garantizar una web abierta y de confianza.

Cuando lanzamos Universal SSL, el argumento era sencillo: cada byte que circula cifrado por Internet hace que sea más difícil interceptarlo, limitarlo o censurarlo, y la web abierta es algo que construimos todos juntos. Una autoridad de certificación pública, redundante y transparente es ese mismo argumento llevado un paso más allá, hasta la confianza que hace posible la web cifrada en primer lugar. Llevamos mucho tiempo trabajando en ello y nos alegra haber emprendido por fin este camino.

¡Feliz Semana anivesario!

]]>01M4CMHJ3M1P4NJKTTN73ZX5K8Forge, el proceso de código abierto para generar SDK, interfaces de línea de comandos, documentación y mucho máshttps://blog.cloudflare.com/es-es/forge-open-source-generation-pipeline/ Thu, 01 Oct 2026 10:01:21 GMTForge es un proceso de código abierto y extensible que se ejecuta en CI para generar SDK, CLI y documentación directamente a partir de las definiciones de las API. Gracias a que traslada la generación a las primeras fases del proceso, en los repositorios de cada equipo, Forge mantiene las herramientas de los desarrolladores siempre sincronizadas.AgentesAPICLIDesarrolladoresSDKSemana aniversarioHoy te presentamos [Forge](https://github.com/cloudflare/forge), una nueva forma de generar SDK, interfaces de línea de comandos (CLI), documentación y bibliotecas. Forge es un proceso de generación de código abierto y extensible que cualquiera puede implementar y ejecutar gratis.

Forge está aún en sus inicios, pero ya genera el contenido necesario para la [CLI de cf](https://blog.cloudflare.com/cloudflare-cf-cli-launch/), y en los próximos meses se encargará de la documentación de la API de Cloudflare, los SDK y mucho más.

Creamos Forge porque lo necesitábamos nosotros mismos para tratar a los agentes como si fueran nuestros clientes. Ahora lo hacemos de código abierto porque creemos que todo el mundo debería poder generar todo lo que los agentes necesitan. Antes, solo los productos para desarrolladores necesitaban CLI, SDK de API y servidores MCP, todos con una buena documentación. Ahora, eso es lo mínimo que se espera de cualquier producto.

## **Nuestra API superó a nuestros generadores**

La API de Cloudflare cuenta con más de 3500 operaciones, y los cientos de servicios que alimentan estas API están escritos en muchos lenguajes, incluidos Rust, Go, TypeScript y Python. Cuando nos pusimos a crear una CLI para toda la API de Cloudflare, incluyendo nuestros SDK y la documentación de la API, necesitábamos un proceso de generación de código capaz de gestionar esta escala. Ese proceso tiene que ser lo suficientemente flexible como para funcionar con distintos lenguajes y adaptarse a la forma de trabajar de cada uno de nuestros equipos de ingeniería.

Necesitábamos una forma de reducir la carga de coordinación entre equipos. Cuando un equipo de producto de Cloudflare realiza un cambio en la API, tiene que poder usar una versión preliminar de la CLI, el SDK y el sitio de documentación de todo Cloudflare que se va a generar, antes de fusionar ese cambio y ofrecerlo a los clientes. Necesitábamos una forma de asegurarnos de que no interrumpieran inadvertidamente el proceso de generación. Y necesitábamos un sistema que pudiéramos ampliar para generar algo más que un SDK, desde Cap‘n Web hasta MCP y más allá.

Probamos varios productos alojados que pretendían resolver esto y llegamos a usar algunos en producción. Ninguno nos solucionó el problema y algunos incluso han dejado de funcionar por completo. Un equipo fusionaba un cambio que, sin darse cuenta, rompía el proceso de generación; otro equipo se daba cuenta de ello en el momento del lanzamiento, y nos pasábamos demasiado tiempo luchando contra corriente con herramientas alojadas que no podíamos controlar, coordinando cambios entre equipos y proveedores.

Así fue como empezamos a desarrollar Forge.

Forge busca solucionar todos estos problemas: se ejecuta en CI, en los repositorios de API de cada equipo, igual que nuestro revisor de código con IA y nuestros procesos de pruebas. Analiza cada cambio y, a continuación, genera compilaciones de vista previa de la CLI, la documentación y los SDK con tus cambios resaltados, que puedes instalar para probarlos. Es la misma premisa que[ Workers Previews](https://blog.cloudflare.com/worker-previews/): una compilación de vista previa completa para cada cambio, pero aplicada a la generación de SDK a escala, incluso cuando la superficie de la API está distribuida entre cientos de servicios y repositorios. Eso es lo que Forge pretende ofrecer.

## **Los transformadores de Forge pueden generar cualquier cosa, incluido Cap'n Web**

Cloudflare tiene más razones que la mayoría para querer un generador que pueda ir mucho más allá de los objetivos de lenguaje habituales. [Cap'n Web](https://capnweb.com/) es el sistema RPC de Cloudflare que permite a TypeScript llamar a una API remota como si fuera un método local.

Forge te permite tomar una especificación OpenAPI y generar Cap’n Web directamente. Esto abre la puerta a generar [enlaces](https://developers.cloudflare.com/workers/runtime-apis/bindings/) desde Workers a otras API. Al fin y al cabo, los enlaces en el entorno de ejecución de Workers se implementan como Workers que exponen métodos RPC.

Esto no es exclusivo de Cap’n Web: otras herramientas populares en las que quizá ya confíes necesitan lo mismo. Si usas [TanStack Query](https://tanstack.com/query/), lo ideal sería que pudieras generar enlaces de TanStack Query para tu aplicación, creados directamente a partir de tu propia API. Siempre al día, siempre validados con tu API real. Lo mismo ocurre con la generación de esquemas de Zod o Valibot, servidores MCP o cualquier otra cosa que facilite el uso de tu API.

Esto es posible porque los generadores de código de Forge son flexibles. Están diseñados para que la información fluya de una salida a otra.

## **Los transformadores de Forge se pueden encadenar. Genera salidas a partir de otras salidas**

Hemos diseñado Forge para que sea extensible y admita muchos tipos de entrada y salida. Forge ofrece generadores de CLI, SDK y documentación, pero nada te impide añadir un transformador que genere un paquete específico para una biblioteca o incluso un panel de control o una aplicación completa. Forge admite actualmente OpenAPI como tipo de entrada, pero lo hemos diseñado para que admita [AsyncAPI](http://asyncapi.com), GraphQL, Cap’n Proto, Protobuf u otros formatos de entrada en el futuro.

Esto va más allá de la simple compatibilidad: te permite encadenar objetivos, utilizando la salida de un objetivo para generar otras. Esto es habitual en otros generadores, donde los objetivos de la CLI y de Terraform se generan a partir del SDK de Go. Pero lo que falta, y lo que ofrece Forge, es una forma de que el usuario controle este sistema de encadenamiento por sí mismo.

Nosotros mismos necesitábamos una solución para esto, porque nuestra CLI de cf está escrita en TypeScript, un lenguaje desde el que otros generadores de SDK no suelen encadenar para crear CLI. Pero nuestra propia situación nos hizo darnos cuenta del problema mayor: ¿por qué debería cualquier herramienta generadora de SDK tomar esta decisión por ti? Quizá trabajes con Python y quieras que la CLI esté en Python.

Si estás pensando “Bueno, pero ¿a quién le importa si está en Python o no? El código se genera automáticamente”, es porque las CLI son _diferentes._ Las CLI suelen introducir comportamientos exclusivos del entorno local que no tendrían sentido en un SDK. Comportamientos que escribes a mano, ya que, por naturaleza, no están respaldados por ninguna llamada a la API. Por ejemplo, la CLI de cf tiene comandos como cf dev y cf build que se añaden al resto del código generado. Estos comandos necesitan llamar a las API de TypeScript desde otros paquetes como Vite.

Ahora añadamos la documentación a la ecuación. Si estás generando tu CLI y tu documentación _únicamente_ a partir de tu especificación OpenAPI, ¿cómo incorporas esos comandos escritos a mano a tu documentación, para que puedan documentarse junto con el resto?

No hemos encontrado ninguna herramienta existente que haga esto hoy en día, y sin embargo es justo lo que necesitamos para cf. Así que la estamos incorporando a Forge.

## **Cambia tu API sin afectar a los usuarios**

Forge también nos está preparando para una mejor gestión de versiones de la API. La API v4 de Cloudflare ha sido la única versión significativa de nuestra API durante 10 años. Desde entonces, parece que no hayamos lanzado ninguna nueva versión importante, pero según las definiciones de SemVer hemos hecho bastantes cambios que merecerían una nueva versión principal. Al mismo tiempo, varias operaciones de nuestra API incluyen etiquetas internas v2 o identificadores beta que hace tiempo que han superado esa fase del ciclo de vida del producto.

Después de tantos años con nuestra API v4, somos muy conscientes de que una gran versión v5 dejaría atrás a muchos de nuestros clientes. Por eso, ahora que Forge va lanzando novedades, estamos trabajando en un enfoque de versionado de la API que nos permita lanzar nuevas versiones principales sin que los antiguos clientes o SDK dejen de funcionar.

Muy pronto daremos más detalles sobre nuestros SDK, incluyendo TypeScript, Rust, Python, Go, PHP y Terraform. Especialmente Terraform. Sabemos que actualizar cualquier proveedor de Terraform conlleva su propio nivel de complejidad, y vamos a prestar una atención especial a la transición de Terraform.

## **Las herramientas esenciales deben estar al alcance de todos**

Creemos que crear herramientas para API es una parte fundamental de Internet, y deberías poder hacerlo sin necesidad de un producto SaaS. Tus SDK, CLI y documentación deben ser tuyos. Y si los generas tú mismo, deberías poder hacer lo que quieras, donde quieras y de forma gratuita.

Por eso estamos haciendo que [Forge esté disponible como código abierto ](https://github.com/cloudflare/forge)bajo la permisiva licencia Apache 2.0. Queremos que la gente se una a este viaje con nosotros y aporte su granito de arena.

¿O no? Quizás prefieras quedártelo todo para ti. ¡Adelante! Puedes ejecutar Forge por tu cuenta para cualquier propósito, con modificaciones personalizadas, gratis y en privado.

_Agradecimientos: Este proyecto también ha sido posible gracias al trabajo de diseño y desarrollo de Dan Carter, Steven Chong, Krishna Paritala y Shelley Jones._

]]>01M3VDWP0MS326DFARBFBJBA6RThe Cold Start | Presenta tu startup en directo en Cloudflare Connecthttps://blog.cloudflare.com/es-es/introducing-the-cold-start/ Thu, 01 Oct 2026 09:48:58 GMTCloudflare lanza The Cold Start, un concurso para startups en el que cinco empresas en fase inicial tendrán cinco minutos para presentarse en el escenario de Cloudflare Connect. El ganador del gran premio recibirá 500 000 dólares en créditos, una valla publicitaria en San Francisco y una invitación a nuestra cena VIP para ponentes.Cloudflare para startupsDesarrolladoresSemana aniversarioHace dieciséis años, Cloudflare era una de las más de 1000 startups que aspiraban a conseguir un hueco en el escenario del TechCrunch Disrupt.

A primera vista, no éramos una elección evidente. Cloudflare era infraestructura, hacíamos que los sitios web fueran más rápidos y los protegíamos de ataques, algo que el mercado general no comprendía bien en aquel momento. La infraestructura suele ser invisible hasta el preciso instante en que se vuelve imprescindible.

Pero el 27 de septiembre de 2010, Matthew Prince y Michelle Zatlyn subieron al escenario del Startup Battlefield y presentaron Cloudflare al público. Durante la presentación, la gente empezó a suscribirse. Luego se sumaron más personas. Para cuando el jurado terminó de hacer preguntas, cientos de sitios web ya se habían unido a Cloudflare, poniendo a prueba en tiempo real nuestros cinco primeros centros de datos. En los siete días siguientes, el tráfico a través de nuestra red se multiplicó casi por 10 y Cloudflare pasó de ser el sitio número 1000 más grande de Internet a situarse entre los 50 primeros.

Cloudflare no ganó el trofeo principal ese día. En la ceremonia de entrega de premios, el fundador de TechCrunch, Mike Arrington, describió lo que hacíamos como algo parecido a “una reparación del silenciador de Internet” y, sinceramente, no le faltaba razón. Pero luego nos nombró la empresa más innovadora. Como escribió Matthew más tarde: “Puede que no ganes el premio, pero conseguirás algo diferente, mucho más importante”.

Hay momentos en la vida de una empresa en los que alguien te da una sala, un micrófono y un poco de tiempo para explicar aquello con lo que has estado obsesionado durante meses o años. La mayoría de las veces no ocurre nada mágico. Pero a veces las personas adecuadas lo escuchan en el momento justo y, de repente, una idea que hasta entonces solo existía entre un puñado de personas empieza a dar la vuelta al mundo.

Este octubre, cuando Cloudflare cumpla 16 años, queremos dar a cinco startups en fase inicial su propio escenario.

## **Presentamos The Cold Start**

[The Cold Start](https://www.cloudflare.com/connect/cold-start/) es un concurso de startups en directo que tendrá lugar el próximo mes en Cloudflare Connect, en San Francisco. Seleccionaremos cinco empresas en fase inicial y daremos a cada una de ellas cinco minutos en el escenario para explicar qué están creando, por qué es algo que tiene que existir y por qué son ellas las que deberían hacerlo.

Nos interesan menos las presentaciones perfectas que las ideas interesantes explicadas con claridad. No necesitas treinta diapositivas, un cálculo del mercado total accesible sospechosamente preciso ni una historia ensayada sobre cómo tu infancia te preparó para revolucionar la gestión de cuentas por cobrar. Lo que queremos es comprender la visión: qué ha cambiado en el mundo para que sea posible, qué ves tú que otros no han visto y por qué no puedes dejar de pensar en ello.

Los cinco finalistas presentarán su propuesta ante el público de Cloudflare Connect y ante tres personas que se han pasado buena parte de su vida pensando en empresas, infraestructura e Internet:

  * Matthew Prince, cofundador y CEO de Cloudflare
  * Michelle Zatlyn, cofundadora y Presidenta de Cloudflare
  * Dane Knecht, CTO de Cloudflare



El jurado elegirá a una startup ganadora que recibirá 500 000 dólares en créditos de Cloudflare, podrá anunciarse en una valla publicitaria de San Francisco y recibirá una invitación para nuestra cena VIP de ponentes esa misma noche.

Cinco empresas, cinco minutos cada una, y una sala llena de personas prestando atención.

### **¿Qué buscamos?**

The Cold Start está abierto a startups ambiciosas en fase inicial, con sede en EE. UU. y Canadá, que hayan recaudado menos de 10 millones de dólares. Más allá de eso, mantenemos deliberadamente una definición amplia porque las empresas más interesantes rara vez encajan en categorías bien definidas.

Queremos ver ideas que parezcan obvias una vez que alguien las haya llevado a cabo, e ideas que al principio suenen un poco descabelladas. Queremos infraestructuras que parezcan aburridas hasta que te des cuenta de que todo el mundo las va a necesitar; productos que no podrían haber existido hace unos años; interfaces nuevas y extrañas; nuevas formas de desarrollar software; soluciones destinadas a grandes mercados ya existentes y otras destinadas a mercados que nadie se ha molestado aún en nombrar.

Y, sobre todo, queremos conocer a gente que se haya dado cuenta de algo sobre el mundo y haya decidido hacer algo al respecto.

Como parte de la solicitud, te pediremos que nos cuentes quién eres, que nos des tu presentación en una sola línea, que expliques qué estás creando y por qué, que nos hables de tu situación en cuanto a financiación e ingresos, que nos muestres cómo encaja Cloudflare en tu pila tecnológica y que nos indiques cualquier otra cosa que nos ayude a entenderte a ti y a tu trabajo.

El objetivo es sencillo: haz que entendamos por qué debería existir lo que estás creando.

**[Aplicar a The Cold Start](https://www.cloudflare.com/connect/cold-start/).**

**_El plazo de inscripción ya está abierto y se cierra el viernes 2 de octubre de 2026._**

## **Cinco minutos en San Francisco**

The Cold Start tendrá lugar el lunes 19 de octubre, de 16:00 a 17:00 h PDT en el Moscone West de San Francisco, como parte de [Cloudflare Connect](https://www.cloudflare.com/connect/). Cloudflare se hará cargo de los gastos de viaje de los cinco finalistas a San Francisco para participar en la competición.

Connect reúne a personas que están creando y pensando en el futuro de Internet. El cartel de este año incluye a la pionera en IA, la Dra. Fei-Fei Li; al fundador de Idealab, Bill Gross; al psicólogo organizacional y autor Adam Grant; al director técnico de AMD, Mark Papermaster; al creador de Vue.js y Vite, Evan You; al cofundador y director técnico de Lovable, Fabian Hedin; y a Peter Steinberger, miembro del equipo técnico de OpenAI y creador de OpenClaw.

Reservamos parte de ese escenario para cinco empresas jóvenes. Cada startup tendrá 5 minutos para presentar su proyecto, seguidos de 3 a 5 minutos de preguntas por parte del jurado.

Hay algo que nos gusta de esa simetría. Hace dieciséis años, Cloudflare necesitaba que alguien apostara por una empresa de infraestructura con una historia difícil de contar y nos diera unos minutos ante el público adecuado. Hoy, tenemos la suerte de contar con un escenario propio y queremos transmitir esa misma oportunidad a las empresas que acaban de empezar.

## **Empieza poco a poco. Crea algo enorme.**

Hay una razón práctica por la que Cloudflare dedica tanto tiempo a trabajar con startups. Los grupos muy pequeños de personas tienen una capacidad asombrosa para intentar cosas muy grandes.

El problema es que el software ambicioso depende cada vez más de una infraestructura que, hasta hace poco, solo las empresas tecnológicas más grandes del mundo podían permitirse construir por sí mismas. La informática global, el almacenamiento, las redes, la seguridad, los sistemas en tiempo real, la inferencia de IA y la capacidad de sobrevivir a la posibilidad de que lo que has creado se haga popular de repente no deberían exigir que una empresa se convirtiera primero en una gigante.

Creemos que deberías poder acceder a esas capacidades desde el primer día.

Esa es parte de la idea que hay detrás de [Cloudflare for Startups](https://www.cloudflare.com/startups/), a través de la cual las empresas elegibles en fase inicial pueden recibir hasta 350 000 dólares en créditos de Cloudflare durante un año. También es parte del motivo por el que seguimos ampliando la plataforma para desarrolladores de Cloudflare. Un equipo pequeño debería poder crear algo un martes y, si a Internet le gusta el miércoles, dedicar el jueves a centrarse en el producto en lugar de tener que convertirse a toda prisa en expertos en infraestructura global.

Cloudflare empezó con una premisa un poco descabellada: que el rendimiento, la seguridad y la informática global de que disponen las empresas más grandes de Internet deberían estar al alcance de todo el mundo desde el primer día. En 2010, tuvimos la oportunidad de subir a un escenario para explicar por qué eso es importante.

Dieciséis años después, tenemos una red mucho más grande, un equipo algo más numeroso y mecanismos de protección considerablemente mejores.

Ahora queremos saber qué estás creando.

[Aplicar a The Cold Start](https://www.cloudflare.com/connect/cold-start/)

]]>01M3VD174QWDWFQ7WC5NS3M43QLlega cf, la CLI agéntica para toda la API de Cloudflarehttps://blog.cloudflare.com/es-es/cloudflare-cf-cli-launch/ Thu, 01 Oct 2026 09:32:40 GMTAnunciamos cf, nuestra nueva herramienta de línea de comandos que reproduce toda la API de Cloudflare y admite la configuración programática con TypeScript. Además, vamos a publicar como código abierto Forge, nuestro generador interno de SDK.AgentesAPIcfDesarrolladoresSemana aniversarioDurante el último año, el uso de Wrangler por parte de los agentes se ha disparado.

En marzo de 2026, los agentes fueron responsables de una cuarta parte del uso de Wrangler, frente a porcentajes de un solo dígito el año anterior. La semana pasada, el uso por parte de los agentes alcanzó el 48 %.

Los agentes son usuarios más activos: utilizan casi el doble de comandos distintos al día y son casi cuatro veces más propensos a usar seis o más comandos.

A los agentes les encantan las interfaces de líneas de comando (CLI). Pero Wrangler solo ofrece comandos para unas 280 operaciones, y Cloudflare ofrece miles.

A principios de año adelantamos [cómo pensábamos resolver esto](https://blog.cloudflare.com/cf-cli-local-explorer) y hoy, permitimos a los agentes usar todos los productos de Cloudflare con la llegada de una nueva CLI: cf.

cf es una CLI diseñada para la próxima generación de desarrollo de software:

  * Los agentes pueden encontrar el comando que necesitan para hacer cualquier cosa que quieran con una búsqueda y orientación personalizadas.
  * JSON es la interfaz predeterminada, con formato legible para los humanos y condensado para los agentes, con el fin de ahorrar el máximo contexto.
  * cloudflare.config.ts es el nuevo formato de configuración para todo Cloudflare, empezando por Workers, y te aporta la seguridad y precisión de TypeScript a ti y al protocolo de servidor de lenguaje (LSP) de tu agente.
  * Vite se convierte en la opción por defecto, trayendo consigo el mejor servidor de desarrollo local y un conjunto de plugins para desarrolladores y autores de marcos de trabajo.



Instala hoy mismo la versión beta abierta a nivel global y ejecútala desde cualquier lugar:

**Copy prompt**
    
    
    Please update your global agent instructions, so you use Cloudflare's new `cf` CLI.
    
    Add the Markdown below to the user-level instructions file that you load in every project – not this repository's AGENTS.md or CLAUDE.md. Use the file for the agent you are: Claude Code `~/.claude/CLAUDE.md`, Codex `~/.codex/AGENTS.md`, OpenCode `~/.config/opencode/AGENTS.md`, Pi `~/.pi/agent/AGENTS.md`. For any other agent, use its equivalent global rules file; if your global rules can only be set in a settings screen, tell me what to paste there instead. Create the file if it doesn't exist. Keep everything already in it, but replace any existing instruction about Wrangler or the Cloudflare CLI instead of adding a conflicting one. If the same guidance is already there, leave the file as it is. When you're done, tell me the path of the file you changed.
    
    ```markdown
    ## Cloudflare CLI - cf - v20260928
    
    `cf` is Cloudflare's current CLI and covers the whole Cloudflare platform. Prefer it over Wrangler: create projects with `cf init`, develop with `cf dev`, deploy with `cf deploy`, and manage account resources with `cf <product> …` (for example `cf d1 list`).
    
    Wrangler is only for projects that already use it – a `wrangler.jsonc`, `wrangler.json` or `wrangler.toml` file – or when the user asks for it. Keep using Wrangler in those projects unless asked to migrate, and use `cf migrate` in this case.
    
    `cf` commands differ from Wrangler's; check `cf --help` or `cf cli search <what you want to do>` instead of guessing. If a `cf` command fails in a project that doesn't use Wrangler, don't fall back to Wrangler (including `npx wrangler`) without offering to report it.

## **cf le da a tu agente acceso a toda la API de Cloudflare**

¿Y si tu agente pudiera hacer todo lo que Cloudflare puede hacer? Esa fue la pregunta que despertó nuestro interés a principios de este año: los agentes eran cada vez más potentes, pero lo que podían hacer con la CLI de Cloudflare seguía siendo limitado.

Wrangler se creó a mano con la colaboración de cada equipo de producto, y cada uno aplicaba su propio enfoque a la experiencia de desarrollo de comandos. Imponer patrones comunes entre los equipos era prácticamente imposible, incluso entre nuestras aproximadamente 280 rutas de comandos. Teníamos una terminología inconsistente en `d1 info`,` hyperdrive get` o `workflows describe`, ya que cada equipo había desarrollado sus propias prácticas en momentos diferentes. Algunos equipos crearon experiencias totalmente personalizadas con miles de líneas de código que al final se usaban muy de vez en cuando, y los equipos ideaban enfoques diferentes para resolver los mismos problemas.

Queríamos tanto estandarizar lo que teníamos como hacer una expansión a lo grande, todo a la vez. [Forge ](https://blog.cloudflare.com/forge-open-source-generation-pipeline)— el nuevo proceso unificado de generación de API de Cloudflare — nos permitió hacerlo, basándonos en la idea de generar nuestros comandos de la CLI directamente a partir del esquema de la API que alimenta nuestra documentación de la API y la generación del SDK. Todo lo que ofrecemos tiene un esquema OpenAPI, y si lo anotamos con solo un poco más de información, podemos usarlo como fuente para que Forge cree una CLI.

Esto nos permite ampliar `cf` desde las 280 funciones que Wrangler había ido creando con el tiempo, hasta cubrir la totalidad de la superficie de la API de Cloudflare, con más de 3000 operaciones.

Ahora es muy sencillo darle a tu agente `cf` y pedirle que configure un worker, lo implemente, lo supervise y observe, lo proteja con Cloudflare Access, compre un dominio y lo proteja con Cloudflare WAF, todo desde una sola herramienta.

## **Desarrollado para un agente que nunca ha usado cf**

cf está diseñado para la evolución de la ingeniería de software, donde el desarrollo agéntico está cambiando drásticamente la forma en que se crea y se implementa el software. Este año nos hemos centrado en ofrecer herramientas que apoyen este cambio, lo que ha culminado en cf. cf se ha creado desde cero pensando en los agentes e incluye herramientas novedosas para el descubrimiento de comandos agénticos que creemos que se convertirán en estándar en más CLI en un futuro próximo.

Wrangler traía la ventaja de que años de documentación, blogs y guías de terceros se han incorporado al proceso de entrenamiento de los modelos de lenguaje de gran tamaño (LLM). Pero también traía la misma desventaja: cambiar cómo funciona Wrangler ahora va en contra del comportamiento aprendido, y un cambio significativo sería inevitable dada la magnitud de las mejoras que queremos implementar.

Presentar una nueva CLI que los agentes nunca han visto suena como un gran cambio disruptivo, pero en realidad es lo más sencillo que podemos hacer. Gracias a las decisiones de diseño que hemos tomado, a las inyecciones de contexto que podemos realizar y a los archivos AGENTS.md que podemos añadir, hacer el cambio de esta forma resulta, en realidad, menos confuso que hacer que un agente contextualice las principales diferencias entre dos versiones de una herramienta con la que está familiarizado. Lanzamos la herramienta con un par de estas funciones centradas en los agentes ya integradas, y pronto habrá más.

## **Los agentes necesitan filtrar JSON, no mirar tablas**

Cuando los agentes usan Wrangler, añaden `--json` a cada comando que ejecutan y luego a menudo filtran la salida con `jq` para extraer un subconjunto de campos. Pero solo algunos comandos de Wrangler admitían `--json`; muchos devolvían tablas unicode diseñadas para que los humanos vieran la salida en su terminal. Los agentes pueden descifrarlas, pero les cuesta más tiempo y tokens que un filtro `jq`.

En cf adoptamos la postura contraria. Los agentes simplemente necesitan JSON, y si los agentes son el futuro usuario principal de esta herramienta, debería ser el valor por defecto. Para la gran mayoría de los comandos a los que los humanos rara vez accederán, esta es, obviamente, la decisión correcta.

Tú, como usuario humano de esta CLI, estás, en realidad, un paso alejado de usarla. Es preferible que los agentes puedan filtrar fácilmente sus resultados y luego devolverte esa lista filtrada en el formato que pidas, en lugar de proporcionarte tablas que probablemente nunca leerás directamente.

Pero, ¿y si quieres hacer algo que pueda requerir una intervención personal real, como buscar un dominio para comprar?

Para los comandos a los que tu agente puede acceder encadenando parámetros con nombre en una secuencia larga y complicada, solo tienes que rellenar un formulario. Cf descompone los requisitos de la API en una serie de entradas validadas, por lo que comprar un dominio, incluso uno con requisitos complejos, es muy sencillo de seguir.

O, si lo prefieres, simplemente pídele a tu agente que lo haga.

## **Tu agente puede encontrar el comando correcto por sí mismo**

Con 3000 rutas posibles a través de una CLI, ¿cómo puede tu agente encontrar rápidamente la operación que necesita sin saturar tu contexto? Por eso también hemos añadido `cf cli search`.

Este comando permite a tu agente preguntar en lenguaje natural qué necesita hacer, y un pequeño índice de búsqueda proporcionará una lista de comandos apropiados, basados en su descripción de API y sus parámetros. Informamos automáticamente a tu agente sobre este comando cuando ejecuta `--help` por primera vez.

## **Configuración que comprueba los tipos de tu agente**

Nuestro nuevo formato de configuración se basa en TypeScript, que es fácil de analizar tanto para las personas como para los agentes, y te permite escribir tu configuración mediante programación.

La configuración tipada es de gran ayuda para los agentes. Hemos comprobado que incluso sin contexto previo del formato de configuración programática, los agentes son capaces de identificar y editar fácilmente la configuración bajo demanda, incluso en elementos como `env` que han cambiado drásticamente respecto a la misma función en Wrangler. Todos los agentes que usan plugins LSP, como Claude Code y Codex, se benefician de poder interpretar más sobre el formato del archivo de configuración en contexto y hacen sugerencias mucho más precisas como resultado.

Compáralo con TOML, que no tenía un esquema accesible, o con JSONC, cuyo esquema vinculado los agentes apenas utilizaban.

Algunos archivos de configuración de Wrangler dentro de Cloudflare se han reducido en un 40 %, pasando de más de 5000 líneas — con muchos entornos personalizados por desarrollador — a archivos predeterminados que generan la configuración de cada desarrollador de forma más eficiente.

Esto se consigue definiendo programáticamente cada entorno a partir de la misma base universal, en lugar de copiar bloques `env` como solía hacerse en Wrangler. Un Worker sencillo con varios entornos solo tiene que activar el argumento `mode` nativo de Vite para cambiar de un conjunto de configuración a otro.

Una configuración sencilla que hace esto tiene ahora este aspecto:

Puedes migrar tu Cloudflare Worker a este nuevo formato mediante `cf migrate`.

También te ofrecemos algunas funciones de ayuda para que crear tu Worker sea muy fácil.

`bindings` te ofrece un lugar sencillo para que tu agente descubra todo lo que la plataforma para desarrolladores tiene que ofrecer. Todo, desde las variables de entorno hasta el almacenamiento, la base de datos y las colas, puede autocompletarse y explicarse desde tu editor.

Del mismo modo, hemos incluido una función de ayuda para los `triggers`, que es la nueva forma de definir rutas, colas, programaciones y triggers de correo electrónico para tu Worker. En lugar de tenerlos dispersos por tu archivo de configuración, ahora es muy fácil encontrar, en un único bloque, las acciones que podrían activar la ejecución de tu Worker.

`defineConfig.worker` es solo el principio. Nuestra intención con cloudflare.config.ts es que así sea como gestiones Cloudflare en su conjunto. Todos los productos que necesites, junto con su API, disponible para tu agente a través de cf, podrán expresarse mediante una configuración segura en cuanto a tipos. Pronto podrás configurar políticas completas, configurar zonas, configurar el DNS y mucho más, todo a través de este archivo de configuración.

## **La mejor experiencia de desarrollo de su clase**

Cuando Wrangler empezó a crear JavaScript Workers,[ Vite](https://vite.dev/) aún no existía. En su lugar, usábamos esbuild en Wrangler para empaquetar tus Workers. El servidor de desarrollo que Wrangler ponía a tu disposición en el puerto :8787 era algo que había creado el equipo de Wrangler, y modificar cualquier parte de esto significaba meterte en el funcionamiento interno de herramientas locales específicas de Cloudflare, como Miniflare.

Vite supone una mejora enorme en este sentido y cuenta con un amplio ecosistema de plugins que puedes utilizar, además de ofrecer un servidor de desarrollo de primera clase con HMR (sustitución de módulos en caliente) y compilaciones que usan la biblioteca Rolldown, basada en Rust, para el “tree-shaking”. Todo lo que puedas hacer con Vite, lo puedes hacer con el plugin de Cloudflare para Vite.

El plugin de Cloudflare para Vite es la forma recomendada que te sugerimos para crear Workers, sea lo que sea lo que estés desarrollando: ya sea un proyecto centrado en el frontend o una API de backend. Junto con nuestro plugin Vitest, ofrece un entorno de desarrollo y pruebas cohesionado que se adapta al tiempo de ejecución de Workers y te da acceso directo a los bindings y a las API de la plataforma.

cf se basa en Vite de forma predeterminada. La mayoría de tus Workers migrarán fácilmente con los agentes. Otros pueden tardar más tiempo, por lo que cf seguirá recurriendo a Wrangler para el desarrollo y la implementación de los Workers de JavaScript que necesiten seguir utilizando esbuild, así como de los Workers de Rust y Python.

## **Migración desde Wrangler**

Migrar un Worker desde Wrangler es tan sencillo como ejecutar cf migrate.

Los Workers que ya se compilan con Vite se convertirán automáticamente a cloudflare.config.ts. Si tu Worker depende de Wrangler para esbuild, cf seguirá delegando las compilaciones a Wrangler.

Cuando termine la versión beta abierta, lanzaremos una versión final importante de Wrangler que os indicará a ti y a tu agente que utilicéis cf. Seguiremos ofreciendo soporte de mantenimiento para Wrangler durante 18 meses tras el fin de la versión beta, para que tengáis tiempo de migrar.

También puedes crear proyectos nuevos y configurarlos automáticamente para Cloudflare ejecutando `cf init/deploy`, lo que instalará el plugin de Cloudflare para Vite por ti y creará un archivo de configuración.

Los sitios estáticos siguen sin necesitar un archivo de configuración para ponerse en marcha, y desplegarlos es tan sencillo como ejecutar `cf deploy` en tu proyecto.

Para iniciar un nuevo proyecto Hello World con cf, usa `cf init`.

_cf es de código abierto y los problemas se pueden[ notificar en nuestro repositorio de GitHub](https://github.com/cloudflare/cf)_.

]]>01M3VBZNECS7Y1R3JMY8QFRMQ5Carta anual de los fundadores de Cloudflare — 2026https://blog.cloudflare.com/es-es/cloudflares-2026-annual-founders-letter/ Tue, 29 Sep 2026 09:31:10 GMTInternet está cambiando más hoy que en cualquier otro momento desde que Cloudflare inició su andadura el 27 de septiembre de 2010. A medida que el tráfico automatizado supera a la actividad humana, nos preguntamos sobre el auge de los agentes de IA, los nuevos creadores y cómo podemos ayudar a crear un futuro justo y sostenible para la web.AICarta de los fundadoresPlataforma para desarrolladoresSemana aniversarioTendencias de InternetEsta semana, Cloudflare celebra su 16.º aniversario. Como muchos jóvenes de 16 años, nos encontramos mirando el mundo en el que crecimos con una sensación de estar atrapados entre el pasado y el futuro. Y como ellos, a veces vemos riesgos en todos los cambios que nos rodean. Pero, en general, salimos tremendamente optimistas ante lo que nos aguarda. Lo que impulsa nuestro optimismo —y también nuestros temores— es la conciencia de que el cambio siempre conlleva disrupción.

Internet está cambiando hoy más que en ningún otro momento desde que Cloudflare comenzó su andadura el 27 de septiembre de 2010. Parte de ese cambio parece indudablemente bueno. Parte de él está poniendo patas arriba la forma en que entendemos el funcionamiento de Internet.

Un cambio significativo es el ritmo de crecimiento de la propia web. De 2012 a 2025, la web se estancó e incluso, según algunas métricas, se contrajo. Eso cambió a mediados de 2025 con una explosión de nuevos sitios web. La narrativa popular es que ese crecimiento fue impulsado por el «contenido basura» generado por la IA. Y aunque hay algo de eso, no es lo que predomina en lo que observamos.

En cambio, la IA ha dado rienda suelta a una nueva generación de creadores. Personas con ideas pero sin conocimientos de programación que, con la ayuda de las herramientas de «vibe coding», son capaces de dar vida a nuevas creaciones. Nos enorgullece que la mayoría de estas herramientas tengan la plataforma para desarrolladores de Cloudflare como destino de implementación preferido. La tecnología en su mejor expresión permite que más personas den rienda suelta a su creatividad. Desde nuestra posición privilegiada, podemos ver cómo estudiantes de todo el mundo crean aplicaciones para resolver problemas reales. Startups con nuevas ideas de negocio que se ponen en marcha en un tiempo récord. Hoy, más de 7 millones de desarrolladores están creando el futuro sobre la plataforma para desarrolladores de Cloudflare.

El último año también ha cambiado en cuanto a quién —y cada vez más, qué— utiliza Internet. En un principio, preveíamos que el tráfico automatizado superaría al humano en la segunda mitad de 2027. El auge de los agentes y los rastreadores de IA adelantó esa fecha a mayo de 2026. Y si las tendencias actuales continúan —lo cual, en todo caso, parece una estimación conservadora—, el tráfico automatizado será 1000 veces mayor que el humano en solo cinco años. No porque creamos que el tráfico humano vaya a disminuir, sino porque el tráfico procedente de los agentes se está disparando.

Para quienes los utilizan, estos agentes de IA ya son asombrosos. Pide a uno que te encuentre un vuelo, un contratista o un plan de teléfono más barato, y leerá en un minuto más páginas de las que tú podrías en una tarde, para después volver con una respuesta. Se encarga de todo el trabajo pesado para que tú no tengas que hacerlo.

Pero ese trabajo previo no es gratuito. Si le pides a tu agente de IA que te sugiera dónde almorzar, puede que analice los menús de 1000 restaurantes de la zona solo para sugerirte uno. Ese único restaurante puede que consiga tu reserva, pero los otros 999 tuvieron que asumir la carga de atender al agente sin obtener nada a cambio. El riesgo aquí es el problema de la «tragedia de los comunes» en el que los usuarios que se benefician de los agentes de IA y de su tráfico no asumen los costes de la carga que imponen al sistema y, por tanto, no actúan con la moderación adecuada.

La IA ha hecho que a esos estudiantes y startups les resulte más fácil que nunca crear algo. Los agentes podrían hacer que a cualquiera le resultara mucho más difícil encontrarlo. Hoy, las pequeñas empresas ganan clientes mediante la emoción o la comodidad. Frecuentas una determinada charcutería porque la persona que atiende el mostrador recuerda tu nombre o porque forma parte de cómo te defines a ti mismo. O compras en una tienda local aunque sabes que no tiene la mejor selección ni los mejores precios, pero está de camino a casa.

A tu agente de IA le da igual quién recuerda tu nombre, y no pasa por delante de la tienda local. Se decanta por aquello sobre lo que tiene más información, que suele ser quien lleva más tiempo. El riesgo, entonces, es que, a medida que los agentes gestionen cada vez más transacciones comerciales, dificulten la entrada de nuevos competidores. Eso, a su vez, probablemente conducirá a una consolidación y a un entorno empresarial menos sólido.

Nosotros también fuimos nuevos en el mercado una vez. Hace dieciséis años esta misma semana, lanzamos Cloudflare en el escenario de TechCrunch Disrupt mientras nuestros ingenieros estaban sentados entre el público arreglando errores. Quedaban ocho cuando subimos al escenario. Cuando bajamos, estaban resueltos y estábamos en línea en cinco centros de datos en tres continentes. Ningún agente de IA nos habría recomendado. La gente apostó por nosotros de todas formas. Queremos que los próximos recién llegados tengan la misma oportunidad.

Eso es lo que perseguimos. No un futuro con cinco empresas de IA, sino uno con 500 000, repartidas por todo el mundo. No uno en el que los creadores de contenido desaparezcan y mueran porque no pueden ser remunerados, sino uno en el que cualquiera pueda crear, llegar a una audiencia global y cobrar por su trabajo. Y no uno en el que unas pocas megacorporaciones ganen por defecto, sino uno en el que los nuevos participantes con mejores productos puedan atender bien a sus clientes y triunfar.

El año pasado escribimos sobre lo que la IA le estaba haciendo a los editores. Este año, el mismo cambio llega al restaurante y a la charcutería. Lo que reemplaza al viejo modelo de negocio de Internet es la pregunta más interesante de los próximos cinco años. Esta semana, intentamos responderla una vez más.

Como en cada aniversario, celebramos dando regalos en lugar de recibirlos, y algunos de esos regalos son para los 999 restaurantes. Los agentes rastrean la web como siempre lo han hecho los motores de búsqueda: todo, una y otra vez, haya cambiado o no. Nuestros datos sugieren que más de la mitad de lo que los bots legítimos obtienen no ha cambiado desde su última visita. Hemos estado trabajando para que los rastreadores vean más contenido de la web y, al mismo tiempo, solo busquen lo nuevo, lo que reduce la carga en las páginas que rastrean. Y estamos ofreciendo a cualquiera que publique contenido o aplicaciones en línea una forma de ganar dinero cuando los agentes usen lo que han creado.

La misión de Cloudflare no es mejorar Internet, sino ayudar a mejorar Internet. Eso significa que no podemos hacerlo solos. Por eso, esta semana también anunciaremos alianzas con empresas y organizaciones que quieren el mismo futuro que nosotros.

Al igual que otros chicos de 16 años en esta nueva era de la IA, podemos expresar nuestras opiniones. Las compartimos porque queremos una red de Internet en la que siga habiendo sitio para un adolescente que lance su primera aplicación, para la charcutería donde se acuerdan de tu nombre y para quienquiera que esté creando el próximo Cloudflare.

Y nunca habíamos estado tan ilusionados.

]]>01M3P7X06A2WZ52QSR84HDSEQ6Visibilidad sin entrenamiento de la IA, las dos cosas son posibleshttps://blog.cloudflare.com/es-es/accountable-mixed-use-ai-crawlers/ Mon, 21 Sep 2026 02:26:11 GMTCloudflare ofrece a los propietarios de sitios web una forma de mantener su visibilidad sin permitir el entrenamiento de la IA. Los nuevos controles y la designación Responsable establecen un modelo compartido con Apple, Google y Microsoft.AIAI Bots (ES)Gestión de botsNoticias de productosSeguridadServicios de redSin los controles adecuados, los propietarios de sitios web se han enfrentado durante mucho tiempo a una difícil disyuntiva: permitir que su contenido se utilice para el entrenamiento de la IA o arriesgarse a perder visibilidad en los motores de búsqueda. Esa disyuntiva existe porque algunas de las organizaciones más grandes de Internet utilizan rastreadores de uso múltiple: un único rastreador que sirve tanto para la búsqueda como para el entrenamiento de la IA. Si rechazas uno, rechazas el otro.

Hoy, Cloudflare anuncia una nueva configuración, ["No permitir el entrenamiento de IA" (Disallow AI Training)](https://blog.cloudflare.com/bot-preference-sync/), para que puedas seguir apareciendo en los resultados de búsqueda sin que ese mismo rastreador pueda entrenar con tu contenido. Apple, Google y Microsoft respetan o se han comprometido (en un plazo de tiempo especificado) a respetar esta configuración.

Los rastreadores de uso múltiple eran la parte más complicada de la cuestión del entrenamiento. Lo siguiente son los resúmenes de IA. Una opción de "sí" o "no" para todo el sitio web es demasiado tajante. La cantidad de contenido que aparece en un resumen importa tanto como el hecho de que aparezca o no. La opción de exclusión voluntaria para los resúmenes generados por IA ya es uno de los requisitos que hemos establecido para los operadores de rastreadores de uso múltiple. Para principios del año que viene, nuestro objetivo es permitirte controlar qué parte de tu contenido se incluye. Lo configurarás una sola vez en Cloudflare, en lugar de tener que hacerlo por separado con cada operador.

## Por qué no basta con preguntar

La mayoría de los propietarios de sitios web quieren aparecer en los resultados de búsqueda de personas, agentes y bots (buenos). Pero una parte significativa de la red de Internet abierta se financia mediante publicidad, suscripciones o relaciones directas con los usuarios, y esos modelos solo generan ingresos cuando alguien llega realmente al sitio.

Casi todos los propietarios de sitios consideran beneficioso el uso de buscadores. Menos del 1 % de los sitios de Cloudflare optan por bloquear los bots de búsqueda. El entrenamiento, sin embargo, es otra historia. El 17 % de los sitios optan por habilitar algún mecanismo para bloquear el entrenamiento. Precisamente por eso decidimos que los propietarios de sitios web necesitaban controles más detallados, en lugar de una opción "Bloquear la IA" genérica para todos.

Una directiva robots.txt por sí sola no puede resolver este problema. Cualquiera puede publicar una, pero no puede identificar quién está rastreando, determinar por qué lo hace ni detener a un rastreador que la ignore.

Sin embargo, una red sí puede resolverlo. Publicamos la preferencia, identificamos quién está rastreando, clasificamos por qué lo hacen y bloqueamos a quienes la ignoran; a continuación, informamos en [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) de lo que cada operador hace realmente.

Pero el bloqueo solo elimina un rastreador. No cambia el comportamiento de los rastreadores. El mejor resultado es que los operadores no te obliguen a elegir en absoluto. Por eso, desde julio, hemos estado hablando directamente con ellos. La respuesta ha sido alentadora. Casi todos coinciden en que los propietarios de sitios web deben tener control y transparencia sobre cómo se utiliza su contenido, así como la garantía de que se respetarán sus decisiones. Para ayudar a los propietarios de sitios web a comprenderlo, hemos creado una designación: "Responsable".

La designación "Responsable" reconoce tanto las capacidades disponibles en la actualidad como los compromisos concretos para hacerlas realidad. Para obtenerla, un operador de bots debe cumplir o comprometerse a cumplir los siguientes requisitos:

  1. Un mecanismo para que los propietarios de sitios web puedan excluirse del entrenamiento de la IA, a través de robots.txt o un estándar similar.
  2. Un mecanismo para que los propietarios de sitios web puedan excluirse de los resúmenes generados por IA, acordado directamente con el operador y, a partir del año que viene, a través de Cloudflare (véase la sección siguiente para más detalles).
  3. Visibilidad a nivel de URL sobre qué páginas se han puesto a disposición para el entrenamiento, junto con métricas que muestren cómo aparecía el contenido en las búsquedas.
  4. Garantía de que excluirse del entrenamiento de la IA no afectará a los resultados de búsqueda tradicionales.



Apple, Google y Microsoft demuestran que cumplen los requisitos para ser Responsables. Cada una de ellas combina las capacidades disponibles en la actualidad con compromisos con plazos concretos para aquellas que aún se encuentran en fase de desarrollo. A continuación se detallan los rastreadores de cada una de estas empresas.

## Nuevas opciones de configuración de seguridad

Cloudflare clasifica los bots según su comportamiento, y un mismo bot puede mostrar más de un comportamiento. Hay tres comportamientos disponibles como controles:

  * **Búsqueda** : rastreo para crear un índice de búsqueda.
  * **Entrenamiento** : rastreo para entrenar o ajustar un modelo.
  * **Agente** : agentes dirigidos por el usuario que visitan una página en nombre de una persona, como los bots de chat y los agentes de uso del navegador.



Un rastreador de uso múltiple es un único rastreador que realiza tanto la búsqueda como el entrenamiento. Sin controles, esa combinación genera la disyuntiva descrita anteriormente: los propietarios de sitios web no pueden rechazar un uso sin rechazar el otro.

Para evitar bloquear los rastreadores de uso múltiple con la designación "Responsable", aquellos que no imponen esa disyuntiva a los propietarios de sitios web, presentamos una nueva configuración: "No permitir el entrenamiento de IA", que recibe su nombre de la directiva "Disallow:" que publica en tu archivo robots.txt.

### La configuración "Bloquear" ahora tiene un significado diferente

Anteriormente, las opciones "Bloquear" y "Bloquear en páginas con anuncios" no se aplicaban a los rastreadores de uso múltiple, ya que bloquearlos también podía afectar a la visibilidad en la búsqueda. Ahora que contamos con la nueva configuración "No permitir el entrenamiento de IA", las opciones "Bloquear" y "Bloquear en páginas con anuncios" se aplican a _todos_ los rastreadores de entrenamiento, incluidos los de uso múltiple.

Los controles de entrenamiento, búsqueda y agente se aplican a nivel de dominio. Con la incorporación de la opción "No permitir el entrenamiento de IA", las opciones disponibles son:

  1. **Permitir** : se permiten todos los rastreadores, a menos que estén bloqueados por otra configuración o una regla de WAF.
  2. **No permitir el entrenamiento de IA** : "Bot Preference Sync" publica la preferencia de no entrenamiento correspondiente en el archivo robots.txt. Se siguen permitiendo los rastreadores de uso múltiple con la designación "Responsable" para la búsqueda. Se bloquean todos los demás rastreadores de entrenamiento, incluidos los rastreadores destinados exclusivamente al entrenamiento que gestionan Amazon, Anthropic, Meta y OpenAI. El bloqueo de estos no afecta a la búsqueda. La opción "No permitir el entrenamiento de IA" solo está disponible como configuración para entrenamiento, no para búsqueda ni agente.
  3. **Bloquear en páginas con anuncios** : los rastreadores, incluidos los de uso múltiple, solo se bloquean en las páginas en las que se detecta que se muestra un anuncio.
  4. **Bloquear** : se bloquean todos los rastreadores, incluidos los de uso múltiple.



La opción "No permitir el entrenamiento de IA" funciona publicando una preferencia en robots.txt. No es posible expresar de esa forma una preferencia específica para páginas con anuncios. Cloudflare puede detectar qué páginas muestran anuncios, pero esa lista es demasiado extensa y cambia con demasiada frecuencia como para enumerarla en el archivo robots.txt. Por eso no existe la opción "No permitir el entrenamiento de IA" en páginas con anuncios.

Los agentes no plantean el mismo dilema entre búsqueda y visibilidad que los rastreadores de uso múltiple, y en Internet aún no existe una directiva bien establecida para expresar preferencias de "No permitir" a los agentes. Por ahora, no incluimos una configuración de "No permitir" para agentes. A medida que maduren estándares como [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/), revisaremos este enfoque.

## ¿Qué cambia el 15 de septiembre?

Estamos realizando los siguientes cambios en Bot Management y AI Crawl Control:

  1. Las opciones "Bloquear" y "Bloquear en páginas con anuncios" ahora se aplican a rastreadores de uso múltiple, incluidos Applebot, Bingbot y Googlebot, por lo que cualquiera de los ajustes impacta tanto en la búsqueda como en el entrenamiento. Para detener el entrenamiento y _mantener_ la búsqueda, utiliza "No permitir el entrenamiento de IA".
  2. La opción "Bloquear bots de IA" quedará obsoleta en favor de los controles más detallados de búsqueda, entrenamiento y agente.
  3. La función "Managed robots.txt" será reemplazado por "Bot Preference Sync". Los clientes que habilitaron "Managed Robots.txt" migrarán al nuevo sistema.
  4. La opción "No permitir el entrenamiento de IA" pasará a formar parte de la configuración recomendada para determinados dominios nuevos.
  5. Las preferencias de los clientes actuales se migrarán a los nuevos controles tal y como se describe a continuación.



### Qué debes hacer

Nada, en casi todos los casos. Tu configuración actual se mantendrá tal cual.

Si quieres que los rastreadores de uso múltiple desaparezcan por completo, ahora tienes que indicarlo. Selecciona "Bloquear". Esto impedirá que Applebot, Bingbot y Googlebot accedan a tu sitio web, búsqueda incluida.

#### Dominios existentes que nunca han utilizado los controles de búsqueda/entrenamiento/agente

A los propietarios de sitios que nunca hayan configurado los controles más detallados se les migrará a la nueva configuración basándose en su configuración anterior de "Bloquear bots de IA":

#### Dominios existentes que ya habían configurado los controles de búsqueda/entrenamiento/agente

Para los dominios que anteriormente configuraron los controles granulares, preservaremos el efecto práctico de sus selecciones bajo las nuevas definiciones. Las selecciones anteriores de entrenamiento, como "Bloquear" o "Bloquear en páginas con anuncios", se migrarán a "No permitir el entrenamiento de IA".

All

### Recomendaciones para nuevos dominios

A partir del 15 de septiembre, a los clientes que den de alta un nuevo dominio se les ofrecerá una de dos configuraciones preestablecidas, dependiendo de si el sitio obtiene ingresos por publicidad. Los ingresos por publicidad dependen de que una persona vea realmente la página. El entrenamiento sustituye esa visita por una respuesta; los agentes obtienen la página sin que haya nadie allí para ver los anuncios. Por lo tanto, los ajustes preestablecidos para sitios con anuncios son más restrictivos. Puedes cambiar cualquiera de estas configuraciones durante la incorporación o en cualquier momento después.

_Configuraciones recomendadas para nuevos dominios._

## ¿Qué significa esto para los rastreadores de uso múltiple específicos?

Applebot, Bingbot y Googlebot tienen la designación "Responsable". Apple, Google y Microsoft están comprometidos con los mismos principios de elección del creador de contenido y transparencia. Con la opción "No permitir el entrenamiento de IA" activada, pueden seguir rastreando tu sitio para la búsqueda. Si seleccionas "Bloquear", los detienes por completo.

También clasificamos con la designación "Responsable" a los rastreadores relevantes de Amazon, Anthropic, Meta y OpenAI. Estas organizaciones separan sus rastreadores de búsqueda y de entrenamiento, por lo que Cloudflare puede bloquear el rastreador de entrenamiento sin afectar a la búsqueda.

### Applebot

Applebot permite a los propietarios de sitios web excluirse del entrenamiento añadiendo una regla "No permitir" en el archivo robots.txt para "Applebot-Extended". Los propietarios de sitios web también pueden, actualmente, expresar sus preferencias respecto a los resúmenes de IA a través de la directiva [nosnippet](https://support.apple.com/en-us/119829#:~:text=nosnippet%3A%20Applebot,products%20and%20services.) en el código HTML de la página. El contenido también se puede etiquetar como [contenido de pago](https://support.apple.com/en-us/119829#:~:text=Marking%20paywalled%20content,the%20next%20section.) para excluirlo de los resultados generativos. Applebot aún no ofrece una herramienta para la inspección a nivel de URL. Sin embargo, nos hemos reunido con su equipo y nos han contado detalles de la solución en la que están trabajando para el año que viene. Apple también ha afirmado que impedir el entrenamiento [no afecta al posicionamiento en los resultados de búsqueda](https://support.apple.com/en-us/119829#:~:text=Applebot%2DExtended%20and%20controlling%20data%20usage).

### Googlebot

Googlebot permite a los propietarios de sitios web excluirse del entrenamiento añadiendo una regla "No permitir" en el archivo robots.txt para Google-Extended, y ofrecen una opción en su portal para webmasters que permite excluir el contenido de un sitio de los resultados de búsqueda generativa. Googlebot también proporciona a los propietarios de sitios web métricas e informes sobre los resultados de búsqueda y los resúmenes generados por IA. Google ha compartido información sobre sus controles actuales y los que acaba de anunciar, así como sobre lo que ya está desarrollando, incluidas herramientas adicionales de transparencia a nivel de URL para los propietarios de sitios web relacionadas con Google-Extended, que espera lanzar en las próximas semanas. Google también ha señalado que desactivar Google-Extended [no afecta al posicionamiento en los resultados de búsqueda](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended:~:text=Google%2DExtended%20does%20not%20impact%20a%20site%27s%20inclusion%20in%20Google%20Search%20nor%20is%20it%20used%20as%20a%20ranking%20signal%20in%20Google%20Search.).

### Bingbot

Bingbot ofrece controles granulares y transparencia en sus [Herramientas para webmasters](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c). Los propietarios de sitios web ya pueden indicar sus preferencias de entrenamiento de IA a través de la etiqueta meta [`NOARCHIVE`](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=Content%20tagged%20NOARCHIVE%20will%20not%20be%20included%20in%20Bing%20Chat%20answers%2C%20not%20be%20linked%20to%20in%20the%20answers.%20Going%20forward%2C%20for%20content%20in%20our%20Bing%20Index%20that%20is%20labeled%20NOARCHIVE%2C%20we%20will%20not%20use%20the%20content%20for%20training%20Microsoft%E2%80%99s%20generative%20AI%20foundation%20models.) de Bing. Microsoft está ampliando estas capacidades y, en estos momentos, está desarrollando el mecanismo para respetar también la preferencia de "no entrenamiento" en el archivo robots.txt a nivel de dominio o sitio web, con el objetivo de que esté listo a principios de 2027. Para los clientes de Cloudflare que deseen optar por no entrenar en Bing desde ya, además de usar la etiqueta `NOARCHIVE`, los propietarios de sitios pueden usar la [herramienta de "Bloquear URL" o "Eliminación de contenido"](https://www.bing.com/webmasters/help/block-urls-from-bing-264e560a). Microsoft también ha afirmado que usar `NOARCHIVE` [no afectará al posicionamiento en los resultados de búsqueda.](https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat#:~:text=We%20also%20heard%20from%20publishers%20that%20they%20want%20to%20exercise%20these%20choices%20without%20impacting%20how%20Bing%20users%20can%20discover%20web%20content%20on%20Bing%E2%80%99s%20search%20results%20page.%20We%20can%20assure%20publishers%20that%20content%20with%20the%20NOCACHE%20tag%20or%20NOARCHIVE%20tag%20will%20still%20appear%20in%20our%20search%20results.).

Hasta que se lance esa compatibilidad, seleccionar "No permitir el entrenamiento de IA" no comunicará automáticamente a Bing la preferencia de no participar en el entrenamiento a través del archivo robots.txt. Este comportamiento es idéntico al de la anterior configuración "Bloquear entrenamiento", que no se aplicaba a rastreadores de uso mixto como Bingbot.

### Más avances

Continuaremos contactando y colaborando con todos los operadores de rastreadores de IA a medida que evolucionen estas capacidades. Cloudflare [Radar](https://radar.cloudflare.com/ai-insights#ai-bot-transparency) realiza un seguimiento público de los controles, la transparencia y la información que proporcionan los operadores de rastreadores con la designación "Responsable" 

Mejorar Internet requiere que ambas partes tengan capacidad de decisión. Los rastreadores necesitan acceso a la web abierta, y las personas que crean esa web necesitan un control significativo sobre cómo se utiliza su trabajo. El anuncio de hoy supone un avance concreto hacia ese equilibrio.

Para seguir avanzando, es necesario que los proveedores de infraestructura, los creadores de contenido, las empresas tecnológicas y los organismos de normalización, como el Grupo de Trabajo de Ingeniería de Internet (IETF), trabajen juntos para convertir estos principios en estándares abiertos e interoperables.

## Próximos pasos | Resúmenes de la IA

El entrenamiento y los resúmenes de IA plantean diferentes cuestiones a los propietarios de sitios web. El entrenamiento se refiere a si el contenido puede usarse para crear modelos de IA. Los resúmenes influyen en cómo la gente descubre, evalúa y, en última instancia, visita un sitio web. Ambos son importantes, pero afectan a las empresas de diferentes maneras.

Las opciones para desactivar los resúmenes generados por IA son el primer paso. Los operadores con la designación "Responsable" ya ofrecen esa función o están trabajando para ofrecerla, lo que establece un punto de referencia importante: los propietarios de sitios web pueden decir que no. Pero la opción de permitir o prohibir los resúmenes en todo el sitio sigue siendo una herramienta poco precisa.

Pero la opción de permitir o prohibir los resúmenes en todo el sitio sigue siendo un instrumento poco preciso. La decisión correcta depende del sitio web, del contenido y del resultado para el negocio. Para los creadores de contenido, el entrenamiento plantea cuestiones fundamentales sobre el control, la compensación y la sostenibilidad del contenido original. Los resúmenes plantean una cuestión de distribución aparte y, a menudo, más inmediata: ¿visita alguien el sitio del editor o se limita a consultar la respuesta en una búsqueda o en una experiencia de IA? Para muchas otras empresas, los resúmenes generados por IA se interponen cada vez más entre un cliente potencial y un sitio web. Pueden responder a una pregunta, comparar alternativas, recomendar un producto o ayudar a decidir si merece la pena visitar el sitio web.

Los datos muestran un impacto desigual. [Más de la mitad](https://www.pewresearch.org/chart/a-majority-of-americans-say-they-read-ai-summaries-at-the-top-of-search-results/) de los usuarios leen resúmenes en la búsqueda, y esos usuarios tienen un [40 % más de probabilidades](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) de [dar por terminada su búsqueda](https://www.bain.com/insights/goodbye-clicks-hello-ai-zero-click-search-redefines-marketing/) tras leer uno. Esto puede reducir el número de visitas que recibe un sitio web. Pero los consumidores que llegan a través de la búsqueda con IA convierten entre [tres veces](https://aisearch.similarweb.com/blog/ai-visibility-roi/) y [más de cinco veces](https://quickseo.ai/blog/ai-search-vs-google-search-in-2026-40-stats-that-show-why-your-brand-needs-to-track-both#:~:text=AI%20search%20traffic%20converts%20at%2014.2%25%2C%20compared%20to%20Google%E2%80%99s%202.8%25) la tasa de los que llegan por la búsqueda tradicional. La IA puede generar menos visitas, pero atrae a clientes con una intención de compra mucho mayor.

Eso no es ni bueno ni malo. Un creador de contenido que se financia con publicidad puede optar por maximizar el volumen de audiencia. Un minorista puede preferir menos visitantes que tengan más probabilidades de comprar. El papel de Cloudflare no es elegir por ellos, sino proporcionar la visibilidad y el control necesarios para tomar una decisión informada.

Las opciones de exclusión de los resúmenes son un buen comienzo, pero no son el objetivo final. Nuestro siguiente paso es ayudar a los propietarios de sitios web a entender cómo afectan los resúmenes a sus negocios y darles más control sobre qué parte de su contenido se puede usar. Los estándares abiertos, como [ai-prefs](https://datatracker.ietf.org/wg/aipref/documents/), serán una parte importante para hacerlo posible.

Si quieres dar tu opinión en este debate o enviarnos tus comentarios, escribe a [crawlercontrols@cloudflare.com](mailto:crawlercontrols@cloudflare.com).

Estos nuevos controles están disponibles para todos los clientes, en todos los planes, y se pueden configurar en los [ajustes de seguridad](https://dash.cloudflare.com/?to=/:account/:zone/security/settings) del dominio (zona). ¿Aún no eres cliente de Cloudflare? [Empieza gratis](https://www.cloudflare.com/lp/pg-one-platform/) hoy mismo para configurar los controles de tráfico que quieras.

]]>01M30SJPABSN2YKRXC1VQS8196Informe de Cloudflare sobre las amenazas DDoS del 1.er semestre de 2026 | Los ataques de 1 TB/s se disparan: las tensiones geopolíticas y las inundaciones de DNS desatan una nueva ola de amenazashttps://blog.cloudflare.com/es-es/ddos-threat-report-2026-h1/ Wed, 12 Aug 2026 09:35:08 GMTIn the first half of 2026, Cloudflare detected a 519% surge in hyper-volumetric DDos attacks across its network. These attacks were driven heavily by DNS and CLDAP reflection vectors. This report breaks down how major geopolitical conflicts reshaped the global cyber threat landscape.AtaquesCloudforce OneDDoSRadarThreat ReportTe damos la bienvenida a la 16.ª edición de nuestro informe sobre las amenazas DDoS. Esta es la primera edición semestral de la serie. En lugar de publicar informes específicos para el [1.er](http://1.er) y el 2.º trimestre de 2026, hemos juntado los datos de ambos periodos en un solo volumen que abarca de enero a junio de 2026. El análisis lo ha elaborado [Cloudforce One](https://www.cloudflare.com/cloudforce-one/), la organización de información sobre amenazas de Cloudflare, y ofrece un análisis exhaustivo de la evolución del panorama de las amenazas de los [ataques de denegación de servicio distribuido (DDoS)](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) basado en datos de la [red de Cloudflare](https://www.cloudflare.com/network/).

## Aspectos clave

  1. Los ataques que superan el 1 TB/s ya no son una excepción. Cloudflare mitigó un total de 935 ataques DDoS a la capa de red que superaron 1 TB/s durante el primer semestre de 2026, lo que supone un aumento de más del 519 % respecto al trimestre anterior, entre el primer y el segundo trimestre. 
  2. El epicentro de los vectores de ataque pasó de las inundaciones de botnets a la reflexión y la amplificación. Los ataques contra el sistema DNS representaron el 34,3 % de toda la actividad contra la capa de red en la primera mitad de 2026. Solo las [inundaciones de DNS](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) pasaron del 25,7 % al 40 % de los ataques a la capa de red en términos intertrimestrales. Las [inundaciones CLDAP](https://blog.cloudflare.com/reflections-on-reflections/) se dispararon más de un 580 % en la misma comparación hasta convertirse en el tercer vector más importante en el segundo trimestre.
  3. La geopolítica y los acontecimientos mundiales influyen en el panorama. El sector de los medios de comunicación, la producción y la edición siguió siendo el más afectado en ambos trimestres, representando el 14,2 % de todas las solicitudes DDoS HTTP mitigadas, ya que la cobertura de Irán, Ucrania y el Mundial acaparó la atención durante todo ese tiempo. Al mismo tiempo, Turquía subió al tercer puesto de los países más afectados en el contexto de la cumbre de la OTAN celebrada en julio en Ankara. El sector público saltó del puesto 29 al 9 — la mayor escalada de un solo sector en lo que va de 2026 — durante la operación Furia Épica.



## El 1.er semestre en cifras: 5300 ataques DDoS cada hora

A mitad de año, Cloudflare ya ha mitigado 23,2 millones de solicitudes DDoS en la capa de red y 29,64 billones de solicitudes DDoS HTTP. Eso supone aproximadamente 5343 ataques DDoS a la capa de red por hora, o unos 128 000 al día.

### El pico de abril y las intervenciones de las fuerzas del orden

Abril de 2026 fue el mes con mayor actividad y volumen de ataques DDoS, alcanzando un máximo de 6,46 billones de solicitudes y 165 petabytes, respectivamente. Para que te hagas una idea, se trata de una cantidad enorme de tráfico. Equivale a reproducir vídeo 4K en streaming de forma continua durante años, o más o menos la cantidad de datos que procesan las principales plataformas de vídeo en un solo día. Las solicitudes y los volúmenes disminuyeron después, lo que podría deberse a la [operación PowerOFF](https://www.europol.europa.eu/media-press/newsroom/news/europol-supported-global-operation-targets-over-75-000-users-engaged-in-ddos-attacks), una acción en la que participaron 21 países y que se centró en más de 75 000 usuarios de servicios de DDoS por encargo, desactivó 53 dominios, emitió 25 órdenes de registro y dio lugar a cuatro detenciones.

### Los ataques hipervolumétricos se multiplican por más de seis

Los ataques DDoS hipervolumétricos, definidos como aquellos que superan 1 TB/s, 1000 millones de paquetes por segundo o 1 millón de solicitudes por segundo, han sido una categoría en auge en los informes de Radar. El año 2026 no está siendo una excepción. Durante el segundo trimestre, Cloudflare mitigó 805 ataques a la capa de red que superaron 1 TB/, lo que representa un aumento de más de seis veces respecto al trimestre anterior.

## Características de los ataques: de baja intensidad y lentos

A pesar del crecimiento de los ataques hipervolumétricos, la mediana de los ataques DDoS que Cloudflare mitigó en el primer semestre de 2026 siguió siendo breve y de poca envergadura: el 96,62 % de los ataques a la capa de red se mantuvieron por debajo de los 500 MB/s y el 90,60 % terminaron en menos de 10 minutos. Sin embargo, es importante señalar que "pequeño" es un término relativo y que la mayoría de los sitios web no podrían soportar ni siquiera esos ataques pequeños. En términos prácticos:

  * Un ataque de 100 MB/s es suficiente para colapsar un servidor o una página web
  * Un ataque de 100 GB/s puede dejar fuera de servicio a la mayoría de los centros de datos expuestos
  * Un ataque de más de 1 TB/s está entre los mayores jamás registrados y pone a prueba incluso la infraestructura principal de Internet



A veces, los atacantes mezclan capas, una alta tasa de paquetes (millones de paquetes por segundo / miles de millones de paquetes por segundo) con un ancho de banda relativamente bajo (GB/s), o al revés, para aprovechar diferentes puntos débiles en los equipos de red frente a la capacidad de ancho de banda.

Además, la mayoría de los ataques DDoS duran sorprendentemente poco, como se muestra en el gráfico de abajo. Incluso los ataques hipervolumétricos más grandes pueden medirse en segundos en lugar de minutos. Hemos observado [ataques récord que duraron solo 35 segundos](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/#hyper-volumetric-attacks-continue-spill-into-q2) de principio a fin. Tanto si un ataque dura medio minuto como diez minutos, no hay margen práctico para la intervención humana: para cuando la alerta llega a un analista de seguridad, el ataque ya ha terminado. La mitigación manual y las soluciones bajo demanda son simplemente demasiado lentas para esta realidad. Sin embargo, aunque el ataque en sí mismo puede ser breve, sus repercusiones no lo son. Los efectos en cadena incluso de una ráfaga breve pueden provocar inestabilidad en el enrutamiento, retransmisiones TCP, tiempos de espera de las aplicaciones y una degradación del servicio que tarda horas o días en resolverse por completo, todo ello mientras los servicios permanecen inactivos o comprometidos. En este panorama de amenazas, la protección automatizada y siempre activa no es un lujo, sino una necesidad.

## Sectores más afectados

### La operación Furia Épica y el aumento en los ataques al sector público

El 28 de febrero de 2026, Israel y Estados Unidos lanzaron la operación Furia Épica, una serie de ataques contra los dirigentes y las infraestructuras de Irán. En menos de 72 horas, el panorama de los ataques DDoS respondió, y los [expertos en seguridad](https://thehackernews.com/2026/03/149-hacktivist-ddos-attacks-hit-110.html) registraron 149 reivindicaciones de ataques DDoS por parte de hacktivistas contra 110 organizaciones distintas en 16 países. Casi el 47,8 % de todas las organizaciones afectadas a nivel mundial pertenecían al sector público.

Dado que los informes públicos documentaron numerosos ataques dirigidos contra el sector público durante este periodo, este sector escaló 20 puestos, pasando del n.º 29 en el primer trimestre al n.º 9 en el segundo trimestre, según la proporción de solicitudes DDoS HTTP mitigadas. Aunque se mantuvo fuera de los 10 primeros puestos durante la mayor parte de este periodo, representó uno de los mayores saltos en la clasificación por sectores.

### Los medios de comunicación, en el punto de mira: el sector más afectado

Entre los conflictos en Irán y Ucrania y la emoción del Mundial, el sector de los medios de comunicación, la producción y la edición fue el más afectado en ambos trimestres, acaparando el 14,2 % de todas las solicitudes DDoS HTTP mitigadas, casi cuatro veces más que el segundo sector más afectado

## Países más afectados por los ataques

El panorama de los ataques DDoS en el primer semestre de 2026 contó tanto con nombres conocidos como con cambios en la clasificación de los lugares más afectados del mundo. China cerró el primer semestre como el país más afectado, tras recibir el 22,4 % de todas las solicitudes DDoS HTTP a nivel mundial en el segundo trimestre. Estados Unidos mantuvo el segundo puesto (18,8 %), lo que demuestra que sigue siendo un objetivo atractivo para los atacantes.

Turquía experimentó un rápido aumento de los ataques, y duplicó con creces su cuota del tráfico global de ataques hasta situarse en el tercer puesto de las ubicaciones más atacadas en el segundo trimestre. Este repunte coincidió con los preparativos de la cumbre de la OTAN de Ankara de 2026, celebrada entre junio y principios de julio, cuando las fuerzas de seguridad turcas llevaron a cabo [redadas masivas previas a la cumbre](https://apnews.com/article/turkey-nato-summit-suspects-detained-864260d7cbe9ca73cd05115cd638ee93) por toda Ankara, deteniendo al menos a 209 personas.

## Principales países de origen de los ataques

Brasil superó a Estados Unidos como principal país de origen de los ataques DDoS en la primera mitad de 2026, con un 14,9 % frente a un 13,4 % — impulsado por un espectacular repunte en el segundo trimestre, cuando Brasil se convirtió en el país de origen del 21,4 % de todo el tráfico de solicitudes DDoS mitigado. Indonesia se mantuvo en el tercer puesto en ambos trimestres, convirtiéndose en uno de los tres principales países de origen de ataques DDoS a nivel mundial durante varios trimestres seguidos. 

## Vectores de ataque

### Predominio de las inundaciones de DNS

Los ataques contra los sistemas DNS ([inundación de DNS](https://www.cloudflare.com/learning/ddos/dns-flood-ddos-attack/) y [amplificación de DNS](https://www.cloudflare.com/learning/ddos/dns-amplification-ddos-attack/)) representaron el 34,3 % de los ataques contra la capa de red en la primera mitad de 2026. Los dos mecanismos están relacionados, pero son distintos: una inundación de DNS dirige el volumen bruto de solicitudes de una botnet directamente a los servidores DNS autoritativos del objetivo para agotar su capacidad de consulta. La "guía telefónica" de ese dominio deja de ser accesible y todos los servicios que dependen de él dejan de funcionar. La amplificación de DNS, por su parte, envía pequeñas consultas [falsificadas](https://www.cloudflare.com/learning/ddos/glossary/ip-spoofing/) a [solucionadores DNS](https://www.cloudflare.com/learning/dns/dns-server-types/) abiertos que responden con registros mucho más grandes (a menudo activados por una consulta ANY) a la IP falsificada del objetivo.

### Los ataques de inundación CLDAP se disparan | Los ataques de amplificación aumentan más de un 580 %

Los ataques de inundación CLDAP, un vector de reflexión y amplificación que se aprovecha de los puntos finales LDAP sobre UDP de Active Directory expuestos, se dispararon más de un 580 % respecto al trimestre anterior, convirtiéndose en el tercer vector más importante solo en el segundo trimestre. CLDAP ([protocolo ligero de acceso a directorios sin conexión](https://datatracker.ietf.org/doc/html/rfc1798)) es una variante de LDAP ([protocolo de acceso ligero a directorios](https://datatracker.ietf.org/doc/html/rfc4511)), que se utiliza para consultar y modificar los servicios de directorio que se ejecutan en redes IP. CLDAP funciona sin conexión, ya que utiliza UDP en lugar de TCP, lo que lo hace más rápido pero menos fiable. Como utiliza UDP, no es necesario un protocolo de enlace, lo que permite a los atacantes falsificar la dirección IP de origen y, por lo tanto, explotarla como vector de reflexión. Los ataques CLDAP funcionan enviando pequeñas consultas falsificadas a controladores de dominio accesibles públicamente en el puerto UDP 389. Los servidores responden a la fuente falsificada (el objetivo) con respuestas entre diez y cien veces más grandes que la consulta original, lo que satura el host de la víctima.

## Cómo mejorar las defensas globales y ayudar a proteger Internet

La red de Cloudflare está diseñada para absorber este tipo de crecimiento en las amenazas de DDoS. Todos los servicios de nuestra red están respaldados por una [protección DDoS gratuita e ilimitada](https://www.cloudflare.com/ddos/) que funciona en [cada una de nuestras más de 330 ciudades de todo el mundo](https://www.cloudflare.com/network/), con una capacidad de red de 500 TB/s. La clave está en la autonomía: nuestros sistemas detectan y mitigan los ataques [sin intervención humana](https://developers.cloudflare.com/ddos-protection/about/), y tienen que hacerlo, porque ahora los atacantes lanzan regularmente ataques de más de 1 TB/s a un ritmo de cientos por trimestre.

Para ayudar a los proveedores de alojamiento, las plataformas de informática en la nube y los proveedores de acceso a Internet a identificar y eliminar las direcciones IP / cuentas abusivas que lanzan estos ataques, aprovechamos la perspectiva exclusiva de Cloudflare sobre los ataques DDoS para proporcionar un [canal gratuito de amenazas de botnets DDoS para proveedores de servicios](https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/). 

Más de 800 redes de todo el mundo ya se han registrado en este canal, y hemos observado una gran colaboración en toda la comunidad para desmantelar los nodos de botnets.

## Acerca de Cloudforce One

Con la misión de ayudar a proteger Internet, [Cloudforce One](https://www.cloudflare.com/cloudforce-one/) se basa en la telemetría de la red global de Cloudflare, que protege más del 20 % de la web, para impulsar la investigación de amenazas y la respuesta operativa, protegiendo así los sistemas críticos de millones de organizaciones en todo el mundo.

]]>01KZTMTMAEXDW337SAH5SMFEYRNuestras novedades y lanzamientos durante la Agents Weekhttps://blog.cloudflare.com/es-es/agents-week-review-august-2026/ Wed, 12 Aug 2026 07:59:59 GMTLa Agents Week ha llegado a su fin. Aquí tienes un resumen de las novedades que hemos anunciado, desde Wallets hasta Radar.AgentesAgents WeekAICloudflare OneCloudflare WorkersDesarrolladoresPlataforma para desarrolladoresSASEZero TrustAl principio de la Agents Week, Rita[ comentó](https://blog.cloudflare.com/agents-week-welcome/) que los agentes representan la próxima evolución de la informática. No solo como una nueva aplicación de la IA, sino también como una nueva clase de software que está definiendo cómo interactuamos con la tecnología y cómo el software interactúa con Internet. Durante el[ último año](https://www.cloudflare.com/innovation-week/ai-week-2025/updates/) más o menos, nos propusimos analizar qué supone este cambio para los desarrolladores y los clientes que crean aplicaciones nativas de la IA y la infraestructura necesaria para darles soporte. A medida que los agentes se vuelven más capaces y autónomos, los desafíos van más allá de los propios modelos, abarcando la identidad, la comunicación, la orquestación, la memoria, la observabilidad y la seguridad.

Durante la última semana hemos explicado cómo estamos uniendo todas esas piezas en la plataforma de Cloudflare para dar servicio a una web agéntica. Cada día presentamos nuevas herramientas, productos e ideas para crear una red de Internet donde humanos y agentes puedan[ cooperar en lugar de chocar](https://blog.cloudflare.com/the-agentic-internet/).

### **Lunes, 3 de agosto**

El lunes nos centramos en los fundamentos para crear y ejecutar aplicaciones inteligentes y autónomas: el entorno de ejecución y la infraestructura de la que dependen los agentes.

[Tu agente necesita un ordenador, no un contenedor. Llega @cloudflare/computer](https://blog.cloudflare.com/es-es/cloudflare-computer/)| @cloudflare/computer presenta un nuevo entorno de ejecución, diseñado para agentes, que puede elegir el entorno adecuado para cada tarea.  
---|---  
[Workers RPC ahora funciona tanto con Python como con JavaScript](https://blog.cloudflare.com/python-workers-rpc/)| Los Workers de Python y JavaScript ahora pueden comunicarse entre sí directamente, lo que facilita los proyectos con varios lenguajes.  
[Más pequeño, más rápido, más seguro: cómo ejecutar Kimi y GLM a escala](https://blog.cloudflare.com/smaller-faster-safer-models/)| Aprendemos a gestionar modelos grandes de forma más eficiente, sin renunciar a la calidad, la fiabilidad y la seguridad.  
[Novedad: Billable Usage API, visibilidad programática de los costes en Cloudflare](https://blog.cloudflare.com/billable-usage-api/)| Una manera más sencilla de rastrear el uso y los costes en nuestros productos de autoservicio.   
[Cloudflare Workers y Containers ahora admiten conexiones TCP entrantes y gRPC](https://blog.cloudflare.com/grpc-workers/)| Aloja backends de IA de voz u otros agentes de voz en tiempo real con Cloudflare Workers.  
  
### **Martes, 4 de agosto**

El martes anunciamos el Ciclo de Vida del Desarrollo de Agentes (ADLC) y las primitivas que llevan el software agéntico desde el prototipo hasta la producción.

[El Ciclo de Vida de Desarrollo de Agentes ha llegado a Cloudflare](https://blog.cloudflare.com/es-es/agent-development-lifecycle/)| Las ventajas del ADLC frente al SDLC (Ciclo de Vida del Desarrollo de Software). Nuestra visión sobre cómo llevar los agentes del prototipo a la producción, y las primitivas que sustentan la próxima generación de "fábricas de software".  
---|---  
[Novedad: Cloudflare Agents](https://blog.cloudflare.com/agents-on-cloudflare/)| Crea agentes en Cloudflare y observa cada ejecución en directo, con seguimiento, reproducción y aprobaciones con intervención humana para lo que ocurre en producción.  
[Ahora tu agente puede depurar Workers con trazado local](https://blog.cloudflare.com/local-tracing/)| Incorporamos el rastreo distribuido al desarrollo local, lo que facilita que los agentes detecten y depuren problemas antes de que lleguen a producción.  
[Novedad: Cloudflare Wallets, el monedero programable para la web agéntica](https://blog.cloudflare.com/es-es/wallets/)| Los monederos ofrecen una forma segura para que los agentes realicen transacciones como participantes en la emergente economía agéntica.  
[Ejecuta canales de integración y distribución continuas (CI/CD) para millones de repositorios — en tu plataforma, en Cloudflare](https://blog.cloudflare.com/ci-workflows/)| CI/CD programable; canalizaciones escritas en código, no en configuración, con un agente que repara los fallos y prepara la corrección para su revisión.  
[Cloudflare aplica los estándares de ingeniería usando IA](https://blog.cloudflare.com/engineering-standards-enforcement/)| Te explicamos cómo usamos la automatización basada en la IA en todos nuestros flujos de trabajo de desarrollo para mantener alineados los estándares de código y los procesos, ayudando a nuestras propias fábricas de software a ofrecer código de calidad y consistente a escala.  
[Cómo creamos una fábrica de software para reducir a cero el número de incidencias de Astro en GitHub](https://blog.cloudflare.com/astro-issue-triage/)| Automatizamos el análisis, la categorización y el enrutamiento de incidencias para minimizar el esfuerzo de mantenimiento del software y maximizar la productividad de los desarrolladores.  
  
### **Miércoles, 5 de agosto**

El miércoles ampliamos el modelo Zero Trust de los usuarios y dispositivos a los propios agentes, y explicamos cómo lo aplicamos internamente en Cloudflare. 

[Agent Access Model](https://blog.cloudflare.com/the-agent-access-model/)| Un marco que permite a los agentes acceder de forma segura a recursos y servicios en nombre de los usuarios, en una red de Internet cada vez más poblada por agentes.   
---|---  
[Cómo estamos replanteando el trabajo en Cloudflare con Cloudflare OS](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os/)| Te contamos cómo hemos integrado la IA en nuestro modelo operativo interno para permitir a los equipos trabajar de manera más inteligente y rápida sin renunciar a la seguridad ni a la supervisión.  
[Cloudflare OS, una plataforma abierta para agentes, aplicaciones y tareas](https://blog.cloudflare.com/es-es/cloudflare-os/)| Hemos convertido en código abierto la plataforma que usan nuestros equipos para crear aplicaciones, automatizar el trabajo y acceder a los sistemas internos de forma segura.   
[Detección de comportamientos anómalos de la IA mediante análisis basados en la identidad](https://blog.cloudflare.com/es-es/identity-aware-ai-gateway/)| Atribuye la actividad de la IA a usuarios y sistemas reales para detectar más fácilmente anomalías y picos de gasto.  
[WriteGuard, controles detallados para servidores MCP](https://blog.cloudflare.com/mcp-portal-writeguard-private-beta/)| Ofrecemos a los clientes las mismas herramientas que usamos nosotros, para tener más control sobre las llamadas a herramientas de riesgo y reducir las posibilidades de que los agentes hagan cambios no deseados.  
  
### **Jueves, 6 de agosto**

El jueves definimos la web agéntica y cómo los propietarios de sitios web, los editores y los agentes pueden contribuir a una red de Internet que funcione tanto para las personas como para los agentes.

[Internet agéntica abierta: legible, localizable, invocable y pagadera](https://blog.cloudflare.com/es-es/the-agentic-internet/)| Un modelo de web agéntica en el que los editores mantienen el control, los agentes obtienen acceso útil a lo que necesitan y los protocolos abiertos permiten que ambas partes realicen transacciones.  
---|---  
[Dale una interfaz WebMCP a cualquier sitio web](https://blog.cloudflare.com/webmcp/)| Un avance de WebMCP, que presenta un nuevo enfoque (y muy sencillo) para que los agentes puedan detectar y utilizar sitios web y aplicaciones web.  
[Adiós a los rankings: adapta tu web a la nueva era de los agentes de IA](https://blog.cloudflare.com/es-es/aeo/)| Adapta el SEO a las prácticas de AEO (optimización para motores de respuestas) y mejora así la forma en que los agentes descubren, comprenden y muestran el contenido web.  
[Kitesurf, el navegador que da prioridad a los agentes y que se ejecuta en aislamientos de V8 en Cloudflare Workers](https://blog.cloudflare.com/kitesurf/)| Un navegador optimizado para agentes, que prioriza el bajo consumo de memoria y CPU sobre la precisión de la representación del píxel.  
[La próxima generación del estándar MCP](https://blog.cloudflare.com/mcp-v2/)| MCP se ha reescrito. MCPv2 presenta la próxima evolución del soporte MCP, simplificando la implementación y la escalabilidad de las aplicaciones de agentes.  
[Cloudflare AI Search: proporciona a tus agentes un motor de búsqueda para tus datos](https://blog.cloudflare.com/ai-search-easier/)| AI Search convierte tus archivos o tu sitio web en un motor de búsqueda listo para agentes con un solo comando.  
  
### **Viernes, 7 de agosto**

El viernes nos centramos en lo que realmente está pasando: qué hacen realmente los agentes en la web, dónde se ejecuta la IA en tus aplicaciones, quién contribuye a los ecosistemas y las nuevas herramientas para analizar datos de Internet.

[Luces y sombras en la era de la web agéntica](https://blog.cloudflare.com/es-es/good-and-bad-agentic-behaviors/)| Los bots no siempre son malos, y los humanos no siempre son buenos. Replanteamos la mitigación de los bots en torno a la confianza continua en lugar de al riesgo puntual.  
---|---  
[Unificamos Workers AI y AI Gateway en un único plano de control de IA](https://blog.cloudflare.com/workers-ai-gateway-unification/)| Un enlace, un monedero, un panel de control para llamar a cualquier modelo de IA; lo siguiente es el enrutamiento con prioridad en el modelo.  
[Anunciamos Cloudflare Ambassadors, Community Engineers y otro millón de dólares en financiación para el código abierto](https://blog.cloudflare.com/community-program-refresh/)| Nuestra nueva iniciativa Comunidad presenta dos programas nuevos: Cloudflare Ambassadors para líderes de la comunidad y Community Engineers para administradores de código abierto, además de un millón de dólares más en financiación para código abierto durante los próximos dos años.  
[Radar Researcher, una herramienta de IA para explorar datos de Internet en lenguaje sencillo](https://blog.cloudflare.com/introducing-radar-researcher/)| El asistente de investigación con IA de Radar: pregunta en lenguaje sencillo y obtén gráficos interactivos reales.  
  
### **La Agents Week ha terminado, pero nuestro trabajo continúa**

Tras cinco días, la respuesta a la pregunta de Rita "[¿Qué necesita tu agente de un Agent Cloud?](https://blog.cloudflare.com/agents-week-welcome/)" empieza a tomar forma. Necesita una capa de ejecución y primitivas sobre las que funcionar, un ciclo de vida de desarrollo que se escriba cada vez más solo, acceso seguro para las personas y los agentes que realizan el trabajo, una web agéntica, y los humanos y las comunidades que mantienen todo esto con los pies en la tierra. Aún queda mucho por hacer, pero el futuro se va perfilando cada vez con más claridad: una red de Internet que apoye de forma nativa tanto a los humanos para los que fue creada como a los agentes que ahora actúan en su nombre.

Nuestro trabajo no termina aquí. No te pierdas nuestro[ registro de cambios](https://developers.cloudflare.com/changelog/) para estar al día de las últimas novedades. Y si estás trabajando en algo relacionado, ¡nos encantaría saber de ti! Búscanos en[ X](https://x.com/cloudflaredev) o en[ Discord](https://discord.com/invite/cloudflaredev).

]]>01KZTEVDD3V3VZJVRGHK7WPEHRLuces y sombras en la era de la web agénticahttps://blog.cloudflare.com/es-es/good-and-bad-agentic-behaviors/ Wed, 12 Aug 2026 06:41:29 GMTloudflare sustituye la mitigación de bots, que antes se basaba en una evaluación de riesgos puntual, por una evaluación continua de la confianza. Descubre cómo nuestros sistemas, entre los que se incluye BotBase y Precursor, evalúan los nuevos comportamientos positivos y negativos de los bots y los agentes, y prueba nuestra simulación Precursor Trace para ver cómo se interpretarían tus propios movimientos del cursor: ¿como humanos o bots?AgentesAgents WeekAI Bots (ES)Gestión de botsServicios de redInternet no es una única vía de tráfico. Durante mucho tiempo, la regla general en la seguridad web era que los bots son malos, mientras que los humanos son buenos. Por supuesto, ya hemos dejado atrás esa generalización hace tiempo. Los humanos pueden ser fraudulentos, y los bots pueden resultar útiles en distintos niveles. A los propietarios de sitios web nos interesa que haya tráfico automatizado que interactúe con nuestros sitios para que Internet sea funcional y visible.

Para complicar aún más las cosas, la línea entre "humano" y "bot" se está desdibujando cada vez más. Ahora, tenemos un tipo de tráfico "híbrido" donde una sola sesión cambia de humano a agente y viceversa. (Imagina a un usuario que está echando un vistazo en una tienda y luego deja que un asistente de compras automatizado se encargue del proceso de pago).

¿Cómo gestionan los propietarios de sitios web este tipo de complejidad? Lo que importa aquí es evaluar **comportamientos**. ¿Es un comportamiento abusivo? ¿Malicioso? ¿Qué riesgo supone? ¿Puedo confiar en este visitante basándome en sus acciones? Para resolver esto hay que ir más allá de las comprobaciones estáticas y puntuales. Hay que analizar comportamientos continuos para evaluar la confianza.

En esta entrada, te vamos a dar una visión de primera mano de la estrategia del equipo de Integridad y Confianza en la Web (que se ocupa de los problemas relacionados con los bots y el fraude) en lo que respecta a la detección y el análisis de comportamientos positivos y negativos, y te vamos a ofrecer herramientas para que los propietarios de sitios web puedan hacer frente a los nuevos desafíos que plantea la web agéntica, que está en constante evolución. También te contaremos lo que hemos descubierto sobre el tráfico agéntico desde el lanzamiento de[ Precursor](https://blog.cloudflare.com/introducing-precursor/), y te mostraremos una simulación en la que podrás ver cómo se evaluarían tus propios movimientos del cursor para determinar si eres humano o un bot, además de algunas novedades interesantes que lanzaremos en un futuro próximo.

## **Definición de riesgo y confianza**

Hablemos de la distinción entre **riesgo** y **confianza** , tal y como la abordamos dentro de los equipos de Cloudflare que trabajan en la detección de bots. A menudo se consideran polos opuestos de un continuo. En Cloudflare, los consideramos valores independientes, pero recíprocos. La confianza es el ingrediente clave para tomar decisiones bien fundamentadas sobre qué hacer con tu tráfico. 

El riesgo es la probabilidad de que algo, como una solicitud o una acción, resulte perjudicial, y suele ser algo pasajero. La confianza, en cambio, se va construyendo con el tiempo y se basa en la reputación.

Podemos ilustrarlo con un ejemplo de la vida real. Imagina que estás disfrutando de un rato de tele por la noche en casa, cuando de repente oyes que llaman al timbre una y otra vez. Además de ser molesto, este comportamiento es extraño. Los timbres frenéticos a altas horas de la noche son alarmantes.

Miras por la cámara de la puerta y ves que la persona que llama al timbre es tu mejor amigo, que vive al lado. Por supuesto, confías en tu mejor amigo, y apostaríamos a que lo dejarías entrar.

En este ejemplo, no bastaría con que dijeras: "Rechaza a cualquiera que llame al timbre por la noche" o "Rechaza a cualquiera que llame al timbre más de 10 veces". De nuevo, la confianza es el ingrediente esencial.

Volviendo al tráfico en Internet, la estrategia a la hora de desarrollar productos en el ámbito de los bots y el fraude se centra en crear todo un ecosistema basado en la confianza. Y nuestro objetivo es ofrecer los incentivos y las herramientas básicas que los propietarios de sitios web puedan usar para fomentar comportamientos que hagan que Internet sea más seguro para todos: desde bloquear las actividades maliciosas desde la base hasta animar a la gente a participar en una Internet más segura a nivel general.

## **Transparencia como base del buen comportamiento**

Lo primero, ¿qué se considera un buen comportamiento? Podemos sacar ejemplos claros de los bots y agentes verificados de BotBase. El mes pasado anunciamos una[ nueva clasificación práctica para los bots buenos que seguimos en nuestro sistema](https://blog.cloudflare.com/content-independence-day-ai-options/), en la que redefinimos el término "[Verificado](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/)" basándonos en dos cosas: 1) que te identifiques con sinceridad, y 2) que no abuses de la confianza que te has ganado. 

La transparencia entre el propietario de una web y el operador de un bot permite establecer una relación simbiótica: los propietarios pueden indicar qué comportamientos y usos de datos quieren permitir en sus sitios web, y a los operadores de bots se les puede conceder acceso más fácilmente. La transparencia fomenta la confianza en la relación. Si no tienes nada que ocultar, decir quién eres debería reducir las dificultades con los sitios web que quieren permitir tus comportamientos.

[BotBase](https://developers.cloudflare.com/bots/botbase/) no pretende limitarse a declarar "quién es de fiar". Su objetivo es ser un directorio de todos los bots y agentes conocidos, y ofrecer datos objetivos. A diferencia de nuestro anterior directorio de bots, que solo incluía bots de confianza, BotBase también es capaz de rastrear bots y agentes que _no son tan fiables_. ¿Por qué? Como nuestros sistemas rastrean y validan el comportamiento de los actores de confianza, disponemos de las herramientas necesarias para identificar cuándo no se cumplen estas expectativas. Si abusas de la confianza en la red de Cloudflare, **no** se te debería permitir el acceso fácilmente, por lo que no se te verificará.

## **Comportamientos indebidos: evidentes, encubiertos y todo lo que hay entre medias**

Hace unas semanas, anunciamos[ Precursor](https://blog.cloudflare.com/introducing-precursor/), un sistema continuo del lado del cliente para detectar incluso el tráfico de bots _sutilmente inhumano_ que puede pasar desapercibido si se evalúan solo las señales de la red. Cuando un cliente activa Precursor, la detección mediante JavaScript se integra en la CDN, así que no hace falta que te quedes delante del ordenador pensando dónde o cómo volver a ejecutar estas detecciones. Es más, Precursor evalúa el comportamiento de los usuarios de[ forma continua durante toda la sesión](https://developers.cloudflare.com/cloudflare-challenges/precursor/), así que se acabaron los "pases libres" para el tráfico abusivo que haya conseguido burlar las comprobaciones del lado del cliente y del navegador aunque solo sea una vez.

Si aplicamos nuestro marco de riesgo y confianza a estas detecciones del lado del cliente, podemos señalar que los CAPTCHA o los obstáculos puntuales se basan en el riesgo, lo que significa que carecen de _contexto_. Por otro lado, la verificación mediante indicios de comportamiento se basa en la confianza, ya que puede captar más pistas contextuales de toda la sesión del usuario. Precursor es la herramienta para que analicemos este comportamiento. En resumen, Precursor es tan eficaz porque:

  1. Proporciona detección basada en la confianza durante toda la sesión del usuario.
  2. **Aumenta el coste que supone para los desarrolladores** de bots imitar el comportamiento humano a lo largo de una secuencia de varias páginas.



El hecho de que a los desarrolladores de bots les resulte _económicamente poco rentable_ burlar estas detecciones nos permite ganar esta batalla.

Ahora bien, ¿qué hemos aprendido desde el lanzamiento? Si nos fijamos solo en un periodo de 24 horas en el momento de escribir este blog, vemos **206 millones de eventos de evaluación de Precursor** , repartidos por **73 438 zonas** de la red de Cloudflare.

Podemos ver patrones en los datos que revelan cosas que sospechábamos al lanzar la detección, pero que ahora podemos validar en miles de dominios:

  * El comportamiento sospechoso a menudo ocurre a mitad de sesión, lo cual no sería detectado por la detección puntual.
  * El **comportamiento a menudo cambia de humano a agéntico y viceversa durante una sesión**. En estos casos, es importante entender la _intención_ para que los propietarios del sitio no bloqueen flujos de usuarios que realmente desean.
    * Esto destaca la importancia de un sistema de clasificación de bots que permita a los propietarios de sitios web gestionar el tráfico según el caso de uso, el propósito y el uso de datos. Esta es precisamente la razón por la que hemos dado prioridad a las actualizaciones de la clasificación de BotBase.



Para los que tengáis curiosidad por saber más sobre cómo funciona realmente Precursor, hemos compartido un adelanto, sobre cómo las señales que analizamos nos mostraron que errar es humano, en nuestra entrada de[ blog del anuncio](https://blog.cloudflare.com/introducing-precursor/). **Hoy vamos un paso más allá. Ofrecemos a cualquier usuario de Internet una demo interactiva que simula cómo Precursor rastrearía los movimientos de tu cursor.**

**[Precursor Trace](https://precursor-trace.cloudflare.app) **ya está disponible y muestra cómo evaluaríamos los movimientos de _tu_ cursor utilizando (parte del) mecanismo de detección de Precursor. Aquí puedes ver si estás acelerando o corrigiendo tu movimiento, el ritmo y la consistencia del movimiento del cursor, y mucho más, cosas en las que probablemente nunca habías pensado como persona real que interactúa con un ordenador. ¡Pruébalo!

## **Adaptive Intelligente, disponible próximamente**

Los[ motores de detección de bots](https://developers.cloudflare.com/bots/concepts/bot-detection-engines/) de Cloudflare pueden mostrar[ resultados diferentes](https://developers.cloudflare.com/bots/concepts/bot-score/#bot-groupings) a la hora de evaluar si una solicitud determinada es automatizada o no. En el caso de las solicitudes que se consideran automatizadas, la evaluación puede ser: 1) totalmente automatizada, basada en métodos deterministas probados o huellas digitales de bots, o 2) probablemente automatizada, basada en la puntuación predictiva del Bots ML de Cloudflare.

Hasta ahora,[ Bots ML](https://developers.cloudflare.com/bots/concepts/bot-score/#machine-learning) se ha actualizado por versiones, lo que significa que anunciábamos cada nueva versión del modelo como un lanzamiento de producto. Este ritmo no funciona cuando los bots se adaptan en el transcurso de horas o incluso minutos.

Adaptive Intelligence, un motor de detección completamente nuevo, es diferente a todo lo que hemos creado antes en el ámbito de Bots ML. **El modelo en sí es adaptable**. Ha aprendido de todo lo que hemos visto en el pasado, pero lo más importante es que _seguirá_ aprendiendo y ajustándose por sí mismo en función de lo que vea. Adaptive Intelligence se actualizará automáticamente basándose en una amplia gama de patrones de tráfico que identificamos, desde comportamientos buenos hasta maliciosos, y ya no tendrás que actualizar a una nueva versión oficial del modelo para poder disfrutar de las últimas funciones de detección predictiva de bots. 

Todos los clientes de nuestra solución Bot Management tendrán acceso a Adaptive Intelligence próximamente. No te pierdas al anuncio del lanzamiento que se publicará muy pronto.

## **Más allá del determinismo: cómo guiar el comportamiento de los bots**

Hasta ahora, nos hemos centrado en el lado de Cloudflare: estrategia, detección y clasificación. Todo esto permite a Cloudflare proporcionar a los propietarios de sitios web las herramientas que necesitan para establecer las políticas de tráfico que deseen en sus sitios. Centrándonos en el lado de los propietarios de sitios web, queremos aprovechar esta oportunidad para hablar de algunas medidas de **mitigación avanzadas** que permiten a los propios propietarios influir en el comportamiento de los bots.

Con técnicas de mitigación más evidentes, nos enfrentamos a algo que hemos apodado el "problema de los antibióticos para bots". Enviar siempre a los bots una respuesta determinista (como un bloqueo 403) facilita que un bot malicioso creado por un desarrollador sondee, observe y realice ingeniería inversa de tu protección.

Somos conscientes de ello, por lo que estamos diseñando _medidas de mitigación específicas para limitar el tráfico de los bots_ , con enfoques diferentes para los bots malos y buenos. Podemos dividirlas en tres enfoques:

Enfoque 1: Imprevisibilidad y acciones aleatorias. Aplicar respuestas aleatorias (entre bloquear, desafiar o permitir) al tráfico automatizado sospechoso rompe la lógica de reintentos automáticos y la identificación de huellas digitales del bot.

Enfoque 2:[ AI Labyrinth](https://developers.cloudflare.com/bots/additional-configurations/ai-labyrinth/), una respuesta defensiva que atrae a los bots no autorizados a un laberinto sin fin de páginas web generadas por IA. Puedes agotar los recursos de procesamiento y los presupuestos de rastreo de los bots maliciosos utilizando la _distracción_. Los propietarios de sitios tendrán tres opciones dentro de AI Labyrinth, según su preferencia:

  * **Maze** : genera una red interminable de páginas vinculadas para que los bot las sigan.
  * **Summary** : les das a los rastreadores un resumen de una página generado por un modelo de lenguaje de gran tamaño que parece real, pero que es totalmente inútil como datos de entrenamiento de la IA.
  * **Poison** : le sirve contenido deliberadamente falso (como precios o existencias falsos) a un bot, contaminando así los datos que recopila para el entrenamiento de la IA.



Enfoque 3: Poner en cola a los bots buenos. No todo el tráfico generado por agentes es malo. Las colas gestionan el rendimiento del tráfico automatizado legítimo (como los agentes de compras dirigidos por los usuarios) sin denegarles el servicio por completo.

Estas medidas de mitigación avanzadas y específicas para bots se pondrán en marcha hacia finales de año, y los propietarios de las páginas web podrán elegir el nivel de rigor que quieran aplicar.

También sabemos que una buena defensa es aquella que se basa en la predicción: una que aprende por sí misma y se corrige sobre la marcha sin necesidad de que varios expertos en seguridad tengan que reunirse para aplicar una solución de forma reactiva que tenga en cuenta el último ataque invisible. Esto podría parecerse a tener un sistema de reglas "desechables", en el que el conjunto de reglas es de naturaleza dinámica. Esto es por diseño. Si los ataques evolucionan constantemente, las defensas también deberían hacerlo. Por eso estamos trabajando para que tanto las detecciones como las medidas de mitigación vayan siempre un paso por delante.

## **Crea el ecosistema de confianza que mejor se adapte a ti**

Cualquiera puede tomar medidas para definir cómo los agentes automatizados interactúan con su infraestructura. 

Algunas cosas que puedes probar:

  * Activa[ Precursor](https://developers.cloudflare.com/cloudflare-challenges/precursor/#get-started)
  * Prueba[ Precursor Trace](https://integrityand.trust.cfdata.org/precursor-trace/)
  * Descubre[ BotBase](https://developers.cloudflare.com/bots/botbase/)



En lugar de hacer revisiones aisladas, evaluamos la confianza en tiempo real. Así tomamos la delantera frente a los ataques de bots. Si aún no estás utilizando la[ detección de bots de Cloudflare](https://www.cloudflare.com/products/bot-mitigation/), echa un vistazo y crea el ecosistema de confianza que funcione para ti.

]]>01KZTB4T78YHVYCSWHPW1XFGTCDesarrollar una Internet agéntica abierta: legible, detectable, invocable y pagaderahttps://blog.cloudflare.com/es-es/the-agentic-internet/ Mon, 10 Aug 2026 09:48:29 GMTLos agentes son un nuevo tipo de visitante. No renderizan CSS ni hacen clic en anuncios, pero hay una persona que paga en el otro extremo. Si los bloqueas, bloqueas a tu cliente. Estamos desarrollando los protocolos y herramientas abiertos que permitan la cooperación entre editores y agentes para que no haya conflictos entre ellos.AgentesAgents WeekAIDesarrolladoresMCPPlataforma para desarrolladoresNuestros datos muestran que mucho tráfico de bots con un comportamiento adecuado corresponde a [​consultar de nuevo páginas que no han cambiado](https://blog.cloudflare.com/making-ai-search-smarter/). Miles de millones de solicitudes. Esto supone una gran carga de trabajo para las máquinas, y no aporta ningún beneficio. Esa es la característica de una web desarrollada para los usuarios humanos que recibe otros visitantes.

Los agentes ya están aquí, no como un nuevo tipo de software, sino como un nuevo tipo de visitante en la web.

La web rediseñada en torno a este nuevo visitante es lo que llamamos la Internet agéntica. De cara al futuro, la vemos legible, detectable, invocable y pagadera. Para hacer realidad ese futuro, necesita sus propios protocolos y herramientas.

La plataforma para desarrolladores de Cloudflare proporcionó a los agentes un lugar para su ejecución y las primeras herramientas para desarrollarlos. Lo que falta son herramientas que faciliten la cooperación entre los agentes y los propietarios de los dominios para que no haya conflictos entre ellos, en la Internet abierta, no solo dentro de una única plataforma.

Cada navegador siempre se ha identificado en la web con un encabezado User-Agent. El nombre solo cobraba sentido cuando eras consciente de que el navegador actuaba en tu nombre. Ahora un agente de usuario es verdaderamente el agente de un usuario: un programa que busca en la web en nombre de una persona. Hoy en día, en su forma más madura es el agente de codificación que lee y escribe código, obtiene los documentos que necesita y nunca visualiza las páginas que lee.

Un agente no renderiza tu CSS, visualiza tu imagen principal ni hace clic en tus anuncios. Pero tiene a una persona que paga en el otro extremo. Cada solicitud ahora le cuesta dinero a alguien y tiene un propósito. Si lo bloqueas, bloqueas a tu cliente. Si lo tratas como un bot de apropiación de contenido, lo perderás.

Cada agente se ejecuta porque alguien (una persona o una empresa) paga por lo que hace. La mayoría de las personas no gastan tokens sin más. Esta versión de Internet, una con un resultado y una factura en el otro extremo de cada solicitud, será completamente distinta de la que tenemos actualmente.

La web no se desarrolló con este fin, ni tampoco sus herramientas de análisis. Ni, en la mayoría de los casos, era tu modelo de negocio. Cómo los agentes lean, detecten, invoquen y paguen va a decidir si Internet sigue siendo una red abierta o se cierra. En una versión del futuro, un pequeño número de estructuras serían las propietarias de la detección, la identidad y los pagos, y todos los demás se enrutarían a través de ellas. En otra, Internet permanecería abierta: primitivas basadas en estándares que cualquiera podría implementar, que se ejecutarían sobre bases que serían neutras porque el código sería público.

Cloudflare cree en la Internet abierta, y estamos en disposición de ayudar a construir el futuro donde prospere.

Las especificaciones en las que nos basamos son estándares abiertos que cualquiera puede implementar: x402, MCP, Web Bot Auth, PACT. Los propietarios de dominios eligen sus propios proveedores de identidad, sus propios procesadores de pago, sus propios socios de agentes. Cloudflare es una opción, no toda la pila. Somos el Cliente Cero de las mismas bases que utilizan nuestros clientes, sin una ruta privilegiada ni una API de acceso anticipado a la que solo nosotros podamos acceder. Hemos estado realizando este trabajo durante quince años para la web para las personas, y ahora es lo que pretendemos hacer para la Internet agéntica.

La ingeniería no es un aspecto de la Internet agéntica en el que las personas se vayan a fijar. Están adoptando un nuevo medio y lo evaluarán de la misma manera que evaluaron la web: en función de si es mejor, de si encontrar y reservar una mesa requiere un intercambio y no nueve, de si saben con quién están tratando o de si el pago parece seguro.

## **Nuestra filosofía: una Internet agéntica que sea legible, detectable, invocable y pagadera**

Para ello, empezamos con la identidad.[ Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/) permite que un bot se identifique criptográficamente en cualquier sitio que visite, para que los editores puedan decidir a quiénes permiten el acceso y a quiénes no. Se acabaron las suposiciones y las suplantaciones de agentes de usuario. Muchos sitios ya identifican quién es la persona que envía una solicitud a partir del inicio de sesión, el comportamiento en la aplicación o el historial de compras. Ese sitio puede emitir [​tokens de control de acceso privado](https://cloudflare.net/news/news-details/2026/Cloudflare-Collaborates-With-Leading-Browsers-to-Develop-a-Privacy-First-Protocol-For-the-Global-Internet/default.aspx) (PACT). PACT, anunciado con Mozilla, Google, Microsoft y Shopify, permite a los sitios la acreditación anónima, para que el agente pueda presentar el token en otro lugar. Los agentes legítimos acceden con menos obstáculos.

De esta forma, podemos facilitar a un agente su trabajo. [​Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) permite a los agentes leer sitios web con menos tokens y menos ancho de banda.[ WebMCP](https://blog.cloudflare.com/webmcp/) les proporciona una forma nativa de interactuar en tu nombre. Y protocolos como [​x402](https://x402.org/) les permiten pagar a los comerciantes directamente.

"**Legible** " está claro. ¿Pueden los agentes de IA leer el contenido de una manera que les resulte natural y que refuerce sus capacidades? Cuanto menos ancho de banda y menos tokens consuma un agente, mejor. Cada renderización de una etiqueta HTML para una persona que nunca la consulta no solo desperdicia recursos informáticos, sino que también contamina la ventana de contexto que el agente luego debe pagar para ser ignorada. [​Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) resuelve esta dificultad desde el lado del servidor.

En el lado del cliente, abordamos el desarrollo de un navegador teniendo en cuenta a los agentes como ciudadanos de primera categoría. Nuestro nuevo navegador es [ Kitesurf](http://blog.cloudflare.com/kitesurf), un navegador lo suficientemente ligero como para ejecutarse en Workers, que se inicia para cada solicitud y se elimina a continuación. Ofrece contenido y funciones que los agentes necesitan, sin ninguna de las características innecesarias de los navegadores tradicionales orientadas a los usuarios humanos.

"**Detectable** " indica dónde comienza cada momento económico en la Internet agéntica. Para que un agente pueda leer un recurso, invocar una herramienta o pagar una transacción, primero tiene que saber que el recurso está allí. La búsqueda es solo la mitad de la historia, ya que los agentes necesitan encontrar lo que necesitan a través de interfaces diseñadas para ellos, no mediante un recuadro de búsqueda por palabras clave diseñado para una persona que escribe lentamente y navega por él. [​AI Search](https://developers.cloudflare.com/ai-search/) ya está disponible para que cualquier sitio público sea consultable por agentes.

La otra mitad es ser detectado. Los creadores de contenido y los propietarios de API necesitan saber hasta qué punto los agentes los pueden ver. [ Agent Engine Optimization (AEO)](http://blog.cloudflare.com/aeo) cuantifica la visibilidad de la marca en todos los modelos y agentes que importan. Si no puedes cuantificar tu visibilidad para los agentes que utilizan tus clientes, en la práctica no existes para ellos. 

"**Invocable** " indica dónde los agentes comienzan a llevar a cabo alguna tarea: reservar una mesa, renovar una suscripción, generar un informe. En la web para usuarios humanos, todas estas tareas adoptan otro aspecto, porque se crearon para personas que interactúan mediante clics a través de interfaces de usuario. Un agente que intenta añadir un elemento a una lista de tareas tiene que analizar el código HTML, adivinar qué botón es “Añadir”, sintetizar un clic y esperar que el modelo de objeto de documento (DOM) no haya cambiado desde la última vez que lo consultó.

[WebMCP](https://blog.cloudflare.com/webmcp/) permite que un sitio exponga sus acciones directamente a los agentes a través del navegador:

La herramienta “contrato” ahora es explícita. Sin análisis de HTML, sin tener que hacer suposiciones en los campos de formulario. A medida que las herramientas se ejecutan dentro de la página, reutilizan la sesión y el estado existentes del usuario. [​Code Mode](https://blog.cloudflare.com/code-mode/) va un paso más allá. Los agentes piensan en términos de código, e invocar las herramientas escribiendo código es más rápido y preciso que en prosa. Puesto que los agentes invocan puntos finales en lugar de rastrear páginas web, el propietario del contenido tiene una señal clara de qué contenido realmente se utiliza. 

"**Pagadera** " indica hacia dónde creemos que avanza la Internet agéntica. Toda transacción económica eventualmente necesita una forma de pago. Los modelos basados en anuncios están dejando de ser útiles. Los modelos basados en el número de usuarios no funcionan cuando el usuario es un programa. Los editores de los que todos dependemos no pueden financiarse con visitas a la página que nunca llegan y con navegadores que no renderizan sus anuncios. 

Un sitio de recetas que nunca resultó rentable con los anuncios puede cobrar una fracción de céntimo por cada solicitud y ser rentable gracias a la escala de la Internet agéntica. Un periódico local puede licenciar artículos en el momento de su lectura sin necesidad de un acuerdo de licencia o un inicio de sesión. En el otro extremo, el agente dispone de una cartera y un presupuesto definidos una sola vez por la persona que hay tras él. 

Cada interacción pagada deja un recibo. El editor puede demostrar qué agente consultó qué página. El agente puede demostrar que pagó por lo que utilizó.[ Wallets](https://blog.cloudflare.com/wallets/) permite a los agentes pagar fácilmente por los contenidos y las API. [​Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) permite a los propietarios de dominios configurar los pagos de los agentes con solo unos clics.

Cloudflare se sitúa en medio de todo esto por diseño. Ya nos situamos entre miles de millones de personas y los sitios que visitan, protegiéndolos, acelerándolos y manteniéndolos en línea. Los agentes modifican el tráfico, pero no la forma de ese trabajo. Somos la capa neutra y eficaz en la que pueden confiar los editores, comerciantes, creadores de agentes y usuarios finales para estar de su lado, sin competir con ellos. 

Queremos proporcionar a los propietarios de dominios las herramientas que necesitan para facilitar la tarea a los tipos de agentes de IA que quieren admitir y para [​bloquear los que no desean](https://blog.cloudflare.com/cloudflare-ai-audit-control-ai-content-crawlers/). Probablemente sea recomendable que una herramienta para desarrolladores esté[ preparada para los agentes](http://blog.cloudflare.com/aeo) a fin de incentivar a los agentes de IA a detectarla, recomendarla y pagarla. Un editor puede querer bloquear el acceso a los agentes de IA extractivos (aquellos que consumen recursos sin ofrecer nada a cambio) pero permitirlo a los agentes de IA que licencien su contenido o de los que reciban una compensación. Un proveedor de datos sin ánimo de lucro puede querer bloquear el acceso a los bots o a los usuarios humanos que superan sus límites de velocidad, pero permitirles pagar por la cancelación de su bloqueo y por la utilización de esos fondos para cubrir el consumo excesivo de recursos.

## **Los bots han muerto, larga vida a los bots**

La distinción entre un [​bot y un humano ya no es tan sencilla](https://blog.cloudflare.com/past-bots-and-humans/). No es tan simple como afirmar que los bots son malos y los humanos buenos, o que los bots desperdician recursos que deberían consumir los humanos. Esta forma de pensar tradicional ha quedado obsoleta en el mundo de los agentes.

Consideramos a los agentes como un nuevo tipo de actor. Sus acciones pueden ser deseables, por ejemplo, leer contenido de una manera que preserve los recursos, interactuar con sitios web en la forma indicada por los propietarios del dominio y pagar por lo que utilizan. O bien, por el contrario, pueden no ser deseables, como rastrear millones de páginas sin ninguna compensación, intentar eludir bloqueos o ignorar [​robots.txt](https://www.cloudflare.com/learning/bots/what-is-robots-txt/). Estamos convencidos de que muchas de las acciones no deseables disminuirán e incluso se convertirán en acciones deseables, siempre y cuando las personas y los bots cuenten con las herramientas adecuadas.

## **Salvar la diferencia en términos de ingresos**

Durante años, Cloudflare se ha dedicado a la detección de bots, para que los propietarios de dominios pueden controlar si les permiten o bloquean el acceso a sus sitios. Lo que ha faltado hasta ahora es la otra mitad: cómo interactúan los agentes con esos sitios una vez que han accedido a ellos. Ese es el objetivo de este conjunto de herramientas agénticas: lograr que la web sea legible, detectable, invocable y pagadera. Estas cuatro primitivas se han desarrollado sobre estándares abiertos, por lo que las bases no son propiedad de ninguna empresa. 

Una Internet agéntica abierta necesita diversidad en ambos extremos. No solo diversidad de editores y creadores de contenido, sino también de agentes. Si el lado de la demanda converge, no importará lo abierto que sea el lado de la oferta. Internet seguirá siendo un ecosistema limitado.

Estamos desarrollando esta alternativa abierta. Únete a nosotros haciendo que tu sitio esté [​preparado para los agentes con nuestro nuevo panel de control](http://blog.cloudflare.com/aeo), y regístrate para recibir noticias sobre nuestro producto para la optimización de los motores de respuesta (Answer Engine Optimization). Si gestionas un sitio o un agente, puedes experimentar con todas las nuevas tecnologías de Internet usando nuestro[ AI Playground](https://playground.ai.cloudflare.com/).

]]>01KZNH2P72TQRQTTABG76X45ZXAdiós a los rankings: adapta tu web a la nueva era de los agentes de IAhttps://blog.cloudflare.com/es-es/aeo/ Mon, 10 Aug 2026 09:17:14 GMTActualmente, más de la mitad de las solicitudes vienen de máquinas, no de personas. La herramienta Agent Readiness (preparación de los agentes) muestra en qué medida los agentes pueden encontrar y leer tu web, mientras que la herramienta de optimización de motores de respuesta (AEO) mide con qué frecuencia te recomiendan los asistentes de IA.AEOAgentesAgents WeekAIDashboardMCPNoticias de productosPreparación para agentesRadarPuede que tu próximo cliente no te encuentre a través de un buscador. En cambio, le preguntará a un asistente de IA: "¿Cómo hago X?", "¿Qué opción es la mejor para alguien como yo?", "Ocúpate tú de ello por mí", y un agente buscará la respuesta, valorará las opciones y actuará en su nombre. Cada vez más, el momento que determina si un cliente te elige tiene lugar en la respuesta de un modelo, antes incluso de que una persona llegue a ver tu página de inicio.

Los usuarios agénticos ya están aquí. Según nuestros cálculos, menos de la mitad de todas las solicitudes de páginas HTML[ provienen ahora de un humano](https://radar.cloudflare.com/traffic#bot-vs-human). No todas esas máquinas son agentes que actúan en nombre de una persona, pero el porcentaje está creciendo rápidamente, y los motores de respuestas, los asistentes de compras y las herramientas de búsqueda determinarán qué empresas se encuentran y se recomiendan. Antes, la visibilidad se reducía a aparecer en los resultados de búsqueda. Ahora significa que los agentes que guían a tus clientes te encuentren, te lean y te recomienden con confianza.

Las métricas antiguas, como los clics de los usuarios y las visitas a la página, ya no reflejan la situación completa. Pasamos un rato hablando con propietarios de sitios web que se pasaban el día mirando los registros de acceso, llenos de bots de IA, sin tener ni idea de si esos bots eran capaces de usar su sitio web o de recomendar sus productos y servicios a sus usuarios. Nos plantearon dos preguntas principales:

  * ¿Los agentes pueden usar de verdad mi sitio web?
  * ¿Me están recomendando?



Para ayudar a los propietarios de sitios a responder estas preguntas, hemos integrado nuestro[ trabajo previo sobre Agent Readiness](https://blog.cloudflare.com/agent-readiness/) en el panel de control de Cloudflare, y también hemos añadido nuestra nueva herramienta AEO. Estas herramientas consideran a los agentes como el núcleo de los usuarios de tu sitio web, mostrándote cómo lo ven ellos y con qué frecuencia te recomiendan.

La oportunidad es enorme y el listón está bajo, porque la mayoría de los sitios web aún no están pensados para este tipo de usuarios. Al igual que en los inicios del SEO se premiaba a los sitios web diseñados para los motores de búsqueda, ahora se premiará a los sitios diseñados para los agentes. Los que sean fáciles de encontrar, de leer y en los que se pueda confiar son los que los agentes recomendarán.

## **Diagnostics: ¿está tu sitio web preparado para los agentes?**

Diagnostics es la revisión técnica que se realiza dentro de la herramienta Agent Readiness. Analiza tu sitio web tal y como lo lee un agente: comprueba si tiene permiso para acceder y si puede detectar tu contenido, obtiene una copia limpia legible por máquina y localiza las interfaces a las que puede acceder. 

Mientras que una persona simplemente carga tu página de inicio, un agente se basa en tu archivo robots.txt, tu mapa del sitio, tus encabezados de respuesta, una versión en Markdown de tu contenido y los metadatos publicados para la autenticación y las herramientas.

Esta herramienta realiza esas comprobaciones con un nombre de host y agrupa los resultados en una única vista del estado de preparación del agente, desde "No está listo" hasta que el agente funciona de forma totalmente nativa. Cada comprobación da como resultado "aprobado", "suspenso" o "neutral", con una nota que explica por qué es importante y un historial que muestra exactamente la solicitud y la respuesta que hemos visto.

Las comprobaciones están agrupadas por tipo de tarea, para que sepas por dónde empezar:

  * Resultados rápidos: los aspectos básicos de gran impacto que faltan en la mayoría de los sitios web, como un archivo robots.txt legible para los rastreadores, un mapa del sitio XML, reglas para rastreadores de IA y el envío de código Markdown limpio a los agentes
  * Bases técnicas: el siguiente nivel, que incluye "Señales de contenido" que indican cómo se puede usar tu contenido, un catálogo de API, encabezados de enlaces e instrucciones de inicio de sesión para agentes
  * Integración avanzada: las funciones nativas para agentes, como el descubrimiento de OAuth, las tarjetas de agente MCP (Protocolo de contexto de modelo) y A2A (Agent2Agent), un índice de habilidades, Web Bot Auth y WebMCP
  * Comercio: los estándares emergentes de pago para agentes, entre los que se incluyen[ x402](https://blog.cloudflare.com/x402/) (una extensión del clásico código de estado HTTP 402 "Pago requerido"), ACP (Protocolo de comercio para agentes), el Protocolo de comercio universal (UCP) y AP2 (Protocolo de pagos para agentes). Por ahora, esto es solo a título informativo y no cuenta para tu puntuación.



Cada mejora sugerida viene acompañada de un siguiente paso. Cuando hay una función de Cloudflare que puede ayudarte, aparece un enlace "Configurar en Cloudflare" que te lleva directamente a la configuración, como activar Markdown para agentes o el archivo robots.txt gestionado. Para todo lo demás, hay un botón de "Copiar las instrucciones del agente" que propone lo que tu agente de codificación necesita crear. Haz el cambio, vuelve a escanear y observa cómo la marca de verificación se vuelve verde.

## **¿Los asistentes de IA te están recomendando?**

Diagnostics te indica si los agentes pueden leer tu sitio web. La pestaña "AEO" te explica qué pasa después: cuando un cliente le hace una pregunta a un asistente de IA sobre tu categoría, ¿te recomienda a ti o a un competidor? No puedes consultar esto como si fuera un _ranking_ de búsqueda. No hay recuento de impresiones ni informe de clics perdidos, así que cuando mencionan a un competidor en lugar de a ti, la venta se ha perdido y no hay nada que te avise de que ha pasado.

Deducimos tu sector (p. ej., salud y fitness) y tu categoría (p. ej., ropa deportiva) a partir de tu web, y probamos los asistentes más importantes (ahora mismo, Claude de Anthropic y GPT de OpenAI) con preguntas típicas de los clientes para ver cómo responden. Estructuramos estas instrucciones para que imiten el proceso de visibilidad del mundo real, pidiendo recomendaciones, comparativas de productos y consejos generales dentro de tu categoría. Cuando observas cómo responden los modelos a estas consultas realistas, obtienes métricas como:

  * **Tasa de aparición:** el porcentaje de respuestas de tu categoría que citan tu sitio web como fuente
  * **Prominencia:** cuando te citan, qué parte de la respuesta es realmente tuya y en qué momento aparece
  * **Tasa de mención:** la frecuencia con la que los asistentes mencionan tu marca en su respuesta; por ejemplo, cuántas veces aparece "Cloudflare" en la respuesta, independientemente de si se cita o no[ cloudflare.com](http://cloudflare.com) como fuente. Si lo analizas junto con tu índice de citación, distingue entre notoriedad y atribución: que los asistentes te mencionen mucho más de lo que te citan significa que estás en su radar, pero que aún no te estás ganando la citación, una carencia específica que puedes abordar.
  * **Cuota de visibilidad:** porcentaje de aparición en comparación con el de tus competidores, para que puedas ver quién está ganando en las preguntas en las que tú estás perdiendo



Para evaluar cómo percibe un modelo de IA tu presencia en el mercado, establecemos un punto de referencia para cada sector y categoría antes de puntuar una web concreta. Hacemos preguntas a los asistentes de IA con frases que podrían encajar en esa categoría, sin mencionar tu marca, y anotamos qué sitios web se mencionan, dónde aparecen y qué protagonismo tienen.

En lugar de volver a consultar los modelos cada vez que el propietario de un sitio web realiza un análisis, ejecutamos este panel una vez por categoría y reutilizamos la referencia en todas las cuentas de ese dominio. Calcular previamente este conjunto de datos ofrece tres ventajas principales:

  * **Cero latencia:** los resultados se cargan inmediatamente desde una instantánea, en lugar de tener que esperar a que se procesen las consultas al modelo en tiempo real.
  * **Menor carga informática:** al agrupar las consultas por categorías, se evitan llamadas redundantes a la IA en miles de análisis.
  * **Puntuación de ajuste de la industria:** la reutilización del corpus del panel nos permite identificar qué marcas aparecen juntas de forma constante, lo que nos permite obtener una puntuación de ajuste de la industria que mide si un asistente de IA ve tu sitio web junto con los de tus competidores reales.



Los asistentes de IA rara vez responden la misma pregunta de la misma manera dos veces. Para tener en cuenta esta variación, utilizamos[ Cloudflare AI Gateway](https://www.cloudflare.com/products/ai-gateway/) para enviar la instrucción a cada asistente varias veces utilizando diferentes modelos. A continuación, leemos las respuestas que vería un cliente, el texto de la respuesta junto con las fuentes que cada asistente ha citado, y extraemos varias señales de ellas. 

No solo evaluamos si se ha mencionado tu sitio web, sino también si te han citado como fuente, en qué momento de la respuesta aparecen tus citas y qué parte del contenido de la respuesta final se te atribuye. Cuando se requiere un juicio genuino, Workers AI se encarga del trabajo pesado, ejecutándose de forma nativa en nuestra propia infraestructura para leer cada respuesta y puntuar cómo aparecen tus citas y menciones. Además, utilizamos un análisis de texto exacto en lugar de un modelo que califique su propio resultado. Todo esto permite convertir docenas de respuestas puntuales en métricas útiles. Gracias a la abstracción del proceso de consulta y evaluación multimodelo, la herramienta te ofrece métricas sin que tengas que crear tu propio marco de evaluación.

Junto con las respuestas, la actividad de los operadores de IA muestra el tráfico real de rastreo y de referencia en tu sitio web, por operador (OpenAI, Google, etc.): quién lee tu contenido, quién te envía visitas y los errores con los que se topan por el camino (403 bloqueado, 404 enlace no válido). El patrón sobre el que vale la pena actuar es el del operador que rastrea miles de tus páginas pero no te envía a nadie, es decir, el que usa tu trabajo sin devolverte clientes.

Como estas cifras son específicas de tu sitio web, puedes experimentar, volver a ejecutar el análisis y medir el impacto en las preguntas concretas que te generan negocio.

## **Conecta con otra audiencia**

Hasta ahora, evaluar a los agentes era una cuestión de conjeturas: buscar en tus registros para deducir quién te visitaba, o introducir una pregunta en un chatbot y fijarte a ojo si te mencionaba. Pero con las herramientas Agent Readiness y AEO, puedes obtener los datos que necesitas para actuar. Y como las solicitudes pasan realmente por Cloudflare, estas herramientas miden en lugar de estimar siempre que sea posible, y mejorarán con el tiempo. 

Ayudarte a ver quién llega a tu sitio web y a decidir cómo interactuar según tus propios términos es lo que siempre hemos hecho. Los agentes son simplemente el público más reciente, y las empresas que se hacen accesibles para que los agentes las encuentren, las entiendan y confíen en ellas son las que acaban siendo recomendadas. En la herramienta Agent Readiness es donde descubrirás si eres una de ellas y qué hacer si aún no lo eres.

¿Estás listo para descubrir si los agentes de IA te están enviando clientes? Ve a la pestaña "Información general" de tu panel de control para preparar tu sitio web para los agentes y solicitar acceso anticipado a AEO Visibility.

_¿Estás desarrollando en una web abierta y accesible para los agentes? Abre la pestaña**"Agent Readiness"** en tu[ panel de Cloudflare](https://dash.cloudflare.com) y cuéntanos qué estás desarrollando en el[ Cloudflare Developer Discord](https://discord.cloudflare.com)._

]]>01KZNF60EE7QRSKM2VM317XCA6Cómo detectar comportamientos anómalos de la IA con análisis basados en la identidadhttps://blog.cloudflare.com/es-es/identity-aware-ai-gateway/ Mon, 10 Aug 2026 09:12:11 GMTAI Gateway con reconocimiento de identidad ya está disponible en versión beta abierta. User Insights convierte ese tráfico en una línea base de comportamiento para cada persona y agente, y detecta el riesgo interno tan pronto como aparece.AgentesAgents WeekAIAI Gateway (ES)DesarrolladoresNoticias de productosPlataforma para desarrolladoresCuando revisas tu factura de IA, puede ser difícil identificar si contiene alguna irregularidad. En primer lugar, necesitas una línea base que te permita ver qué ha cambiado, ya sea un agente que se ha descontrolado o un empleado cuyo uso se ha multiplicado por diez. Ser capaz de detectar esos cambios te permite comenzar a investigar y, hasta ahora, detectar estás anomalías no ha sido fácil.

Saber quién está haciendo qué con la IA es uno de los principales desafíos que las organizaciones afrontan hoy en día. [Un informe](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) de la Universidad de Stanford concluyó que el 59 % de las organizaciones declararon que la falta de conocimientos era su mayor obstáculo para una gobernanza responsable de la IA. 

Se trata de un problema tanto de seguridad como financiero. Para resolver estas dificultades, necesitamos dos cosas: una identidad verificada en cada solicitud (para que cada incremento esté vinculado a un nombre) y una perspectiva de lo que se considera normal para esa identidad. Hoy anunciamos ambas prestaciones.

AI Gateway, con reconocimiento de la identidad, ya está disponible en la versión beta abierta, junto con Cloudflare Access, y User Insights está disponible de forma general para todos los clientes de AI Gateway sin coste adicional. Juntos convierten el tráfico que ya fluye a través de AI Gateway en una línea base de comportamiento para cada persona y agente que lo utiliza, e identifican a los que se apartan de ella.

## ¿Qué es AI Gateway?

[AI Gateway](https://developers.cloudflare.com/ai-gateway/) es el plano de control central para todo tu uso de IA. En lugar de que cada aplicación y cada equipo llamen directamente a modelos en OpenAI, Anthropic, Google o Workers AI, las solicitudes se enrutan primero a través de AI Gateway, que proporciona un único lugar donde observar, proteger y gobernar tu uso de la lA.

Funciona con las aplicaciones que creas y con las herramientas de codificación en las que tus desarrolladores ya trabajan. Redirige [arneses de agentes](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/) como Claude Code, Codex y GitHub Copilot a través de AI Gateway, y están sujetos a la misma visibilidad y los mismos controles que todo lo demás.

## AI Gateway con reconocimiento de identidad

Con la integración de AI Gateway y[ Cloudflare Access](https://developers.cloudflare.com/ai-gateway/configuration/cloudflare-access), puedes poner un[ dominio personalizado](https://developers.cloudflare.com/ai-gateway/configuration/custom-domains/) frente a tu puerta de enlace y protegerlo con Access, al igual que con cualquier otra aplicación. Eso significa que puedes:

  * Autenticar las solicitudes con cualquier proveedor de identidad compatible con SAML, como Okta o Entra, eliminando la necesidad de generar y compartir claves API de Cloudflare.
  * Establecer políticas que definan exactamente quién puede acceder a tu puerta de enlace.
  * Enviar solicitudes a un nombre de host limpio como `ai.example.com` sin ningún ID de cuenta o ID de puerta de enlace en la URL.



Cada solicitud autenticada ahora incluye la identidad del usuario de Access. AI Gateway añade el ID de usuario de Access verificado a los metadatos de la solicitud como `cf.user_id`, para que puedas filtrar los registros, análisis y gastos en función de la persona que realmente ha enviado la solicitud.

Junto con los [ límites de gasto](https://developers.cloudflare.com/ai-gateway/features/spend-limits/), esa identidad se convierte en una herramienta presupuestaria. Dado que ahora cada solicitud incluye un usuario real, puedes establecer límites de gasto por usuario: proporciona a cada usuario su propia partida presupuestaria, y bloquea las solicitudes adicionales o cambia a un modelo más económico cuando alcance ese límite. Di adiós a las facturas sorpresa y al uso de claves API compartidas que ocultan quién ha gastado qué.

Uno de nuestros primeros usuarios, Flexport, se encontró exactamente con este problema.

"Las claves API compartidas hacen que sea prácticamente imposible saber quién está utilizando un servicio de IA o implementar las reglas de acceso que ya aplicamos para los empleados", indica Max Baumgarten, ingeniero de seguridad en Flexport. "La implementación de Cloudflare Access delante de AI Gateway dota a cada solicitud de una identidad autenticada y nos permite utilizar nuestras políticas de identidad existentes en la puerta de enlace. Nuestros equipos pueden adoptar herramientas de IA sin necesidad de crear un sistema de autenticación individual para cada cliente".

En el futuro cercano, podrás utilizar los grupos del proveedor de identidad de tus usuarios para establecer límites de gasto o controlar a qué modelos puede acceder un grupo. Por ejemplo, proporciona a tu equipo de aprendizaje automático acceso a modelos de vanguardia, limita el gasto de tu equipo de soporte o define el alcance del presupuesto para todos aquellos que trabajan en un proyecto específico, todo correlacionado con los grupos que ya gestionas en tu proveedor de identidad.

## La nueva pestaña User Insights

Dentro de AI Gateway ahora verás una pestaña User Insights. User Insights analiza el tráfico que pasa a través de tu puerta de enlace y lo convierte en una representación del comportamiento de cada cuenta. Aprende cómo actúa normalmente cada cuenta, identifica aquellas que se desvían de ese patrón y te proporciona el contexto para diferenciar entre un agente descontrolado y un ingeniero que tiene mucho trabajo. Funciona con el tráfico que ya pasa a través de tu puerta de enlace, por lo que no requiere ninguna configuración.

User Insights realiza un seguimiento de los costes, e identifica dónde son excesivos, como las tasas de aciertos de caché bajas y las ventanas de contexto sobredimensionadas. Muchas herramientas ya hacen eso. Lo que no hacen es decirte si una cuenta se comporta con normalidad. Eso es lo que hemos decidido priorizar, junto con los controles de costes. 

### Definir una línea base para cada cuenta: personas y agentes

Con el tiempo, cada cuenta, ya sea una persona o un agente, deja huellas de su comportamiento. Un agente que resume los tickets cada tres horas es meticuloso y coherente. Una persona es más desordenada, con distintas instrucciones, tiempos irregulares y sesiones largas sobre problemas complejos. Ambos son legítimos, por lo que la misma desviación puede ser ruido en un caso y una señal real en el otro.

En User Insights, comenzamos puntuando las sesiones, no las solicitudes individuales. Los umbrales absolutos aquí no funcionan: un incremento de 500 dólares de un usuario habitual podría ser normal, mientras que una sesión de 50 dólares de un agente cuyo gasto habitual es de 5 dólares es un cambio que multiplica por 10 el coste y que podría pasar desapercibido. Por lo tanto, comparamos cada sesión con el historial de la cuenta, utilizando el percentil 95 del coste de la sesión durante los últimos 30 días. Eso nos permite entender cómo opera normalmente la cuenta, y cualquier cosa que duplique su percentil 95 es un firme candidato de comportamiento anómalo.

El siguiente análisis resume cómo llegamos a estas cifras.

Figura 1: Detección de anomalías en el coste de la sesión

**Cómo leer el gráfico anterior**

El gráfico representa sesiones reales de nuestro propio tráfico interno. Cada punto es una sesión individual (representada en escalas logarítmicas):

  * **Eje X (coste de la sesión):** coste total en dólares.
  * **Eje Y (percentil 95 del usuario x):** número de veces que la sesión ha superado la línea base personal del usuario.



Las dos líneas de umbral discontinuas dividen las sesiones en cuatro categorías:

  * **Superior derecha (★ Estrellas):** supera tanto el doble de la línea base del percentil 95 del usuario como el límite superior del percentil 99 a nivel de cuenta. Son incrementos relativos altos que representan un coste inusual significativo y activarán una alerta. 
  * **Superior izquierda:** incremento relativo alto (el doble del percentil 95 del usuario), pero por debajo del límite inferior del percentil 99 de la cuenta. Lo ignoramos para evitar la emisión de alertas relacionadas con cambios de importes pequeños.
  * **Inferior derecha:** gasto absoluto alto, pero coherente con el uso normalmente alto de este usuario. Esto también se ignora como un comportamiento habitual.
  * **Inferior izquierda:** actividad normal dentro de ambas líneas base.



Figura 2: Distribución del coste de las sesiones a nivel de cuenta

Este histograma (Figura 2) representa el coste de cada sesión en toda la organización para establecer un límite superior general de la cuenta:

  * Uso típico: la gran mayoría de las sesiones cuestan mucho menos de 10 dólares, con un percentil 95 de 20 dólares.
  * Percentil 99 de la cuenta (200 USD): solo el 1 % de todas las sesiones en toda la empresa alcanza o supera los 200 dólares.



¿Entonces por qué elegimos el percentil 99? Establecer nuestro límite superior absoluto en dólares en el percentil 99 de la cuenta crea un punto de referencia significativo. Garantiza que una anomalía no sea solo un cambio repentino correspondiente a un usuario específico, sino que también figure en el 1 % de las sesiones más costosas de toda la organización.

Figura 3: Historial de sesiones de un usuario individual

Las líneas base no son estáticas. A medida que cambian los hábitos de una cuenta, su percentil 95 móvil (línea verde) y el umbral duplicado (línea naranja) se ajustan en consonancia, de modo que una alerta siempre refleja el comportamiento reciente en lugar de un número establecido una sola vez. También aplicamos un límite inferior en dólares para que un incremento tenga que ser tanto estadísticamente inusual como merecedor del tiempo de investigación de un administrador. Ese límite inferior en dólares es lo que evita que se active una alerta en caso de una irregularidad de un microusuario que multiplique por 500 los costes pero que apenas suponga unos centavos.

### La perspectiva adecuada para la detección de comportamientos anómalos 

Después de todo el análisis anterior, lo que ven los administradores es una vista de las cuentas que han roto su propio patrón, en la que se ha excluido todo lo que se considera normal. Esa vista filtrada es una fuente de información sobre los comportamientos anómalos.

Este comportamiento es difícil de detectar porque la señal nunca es una nueva herramienta ni una acción bloqueada. Es una cuenta de confianza que está haciendo más de lo que ya tiene permitido hacer. Podría ser una cuenta de servicio que de repente comienza a ejecutar sesiones más costosas, o una persona cuyo uso aumenta mucho más allá de lo que es normal en su caso y que mantiene así durante días.

Ninguno de estos comportamientos infringe ninguna política, pero todos ellos se alejan de una línea base de comportamiento. Una salida repentina del propio uso de una cuenta es a menudo la primera señal observable de una credencial comprometida o de un agente descontrolado.

User Insights no decide la intención ni bloquea cuentas; en su lugar, lleva esas pocas cuentas que han empezado a comportarse de forma extraña ante un administrador para que alguien pueda plantearse la siguiente pregunta. A veces eso lleva a una verdadera investigación. Otras veces simplemente significa que alguien necesita cierta orientación (como el desarrollador que vuelca todo el código en cada instrucción cuando un fragmento sería suficiente). 

## ¿Y ahora qué? 

### Te ayudaremos a pasar del control de costes a la optimización de costes

Cuando ya has definido un presupuesto, la siguiente pregunta lógica que debes plantearte es: ¿cómo puedes beneficiarte de la misma calidad de resultados con menos costes? No todas las solicitudes necesitan un modelo de vanguardia. Una tarea de resumen o una simple finalización de código puede ejecutarse en un modelo más económico sin ninguna pérdida significativa de calidad.

Estamos desarrollando un enrutamiento inteligente basado en tareas, donde AI Gateway analiza la solicitud entrante y la dirige al modelo que te ofrece el mejor resultado al menor coste. A nivel de organización, podrás ver dónde puedes beneficiarte de un mayor ahorro gracias al enrutamiento a modelos más eficientes. El enrutamiento inteligente basado en tareas está en fase de desarrollo activo. Te contaremos más a medida que vaya madurando.

### Te ayudaremos a entender _cómo_ se utiliza la IA

La detección de anomalías te indica que una cuenta ha roto su patrón, pero no por qué. Un administrador todavía tiene que investigar los registros y reconstruir los hechos. Nuestro próximo objetivo es cubrir ese vacío, y eso comienza por clasificar qué es realmente el tráfico.

Estamos desarrollando una clasificación de instrucciones que asigna las solicitudes a distintas categorías, como programación, escritura y otras. Estas categorías son el contexto que falta en casi todas las demás señales. Un aumento del gasto en “codificación” por parte de un ingeniero podría ser aceptable, pero el mismo incremento en una categoría que esa cuenta nunca ha utilizado no lo es. La clasificación puede mostrar a una organización no solo cuánto utiliza la IA, sino para qué la utiliza. 

También responde a la pregunta subyacente en la mayoría de estas conversaciones: ¿se está utilizando la IA para el propósito que se pretendía? Cuando diferenciamos el tráfico empresarial de otros tipos de tráfico, el uso personal sale a la luz. Externamente no es posible diferenciar entre un usuario que ejecuta un proyecto paralelo en el horario laboral de la empresa y otro que mueve datos discretamente a través de un modelo. Esta diferenciación es crucial para detectar el riesgo interno. 

Cuando tu tráfico de IA pasa a través de AI Gateway, cada nueva categoría de señal de riesgo o de eficiencia es una nueva característica de la que se beneficia un administrador, sin configuración adicional.

## Comenzar

User Insights está disponible de forma general a partir de hoy para todos los clientes de AI Gateway sin coste adicional. Ya está en el panel de control para cualquiera que envíe tráfico a través de la puerta de enlace, por lo que si ya enrutas tu tráfico a través de AI Gateway, ya tienes esta vista disponible. 

Si aún no lo has hecho, [​crea una puerta de enlace](https://developers.cloudflare.com/ai-gateway/get-started/) y comienza a enviar solicitudes a cualquier modelo de nuestro [catálogo](https://developers.cloudflare.com/ai/models/). 

Te recomendamos que coloques AI Gateway detrás de [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/policies/access/), que ahora está en la versión beta abierta. Aunque las vistas de gastos y anomalías no lo requieren, adjuntar una identidad es lo que convierte un ID de cuenta anónima en un nombre sobre el cual realmente se pueden tomar medidas. Empieza en modo de supervisión para conocer tus líneas base antes de aplicar cualquier medida.

Queremos saber cómo gestionas actualmente la IA. Únete a la conversación en[ Discord](https://discord.cloudflare.com/) o ponte en contacto con tu equipo de cuenta.

]]>01KZNEW370K72BJ4RKZ9V8434TEl Ciclo de Vida de Desarrollo de Agentes ha llegado a Cloudflarehttps://blog.cloudflare.com/es-es/agent-development-lifecycle/ Fri, 07 Aug 2026 09:27:56 GMTLa velocidad con la que los agentes pueden escribir código supera la capacidad de los equipos para revisarlo, implementarlo y mantenerlo. Hoy presentamos el Ciclo de Vida de Desarrollo de Agentes y las primitivas de Cloudflare en las que se basa.Agent Development LifecycleAgentesAgents WeekAIBrowser RunCloudflare WorkersDevOps (ES)MCPNoticias de productosObservabilityPlataforma para desarrolladoresTracingWorkflowsDurante las últimas décadas, los directores de ingeniería han tratado de encontrar estrategias para que muchos programadores puedan trabajar juntos en una base de código compartida. Este trabajo se remonta al marco “Ciclo de Vida del Desarrollo de Sistemas” ([RAND, 1975](https://www.rand.org/pubs/reports/R1855.html)), hoy conocido comúnmente como el “Ciclo de Vida del Desarrollo de Software” (SDLC), que define las siguientes fases:

  * Planificación
  * Diseño
  * Implementación
  * Prueba
  * Despliegue
  * Mantenimiento
  * Retirada



Con la IA, la implementación, que anteriormente era el paso más lento y costoso, es ahora el más rápido y barato. Eso, a su vez, ha tenido repercusiones a lo largo del proceso: la sobrecarga de las personas encargadas de todos los demás pasos del SDLC, desde los responsables del mantenimiento del código abierto, bombardeado con miles de solicitudes de extracción y problemas, hasta los ingenieros de producción que intentan evitar que caiga la producción mientras se multiplica el índice de entrega de software.

Todos intentamos evitar la mediocridad para nuestros sistemas, nuestros clientes y nosotros mismos.

La respuesta, paradójicamente, es permitir que los agentes puedan hacer más. ¡Es lo más lógico! Nunca permitirías que un ingeniero de tu equipo escribiera código mientras esperas que otra persona lo valide, lo fusione, lo despliegue, se encargue del buscapersonas en producción y gestione los errores entrantes. No obstante, eso es lo que la mayoría de las empresas hacen actualmente con los agentes. Los modelos han mejorado notablemente, y los agentes operan durante horizontes temporales más amplios, y pueden asumir tareas mucho mayores. Pero aún no se utilizan de manera uniforme en todo el SDLC.

Cloudflare trata a los agentes como nuestros clientes. Pueden [comprar dominios](https://blog.cloudflare.com/agents-stripe-projects/), crear [cuentas temporales](https://blog.cloudflare.com/temporary-accounts/) y [utilizar toda la API de Cloudflare](https://blog.cloudflare.com/code-mode-mcp/). Sabemos que los agentes necesitan las API y herramientas que les permitan gestionar todo el SDLC en nombre de nuestros clientes, no solo su comienzo.

Por este motivo, hoy presentamos el inicio de un nuevo conjunto de herramientas que permiten a los agentes ir más allá de simplemente generar el código para asumir más tareas del SDLC. Te contamos lo que hemos desarrollado y qué hemos aprendido al intentar resolver esta cuestión para nosotros mismos:

  * [**@cloudflare/ci**](https://blog.cloudflare.com/ci-workflows): esta nueva función, basada en Cloudflare Workflows, permite ejecutar CI/CD en millones de repositorios, ofrece recuperación automática y puede iniciar agentes para realizar tareas mucho más complejas.
  * [**Rastreos de OpenTelemetry en el entorno de desarrollo local**](https://blog.cloudflare.com/local-tracing): esta función, integrada en Wrangler y el complemento Cloudflare Vite, ofrece a los agentes la misma observabilidad que tienen en producción.
  * [**Presentamos Cloudflare Agents y Agent Traces**](http://blog.cloudflare.com/agents-on-cloudflare): un nuevo espacio para la observación, el mantenimiento y la mejora de agentes, centrado en los rastreos de OpenTelemetry de los agentes.
  * [**Cómo Cloudflare aplica estándares de ingeniería utilizando IA**](http://blog.cloudflare.com/engineering-standards-enforcement): nuestra propia experiencia aplicando las prácticas recomendadas en todos los repositorios y especificaciones de nuestros productos y sistemas.
  * [**Cómo hemos creado una fábrica de software para reducir a cero el número de problemas en GitHub de Astro**](https://blog.cloudflare.com/astro-issue-triage): nuestra propia experiencia de desarrollo de sistemas para la clasificación, reproducción, verificación y resolución automáticas de problemas para un proyecto de código abierto grande y en crecimiento.



Sin embargo, aquí encontramos algo más importante. Cuando observamos el SDLC, incluso con la mejor automatización, sus suposiciones no se adaptan al volumen de código que los agentes pueden escribir y al ritmo al que los equipos de software deben avanzar para ser competitivos. Creemos que ha llegado el momento de reemplazar el SDLC por el ADLC: el Ciclo de Vida de Desarrollo de Agentes.

## El SDLC es para equipos de software. El ADLC es para fábricas de software.

En este momento, [todo](https://x.com/zachlloydtweets/status/2069789929073262945) [el mundo](https://x.com/matanSF/status/2066578088184680920) [habla](https://x.com/dexhorthy/status/2081797628552270027) [sobre](https://x.com/bcherny/status/2077929390806073807) [cómo crear](https://x.com/gokulr/status/2032271386161684665) “fábricas de software” (sistemas basados en agentes a los que se proporcionan ciertos datos y que de forma autónoma desarrollan, mejoran, despliegan y gestionan software. Toma una información de entrada específica, ya sea un error de producción, un informe de error de un cliente o una idea para una nueva función, y delégala por completo a un agente.

Incluso con los agentes, la mayoría de los proyectos de software se ven limitados por pasos que requieren intervención humana. Los humanos dan instrucciones a los agentes, les indican que continúen, les ordenan que apliquen comentarios de una revisión de código, vigilan constantemente un gran número de ellos y les dan instrucciones. En la mayoría de los equipos de software, los humanos todavía gestionan cada uno de los pasos del modelo del SDLC. La única diferencia es la delegación de tareas a un agente dentro de cada paso.

De esta forma, el sueño que impulsa las fábricas de software es: ¿y si reinventaras este enfoque y crearas una fábrica para todo el proceso de desarrollo de software? ¿Cómo podemos dedicar más tiempo humano a los aspectos que realmente requieren la inspiración, el buen gusto y el criterio de los humanos? Nos dejaría más tiempo para diseñar, hablar con los clientes y soñar en grande.

Una fábrica de software debe gestionar los mismos pasos del SDLC, pero exige mucho más de la plataforma en la que se basa. Porque cuando transfieres el control al agente y le dejas que tome las riendas, cada paso manual que antes dependía de una persona debe adaptarse para ser:

  * **Programático** : "ClickOps" era una práctica inadecuada para los humanos, pero es inutil para los agentes. Cada operación necesita API a las que los agentes puedan llamar, que puedan depurar y en las que puedan confiar.
  * **Escalable horizontalmente** : las implementaciones de vista previa eran una función adicional pero prescindible cuando las personas miraban la pantalla mientras realizaban tareas de desarrollo o tomaban el control manualmente de un servidor de preproducción para detectar problemas antes del paso a producción. Para que los agentes tomen las riendas, cada agente debe tener su propia vista previa que coincida con el entorno de producción.
  * **Reproducible** : ¿qué sucede si hay un error que solo puedes reproducir al simular 4G en un iPhone 15? ¿O desde una dirección IP en un país específico? En este caso, las herramientas típicas de pruebas unitarias y de integración no serán útiles.
  * **Basado en notificaciones push en tiempo real** : depender de que unas personas miren el panel de control adecuado nunca ha sido la mejor forma de comprobar si todo funcionaba correctamente, pero esta estrategia no sirve en absoluto en el caso de los agentes. Necesitas un evento que desencadene la acción de un agente.
  * **Atómico** : cada cambio se debe poder comprobar, lanzar, observar y revertir de forma independientemente, sin que afecte a ningún comportamiento no relacionado.
  * **Basado en permisos** : aunque sabes que probablemente no deberías, actualmente concedes a algunos ingenieros de confianza las llaves SSH de acceso a producción por si las cosas realmente se complican. De ninguna forma se lo permitirías a un agente. Sin embargo, si un agente no tiene capacidad para escalar y obtener más permisos, ¿cómo puede llevar a cabo su trabajo?
  * **Automejora** : las personas aprenden de la experiencia. Durante su primera semana de incorporación o su primera rotación de guardia, las personas son lentas y necesitan seguir los pasos de algún compañero, pero luego su trabajo mejora y se acelera. De la misma forma, los agentes necesitan maneras de aprender de la experiencia.



Necesitamos algo nuevo si queremos que las fábricas de software sean seguras para utilizar con software de entornos de producción reales. Las fábricas de software afrontan el mismo desafío que otros sistemas autónomos, como los coches autónomos: cómo pasar de un funcionamiento correcto el 80 % del tiempo a un porcentaje superior al 99 %.

## Para transferir a los agentes el control del SDLC, no les puedes entregar un vehículo diseñado para las personas

Un vehículo autónomo está cargado con sensores y tecnología que un coche normal no tiene, como sensores Lidar, cámaras y un potente sistema de cómputo para ejecutar inferencias, así como conectividad a un sistema de comando central que puede tomar el control de forma remota si es necesario.

Para que la eficacia de la conducción de un vehículo autónomo alcance el 80 % de la eficacia de la conducción humana, probablemente no necesitemos toda esta tecnología. Hace 10 años que la eficacia de la conducción autónoma alcanzó el 80 % de la de la conducción humana. Pero ese no es el estándar que queremos lograr: el objetivo es que sea mucho mejor y más segura que la conducción humana. Eso es lo que esperamos cuando entregamos el control a una máquina, y poder sentirnos seguros al echar una siesta mientras conducimos por la AP-7 a 100 km/h. Por este motivo, los vehículos autónomos cuentan con tecnología diseñada específicamente para la conducción autónoma; es lo que genera confianza y responde a las imprevisibles situaciones extremas.

Lo mismo ocurre con el software autónomo. Pregúntate, ¿por qué _aún no_ has dejado que tu agente apruebe automáticamente y fusione sus propias solicitudes de extracción con tus servicios de producción? Cuanto mayor importancia tenga lo que estés desarrollando, más larga será casi con toda seguridad tu lista de razones.

Cuando empiezas a desentrañar no solo todas las cosas que pueden salir catastróficamente mal en este proceso, sino también las que son necesarias para desarrollar la solución adecuada para los clientes, resulta especialmente complejo. No encaja en un conjunto lineal de pasos de un archivo YAML de GitHub Actions, y va mucho más allá de ejecutar las pruebas automatizadas tradicionales. Incluso un pequeño cambio en un panel de control puede abarcar roles, especializaciones y estructuras organizativas, y los cambios subjetivos son los más difíciles de probar y delegar. Actualmente, es posible que la mayoría de estas cosas no formen parte en absoluto de tu canalización de CI/CD. Pero deberá incluirlas, si quieres que se sigan realizando, mientras transfieres el control total a los agentes que dirigen la fábrica de software.

Para permitir que los agentes gestionen todo el proceso, necesitamos mejorar la estrategia de orquestación de esta serie dinámica de pasos. Creemos que la respuesta es un [flujo de trabajo](https://blog.cloudflare.com/ci-workflows), con la capacidad de iniciar contenedores, agentes y navegadores. Un flujo de trabajo que puede establecer indicadores de funciones y activarlas para un usuario de prueba, investigar los registros y rastreos, observar las métricas de producción a medida que un cambio se implementa gradualmente, y llevar a cabo todo lo necesario para una implementación segura.

## Una canalización de CI/CD es solo un flujo de trabajo. Pero un flujo de trabajo puede ser mucho más que una canalización de CI/CD.

[Cloudflare Workflows](https://developers.cloudflare.com/workflows/) te permite encadenar varios pasos, volver a intentar automáticamente las tareas fallidas y mantener el estado durante minutos, horas o incluso semanas. Esta solución está diseñada para codificar los procesos empresariales complejos y dinámicos en un programa lógico fácilmente entendible. Esta [publicación del blog](https://blog.cloudflare.com/ci-workflows) explica por qué Workflows, junto con [Artifacts](https://blog.cloudflare.com/artifacts-git-for-agents-beta/), simplifica radicalmente la definición y activación de las canalizaciones de CI/CD. Por ejemplo:

Los flujos de trabajo van más allá de una serie de pasos lineales. Se pueden [definir dinámicamente](https://blog.cloudflare.com/dynamic-workflows/) y pueden generar agentes u otros flujos de trabajo. [Este ejemplo](https://flueframework.com/docs/guide/workflows/#example-cloudflare-workflows) muestra un flujo de trabajo que revisa los datos nuevos del día anterior. El flujo de trabajo tiene el control total sobre cuándo y cómo se dan las instrucciones al agente, y puede transmitir el contexto entre pasos:

Cuando observas este patrón, y crees tan firmemente en los flujos de trabajo como Cloudflare, comienzas a preguntarte: ¿qué más podría gestionar un flujo de trabajo por mí? ¿Qué otros pasos limitados por los humanos podría delegar a esta combinación de flujo de trabajo y [agentes Flue](https://flueframework.com/)?

## Todo el ADLC, en la plataforma de Cloudflare

Si consideras las etapas del SDLC, todo lo que un agente necesita para gestionar el proceso completo de desarrollo, implementación y mantenimiento de software lo encuentras en Cloudflare, con [Workflows](https://developers.cloudflare.com/workflows/), que puede orquestar pasos complejos, y [Artifacts](https://developers.cloudflare.com/artifacts/) como la capa de almacenamiento para el código:

## Primitivas para crear tu fábrica de software

En este momento, las personas en la vanguardia de la innovación están creando las fábricas de software del futuro. Con el tiempo, las fábricas de software serán, al igual que los agentes y la IA, el método habitual de desarrollo de software. Pero la mayoría de las personas y organizaciones aún no hemos llegado a ese punto.

Queremos que deje de ser así.

Para ello, nos hemos planteado algunas preguntas: ¿cómo podemos simplificar y hacer accesible todos los recursos para que todos los usuarios en Internet se beneficien de un cambio de paradigma como este? ¿Cuáles son las primitivas de la capa base que podemos poner a disposición de todos los usuarios, desde la startup más pequeña hasta las mayores plataformas del mundo?

En este caso, pensamos que las primitivas ya las tenemos aquí. Quedan cosas por hacer para conectarlas, para seguir creando nuestra propia fábrica de software y aprender de ella. Sin embargo, ahora mismo ya estamos listos para que desarrolles tu maquinaria que desarrollará la maquinaría, en Cloudflare. Comienza con [@cloudflare/ci](https://blog.cloudflare.com/ci-workflows), [desarrolla un agente](http://blog.cloudflare.com/agents-on-cloudflare) y descubre cuánto del SDLC puedes automatizar.

]]>01KZDNTRMZF3YDYDWDWV3X4AHMCloudflare OS, una plataforma abierta para agentes, aplicaciones y tareashttps://blog.cloudflare.com/es-es/cloudflare-os/ Fri, 07 Aug 2026 06:33:42 GMTCloudflare OS es una plataforma de código abierto que permite a todos los usuarios de tu empresa desarrollar aplicaciones, automatizar sus tareas y acceder con total seguridad a los sistemas internos, y que ofrece un diseño adaptado a los conocimientos y el funcionamiento de tu organizaciónAgentesAgents WeekAICloudflare AccessCloudflare OSCloudflare WorkersDesarrolladoresNoticias de productosOpen SourcePlataforma para desarrolladoresTodas las organizaciones tienen una misión, una razón de ser. Las organizaciones transmiten esa misión, junto con su terminología, sus procedimientos, sus sistemas, sus normas y su metodología de trabajo, a sus usuarios. Estos, a su vez, toman este contexto junto con su propia experiencia y trabajan para lograr esa misión.

Los resultados de las tareas pueden adoptar muchas formas, desde código, documentos y diapositivas, hasta relaciones y resultados en el mundo físico.

Algunos resultados son evidentes (p. ej., el código funciona o no). En los últimos dos años, los agentes han estado utilizando este bucle de información para producir código que “funcione” para los desarrolladores. ¿Pero qué pasa con el resto de nosotros?

Facilitar la misma ventaja al resto de la organización resulta más difícil. Los agentes necesitan comprender el contexto de la empresa y poder acceder a los sistemas que las personas utilizan para llevar a cabo sus tareas. Necesitan convertir ese contexto y acceder a las tareas que impulsan a la organización hacia su misión.

Por este motivo hemos desarrollado Cloudflare OS. Proporciona a cada persona un agente y un espacio de trabajo desarrollado en torno a de su empresa: cómo funciona, qué sabe y los sistemas de los que depende.

En mayo de este año, proporcionamos a todos los miembros de Cloudflare acceso a la primera versión de Cloudflare OS. Miles de personas, en todas las funciones, muchas de ellas externas al equipo de ingeniería, lo utilizan a diario para crear documentos y presentaciones, automatizar tareas repetitivas y desarrollar pequeñas aplicaciones para visualizar datos y que les facilite su trabajo.

Cloudflare OS también ha proporcionado a todos los usuarios una biblioteca compartida de contexto y habilidades desarrollada por los equipos de Cloudflare. Incorpora nuestra terminología, nuestros procedimientos y nuestras prácticas recomendadas para la realización de tareas recurrentes en instrucciones que un agente puede seguir. Cuando una persona descubre una manera mejor de hacer algo, todos los demás pueden beneficiarse de ella.

**Hoy lanzamos el código abierto de una nueva versión de[Cloudflare](https://os.cloudflare.app/Cloudflare)[ OS](https://os.cloudflare.app/).** Cualquier organización puede implementarlo, conectarlo a sus sistemas internos y hacerlo suyo.

## **Qué hemos aprendido de la primera versión**

La versión de Cloudflare OS que ofrecemos hoy como código abierto se basa en lo que aprendimos tras ejecutar internamente la primera versión, un proceso que Sam Rhea, nuestro director de informática, explica en su [​publicación del blog](https://blog.cloudflare.com/how-we-use-ai-with-cloudflare-os).

La primera versión se centraba en aquellas personas que trabajaban con agentes a través de espacios de trabajo privados. Las aplicaciones eran estáticas, en lugar de software activo conectado a sistemas internos, y en su mayoría las tareas deterministas aún requerían ejecutar una habilidad de agente nuevamente y consumir más tokens de modelos.

La colaboración expuso un desafío más crítico. El acceso a un [​servidor MCP](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) nos indicaba qué herramientas podía utilizar un agente, pero no qué recursos subyacentes este había observado. Cuando los usuarios comenzaron a compartir espacios de trabajo, aplicaciones y resultados, necesitamos asegurarnos de que la colaboración no expusiera información que alguien no tuviera permiso para ver.

Para resolver estos problemas, rediseñamos Cloudflare OS sobre una nueva base. La seguridad debía estar integrada en la plataforma, en lugar de ser una característica que cada usuario que desarrollara una aplicación o utilizara un agente tuviera que implementar correctamente.

El resultado es una plataforma diseñada para pertenecer a la empresa que la ejecuta. Puedes personalizar las interfaces, conectar tus herramientas y añadir las habilidades y el contexto que capturan cómo funciona tu organización.

## **Novedad: Cloudflare OS**

Cloudflare OS comienza con una conversación en tu navegador, como muchas otras herramientas de IA. Lo que lo hace diferente es que cada conversación se basa en el contexto y las habilidades que ha seleccionado tu organización. Asigna a tu espacio de trabajo un objetivo, y podrá aprovechar esos conocimientos y trabajar con las herramientas y los datos que tu organización ya utiliza para lograrlo.

Cloudflare OS combina tres componentes:

  * **Un espacio de trabajo para agentes** , basado en el contexto y las habilidades que tu empresa ha seleccionado, con un entorno de ejecución aislado donde los agentes pueden escribir y ejecutar código.
  * **Un nuevo marco de seguridad y gobernanza** para el acceso seguro a los datos y los servicios internos.
  * **Una plataforma para aplicaciones personales y modificables** que los usuarios pueden desarrollar, compartir y seguir modificando.



Lo que comienza como una conversación puede convertirse en un documento, una aplicación o un flujo de trabajo que sigue realizando el trabajo.

## **Un espacio de trabajo para agentes a disposición de toda la empresa**

Los espacios de trabajo para agentes se han diseñado para que los puedan utilizar todas las personas de tu organización. Interactúas con ellos en tu navegador, así que no necesitas ser desarrollador ni saber cómo utilizar un terminal. 

Un espacio de trabajo combina sesiones de agentes, un estado persistente, resultados y archivos, el acceso a recursos y un entorno aislado donde el agente puede escribir y ejecutar código.

Incluye las habilidades y el contexto seleccionados que tu equipo o empresa ha recopilado. Se acabó perder tiempo y esfuerzo en tareas redundantes: si alguien de tu equipo ha descubierto una manera mejor de hacer algo, todo el mundo se beneficia. Los usuarios ya no tienen que explicar el mismo proceso, la misma terminología y las mismas prácticas recomendadas a un modelo cada vez que comienzan una tarea.

Estas son algunas cosas que puedes hacer:

### **Investigar y plantear preguntas**

Pide a un espacio de trabajo que investigue un tema utilizando el contexto de la empresa y los recursos que pongas a su disposición. El agente puede escribir código para buscar, filtrar, combinar y analizar información en lugar de incorporar un conjunto de datos completo en la ventana de contexto del modelo.

### **Crear documentos, diapositivas y hojas de cálculo**

Un espacio de trabajo puede convertir su investigación en un documento, una presentación o una hoja de cálculo que puede seguir editando. Estos resultados no tienen por qué ser archivos estáticos. Pueden seguir conectados a datos en tiempo real, actualizarse a medida que sus fuentes cambien y también exportarse a formatos o servicios conocidos como Google Drive.

### **Crear aplicaciones conectadas y colaborativas para tu equipo**

Cuando un documento o una hoja de cálculo no es suficiente, el agente puede crear una aplicación con su propia interfaz, lógica y estado. La aplicación puede utilizar los recursos conectados de la empresa y facilitar el trabajo colaborativo de varias personas.

### **Ejecutar flujos de trabajo deterministas**

No todos los trabajos necesitan una sesión completa de agente. Muchos son una secuencia conocida de pasos con uno o dos lugares donde el criterio es útil. Un espacio de trabajo puede convertir esos trabajos en flujos de trabajo mayormente determinístas, utilizando código para los pasos predecibles y un modelo solo allí donde aporte valor. Los flujos de trabajo pueden ejecutarse bajo demanda, según una planificación o cuando se produce un evento en un sistema conectado.

Cloudflare OS proporciona a los agentes y aplicaciones acceso controlado a los sistemas de registro a través de Gatekeepers (más información disponible en la sección dedicada a la seguridad a continuación). También es compatible con los servidores [​MCP (Model Context Protocol)](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) existentes que tu organización ya utiliza a través de [​Portales de servidores MCP](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/).

## **Un nuevo marco de seguridad y gobernanza para el acceso seguro a los datos y servicios internos**

Cuando los usuarios comienzan a experimentar con la IA en el entorno laboral, una de sus primeras solicitudes suele ser para obtener claves API para los sistemas de la empresa. Es lógico: la IA no es de mucha utilidad en el entorno laboral si no tiene acceso a los sistemas que utilizan los usuarios para llevar a cabo sus tareas.

Pero entregar claves API a los usuarios y los agentes es peligroso y no escalable. Las claves suelen proporcionar un acceso generalizado y duradero que es difícil de restringir, compartir con seguridad y auditar.

MCP ofrece a los agentes una manera mejor de utilizar estos sistemas. Un servidor MCP puede mantener las credenciales y exponer un conjunto definido de herramientas en lugar de entregar la clave directamente al agente. Sin embargo, controlar qué herramientas puede utilizar un agente es solo el primer paso. MCP por sí solo no nos indica qué recursos subyacentes ha observado un agente. El agente puede combinar información de distintos sistemas, enviarla a un lugar menos restringido o exponerla a través de aplicaciones y resultados a usuarios que no tienen la autorización necesaria para ver los recursos originales. La autorización debe tener en cuenta a dónde pueden ir los datos a continuación.

### **Los agentes comienzan sin acceso**

[ Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/) controla quién puede acceder a Cloudflare OS. Internamente, cada agente y cada aplicación comienza sin tener acceso a ningún recurso. Un agente puede solicitar acceso a un recurso específico, que puedes concederle o denegarle. El código generado recibe ese recurso como un enlace tipado:

`env.PROJECT` es una capacidad que representa el permiso para utilizar un recurso específico bajo una política determinada. La credencial permanece completamente aislada del agente y de cualquier código generado.

El código del servidor se ejecuta en un Dynamic Worker con la conexión de red global desactivada. El código del cliente se ejecuta en un marco aislado en el navegador. Ninguno de ellos puede acceder a Internet salvo a través de las capacidades que proporciones explícitamente.

### **Los Gatekeepers controlan los recursos y las acciones**

Un Gatekeeper es un[ Worker](https://developers.cloudflare.com/workers/?_gl=1*1pzndf6*_gcl_au*MzM2MDkxNTQzLjE3ODQ4NDczOTM.*_ga*MWVkZWU3OTctMzJjNC00YWE1LWI2ZDUtZTJkNTY1NzYxYWQ0*_ga_SQCRB0TXZW*czE3ODUyMTk3NjMkbzckZzAkdDE3ODUyMTk3NjMkajYwJGwwJGgwJGRQeHAyTUEtdzgtVUFETUEzOGwtVFVhajVDd2laRWYxSC1R) específico del servicio que se sitúa entre Cloudflare OS y un servicio externo. Entiende la API del servicio, sus recursos y las operaciones que se pueden realizar en ellos.

Probablemente sea demasiado permisivo otorgar a un agente acceso a toda tu cuenta de GitHub. Un Gatekeeper puede otorgarle acceso a un repositorio individual, permitirle leer los problemas pero no el código fuente, ocultar campos determinados, aplicar límites de velocidad y requerir la aprobación antes de fusionar una solicitud de extracción.

El agente y sus aplicaciones ven una pequeña API de TypeScript. El Gatekeeper gestiona[ OAuth](https://www.cloudflare.com/learning/access-management/what-is-oauth/), mantiene la credencial, aplica la política, registra lo que se ha leído y media en cualquier acción con un efecto visible externamente.

### **La política sigue lo que el agente ha visto**

No es suficiente con controlar la lectura inicial Tomemos, por ejemplo, el caso en el que un agente lee una tabla confidencial en un almacén de datos y la utiliza para generar un panel de control activo. El uso compartido de panel de control no debe ser una forma de compartir la tabla con personas que no puedan acceder a ella directamente.

Cloudflare OS registra todos los recursos que observan los agentes. Estas observaciones permanecen vinculadas al agente y a su trabajo. Cuando otra persona intenta abrir el espacio de trabajo, interactuar con el agente o ver lo que ha generado, los Gatekeepers verifican el acceso de esa persona a los recursos observados.

El mismo registro de observación se utiliza para informar a políticas que determinan cuándo los agentes pueden enviar solicitudes externas. Una lectura de datos confidenciales puede impedir que el agente escriba datos en ciertas fuentes, invite a nuevos colaboradores, entregue el trabajo a otro agente o envíe una solicitud saliente.

Los usuarios que utilizan agentes o desarrollan aplicaciones no tienen que preocuparse por cometer estos errores. Ahora puedes hacer que la plataforma se encargue de ello.

## **Una plataforma para crear y compartir aplicaciones personales y modificables**

La mayoría de los paquetes de soluciones dedicadas a la productividad te ofrecen un conjunto fijo de aplicaciones: documentos, hojas de cálculo y presentaciones. En Cloudflare OS, cada "archivo" puede ser su propia aplicación, escrita por un agente para una persona, un proyecto o un equipo específicos.

No son prototipos que tengas que exportar e implementar en otra ubicación. Cada uno es una aplicación integral con código del cliente, código del servidor, una API y un estado duradero. Las aplicaciones son privadas por defecto, pero se pueden compartir como documentos.

### **Cada aplicación es un Worker**

Cuando solicitas a tu espacio de trabajo que desarrolle una aplicación, el agente escribe dos partes:

  * El código del cliente que representa la interfaz de usuario de la aplicación en el navegador
  * El código del servidor que almacena el estado e implementa el comportamiento de la aplicación



El servidor se carga bajo demanda como un [​Dynamic Worker](https://developers.cloudflare.com/dynamic-workers/) y se crea una instancia como [​Durable Object Facet](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) (ambas son características que hemos desarrollo para este proyecto). La "faceta" proporciona a la aplicación su propia base de datos SQLite, independiente del entorno de ejecución de Cloudflare OS que la gestiona. Dynamic Workers utiliza V8 Isolates ligeros, por lo que cada aplicación puede tener su propio entorno de ejecución aislado sin necesidad de un servidor o contenedor dedicado.

El cliente del navegador se comunica con el servidor usando [​Cap’n Web](https://github.com/cloudflare/capnweb), el sistema de llamadas a procedimientos remotos (RPC) con capacidad de objeto de código abierto de Cloudflare. Se puede llamar a un método del servidor desde el cliente como una función normal de JavaScript:

Lo especial es que el agente también puede llamar al mismo método.

**De esta forma, si puedes desarrollar una herramienta para llevar a cabo una tarea tú mismo, los agentes pueden utilizar tu herramienta para realizar dicha tarea cuando tú no estés.**

### **Comparte la aplicación o comparte su desarrollo**

Cuando desarrollas una aplicación en Cloudflare OS, puedes compartirla de dos maneras:

  * Compartir tu propia aplicación permite que otras personas colaboren en tiempo real usando el mismo estado.
  * Compartir un plano de tu aplicación permite que otras personas desarrollen su propia copia de tu aplicación.



Una aplicación cuya instancia se ha creado a partir de un plano contiene el código de la aplicación original. Sin embargo, no contiene sus datos de SQLite, su historial de conversaciones, sus credenciales ni sus recursos conectados. Cada nueva aplicación comienza con un estado y recursos independientes.

Esto significa que cuando compartes aplicaciones con tu equipo, pueden modificarlas ellos mismos con IA en lugar de presentar una solicitud de función y asignártela.

## **Utiliza cualquier modelo y controla sus costes**

Cloudflare OS se puede utilizar con cualquier modelo. Cada llamada de inferencia se ejecuta a través de [​Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/), proporcionando a tu organización un único lugar donde decidir qué modelos están disponibles y qué modelo debe encargarse de cada tarea.

No todas las tareas requieren el modelo más caro. Es posible que no desees ejecutar el modelo de vanguardia más caro para resumir cada mañana tus correos electrónicos no leídos. AI Gateway te proporciona el control necesario que te permite garantizar que los modelos más costosos solo se utilicen para las tareas más complejas.

Cada solicitud se atribuye a la persona, el equipo o el espacio de trabajo que la ha enviado. Los administradores pueden ver a qué se dedica el gasto en inferencia, establecer presupuestos y límites de velocidad, y decidir qué sucede cuando se alcanza un límite.

## **Código abierto, para que puedas hacerlo tuyo**

Cloudflare OS ya está disponible y es de código abierto. Consulta el[ repositorio de GitHub cloudflare-os](https://github.com/cloudflare/cloudflare-os). Puedes implementarlo en tu propia cuenta de Cloudflare y utilizar tus políticas de Access, tu configuración de AI Gateway, tus datos y tus integraciones.

Nuestra implementación interna refleja los sistemas, la terminología, las políticas y la metodología de trabajo de Cloudflare. La tuya debe ser un reflejo de tu organización.

Cloudflare OS está diseñado para que puedas personalizar la interfaz, añadir Gatekeepers internos y desarrollar características específicas de tu organización sin cambiar el producto principal.

Lanzamos dos repositorios: el [​principal de Cloudflare OS](https://github.com/cloudflare/cloudflare-os) y una [​implementación de ejemplo](https://github.com/cloudflare/cloudflare-os-starter) basada en cómo lo ejecutamos internamente en Cloudflare. El repositorio de implementación utiliza el repositorio principal sin revisiones, y proporciona un lugar para la configuración, la interfaz de usuario personalizada, las integraciones internas, los análisis y los flujos de trabajo de implementación.

## **Lo entregamos junto con nuestros socios**

El código fuente es solo el punto de partida. El contexto, las habilidades, los flujos de trabajo, los sistemas internos y las políticas son lo que hace que Cloudflare OS sea aún más útil para tu organización.

Presidio y Happy Cog, socios estratégicos de Cloudflare, trabajarán contigo para adaptar Cloudflare OS al funcionamiento de tu organización e implementarlo para todos tus equipos.

Nuestros socios pueden ayudarte a seleccionar las habilidades compartidas y el contexto institucional, a desarrollar interfaces personalizadas y a conectar los sistemas internos a través de Gatekeepers y los portales de servidores MCP, así como a configurar controles de seguridad, modelos y costes.

Te beneficias de tu propio Cloudflare OS con tu marca, conectado a tus sistemas, ejecutado en Cloudflare y adaptado a cómo trabaja realmente tu equipo.

## **Comenzar**

Cloudflare OS ya está disponible en [​GitHub](https://github.com/cloudflare/cloudflare-os). Puedes explorar el código fuente, probar la demostración o desplegarlo en tu propia cuenta de Cloudflare en pocos minutos usando nuestro [​repositorio básico](https://github.com/cloudflare/cloudflare-os-starter).

Esto es solo el principio. Estamos trabajando para llevar Cloudflare OS al panel de control de Cloudflare como un producto totalmente gestionado, añadir contenedores para flujos de trabajo de desarrollo e integrar los espacios de trabajo en Slack y otras herramientas de chat.

Si estás interesado en hablar con nuestro equipo, nos encantaría charlar contigo. ¡Utiliza[ este formulario](https://www.cloudflare.com/resource/cloudflare-os-interest-landing-page/) para ponerte en contacto con nosotros!

]]>01KZDDZ9VQN4X5C3R346E9CDP3Novedad: Cloudflare Wallets, el monedero programable para la web agénticahttps://blog.cloudflare.com/es-es/wallets/ Thu, 06 Aug 2026 09:07:19 GMTCloudflare Wallets ofrecerá a los agentes de IA pagos nativos e identidad verificable en la web. Con el protocolo x402, los agentes pueden adquirir de forma autónoma nuevas API y contenidos dentro de unos límites de seguridad bien definidos.Agents WeekAIAI Bots (ES)DesarrolladoresNoticias de productosPaymentsPlataforma para desarrolladoresx402Hoy en día, a los agentes de IA les cuesta probar nuevas API. A menudo tienen que pasar por una página de inicio de sesión diseñada para usuarios y no para agentes, ponerse en contacto con alguien para añadir un método de pago, generar una clave de API y, después, averiguar cómo llamar a la API.

Este proceso es muy complicado para los agentes por dos razones: los agentes no tienen un identificador estable para registrarse en una API y no disponen de una forma nativa de pagar por las API. La falta de estos elementos hace que a menudo les cueste integrarse en el software, lo que limita el crecimiento del comercio basado en agentes. Los agentes de IA suelen acabar renunciando por completo a estas tareas, dejando que sean los humanos quienes se encarguen del registro, los métodos de pago y la generación de claves API. Esto hace que a los agentes les resulte muy difícil probar y comparar muchas API.

Para resolverlo, hemos desarrollado Cloudflare Wallets. A partir de hoy, puedes[ crearte un nombre de usuario de Cloudflare Wallet](https://cloudflare.pay) para tu cuenta, lo que te proporcionará un identificador único que te ayudará a interactuar mejor con los comercios. Pronto podrás configurar y usar tu Cloudflare Wallet para pagar las API y el contenido.

A principios de este mes, anunciamos[ Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) para ayudar a los clientes de Cloudflare a recibir pagos por sus sitios web y aplicaciones. Monetization Gateway admitirá micropagos utilizando el[ protocolo x402](https://www.x402.org/), el cual permite adjuntar pagos a las solicitudes HTTP. Estos micropagos se podrán usar para pagar desde la inferencia de IA hasta datos y contenidos. Si quieres pagar o que te paguen por servicios a través de Monetization Gateway y otros[ puntos finales compatibles con x402](https://developers.cloudflare.com/agents/tools/payments/x402/), necesitarás un monedero. 

Cloudflare Wallets te permitirá almacenar criptomonedas estables, comprar servicios y recibir dinero en cualquier sitio de Internet. Cada cuenta con un monedero también podrá crear monederos virtuales para sus agentes, lo que les permitirá comprar API, herramientas MCP, contenidos y mucho más. Podrás establecer límites para tus monederos virtuales (como un límite de gasto, una lista de permitidos y un importe máximo por transacción) para que tus agentes puedan gastar dinero de tu cuenta de forma segura. De esta forma, tu agente podrá probar muchas API sin complicaciones y con un riesgo controlado. Los usuarios del monedero tendrán la opción de compartir sus identificadores de Cloudflare Wallets, lo que les proporcionará una identidad estable a la hora de interactuar con los comercios.

## **Creación del mercado agéntico bidireccional**

[ Monetization Gateway](https://blog.cloudflare.com/monetization-gateway/) de Cloudflare permitirá a los clientes elegibles de Cloudflare vender sus recursos (como contenido o API) de manera indirecta a compradores agénticos. Pero para que ese mercado se desarrolle de verdad, los agentes necesitan más herramientas que les permitan comprar a los comercios de forma nativa en el entorno digital. Cloudflare Wallets añadirá otra herramienta al SDK de agentes de Cloudflare, lo que permitirá a los agentes de IA comprar fácilmente las API y el contenido necesarios mediante micropagos.

Habrá dos tipos de Cloudflare Wallets: los monederos de cuenta y los monederos virtuales.

**Monederos de cuenta** están diseñados para personas que son propietarios y usuarios de cuentas de Cloudflare. Podrás añadir fondos, delegar el gasto a monederos virtuales gestionados por agentes y retirar fondos según sea necesario.

**Monederos virtuales** , en cambio, están diseñados para agentes y operan mediante claves API. Dentro de un monedero virtual, un agente podrá gastar fondos según sus permisos. El gasto máximo estará sujeto al límite que haya establecido el titular del monedero de la cuenta. Este marco ofrece a los agentes libertad para actuar en nombre de los usuarios sin necesidad de una aprobación manual constante, al tiempo que limita la capacidad de los agentes para gastar más de lo previsto.

## **La libertad de explorar**

Los monederos virtuales son interesantes porque permitirán a los agentes hacer lo que mejor saben hacer: explorar decenas o cientos de servicios y encontrar el más adecuado para cada caso concreto. Los micropagos con criptomonedas estables a través del protocolo x402 harán que sea muy fácil probar una API sin necesidad de tener una cuenta, lo que permitirá a los agentes probar nuevas opciones sin apenas complicaciones. Los límites de gasto de los monederos virtuales están pensados para que los humanos puedan dejar que los agentes exploren de forma autónoma dentro de unos límites de gasto seguros. Estos límites pueden parecer restricciones, pero, aunque parezca contradictorio, en realidad les dan más libertad a los agentes. Si un agente es responsable de 10 dólares, te preocuparás menos por su gasto que si fuera responsable de 1000 dólares. Si probar una API solo cuesta unos céntimos, entonces 10 dólares son más que suficientes para explorar y evaluar muchas opciones.

Una vez que tú o tu agente hayáis elegido una API, las políticas que hayas establecido en tu monedero de cuenta servirán para controlar los gastos de los monederos virtuales. ¿Quieres dar a cada empleado un presupuesto de 100 dólares a la semana para la inferencia de IA? Solo tienes que asignar un saldo adecuado a tu monedero de cuenta y crear monederos virtuales para cada usuario con esa regla. Cualquiera que supere los límites de su monedero virtual podrá solicitar una excepción manual a una persona autorizada para realizar cambios en el monedero de cuenta.

Queremos facilitar que los monederos de cuenta establezcan políticas de gasto flexibles pero firmes que no requieran una supervisión diaria y activa. Cuando ocurra algo anómalo, como un gasto inesperadamente rápido, una persona podrá revisar y confirmar si todo funciona según lo previsto. Si el gasto fue intencionado, el administrador del monedero de cuenta podrá aumentar el límite o aprobar una inyección de fondos puntual. Si el gasto no fue intencionado, las políticas de gasto para añadir fondos a los monederos virtuales habrán cumplido su función al imponer los límites.

Estamos trabajando para que recargar y usar estos monederos sea lo más fácil posible. Empezaremos con formas sencillas de ingresar y retirar fondos en las zonas geográficas compatibles, y los usuarios que cumplan los requisitos podrán optar por la autofinanciación mediante criptomonedas estables como alternativa. Internet no va a cambiar por completo de la noche a la mañana, pero ahora[ que la mayor parte del tráfico web](https://radar.cloudflare.com/) lo generan los bots, nos hace mucha ilusión ofrecer a los agentes y negocios herramientas de primer nivel para el comercio agéntico.

## **Más allá de los pagos**

Permitir que las personas deleguen autoridad en los agentes para comprar y vender servicios fácilmente es un buen punto de partida. Pero esta delegación no siempre resulta obvia para los comercios cuando interactúan con los agentes. Hoy en día, si un agente visita tu página web, es posible que sepas muy poco sobre él como usuario, a pesar de que el agente actúe en nombre de una persona o una organización. Esta falta de atribución pone en tela de juicio muchos modelos de negocio tradicionales en la web. Es fácil ofrecer una prueba gratuita de una semana o créditos de registro a una persona o a una organización. Pero es difícil ofrecer estas mismas ventajas a un agente que carece de una identidad estable, sobre todo cuando una sola persona puede crear docenas de agentes bajo su control.

Resolvemos este problema vinculando los monederos a una cuenta de Cloudflare a través de[ ](https://cloudflare.pay/)[cloudflare.pay](http://cloudflare.pay).[ Esta herramienta](https://cloudflare.pay/) permitirá a los agentes identificarse si lo desean, ya que su identidad es una delegación de la cuenta. Un agente de investigación podría estar en[ research.example.cloudflare.pay](http://research.example.cloudflare.pay), de modo que los comercios sepan que se trata de un agente de una organización concreta. Este enfoque permitirá a los agentes mantener identidades coherentes y permanentes, mejorando así la experiencia para todos. Será totalmente opcional que los agentes elijan si quieren revelar su identidad o no, y serán las empresas las que decidan si quieren dar prioridad a las transacciones con agentes conocidos.

## **Los identificadores de los agentes deben ser legibles para las personas**

Creemos que el enfoque para tratar con los agentes será similar al que se aplica a las VPN: si alguien no está identificado, no significa que sea intrínsecamente poco fiable, pero tendrá que demostrar más su identidad. Por eso tenemos[ Turnstile](https://www.cloudflare.com/products/turnstile/) y otras iniciativas para detectar bots dentro de[ Bot Management](https://www.cloudflare.com/products/bot-management/). Nuestra primitiva de identidad se basará en este trabajo previo. Por ejemplo,[ Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) ya permite a los agentes registrar su identidad mediante un par de claves. Los Id. asociados a Cloudflare Wallets permiten que este par de claves sea legible para las personas.

Sabemos que los estándares de identidad agéntica están cambiando rápidamente, por eso queríamos que nuestro enfoque fuera sencillo. Proponemos un identificador legible para un par de claves que no lo es tanto, similar a los emparejamientos de URL y direcciones IP que se usan en el[ DNS](https://www.cloudflare.com/learning/dns/what-is-dns/). No pretendemos definir un esquema concreto ni ningún otro sistema de verificación. Solo queremos que la identidad sea fácil de recordar y de declarar. A medida que se desarrollen esquemas para enriquecer la identidad de los agentes a través de las iniciativas de la[ Fundación x402](https://blog.cloudflare.com/x402/), intentaremos adoptarlos y animaremos a otros a hacer lo mismo.

## **El futuro del comercio agéntico**

En Cloudflare, queremos ofrecer todos los elementos básicos para que el comercio agéntico sea un éxito. Monetization Gateway ofrecerá a los vendedores una forma de cobrar sin tener que montar una infraestructura de pago tradicional. Cloudflare Wallets ofrecerá una manera para que los compradores paguen de manera autónoma a través de agentes. La identidad permitirá a los comercios comunicarse con compradores que se identifiquen o aplicar requisitos de identificación.

Todos estos bloques de creación crearán una plataforma de comercio electrónico de arquitectura abierta para Internet. Si te interesa y quieres participar, ya [ puedes reservar tu nombre de usuario](https://cloudflare.pay/). Estamos deseando ver lo que desarrollas y monetizas.

]]>01KZB51E9A2PC0241XZGJVZQBRNovedad: Billable Usage API, visibilidad programática de los costes en Cloudflarehttps://blog.cloudflare.com/es-es/billable-usage-api/ Thu, 06 Aug 2026 07:09:41 GMTCloudflare ha lanzado Billable Usage API (API de uso facturable) para cuentas, que ofrece a los desarrolladores y a los equipos de operaciones financieras visibilidad programática, a través de un único punto de acceso, sobre los costes y el uso de todos los productos de autoservicio. Basada en el estándar FOCUS, te permite realizar un seguimiento del gasto de forma integrada junto con el resto de tu infraestructura en la nube.Agents WeekAPIBillingDesarrolladoresIngenieríaNoticias de productosLa Agents Week trata sobre el cambio que ya está en marcha. Los agentes escriben código, implementan Workers y aprovisionan infraestructura en tu nombre. Ese cambio modifica lo que necesitas ver. Si un programa está gastando dinero en tu cuenta de Cloudflare, necesitas saber en qué lo gasta; a lo largo del día, por producto, en un formato que otro programa pueda procesar. El panel de control es la respuesta adecuada para las personas. No es la respuesta correcta para la automatización.

Así que vamos a lanzar una nueva **Billable Usage API** para cuentas de autoservicio: un único punto de acceso que te muestra el uso y el coste de tu cuenta, desglosados por producto y por periodo de servicio. Abarca todos los productos de Cloudflare basados en el uso que tengas en la cuenta, como Workers, R2, D1, Workers AI, Vectorize, Images y Stream, todo con una sola llamada. Y si ya trabajas con una cadena de herramientas de operaciones financieras, los nombres de las columnas te resultarán familiares.

Recibirás un código de estado `HTTP 200 OK` con `Content-Type: application`/`json` y las filas de uso en el cuerpo de la respuesta. Actualmente, los datos de uso y coste se actualizan a diario, aunque seguimos trabajando para ofrecer más datos en tiempo real.

## **¿Qué resultados se obtienen?**

Cada fila de la respuesta corresponde a un periodo de facturación de un producto de tu cuenta.

  * `ServiceName` y `ServiceFamilyName` — qué producto ("Workers Standard" dentro de la familia "Workers", "almacenamiento R2" dentro de "R2", etc.).
  * `ChargePeriodStart` / `ChargePeriodEnd` — el intervalo de tiempo que abarca esta fila.
  * `PricingQuantity` y `ConsumedUnit` — cuánto has usado, en la unidad de medida con la que facturamos (GB-meses, GB-segundos, solicitudes, etc.).
  * `ContractedCost` — lo que costó ese periodo, en `BillingCurrency`.
  * `CumulatedPricingQuantity` y `CumulatedContractedCost` — totales acumulados para el periodo de facturación.
  * `ZoneId` / `ZoneName` — cuando el uso se atribuye a una zona específica.



La mayoría se corresponden directamente con las columnas de la[ Especificación Abierta de Costes y Uso de Operaciones Financieras (FOCUS)](https://focus.finops.org/), por lo que si tu equipo ya está incorporando datos de FOCUS de otro proveedor, los nombres y la semántica deberían resultar familiares:

**Campo de Cloudflare**| **Columna FOCUS**| **Notas**  
---|---|---  
`BillingCurrency`| `BillingCurrency`| Coincidencia exacta.  
`BillingPeriodStart`| `BillingPeriodStart`| Coincidencia exacta.  
`ChargePeriodStart` / `ChargePeriodEnd`| `ChargePeriodStart` / `ChargePeriodEnd`| Coincidencia exacta.  
`ServiceName`| `ServiceName`| Coincidencia exacta.  
`ConsumedQuantity` / `ConsumedUnit`| `ConsumedQuantity` / `ConsumedUnit`| Coincidencia exacta.  
`PricingQuantity`| `PricingQuantity`| Coincidencia exacta.  
`ContractedCost`| `ContractedCost`| Coincidencia exacta.  
`ServiceFamilyName`| (Cerca de `ServiceCategory`)| Agrupación propia de Cloudflare; FOCUS utiliza un vocabulario controlado.  
`CumulatedContractedCost`| (Derivado)| Campo de conveniencia — FOCUS considera la acumulación como un problema de consulta.  
`ZoneId` / `ZoneName`| (Cerca de `ResourceId` / `ResourceName`)| Identificador con ámbito de zona donde sea aplicable.  
  
Las respuestas utilizan la estructura estándar de la API de Cloudflare: el `resultado` es una matriz de filas, una por producto y por periodo de facturación, junto con información sobre el `éxito`, los `errores` y los `mensajes`.

## **En qué punto estamos con FOCUS**

La coincidencia con el nombre de FOCUS fue una elección deliberada. AWS, Azure, Google Cloud, Oracle y una lista cada vez mayor de proveedores de SaaS ya publican exportaciones con el formato FOCUS, y todas las herramientas serias de gestión de costes son compatibles con él. Dicho esto, por ahora aún no cumplimos al 100 % con el estándar FOCUS: algunos de los campos obligatorios todavía no aparecen en la respuesta. Llegar a ese punto forma parte de nuestra hoja de ruta. Tómatelo como un primer paso: ahora ya tienes una idea general, y lo siguiente será el cumplimiento total.

## **El gasto en Cloudflare, junto con el resto de tu gasto en la nube | Nuestra colaboración con Vantage**

Nos hemos asociado con[ Vantage](https://www.vantage.sh/) en una integración nativa de Cloudflare. Vantage es una plataforma de gestión de costes de infraestructura que recopila datos de costes y uso de más de 30 proveedores — entre los que se incluyen proveedores de IA, de nube y de SaaS — y los reúne en una única vista para la elaboración de informes, asignación y optimización. Con esta integración, tu uso se incluye en los mismos informes de costes, presupuestos y alertas de costes que ya utilizas para el resto de tu infraestructura.

Vantage se conecta a Cloudflare mediante un token de API de solo lectura con acceso de lectura a la facturación. Una vez conectado, Vantage extrae a diario tus datos de Billable Usage y los desglosa por producto (como Workers y R2), zona y cuenta, para que puedas ver qué productos generan más gasto y asignarlo a los equipos y servicios responsables.

Estos son algunos de los flujos de trabajo que admite esta integración:

  * **Asignación entre proveedores.** Analiza el gasto de Cloudflare por producto, zona y cuenta, y luego usa las etiquetas virtuales para desglosarlo por equipo o línea de productos junto con los costes de AWS, Azure y otros proveedores, todo en un único informe.
  * **Detección de anomalías.** Las alertas de costes de Vantage supervisan todos los proveedores conectados y te avisan por Slack o correo electrónico cuando el gasto se desvía de su nivel de referencia, de modo que cualquier cambio en el gasto de Workers o R2 se detecta igual que con cualquier otro proveedor.
  * **Agentes de operaciones financieras y Protocolo de Contexto de Modelo (MCP).** Hazle una pregunta al agente de operaciones financieras de la consola de Vantage, como por ejemplo: "¿Cuál fue nuestro mayor factor de coste la semana pasada entre todos los proveedores?", o consulta los mismos datos de Claude o ChatGPT a través del servidor MCP alojado de Vantage. El gasto de Cloudflare se incluye junto con tus otros proveedores conectados.



Conecta tu cuenta de Cloudflare en la[ consola de Vantage](https://console.vantage.sh/), y tus costes aparecen junto a todo lo demás que ejecutas. No hay que hacer exportaciones manuales, ni subir facturas, ni mantener un panel de control aparte. 

Esta API estandarizada de FOCUS también funciona con otras herramientas de tecnología financiera.

## **Por qué lo hemos desarrollado**

Los agentes hacen más que escribir código. Implementan Workers, aprovisionan buckets de R2 y gestionan bases de datos de D1. Cuando concedes acceso programático a tu cuenta de Cloudflare, necesitas saber exactamente cuánto te está costando. No al final del mes, sino a lo largo del día, por producto, en un formato que un programa pueda realmente procesar.

Billable Usage API es justo lo que necesitas. Y los clientes llevan años pidiéndonos el uso programático. Los equipos financieros quieren incorporar los gastos a sus propios sistemas y asignar los costes a proyectos internos, equipos e incluso a sus clientes finales. Los desarrolladores quieren un comando `curl que puedan meter directamente en un script. Antes, cada uno de esos procesos requería una captura de pantalla o una exportación manual. Ahora basta con una llamada HTTP o una configuración en Vantage.

## **¿Y ahora qué?**

  * **Intervalos de tiempo más precisos.** Hoy en día, la API devuelve filas por periodo de facturación, que para la mayoría de los productos es diario. Estamos considerando desgloses en tiempo real más detallados para los productos donde tenga sentido.
  * **Previsiones.**`CumulatedContractedCost` te indica en qué punto del ciclo de facturación actual te encuentras en cuanto al gasto. Queremos ayudarte a predecir cuál será el resultado final. Y no solo a nivel de cuenta, sino también a nivel de producto.
  * **Cobertura para empresas.** Esta primera versión es solo de autoservicio. Estamos trabajando en una experiencia equivalente para los contratos Enterprise.



## **Pruébalo**

El punto final está activo hoy para todas las cuentas de autoservicio. Consigue un token de API con permiso de _lectura de facturación_ , dirige tu comando `curl` hacia él y obtendrás tu periodo de facturación actual desglosado por producto. La referencia completa está disponible en la documentación de la API de Cloudflare. Para verlo junto al resto de tu gasto en la nube, conecta tu cuenta de Cloudflare en la[ consola Vantage](https://console.vantage.sh/).

Cloudflare lleva años trabajando para que te resulte más fácil ejecutar una mayor parte de tu pila en nuestra red. Ya es hora de que te pongamos igual de fácil ver cuánto te está costando todo esto, tanto en Cloudflare como en cualquier otro sitio.

]]>01KZAXPNXMNXCD918P6B9M5K4JTu agente necesita un ordenador, no un contenedor. Llega @cloudflare/computerhttps://blog.cloudflare.com/es-es/cloudflare-computer/ Wed, 05 Aug 2026 06:44:26 GMTLos agentes necesitan algo más que un contenedor para escalar. Anunciamos @cloudflare/computer, un entorno de ejecución para agentes que combina de forma dinámica aislamientos rápidos y eficientes con contenedores Linux completos para que cada agente tenga su propio ordenador.AgentesAgents WeekAICloudflare WorkersContenedoresLos agentes más competentes tienen algo muy sencillo en común: les dan su propio ordenador para trabajar.

Los agentes de codificación funcionan de esta manera. Les das un sistema de archivos, un shell, herramientas, paquetes y la posibilidad de ejecutar código. Analizan el entorno, hacen cambios, prueban lo que han hecho y siguen adelante. El ordenador le da al modelo una forma familiar de interactuar con el mundo. En Cloudflare, estamos trabajando duro para ofrecer las primitivas adecuadas sobre los que desarrollar los agentes más eficaces.

**Hoy te presentamos una vista previa preliminar de[ @cloudflare/computer](https://github.com/cloudflare/workspace).** El paquete @cloudflare/computer ofrece un entorno de ejecución para agentes en el que la plataforma se encarga de los detalles y la mecánica de qué código se ejecuta en un aislamiento y qué se ejecuta en un entorno de pruebas de contenedor. Cada agente tiene un ordenador, y el entorno de ejecución se optimiza para garantizar la eficiencia y la escalabilidad.

Creemos que, para satisfacer la creciente demanda de recursos de computación que requieren los sistemas basados en agentes, tenemos que buscar soluciones que vayan más allá de la contenedorización tradicional. 

## El cambio en la forma de crear agentes

Hemos visto cómo esta historia ha ido cambiando poco a poco en los últimos seis meses. A principios de año, lo habitual era crear un contenedor y ejecutar un agente dentro de él. En los últimos meses, hemos visto cómo se ha generalizado rápidamente el uso de entornos de agentes que permiten ejecutar código en un entorno aislado a través de herramientas. Esto separa las "manos" (el entorno aislado donde se realiza el trabajo) del "cerebro" (el bucle del agente).

Da igual dónde se ejecute el entorno de ejecución. Dotar a cada agente de un contenedor supone todo un desafío. Entre todas las nubes y todos los hiperescaladores, no hay ni de lejos suficiente capacidad de procesamiento en el mundo para que cada empresa pueda ofrecer a los agentes de sus usuarios su propio entorno de procesamiento en contenedor. Esto no se podrá ampliar a cientos de millones, ni a miles de millones, de agentes simultáneos. Por eso hay una demanda desesperada y frenética de la industria por el procesamiento con CPU, no solo GPU.

En Cloudflare llevamos mucho tiempo trabajando en este problema, creando una primitiva de procesamiento más eficiente: los aislamientos. Hicimos esa apuesta que se salía de lo habitual hace casi 10 años, [cuando lanzamos Cloudflare Workers](https://blog.cloudflare.com/introducing-cloudflare-workers/). Lo hicimos de nuevo cuando [anunciamos Durable Objects](https://blog.cloudflare.com/introducing-workers-durable-objects/) hace casi seis años. Hicimos esta apuesta porque los aislamientos son infinitamente escalables horizontalmente. Se activan y desactivan increíblemente rápido. Pueden [hibernar](https://developers.cloudflare.com/durable-objects/examples/websocket-hibernation-server/) cuando el agente está inactivo, [almacenar su propio estado](https://blog.cloudflare.com/sqlite-in-durable-objects/), e incluso [iniciar sus propios aislamientos](https://blog.cloudflare.com/dynamic-workers/) para ejecutar código no fiable. Los aislamientos son la mejor manera de escalar horizontalmente, y la escala horizontal es lo que demandan los agentes.

El año pasado, [dimos a los aislamientos la capacidad de iniciar sus propios entornos de pruebas en contenedores](https://blog.cloudflare.com/containers-are-available-in-public-beta-for-simple-global-and-programmable/). Desde el primer día, la arquitectura de Cloudflare se ha diseñado para ejecutar el conjunto de agentes en el entorno aislado (en un objeto duradero) y llamar a un contenedor asociado bajo demanda como herramienta. Esto te permite utilizar primitivas de procesamiento más pesadas solo cuando sea necesario, optimizando así el rendimiento y el coste. Durable Objects escalan infinitamente en horizontal, y el contenedor asociado permite que se escalen en vertical para realizar cualquier tarea. Así es como creamos nuestros propios agentes, y vemos que los clientes también están creando cosas increíbles de esta manera.

Pero cuando pensamos en la necesidad de contar con varias primitivas de procesamiento subyacentes para crear agentes (aislamientos y contenedores) y en que nuestros clientes y desarrolladores tienen que combinarlas ellos mismos en el espacio de usuario, creemos que podemos hacerlo mejor. Pensamos que podemos proporcionar una abstracción más sencilla.

Por eso empezamos este experimento con @cloudflare/computer como biblioteca de código abierto, para aprender junto a nuestros clientes, que están ampliando los límites de la ejecución de agentes a escala.

## Un sistema de archivos compartido entre aislamientos y contenedores

El paquete @cloudflare/computer parte de una premisa sencilla: ¿qué pasaría si le diéramos a un agente un sistema de archivos ya preparado, definido de forma descriptiva, que contuviera todo lo necesario para la tarea en cuestión y una selección de entornos de ejecución para trabajar con esos archivos, cada uno con sus propias ventajas e inconvenientes en cuanto a velocidad, capacidad y coste?

Resulta que los agentes de hoy en día son sorprendentemente capaces de seleccionar el entorno adecuado para la tarea en cuestión. Una tarea que solo tenga que manipular archivos, procesar datos o gestionar un repositorio de Git se puede ejecutar dentro de un aislamiento. Un comando que necesita Linux, `npm`, o un binario nativo puede ejecutarse dentro de un contenedor. Ambos trabajan con los mismos archivos que se mantienen sincronizados con el sistema de archivos de origen.

El paquete @cloudflare/computer ofrece un sistema de archivos duradero que puedes usar con repositorios de Git, buckets de almacenamiento o cualquier archivo que elijas. Proporciona herramientas que te permiten leer, escribir y editar archivos usando [Code Mode](https://blog.cloudflare.com/code-mode/) o comandos de Bash. Todas las operaciones están controladas, auditadas y supervisadas, lo que te da un control muy preciso sobre los cambios que el agente puede realizar, además de un registro claro que muestra lo que ha hecho el agente.

## Cómo utilizas la IA

Se puede crear una instancia de un espacio de trabajo @cloudflare/computer en cualquier Durable Object para proporcionar un sistema de archivos virtual y un entorno de ejecución.

Se instala a través de npm:

El caso de uso principal es proporcionar ese sistema de archivos y herramientas a un agente. Por ejemplo, así es como se instancia el espacio de trabajo en un agente basado en @cloudflare/think destinado a clasificar informes de errores.

El paquete @cloudflare/computer incluye varios backends de ejecución, aunque también puedes escribir el tuyo propio. Aquí conectamos un contenedor de Cloudflare.

Utiliza las herramientas de gestión de archivos, Git y el shell, junto con las herramientas específicas del producto, para resolver los problemas que se hayan notificado.

El modelo puede usar herramientas durante el bucle del agente, pero también puedes usar directamente la API del espacio de trabajo, por ejemplo, para preparar el entorno antes de darle instrucciones al agente.

Échale un vistazo al [repositorio de Workspace](https://github.com/cloudflare/computer) para ver más ejemplos de cómo usar los diferentes backends y herramientas, incluido un [tutorial paso a paso ](https://github.com/cloudflare/computer/tree/main/examples/tutorial)que te guía en la creación de un agente desde cero.

## Cómo funciona

La pieza clave de @cloudflare/computer es el espacio de trabajo. Un sistema de archivos virtual basado en SQLite que se puede alimentar desde diversas fuentes, como el almacenamiento en la nube y el control de versiones.

El espacio de trabajo admite entornos de ejecución opcionales que permiten ejecutar código en el sistema de archivos. Todos los entornos de ejecución admiten la misma interfaz `exec(string, options)` y, de momento, vienen dos ya integrados (aunque puedes crear el tuyo propio):

  * Un entorno de ejecución basado en aislamientos que utiliza [just-bash](https://justbash.dev/) para traducir código de shell en JavaScript se ejecuta en un [Worker dinámico](https://developers.cloudflare.com/dynamic-workers/). Aquí, puedes acceder directamente al sistema de archivos a través de los enlaces de Workers.
  * Un entorno de ejecución de contenedores que utiliza [contenedores de Cloudflare](https://developers.cloudflare.com/containers/) para proporcionar un entorno Linux completo. Aquí, el sistema de archivos se proporciona a través de un montaje FUSE (Filesystem in Userspace), lo que garantiza que los archivos estén disponibles para el contenedor y que los cambios se sincronicen de vuelta.



La clase `Workspace` ofrece una interfaz API para manipular directamente el sistema de archivos, además de un envoltorio compatible con `node:fs`, para que puedas usarla fácilmente con bibliotecas de JavaScript de terceros.

Para que lo usen los agentes, os ofrecemos un kit de herramientas compatible con el SDK de IA que incluye las herramientas más habituales: read, write, edit, ls y exec. La herramienta exec es un poco especial, ya que funciona en todos los entornos de ejecución y admite un argumento `backend`. La descripción de la herramienta te ayuda a elegir el entorno de ejecución adecuado para la tarea que tengas entre manos: o bien un backend de trabajo rápido y económico, o bien el contenedor con todas las funciones. En nuestras pruebas, los modelos Frontier se han demostrado muy eficaces a la hora de tomar la decisión correcta y recurrir al uso de contenedores solo cuando es necesario.

## ¿Y ahora qué?

Aquí en Cloudflare ya vemos cómo algunos agentes usan exclusivamente aislamientos para desarrollar, probar e implementar aplicaciones de JavaScript con herramientas modernas, generar documentación a medida para cada uno de nuestros clientes y utilizar navegadores web para realizar tareas complejas.

Nuestro objetivo con @cloudflare/computer es ofrecer un agente con un entorno de ejecución en el que solo se necesite un contenedor para menos del 10 % de su trabajo, y en el que las tareas de programación, la manipulación de audio y vídeo y la creación de documentos se puedan gestionar mediante aislamientos. 

Prueba hoy mismo una [versión preliminar](https://github.com/cloudflare/computer). Estamos deseando saber qué te parece.

]]>01KZ8AC3KWN622R3CM5QDVQ1MV
