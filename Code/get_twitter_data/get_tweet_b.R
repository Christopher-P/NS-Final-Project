## load rtweet package
library(rtweet)
library(dplyr)
library(ggplot2)

#More max display
options(max.print=1000000)

save_path = "C:/Users/chris/Desktop/NS-FinalProject/whole_data_tweet/"
names = read.csv("C:/Users/chris/Desktop/NS-FinalProject/whole_data.csv", header = FALSE)

calls = 0

#F rtweet and their lack of evaluation
get_safe_data <- function(user_name) {
  out <- tryCatch(
    {
      get_timeline(user_name, n=1000)
    },
    error=function(cond) {
      print(cond)
      message("Continuing onward and forward after fataly dieing!!")
      return(NA)
    },
    warning=function(cond) {
      print(cond$message)
      if(cond$message[1] == "Rate limit exceeded - 88"){
        return(-1)
      }
      message("Continuing onward and forward after only slightly dieing!!")
      return(NA)
    }
  )    
  return(out)
}

write_safe_data <- function(data2) {
  out <- tryCatch(
    {
      save_as_csv(data2, paste(save_path, user_id, ".csv", sep=""), prepend_ids = TRUE, na = "", fileEncoding = "UTF-8")
    },
    error=function(cond) {
      print(cond)
      message("Continuing onward and forward after fataly dieing!!")
      return(NA)
    },
    warning=function(cond) {
      print(cond$message)
      if(cond$message[1] == "Rate limit exceeded - 88"){
        return(-1)
      }
      message("Continuing onward and forward after only slightly dieing!!")
      return(NA)
    }
  )    
  return(out)
}


#counter = 53490

counter = 0

for (user_id in names$V1[counter:length(names$V1)]){

  counter = counter + 1
  print(counter)
  
  data = get_safe_data(user_id)

  #check if data was succesfully gotten, then write
  if (typeof(data) != "logical"){
    
    #Check if over limit call
    while(typeof(data) == "double"){
      print("sleeping for 60 seconds!")
      Sys.sleep(60)
      data = get_safe_data(user_id)
    }
    
    write_safe_data(data)
  }
}
 