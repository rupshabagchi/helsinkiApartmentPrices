#so lets start with condition, total size, number of rooms, built year
#postal code

postalCodes <- unique(rd$postal_code)
rd[1,]
coefs <- matrix(data = NA, ncol = length(postalCodes) + 1, nrow = 6)
a <- as.character(postalCodes)
colnames(coefs) <- c('avg', a)

srd <- subset(rd, rd$type=="kerrostalo")
lev <- levels(srd$condition)
val <- srd$condition==lev[1]
eka <- lm(srd$rentC ~ srd$condition + srd$total_size)$coefficients
plot(srd$total_sizeC, srd$rentC, col=alpha(c('red', 'green', 'blue', 'black'), 0.7)[srd$condition])
lines(x = srd$total_sizeC, y = eka[1]+eka[2]+eka[5]*srd$total_sizeC)
lines(x = srd$total_sizeC, y = eka[1]+eka[3]+eka[5]*srd$total_sizeC, col='red')
lines(x = srd$total_sizeC, y = eka[1]+eka[4]+eka[5]*srd$total_sizeC, col ='blue')

plot(srd$total_sizeC[val], srd$rentC[val], col='green')
lines(x = srd$total_sizeC, y = eka[1]+eka[2]+eka[5]*srd$total_sizeC)
lines(x = srd$total_sizeC, y = eka[1]+eka[3]+eka[5]*srd$total_sizeC, col='red')
lines(x = srd$total_sizeC, y = eka[1]+eka[4]+eka[5]*srd$total_sizeC, col ='blue')

srd$total_sizeC[val]
table(srd$condition)
eka

srd <- subset(rd, rd$type=="kerrostalo")
lev <- levels(srd$condition)
val <- srd$condition==lev[2]
toka <- lm(log(srd$rentC) ~ srd$condition + srd$total_sizeC)$coefficients
plot(srd$total_sizeC[val], srd$rentC[val], col=alpha(c('red', 'green', 'blue', 'black'), 0.7)[srd$condition])
points(x = srd$total_sizeC, y = exp(toka[1]+toka[3]+toka[5]*srd$total_sizeC))
toka
cor(srd$rentC[val],exp(toka[1]+toka[3]+toka[5]*srd$total_sizeC[val]) )
cor(srd$rentC[val],eka[1]+eka[2]+eka[5]*srd$total_sizeC[val] )
sum(val)
lev
toka

toka
## is good
toka <- lm(log(srd$rentC) ~ srd$condition + srd$total_sizeC)$coefficients

#lets look at built_year
by <- lm(srd$rentC ~ srd$built_year)$coefficients
by
plot(srd$built_year, srd$rentC)
points(x = srd$built_year, y = exp(toka[1]+toka[2]+toka[5]*srd$total_sizeC), col='red')
points(x = srd$built_year, y = by[1]+by[2]*srd$built_year, col='green')

plot(srd$total_sizeC, srd$rentC)
points(x = srd$total_sizeC, y = by[1]+by[2]*srd$built_year, col='green')
points(x = srd$total_sizeC, y = exp(toka[1]+toka[2]+toka[5]*srd$total_sizeC), col='red')

kolmas <- lm(log(srd$rentC) ~ srd$condition + srd$total_sizeC + srd$built_year)$coefficients
kolmas

pisteet <- exp(kolmas[1]+kolmas[2]+kolmas[5]*srd$total_sizeC+kolmas[6]*srd$built_year) + exp(kolmas[1]+kolmas[3]+kolmas[5]*srd$total_sizeC+kolmas[6]*srd$built_year) + exp(kolmas[1]+kolmas[4]+kolmas[5]*srd$total_sizeC+kolmas[6]*srd$built_year)
pisteet
pist <- pisteet/3
points(x = srd$total_sizeC, y = exp(kolmas[1]+kolmas[2]+kolmas[5]*srd$total_sizeC+kolmas[6]*srd$built_year), col='green')
cor(srd$rentC, exp(kolmas[1]+kolmas[2]+kolmas[5]*srd$total_sizeC+kolmas[6]*srd$built_year))

points(x = srd$total_sizeC, y = exp(kolmas[1]+kolmas[2]*as.numeric(srd$condition)+kolmas[3]*as.numeric(srd$condition)+kolmas[4]*as.numeric(srd$condition)+kolmas[5]*srd$total_sizeC+kolmas[6]*srd$built_year), col='red')
kolmas[2]*as.numeric(srd$condition)
plot(srd$total_sizeC, srd$rentC)
points(srd$total_sizeC, pist, col='red')
length(srd$total_sizeC)
length(pist)
cor(srd$rentC, pist)
sd(srd$rentC[srd$postal_code==00140])

