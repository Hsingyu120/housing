import housing

price1 = housing.Price("c:151","Taiwan")
price2 = housing.Price("c:125","TPE_YoY")
price1.df.plot('Date','Index',title=f"Source: {price1.source} Price Index: {price1.target}",legend=False)
price2.df.plot('Date','Index',title=f"Source: {price2.source} Price Index: {price2.target}",legend=False)