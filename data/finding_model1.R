getwd()
rentdata <- read.csv('formatted_full_data.csv', stringsAsFactors = T)

#rentdata$X <- NULL

rentdata$rent <- as.character(rentdata$rent)
rentdata[1,]

#total size
a <- gsub("[^[:digit:]., ]", "", rentdata$total_size)
b <- str_sub(a, 1, str_length(a)-1)
c <- gsub(",", '.', b, fixed = T)
d <- as.numeric(c)
rentdata$total_sizeC <- d
rentdata[1,]

#rent
e <- gsub(" ", "", rentdata$rent, fixed = TRUE)
e
a <- gsub("[^[:digit:]., ]", "", rentdata$rent)
a
b <- str_sub(a, 1, str_length(a)-1)
b
c <- gsub(",", '.', b, fixed = T)
c
d <- as.numeric(c)
d
rentdata$rentC <- d
rentdata[1,]
rentdata[,c('rent', 'rentC')]

rentdata$postal_codeC <- as.factor(rentdata$postal_code)


rd <- subset(rentdata, select = c(X,allow_pets, built_year, condition, number_of_rooms, postal_code, postal_codeC, rentC, total_sizeC, type))
rd <- subset(rd, rentC != 25000)
rd <- subset(rd, type != 'varastotila')
r <- rd$rentC
n <- names(rd)

plot(rd$allow_pets, r)
sum(rd$allow_pets=='sallittu')
table(rd$allow_pets)
#only 8 apartments allow pets, so maybe not smart to use

plot(rd$built_year, r)
rd[rd$built_year < 1500,]
# one apartment with built_year about 1400
#not anymore in vuokraovi so remove that
rd <- subset(rd, built_year>1500)
r <- rd$rentC
plot(rd$built_year, r)
cor(rd$built_year, r)
#correlation is very weak -0.11, so probably not important

plot(rd$condition, r)
plot(r, rd$condition)
cor(as.numeric(rd$condition), rd$rentC)
sum(as.numeric(rd$condition)==1)
#0.03 correlation, so probably not important
#also there is 1913 "hyvä" conditions and 188 "ei luokiteltu", so 
# difficult to find much

plot(rd$number_of_rooms, r)
cor(rd$number_of_rooms, r)

a <- as.character(rd$number_of_rooms)
huoneet <- c("YksiÃ¶","Kaksio", "3 huonetta", "4 huonetta", "5 +")
for(i in 1:5){
  a[a==huoneet[i]] <- i
}
b <- as.numeric(a)
b[1:20]
rd$number_of_rooms[1:20]

rd$number_of_roomsC <- b
n <- names(rd)

plot(rd$number_of_roomsC, r)
cor(rd$number_of_roomsC, r)
#very strong correlation of 0.633, so we should look at this
#Though this might be same as size

#postal code will be dealt with by dividing the data
plot(rd$postal_codeC, r)
plot(r, rd$postal_codeC)
#looks like it doesn't have much effect?
a <- rd$rentC/rd$total_sizeC
#maybe it has effect on the ???/sqm?
min(a)
max(a)
rd$epsm <- a
plot(rd$epsm, rd$postal_codeC)
plot(rd$total_sizeC, rd$postal_codeC)
plot(rd$postal_codeC, rd$total_sizeC)
cor(rd$postal_code, rd$total_sizeC)
#maybe something, hard to say

plot(rd$number_of_roomsC, r)


tots <- lm(r ~rd$total_sizeC)$coefficients
tots
plot(rd$total_sizeC, r)
lines(x = rd$total_sizeC, y = tots[1] + tots[2]*rd$total_sizeC, col='red')

totr <- lm(r ~rd$number_of_roomsC)$coefficients
plot(rd$number_of_roomsC, r)
lines(x = rd$number_of_roomsC, y = totr[1] + totr[2]*rd$number_of_roomsC, col='red')
tots[1]+70*tots[2]
plot(rd$total_sizeC, r, col=alpha(c('red', 'green', 'blue', 'purple', 'black'), 0.7)[rd$number_of_roomsC])
# so wee see that the number of rooms is basically the same as 
# total size
n
a <- subset(rentdata, rentdata$rentC < 10000)
plot(a$renter, a$rentC)
plot(rentdata$rentC/rentdata$total_sizeC, rentdata$renter)
plot(a$renter, a$rentC/a$total_sizeC)
a$epsm <- a$rentC/a$total_sizeC
b <- sort(a$epsm, decreasing = T)
table(a$renter[a$epsm > 32])[table(a$renter[a$epsm > 32])>1]
table(rd$type)
n
