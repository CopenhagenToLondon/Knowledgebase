| # | Title                                     | Correspondence                   | Add. details / interpretation              |
| - |:-:                                        |:-:                               |:-:                                         |
|1| Hvad er mit afkast? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#1-what-is-my-return)                          | Returns          | Level: Asset Portfolio. times: Various                     | 
|2| How diversified is my portfolio? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#2-how-diversified-is-my-portfolio)           | Diversification  | Level: Portfolio. times: 1 year minimum                    | 
|3| How much market risk is in my portfolio? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#3-how-much-market-risk-is-in-my-portfolio)    | Market risk      | Level: Asset, Portfolio. times: Various                    | 
|4| how much liquidity risk is in my portfolio? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#4-how-much-liquidity-risk-is-in-my-portfolio) | Liquidity risk   | Level: Asset, Portfolio. times: Various, less than 2 years | 
|5| General portfolio management [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#5-general-portfolio-management)                | Optimization     | Level: Asset, Portfolio. times: Various, less than 2 years | 




# 1. Hvad er mit afkast?

## 1.1. Afkast typer
Hvis dette endnu ikke er implementeret, så vil jeg anbefale at det bliver det første der gøres.

Afkast fra års start til dagsdato.
Afkast fra nu og et år bagud.
Afkast fra nu og tilbage til første investering.

Disse er utroligt gode mål til at kigge på egne investeringers performance.
Hvis man holder disse op imod SP500, FTSE100, NASDAQ eller OMXC25 så kan man få en rigtig klar indikation af om man er over eller under middel. 

**Afkast formler**

$$r_{1} = \frac{værdi_{1} - værdi_{0}}{1-0}$$ 

$$r_{ytd} = \frac{værdi_{nu} - værdi_{1jan}}{nu-1jan}$$

$$r_{yty} = \frac{værdi_{år} - værdi_{år-1}}{år_{nu}-år_{forrige}}$$

$$r_{absolute} = \frac{værdi_{slut} - værdi_{start}}{slut-start}$$


**Metode**
1. Find start værdi og start tidspunkt - disse skal gemmes et sted
2. Find slut værdi og slut tidspunkt - findes løbende
3. Beregn forskellene slut - start
4. Regn afkast

**Kode** \
Her er en mulig python kode for intraday afkast, som kan redigeres en smule for at finde de øvrige afkast typer.
```
def returns(x, logs = False):

    if type(x) == list:
        _return = np.zeros(len(x))
        for i in range(len(x)):
            _return[i] = ((x[i]/x[i-1])-1)
    elif type(x) == pd.DataFrame:
        _return = x.pct_change().dropna()   
    else:
        _return = x.pct_change().dropna()
    
    if logs == True:
        _return = np.log(abs(_return))
    
    df = pd.DataFrame(data=_return, dtype=np.float64)
    df.columns = ["returns"]
    return(df)
```

## 1.2. Hvad er mit Risikojusterede afkast?
For at måle det risikovægted afkast kan man bruge en række forskellige måle metoder.

1. Sharpe Ratio
2. Treynor Ratio
3. Portefølje Beta

Sharpe ratio er et simpelt, men brugbart mål. Det er afkastet i perioden divideret med standard afvigelsen i perioden.\
Du får altså at vide hvor meget afkastet er i forhold til muligheden for udsving. Om sharpe ratio gælder der følgende.
![alt text](https://getmoneyrich.com/wp-content/uploads/2010/04/Sharpe-Ratio-Thumb-Rule.png)

**Sharpe, Beta og Treynor formlerne**

$$S = \frac{R_{port} - R_{free}}{std_{port}}$$

$$\beta_{port} = \frac{Covar(R_{port}, R_{market})}{Var(R_{market}}$$

$$T = \frac{R_{port} - R_{free}}{\beta_{port}}$$

**Metode**\
Denne metode anvendes til at bestemme Sharpe ratio'en for en portefølje

1. Find start værdi og start tidspunkt - disse skal gemmes et sted
2. Gem løbende værdier og tidspunkter - disse skal gemmes for at beregne standard afvigelsen.
3. Find slut værdi og slut tidspunkt - findes løbende
4. Beregn herefter afkast ligesom angivet tidligere
5. Beregn standard afvigelsen af hele tidsserien af løbende værdier
6. Regn derefter Sharpe ratio

**Kode**
```
def sharpe(data):
    s = data.iloc[0,0]
    std = np.std(data.iloc[:,0])
    s = (data.iloc[-1,0] - s) / std
    return(s)
```

## 1.3. Hvad er mit forventede afkast?
Til dette skal der bruges et større setup, som jeg ikke forventer at I hos Endavu vil ønske at udvikle som det næste.\
Dette setup var et, som LD Fonde heller ikke ønskede at sætte igang på nuværende tidspunkt. Men deres afgående head of investments havde haft det i pipelinen med Morgan Stanley i en række år. \
Man udføre en række simuleringer med forskellige scenarier, for at danne et samlet billede over hvor stort et tab man kunne ende ud med indenfor det næste år og inden for hvilket interval man ville forvente at afkastet nåede indenfor det næste år.

Almindeligevis anvendes Monte Carlo simuleringer og en række forskellige stokastiske processer såsom.
1. Geometrisk brownsk bevægelse
2. Aritmetisk Brownsk bevægelse
3. ARMA
4. ARIMA
5. ARCH
6. GARCH
7. Unikke processer af blandet art. Orhstein-Uhlenbeck, Heston modellen, $\sigma$-diffusion mm.

**Beskrivelse**\
Dette er en række metoder der bruges på højt niveau og jeg har valgt at lægge meget arbejde i dette.
Middel stigen er den stig og det afkast der er højest sandsynlighed for at modtage igennem perioden.
![](https://github.com/CopenhagenToLondon/Knowledgebase/blob/9dc051ffda0b08e68a9dc04a05db6056ca3275bf/1.%20Quantitative%20Finance/PortfolioManagement/download%20(2).png)

*Jeg ligger inde med et python bibliotek på lige præcis dette område, men jeg deler desværre ikke koden uden betaling.*

# 2. Hvor diversificeret er min portefølje?

## 2.1. Hvad er diversificeringsraten på min portefølje?
Dette kan gå i rigtigt mange niveauer

$$DR = \frac{\sigma^{t} \cdot w }{ \sqrt{w^t \cdot \Sigma \cdot w }  }$$


## 2.2. Hvor koncentreret er min portefølje?
Am I too heavily exposed to some industries that are inherently riskier than others?

### Aktiegrupperinger?
Er der nogle aktier i min portefølje som er forbundet significant?
- Co-integration?
- Copula'er?


### Lande og regioner?
Er der et bestemt land eller region, som bærer min portefølje?
F.eks. Eurozonen eller England, som ved fald i økonomien vil betyde at min portefølje falder i værdi?

### Valuta?
Er der en bestemt valuta som bærer min portefølje værdi?
F.eks. GBP, som ved et fald i valuta vil betyde at min portefølje falder i værdi?

### Aktivtyper?
Skal jeg diversificere mig ud over forskellige aktivtyper?


# 3. Hvor stor er markedsrisikoen?
1. Hvis markedet bevæger sig nedad, hvordan kan jeg så sørge for ikke at tabe noget?
2. Hvis markedet har en større nedtur, hvordan sørger jeg for ikke at tabe for meget?
3. Hvis markedet rammer et rigtigt slemt scenerie, hvordan sørger jeg for ikke at tabe for meget?

How much can I potentially lose in a realistic but low-likelihood scenario?

## 3.1. Hvad er standard afvigelsen på min portefølje?

## 3.2. Hvor sensitiv er min portefølje overfor markedet?
Dette kan være svært at måle med nogen form for konkret resultat

## 3.3. Hvad er VAR, på min portefølje?
Hvis vi rammer lige præcis 10%, hvor meget står jeg så til at tabe?

## 3.4. Hvad er CVAR, på min portefølje?
I de værste 10%, hvad er så gennemsnitstabet for mig?

## 3.5. Hvad er min hale/ekstreme risiko?
Hvis en ekstrem event sker, hvor meget står jeg så til at tabe?


# 4. Hvor stor er min likviditetsrisiko?

## 4.1. Hvor likvid er min portefølje?
handelsomkostninger?
volumehastighed?

# 5. Porteføljestyring

## Hvilken portion af mine investeringer kan siges at være risikable?
Del porteføljen op i segmenter af aktiver med niveauer af løbende standard afvigelser, likviditetsrisiko og koncentrationsforhold?

## Hvor stor en short position har jeg?
Check den procentvise størrelse af short positions i porteføljen?
Er vores samlede short position mere end 20%?

## Hvilke makroøkonomiske risici står jeg overfor?
renter
globale økonomier
employment statistics?

## hvordan ville en investering i x aktie påvirke min diversificeringsrate?
Hvis jeg køber en bestemt aktie eller obligation, vil det så hjælpe mig med at diversificere?
Har jeg nogle uforudsete købsmønstre der kan påvirke min koncentrations risiko?
Er de aktiver jeg ejer mest ejet af institutioner eller private investorer?

