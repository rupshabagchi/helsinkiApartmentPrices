getwd()
setwd('C://Users//8560W//Documents//GitHub//helsinkiApartmentPrices//data')
cols <- c('character', 'character', 'character', 'character', 'character','character','character','character','character')
rentdata <- read.csv('apartments_new.csv', stringsAsFactors = F, colClasses = cols)

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

#condition
a <- as.factor(rentdata$condition)
b <- as.numeric(a)
c <- b
rentdata$conditionC <- c
rentdata[,c('condition', 'conditionC')]
#0 = not defined, 1..3 = hyvä, tyydyttävä, välttävä

rentdata$X <- NULL
rentdata[1,]

#allow_pets
a <- as.factor(rentdata$allow_pets)
b <- as.numeric(a)
c <- b
rentdata$allow_petsC <- c
#0 = not allowed, 1 = not known 2 = sallittu

#number of rooms
a <- rentdata$number_of_rooms
huoneet <- c("YksiÃ¶","Kaksio", "3 huonetta", "4 huonetta", "5 +")
for(i in 1:5){
  a[a==huoneet[i]] <- i
}
b <- as.numeric(a)
b[1:20]
rentdata$number_of_rooms[1:20]

rentdata$number_of_roomsC <- b
rentdata[1,]

#type
a <- as.factor(rentdata$type)
levels(a)
b <- as.numeric(a)
c <- b
rentdata$typeC <- c
#0 = "erillistalo"
#1 = "kerrostalo"
#2 = "luhtitalo"
#3 = "omakotitalo"  
#4 = "paritalo"
#5 = "puutalo-osake"
#6 = "rivitalo"
#7 = "varastotila"

rentdata[1,]
#postal_code
str(rentdata$postal_code)
a <- as.numeric(rentdata$postal_code)
a
rentdata$postal_codeC <- a
rentdata[,c('postal_code', 'postal_codeC')]

rentdata <- subset(rentdata, rentC != 0 & total_sizeC != 0)
sum(rentdata$rentC==0)
a <- rentdata$rentC/rentdata$total_sizeC
rentdata$epsm <- a
write.csv(rentdata, file = "apartments_modeling.csv", row.names = F)


#for reading, if needed
colnam = c(replicate(9, "character"), replicate(8, "numeric"))
a <- read.csv('apartments_modeling.csv', stringsAsFactors = F, colClasses = colnam)
a$built_year <- as.numeric(a$built_year)

