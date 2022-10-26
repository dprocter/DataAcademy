require(data.table)
require(png)
require(shiny)
require(shinydashboard)
require(dplyr)
require(ggplot2)
require(scales)
library(ggpol)
library(magick)

############################
# PATHS
celeb_lookalikes_prediction_path <- "C:/Github/DataAcademy/predictions/celeb_lookalikes"
celeb_photos_path <- "C:/Github/DataAcademy/data/Images"
fill_in_image_path <- "C:/Github/DataAcademy/predictions/f1eba5ef0ca7b4149228a60c1fd6a5db.jpg"
multialabel_prediction_path <- "C:/Github/DataAcademy/predictions/output"
eigenface_path <- "C:/Github/DataAcademy/predictions/eigenfaces"

celeb_ids<- fread("C:/Github/DataAcademy/data/identity_CelebA.csv", data.table = FALSE)

max(celeb_ids$label)

process_data<-function(data_path){
  
  
  files<-sort(dir(data_path, full.names = TRUE))
  model_data <- read.csv(files[length(files)]) 
  
  temp <- model_data[,c("Black_Hair","Blond_Hair","Brown_Hair","Gray_Hair","Bald")] %>%
    mutate(Hair_Colour = names(.)[max.col(.)])
  
  model_data <- cbind(model_data,Hair_Colour = temp$Hair_Colour)
  return(model_data)
}

get_recent_file<-function(data_path){
  files<-sort(dir(data_path, full.names = TRUE))
  newest_file<-files[length(files)]
}

get_image<-function(data_path){
  file_path<-get_recent_file(data_path)
  img <- magick::image_read(file_path)
  return(img)
}


format_predictions<-function(prediction_path){
  
  df = data.table::fread(get_recent_file(prediction_path))
  colnames(df)<-as.character(seq(0, ncol(df)-1, 1 ))
  
  df <- df %>% select(-"0") %>% 
    mutate(Id = as.numeric(names(.)[max.col(.)])) %>% 
    select(Id) %>% 
    group_by(Id) %>% 
    summarise(countrow = n()) %>% 
    arrange(-countrow)
  
  return(df)
}

extract_photo<-function(prediction_path, photo_path, id_data, which_to_extract){
  
  formatted_predictions <-format_predictions(prediction_path)
  
  both <- inner_join(formatted_predictions, id_data, by = c("Id" = "label")) %>% 
    filter(Id == formatted_predictions$Id[which_to_extract])
  
  return(glue::glue("{photo_path}/{both$photo[1]}"))
  
}

get_photo_1 <-function(prediction_path){
  out_path<- extract_photo(
    prediction_path = prediction_path
    , photo_path = celeb_photos_path
    , id_data = celeb_ids
    , 1
  )
  if (substr(out_path, nchar(out_path)-1, nchar(out_path)) =="NA"){
    return(magick::image_read(fill_in_image_path))
  } else{
    return(magick::image_read(out_path))
  }
  
}

get_photo_2 <-function(prediction_path){
  out_path<- extract_photo(
    prediction_path = prediction_path
    , photo_path = celeb_photos_path
    , id_data = celeb_ids
    , 2
  )
  if (substr(out_path, nchar(out_path)-1, nchar(out_path)) =="NA"){
    return(magick::image_read(fill_in_image_path))
  } else{
    return(magick::image_read(out_path))
  }
  
}

get_photo_3 <-function(prediction_path){
  out_path<- extract_photo(
    prediction_path = prediction_path
    , photo_path = celeb_photos_path
    , id_data = celeb_ids
    , 3
  )
  if (substr(out_path, nchar(out_path)-1, nchar(out_path)) =="NA"){
    return(magick::image_read(fill_in_image_path))
  } else{
    return(magick::image_read(out_path))
  }
  
  
}

get_photo_4 <-function(prediction_path){
  out_path<- extract_photo(
    prediction_path = prediction_path
    , photo_path = celeb_photos_path
    , id_data = celeb_ids
    , 4
  )
  if (substr(out_path, nchar(out_path)-1, nchar(out_path)) =="NA"){
    return(magick::image_read(fill_in_image_path))
  } else{
    return(magick::image_read(out_path))
  }
  
  
}

get_photo_5 <-function(prediction_path){
  out_path<- extract_photo(
    prediction_path = prediction_path
    , photo_path = celeb_photos_path
    , id_data = celeb_ids
    , 5
  )
  if (substr(out_path, nchar(out_path)-1, nchar(out_path)) =="NA"){
    return(magick::image_read(fill_in_image_path))
  } else{
    return(magick::image_read(out_path))
  }
  
  
}



