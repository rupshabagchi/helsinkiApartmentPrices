stuff <- read.csv('formatted_full_data.csv', stringsAsFactors = F, colClasses = cols)
stuff <- subset(stuff,!grepl("Forenom", stuff$renter))

stuff[1,]
stuff$X <- NULL
#total size
a <- gsub("[^[:digit:]., ]", "", stuff$total_size)
b <- str_sub(a, 1, str_length(a)-1)
c <- gsub(",", '.', b, fixed = T)
d <- as.numeric(c)
stuff$total_sizeC <- d
stuff[1,]

#rent
e <- gsub(" ", "", stuff$rent, fixed = TRUE)
e
a <- gsub("[^[:digit:]., ]", "", stuff$rent)
a
b <- str_sub(a, 1, str_length(a)-1)
b
c <- gsub(",", '.', b, fixed = T)
c
d <- as.numeric(c)
d
stuff$rentC <- d
stuff[1,]
stuff[,c('rent', 'rentC')]

#condition
a <- as.factor(stuff$condition)
b <- as.numeric(a)
c <- b
stuff$conditionC <- c
stuff[,c('condition', 'conditionC')]
#0 = not defined, 1..3 = hyvä, tyydyttävä, välttävä

stuff$X <- NULL
stuff[1,]

#allow_pets
a <- as.factor(stuff$allow_pets)
b <- as.numeric(a)
c <- b
stuff$allow_petsC <- c
#0 = not allowed, 1 = not known 2 = sallittu

#number of rooms
a <- stuff$number_of_rooms
huoneet <- c("YksiÃ¶","Kaksio", "3 huonetta", "4 huonetta", "5 +")
for(i in 1:5){
  a[a==huoneet[i]] <- i
}
b <- as.numeric(a)
b[1:20]
stuff$number_of_rooms[1:20]

stuff$number_of_roomsC <- b
stuff[1,]

#type
a <- as.factor(stuff$type)
levels(a)
b <- as.numeric(a)
c <- b
stuff$typeC <- c
#0 = "erillistalo"
#1 = "kerrostalo"
#2 = "luhtitalo"
#3 = "omakotitalo"  
#4 = "paritalo"
#5 = "puutalo-osake"
#6 = "rivitalo"
#7 = "varastotila"

stuff[1,]
#postal_code
str(stuff$postal_code)
a <- as.numeric(stuff$postal_code)
a
stuff$postal_codeC <- a
stuff[,c('postal_code', 'postal_codeC')]


stuff <- subset(stuff, rentC != 0 & total_sizeC != 0)
#way too high rent
stuff <- subset(stuff, rentC != 123456)
#There probably isn't 1m^2 apartment
stuff <- subset(stuff, total_sizeC != 1)

plot(stuff$total_sizeC)
stuff[stuff$total_sizeC>800,]
#These look fishy, lets drop them
stuff <- subset(stuff, total_sizeC<4000)

write.csv(stuff1, file = "apartments_modeling_all.csv", row.names = F)


#for reading, if needed
colnam = c(replicate(9, "character"), replicate(8, "numeric"))
a <- read.csv('apartments_modeling.csv', stringsAsFactors = F, colClasses = colnam)
a$built_year <- as.numeric(a$built_year)