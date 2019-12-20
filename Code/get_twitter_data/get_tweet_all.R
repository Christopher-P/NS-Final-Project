## load rtweet package
library(rtweet)
library(dplyr)
library(ggplot2)

#More max display
options(max.print=1000000)

save_path = "C:/Users/chris/Desktop/NS-FinalProject/tweet_half_data_a/"
names = read.csv("C:/Users/chris/Desktop/NS-FinalProject/half_data_a_friends.csv", header = FALSE)

calls = 0

#F rtweet and their lack of evaluation
get_safe_data <- function(user_name) {
  out <- tryCatch(
    {
      get_timeline(user_name)
    },
    error=function(cond) {
      print(cond)
      message("Continuing onward and forward after fataly dieing!!")
      return(NA)
    },
    warning=function(cond) {
      print(cond)
      message("Continuing onward and forward after only slightly dieing!!")
      return(NA)
    },
    finally={
      return(NA)
    }
  )    
  return(out)
}


#incase of crash use number of files gotten/2 to start at new place in names

for (user_id in names$V1){
  data = get_safe_data(user_id)
  
  #check if data was succesfully gotten, then write
  if (!(is.na(data))){
    save_as_csv(data, paste(save_path, user_id, ".csv", sep=""), prepend_ids = TRUE, na = "", fileEncoding = "UTF-8")
  }
  
  
  #check API limits
  calls = calls + 1
  if (calls >= 899){
    print("sleeeeeeeeping")
    calls = 0
    Sys.sleep(60 * 15 + 10)
  }
}
