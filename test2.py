#install the necessary library 
install.packages("hms")
install.packages("gridExtra")
install.packages("lubridate")

#read the data 
data_2019_dec <- read.csv("dataset/2019-Dec.csv")
data_2019_nov <- read.csv("dataset/2019-Nov.csv")
data_2019_oct <- read.csv("dataset/2019-Oct.csv")
data_2020_feb <- read.csv("dataset/2020-Feb.csv")
data_2020_jan <- read.csv("dataset/2020-Jan.csv")

#look into the structure of the data 
str(data_2019_oct)
cat("\n")
str(data_2019_nov)
cat("\n")
str(data_2019_dec)
cat("\n")
str(data_2020_jan)
cat("\n")
str(data_2020_feb)