#okey lest see
kolmas1 <- lm(log(srd$rentC) ~  srd$condition + srd$total_sizeC + srd$built_year)$coefficients
kolmas1
malli <- kolmas1
plot(srd$rentC,srd$X)
k <- lm(srd$rentC ~srd$condition)$coefficients
plot(y=srd$rentC, x=srd$total_sizeC, col ='white')
points(srd$total_sizeC[srd$condition=='ei luokiteltu'], srd$rentC[srd$condition=='ei luokiteltu'], col='red')
points(srd$total_sizeC[srd$condition=='hyvä'], srd$rentC[srd$condition=='hyvä'], col='green')
points(srd$total_sizeC[srd$condition=='tyydyttävä'], srd$rentC[srd$condition=='tyydyttävä'], col='blue')
points(srd$total_sizeC[srd$condition=='välttävä'], srd$rentC[srd$condition=='välttävä'], col='black')
abline(h = k[1], col = 'red')
abline(h=k[1]+k[3], col = 'blue' )
abline(h=k[1]+k[4], col = 'black' )
abline(h=k[1]+k[2], col = 'green' )
?abline
k[1]*k[3]
kolmas1
#price for this:
dummy[srd$condition]
dummy <- kolmas1
dummy["srd$conditionhyvä"] <- kolmas1[1]+kolmas[2]
dummy["srd$conditiontyydyttävä"] <- kolmas1[1]+kolmas[3]
dummy["srd$conditionvälttävä"] <- kolmas1[1]+kolmas[4]
dummy["srd$conditionhyvä"] <- kolmas1[1]+kolmas[2]
dummy

plot(y=srd$rentC, x=srd$total_sizeC)
points(x = srd$total_sizeC, y = exp(dummy[srd$condition] + kolmas1[5]*srd$total_sizeC+kolmas1[6]*srd$built_year), col = 'red')
y = exp(dummy[srd$condition] + kolmas1[5]*srd$total_sizeC+kolmas1[6]*srd$built_year)
cor(srd$rentC, y)
levels(srd$condition)
#testing
pc1 <- lm(srd$rentC ~srd$postal_codeC)$coefficients
pc2 <- lm(srd$rentC ~srd$postal_codeC + srd$condition)$coefficients
#pc[2:length(pc)] + pc[1]
pc1[1:5]
pc1[115:120]
pc2[1:5]
pc2[120:123]
length(pc2)
plot(srd$total_sizeC[srd$postal_code==2200 & srd$condition=='ei luokiteltu'], srd$rentC[srd$postal_code==2200 & srd$condition=='ei luokiteltu'])
srd$postal_codeC[srd$condition=='ei luokiteltu']
points(srd$total_sizeC[srd$postal_code==2200 & srd$condition=='ei luokiteltu'],pc2[1]+pc2[srd$postal_code==2200], col = 'red')
pc2[srd$postal_code==2200]

rownames(coefs)  <- c('intercept', 'hyva', 'tyydyttava', 'valttava', 'totalsize', 'builtyear')
for(i in 2:4){
  kolmas1[i] <- kolmas1[1]+kolmas1[i]
}
cor(srd$rentC, exp(kolmas1[srd$condition]+kolmas1[5]*srd$total_sizeC+kolmas1[6]*srd$built_year))
y <- exp(kolmas1[srd$condition]+kolmas1[5]*srd$total_sizeC+kolmas1[6]*srd$built_year)
exp(kolmas[srd$condition]+1)
plot(srd$rentC, y)
summary(malli)

levels(srd$condition)

neljas <- lm(log(srd$rentC) ~  srd$condition + srd$total_sizeC + srd$built_year + srd$postal_codeC)
neljas2 <- neljas$coefficients
neljas2[2:4] + neljas2[1]
neljas2[7:length(neljas2)] + neljas2[1]
price <- exp(neljas2[srd$condition]+ neljas2[srd$postal_codeC]+neljas2[5]*srd$total_sizeC+neljas2[6]*srd$built_year)
cor(price2, srd$rentC)
neljas2[srd$postal_codeC][is.na(price)]
neljas2[srd$condition]
neljas2[srd$postal_codeC]
neljas2[srd$condition[1:10]]
srd[is.na(price),]
length(neljas2)-6
length(postalCodes)
price2 <- subset(price, !is.na(price))
length(price2)
str(price2)
price2
neljas2[srd$condition[1:5]]+ neljas2[srd$postal_codeC[1:5]]+neljas2[5]*srd$total_sizeC[1:5]+neljas2[6]*srd$built_year[1:5]
neljas
kolmas1
plot(srd$built_year, srd$rentC)
points(srd$built_year, y, col='red')


kolmas1[1]
coefs[1,1] <- kolmas1[1]
coefs[,1] <- kolmas1
coefs

