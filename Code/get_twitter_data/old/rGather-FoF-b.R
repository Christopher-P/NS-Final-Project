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

## api key (example below is not a real key)
key <- "P7f7hSuh4Tn1FAN3w8WCdJUJa"

## api secret (example below is not a real key)
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

#-----------------End Init-------------------#

## load rtweet package
library(rtweet)
library(dplyr)
library(ggplot2)

names = read.csv("C:/Users/chris/Desktop/NS-FinalProject/half_data_b.csv", header = FALSE)

## get first layer of people fairly
searched = names$V1



#get_friends wrapped cause rtweet doesnt handle errors
get_safe_data <- function(user_name) {
  out <- tryCatch(
    {
      get_friends(user_name)
    },
    error=function(cond) {
      print(cond)
      message("Continuing onward and forward after fataly dieing!!")
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

#Counter can be used as a save_state
counter = 29

#user_pos can be used as a save_state
user_pos = 47
set_user_pos = TRUE

#Cannot exceed 15calls / 15min
calls = 0

#5000 = max friends a person can have
while (counter < 5000) {
  print(counter)
  if (set_user_pos){
    set_user_pos = FALSE
  }
  else{
    user_pos = 1
  }
  
  
  
  for (user in names$V2){
    print(user_pos)
    FoF = read.csv(paste("C:/Users/chris/Desktop/NS-FinalProject/half_data_b/", user, sep=""), header = TRUE)
    name = FoF$user_id[counter]
    
    #rtweet returns large ids for some reason - idk/idc
    if (!(is.na(name)) && name < 325000000) {
      #Check if we have serached it already
      if (!(is.null(name %in% searched))){
        
        #wrapped in try_catch because rtweet sucks
        data = get_safe_data(name)
        
        #check API limits
        calls = calls + 1
        if (calls >= 14){
          print("sleeeeeeeeping")
          calls = 0
          Sys.sleep(60 * 15 + 10)
        }
        
        #check if data was succesfully gotten, then write
        if (!(is.na(data))){
          write.csv(data, file = paste("C:/Users/chris/Desktop/NS-FinalProject/data_FoF_b/", name, ".csv", sep=""))
          
          #add name to searched to only request on new users
          searched = append(searched, name)
        }
      }
    }
  
    #keep track of save state
    user_pos = user_pos + 1
  }
  #keep track of save state
  counter = counter + 1 
}

#If closing r should save searched to a file and load it where we init searched
write.csv(searched, file = "C:/Users/chris/Desktop/NS-FinalProject/searched_b.csv")

print("We done boiz")