server <- function(input, output) {
  
  model_data<-reactiveFileReader(intervalMillis =  5000, session = NULL, filePath = multialabel_prediction_path, readFunc = process_data)
  
  person_count <- reactive({
    nrow(model_data())
  })
  
  output$PersonCountBox <- renderValueBox({
    valueBox(
      person_count(), h3("Total Guests", style = 'font-size:30px;color:white;'), icon = icon("users"),
      color = "blue"
    )
  })
  
  smiling_count<- reactive({
    nrow(model_data()[model_data()$Smiling > 0.5,])
  })
  
  output$SmilingCountBox <- renderValueBox({
    valueBox(
      smiling_count(), h3("Guests Smiling", style = 'font-size:30px;color:white;'), icon = icon("smile-o"),
      color = "red"
    )
  })
  
  glasses_count<- reactive({
    nrow(model_data()[model_data()$Eyeglasses > 0.5,])
  })
  
  output$GlassesCountBox <- renderValueBox({
    valueBox(
      glasses_count(), h3("Guests Wearing Glasses", style = 'font-size:30px;color:white;'), icon = icon("eye"),
      color = "blue"
    )
  })
  
  jewellery_count<-reactive({
    nrow(model_data()[model_data()$Wearing_Earrings > 0.5 | model_data()$Wearing_Necklace > 0.5,])
  })
  
  output$JewelleryCountBox <- renderValueBox({
    valueBox(
     jewellery_count(), h3("Guests Wearing Jewelery", style = 'font-size:30px;color:white;'), icon = icon("chain"),
      color = "red"
    )
  })
  
  df_colour<-reactive({
    model_data() %>% 
      group_by(Hair_Colour) %>% # Variable to be transformed
      count()
  })
  
  #set colors manually
  colors<-c("bisque","black","darkgoldenrod2","chocolate4","azure4")
  
  output$haircolourpie <- renderPlot({
    ggplot(df_colour()) + 
      geom_parliament(aes(seats = n, fill =  Hair_Colour), color = "white") + 
      scale_fill_manual(values = colors) +
      coord_fixed() + 
      theme_void()+
      theme(
        legend.position = 'bottom',
        legend.direction = "horizontal",
        legend.spacing.y = unit(0.1,"cm"),
        legend.spacing.x = unit(0.1,"cm"),
        legend.key.size = unit(0.8, 'lines'),
        legend.text = element_text(margin = margin(r = 1, unit = 'cm')),
        legend.text.align = 0) +
      guides(fill=guide_legend(nrow=3,byrow=TRUE,reverse = TRUE,title=NULL))
    
  })
  
  eigenface<-reactiveFileReader(intervalMillis =  5000
                                , session = NULL
                                , filePath = eigenface_path
                                , readFunc = get_image)
  
  
  
  output$eigenfaces_img <- renderPlot({
    plot(eigenface())
    
  })
  
  #################
  # pull in celebs most looked like
  photo1<-reactiveFileReader(intervalMillis =  10000
                                , session = NULL
                                , filePath = celeb_lookalikes_prediction_path
                                , readFunc = get_photo_1)
  
  
  photo2<-reactiveFileReader(intervalMillis =  10000
                             , session = NULL
                             , filePath = celeb_lookalikes_prediction_path
                             , readFunc = get_photo_2)
  
  photo3<-reactiveFileReader(intervalMillis =  10000
                             , session = NULL
                             , filePath = celeb_lookalikes_prediction_path
                             , readFunc = get_photo_3)
  
  photo4<-reactiveFileReader(intervalMillis =  10000
                             , session = NULL
                             , filePath = celeb_lookalikes_prediction_path
                             , readFunc = get_photo_4)
  
  photo5<-reactiveFileReader(intervalMillis =  10000
                             , session = NULL
                             , filePath = celeb_lookalikes_prediction_path
                             , readFunc = get_photo_5)
  
  
  output$celeb1 <- renderPlot({
    plot(photo1())
  })
  
  output$celeb2 <- renderPlot({
    plot(photo2())
  })
  
  output$celeb3 <- renderPlot({
    plot(photo3())
  })
  
  output$celeb4 <- renderPlot({
    plot(photo4())
  })
  
  output$celeb5 <- renderPlot({
    plot(photo5())
  })
  
  
  
  
}