#now the postal codes
for (i in postalCodes){
ii <- as.character(i)
print(i)
datapoints <- subset(rd, rd$postal_code==i)
if(length(datapoints[,1])<3){
  coefs[,ii] <- coefs[,'avg']
  next
}
if(length(datapoints[,1]) > 10){
  model <- lm(log(datapoints$rentC) ~  datapoints$condition + datapoints$total_sizeC + datapoints$built_year)$coefficients
  l <- length(model)-2
  model[2:l] <- model[2:l] + model[1]
  if(sum(is.na(model)==0)){
  coefs[c('intercept', 'hyva', 'tyydyttava', 'totalsize', 'builtyear'),ii] <- model
  }
  if(sum(is.na(model)>0)){
  coefs[,ii] <- coefs[,'avg']
  }
}
if(length(unique(datapoints$condition)) <= 2){
  model <- lm(log(datapoints$rentC) ~  datapoints$total_sizeC + datapoints$built_year)$coefficients
  if(sum(is.na(model)>0)){
    coefs[,ii] <- coefs[,'avg']
  }
  if(sum(is.na(model)==0)){
    coefs[c('intercept', 'totalsize', 'builtyear'), ii] <- model
  }
  }
}
rd[rd$postal_code==890,]
lm(rd$rentC[rd$postal_code==890]~rd$total_sizeC[rd$postal_code==890] + rd$built_year[rd$postal_code==890])
postalCodes[2:2] + 2
postalCodes[2:2]
coefs
table(rd$condition)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
coefs[c('intercept', 'hyva', ''),'avg']
coefs
kolmas1
coefsTest1 <- coefs
for (i in 1:6){
  coefsTest1[i,][is.na(coefsTest1[i,])] <- coefsTest1[i,1]
}
dd <- coefsTest2[,'100']
exp(dd['hyva']+dd['totalsize']*70+dd['builtyear']*1990)
rd[rd$postal_code==100,]
coefsTest2[,'100']
kolmas1
coefsTest1['builtyear',]
coefs
coefsTest2 <- coefsTest1
coefsTest2['builtyear',][coefsTest2['builtyear',] >0] <- coefs['builtyear','avg']
levels(rd$condition)
rownames(coefsTest2) <- c("intercept","hyva","tyydyttava","valttava","totas", "builtyear")

plot(rd$X, rd$rentC, col='white')
rownames
x  = 1
for(i in a){
  print(i)
dd <- coefsTest2[,i]
j <- rd[postal_codeC==as.numeric(i),]
print(exp(dd[as.character(j$condition)]+dd['total_size']*j$total_sizeC+dd['built_year']*j$built_year))
points(j$X, exp(dd[as.character(j$condition)]+dd['total_size']*j$total_sizeC+dd['built_year']*j$built_year))
}
coefsTest2
dd <- coefsTest2[,'100']
mean(rd$rentC[rd$postal_codeC==00150])

pc=120
t <- 'intercept'
m2 <- 40
ya <- 1966
a <- coefsTest2[,as.character(pc)]
a
exp(a[t]+a['totas']*m2+a['builtyear']*ya)
str(rd[postal_codeC==pc,])
mean(rd$built_year[rd$postal_codeC==pc])
mean(rd$total_sizeC[rd$postal_codeC==pc])
exp(kolmas1[])
x = 1

plot(x=1:136, y = c(1:136)*30, col='white')
for (i in a){
  dd <- coefsTest2[,'avg']
  pris <- exp(dd['intercept']+dd['totas']*mean(rd$total_sizeC[rd$postal_codeC==as.numeric(i)])+dd['builtyear']*mean(rd$built_year[rd$postal_codeC==as.numeric(i)]))
  print(pris)
  print(mean(rd$rentC[rd$postal_code==as.numeric(i)]))
  points(x, mean(rd$rentC[rd$postal_code==as.numeric(i)]), col = 'red')
  points(x, exp(dd['hyva']+dd['totas']*mean(rd$total_sizeC[rd$postal_codeC==as.numeric(i)])+dd['builtyear']*mean(rd$built_year[rd$postal_codeC==as.numeric(i)])))
  x = x +1
   }
coefsTest2
length(a)
rd$postal_code == as.numeric(a)
coefsTest2
kolmas1
kolmas1
eka
tt <- lm(rd$rentC ~ rd$total_sizeC)$coefficients
tt[2:length(tt)-1] <- tt[2:length(tt)-1]+tt[1]
plot(rd$total_sizeC, exp(tt[rd$postal_codeC]+tt[length(tt)]*rd$total_sizeC))
tt[rd$postal_code]
rd$postal_code[1:10]
plot(rd$total_sizeC, tt[1]+tt[2]*rd$total_sizeC)
points(rd$total_sizeC, rd$rentC, col='red')
plot(rd$total_sizeC, tt[paste("rd$postal_codeC", rd$postal_code, sep="")]+ tt[2]*rd$total_sizeC)
tt[2]
plot(rd$total_sizeC, (tt[1]+tt[2]*rd$total_sizeC))
points(rd$total_sizeC*0.1, (tt[1]+tt[2]*rd$total_sizeC))
tt[2]

toka
toka[2:4] <- toka[2:4]+toka[1]
toka
rd$condition
toka2 <- lm(log(rd$rentC) ~ rd$condition + rd$total_sizeC)$coefficients
plot(rd$total_sizeC,rd$rentC)
points(x = rd$total_sizeC, y = exp(toka2[1]+toka2[5]*rd$total_sizeC), col='red')
toka
