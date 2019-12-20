#### Init once ###################

## install rtweet from CRAN
install.packages("rtweet")
install.packages("httpuv")
install.packages("dplyr")
install.packages("ggplot2")

## load rtweet package
library(rtweet)

## whatever name you assigned to your created app
appname <- "NetworkSentimentAnalyzer"

## api key
key <- "P7f7hSuh4Tn1FAN3w8WCdJUJa"

## api secret
secret <- "tsgnyvqemt5EXwO7swnpsH3vhSVzUmLMjWjgWQbY48u6Cx2kcC"

## create token named "twitter_token"
twitter_token <- create_token(
  app = appname,
  consumer_key = key,
  consumer_secret = secret)

## path of home directory
home_directory <- path.expand("~/")

## combine with name for token
file_name <- file.path(home_directory, "twitter_token.rds")

## save token to home directory
saveRDS(twitter_token, file = file_name)

## assuming you followed the procodures to create "file_name"
##     from the previous code chunk, then the code below should
##     create and save your environment variable.
cat(paste0("TWITTER_PAT=", file_name),
    file = file.path(home_directory, ".Renviron"),
    append = TRUE)




## get user IDs of accounts followed by "seeders"

data_path = "C:/Users/chris/Desktop/NS_Final_Project/Code/data/"

name = "759251" #cnn
data <- get_friends(name)
write.csv(data, file = paste(data_path, name, ".csv", sep=""))

name = "1367531" #foxnews
data <- get_friends(name)
write.csv(data, file = paste(data_path, name, ".csv", sep=""))

name = "25073877" #realDonaldTrump
data <- get_friends(name)
write.csv(data, file = paste(data_path, name, ".csv", sep=""))

name = "1339835893" #HillaryClinton
data <- get_friends(name)
write.csv(data, file = paste(data_path, name, ".csv", sep=""))


#-----------------End Init-------------------#

## load rtweet package
library(rtweet)
library(dplyr)
library(ggplot2)



## get first layer of people fairly
searched = c(759251, 1367531, 25073877, 1339835893)

name = "759251" #cnn
dat1 = read.csv(file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""), header = TRUE)

name = "1367531" #fox
dat2 = read.csv(file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""), header = TRUE)

name = "25073877" #trump
dat3 = read.csv(file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""), header = TRUE)

name = "1339835893" #hillary
dat4 = read.csv(file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""), header = TRUE)


limit_calls <- function(num_calls){
  if (num_calls > 14){
    print("sleeeeeeeeping")
    Sys.sleep(60 * 15 + 10)
    return(0)
  }
  else{
    return(num_calls)
  }
}

counter = 1114
calls = 0

while (counter < length(dat1$user_id) || counter < length(dat2$user_id) || counter < length(dat3$user_id) || counter < length(dat4$user_id))
{
  print(counter)
  if (counter < length(dat1$user_id) - 1){
    calls = limit_calls(calls)
    name = dat1$user_id[counter]
    if (name < 325000000) {
      if (!(is.null(name %in% searched))){
        data = get_safe_data(name)
        calls = calls + 1
        if (!(is.na(data))){
          write.csv(data, file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""))
          searched = append(searched, name)
        }
      }
    }
  }

  if (counter < length(dat2$user_id) - 1){
    print("--- 1")
    calls = limit_calls(calls)
    name = dat2$user_id[counter]
    if (name < 325000000) {
      if (!(is.null(name %in% searched))){
        data = get_safe_data(name)
        calls = calls + 1
        if (!(is.na(data))){
          write.csv(data, file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""))
          searched = append(searched, name)
        }
      }
    }
  }

  if (counter < length(dat3$user_id) - 1){
    print("--- 2")
    calls = limit_calls(calls)
    name = dat3$user_id[counter]
    if (name < 325000000) {
      if (!(is.null(name %in% searched))){
        data = get_safe_data(name)
        calls = calls + 1
        if (!(is.na(data))){
          write.csv(data, file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""))
          searched = append(searched, name)
        }
      }
    }
  }

  if (counter < length(dat4$user_id) - 1){
    print("--- 3")
    calls = limit_calls(calls)
    name = dat4$user_id[counter]
    if (name < 325000000) {
      if (!(is.null(name %in% searched))){
        data = get_safe_data(name)
        calls = calls + 1
        if (!(is.na(data))){
          write.csv(data, file = paste("C:/Users/chris/Desktop/NS-FinalProject/data/", name, ".csv", sep=""))
          searched = append(searched, name)
        }
      }
    }
  }
  counter = counter + 1 
}

print("We done boiz")

get_safe_data <- function(user_name) {
  out <- tryCatch(
    {
      get_friends(user_name)
    },
    error=function(cond) {
      print(cond)
      message("Continuing onward and forward after fataly!!")
      return(NA)
    },
    warning=function(cond) {
      print(cond)
      return(NA)
    },
    finally={

    }
  )    
  return(out)
}
