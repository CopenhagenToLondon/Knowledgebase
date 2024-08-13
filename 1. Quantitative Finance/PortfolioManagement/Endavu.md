# Subjects

| # | Title                                     | Correspondence                   | Add. details / interpretation              |
| - |:-:                                        |:-:                               |:-:                                         |
|1| What is my return? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#1-what-is-my-return)                          | Returns          | Level: Asset Portfolio. times: Various                     | 
|2| How diversified is my portfolio? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#2-how-diversified-is-my-portfolio)           | Diversification  | Level: Portfolio. times: 1 year minimum                    | 
|3| How much market risk is in my portfolio? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#3-how-much-market-risk-is-in-my-portfolio)    | Market risk      | Level: Asset, Portfolio. times: Various                    | 
|4| how much liquidity risk is in my portfolio? [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#4-how-much-liquidity-risk-is-in-my-portfolio) | Liquidity risk   | Level: Asset, Portfolio. times: Various, less than 2 years | 
|5| General portfolio management [link](https://github.com/CopenhagenToLondon/Knowledgebase/blob/main/1.%20Quantitative%20Finance/PortfolioManagement/Endavu.md#5-general-portfolio-management)                | Optimization     | Level: Asset, Portfolio. times: Various, less than 2 years | 




## 1. What is my return?

### 1.1. What is the current year to date, year to year and absolute return for my portfolio?
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

### 1.2. What is the Risk adjusted return for my portfolio?
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

**Metode**
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

### 1.3. What is the risk adjusted return for my portfolio?

### 1.4. What is the expected return of my portfolio?




## 2. How diversified is my portfolio?

### 2.1. How well-diversified is my portfolio?

### 2.2. How concentrated is my portfolio?
Am I too heavily exposed to some industries that are inherently riskier than others?

### 2.3. Too exposed to any region/country?

### 2.4. Too exposed to any certain currency?

### 2.5. Too exposed to any asset type?

### 2.6. Are there any significant couplings in my portfolio?


## 3. How much market risk is in my portfolio?
How much can I potentially lose in a realistic but low-likelihood scenario?

### 3.1. What is the standard deviation of my portfolio?

### 3.2. How sensitive is my portfolio to market movements?

### 3.3. What is my Value at Risk?

### 3.4. What is my Conditional VAR?

### 3.5. What is my tail risk?

### 3.6. Extremal event risk?



## 4. How much liquidity risk is in my portfolio?

### 4.1. How liquid is my portfolio?


## 5. General portfolio management

### What proportion of my portfolio can be considered risky investments?

### What macroeconomic risks am i exposed to?

### How would investing in this stock impact my portfolio diversification?

### How large an exposure do I have to my short positions?

### Are my assets mostly retail investor owned or institutional investor owned?

