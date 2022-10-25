#Load required packages
require(data.table)
require(png)
require(shiny)
require(shinydashboard)
require(dplyr)
require(ggplot2)
require(scales)
library(ggpol)

#Read in data

#model_data <- fread("placeholder.csv")
#eigenface <- readPNG("placeholder.png")

col_names <- c("Bald",
               "Black_Hair",
               "Blond_Hair",
               "Brown_Hair",
               "Gray_Hair",
               "Smiling",
               "Wavy_Hair",
               "Straight_Hair",
               "Wearing_Hat",
               "Wearing_Earrings",
               "Wearing_Necklace",
               "Eyeglasses")

#model_data <- as.data.table(1:50)

model_data <- read.csv("C:/Github/DataAcademy/predictions/output/predictions0.csv") 

temp <- model_data[,c("Black_Hair","Blond_Hair","Brown_Hair","Gray_Hair","Bald")] %>%
  mutate(Hair_Colour = names(.)[max.col(.)])


process_data<-function(data_path){
  
  
  files<-sort(dir(data_path, full.names = TRUE))
  model_data <- read.csv(files[length(files)]) 
  
  temp <- model_data[,c("Black_Hair","Blond_Hair","Brown_Hair","Gray_Hair","Bald")] %>%
    mutate(Hair_Colour = names(.)[max.col(.)])
  
  model_data <- cbind(model_data,Hair_Colour = temp$Hair_Colour)
  return(model_data)
}

process_data("C:/Github/DataAcademy/predictions/output")

#Shiny Part

title <- tags$a(tags$img(src = "./twitter_PMG9.png",height = 50, width = 50),
                'Launch Party')

ui <- dashboardPage(
  dashboardHeader(title = title),
  dashboardSidebar(),
  
  dashboardBody(
    fluidRow(
    valueBoxOutput("PersonCountBox", width = 3),
    valueBoxOutput("SmilingCountBox", width = 3),
    valueBoxOutput("HatCountBox", width = 3),
    valueBoxOutput("JewelleryCountBox", width = 3))
    ,
    box(title = "Average Face", div(imageOutput("eigenfaces_img"))),
    box(title = "Hair Colour Distribution", plotOutput("haircolourpie"))
  )
)

server <- function(input, output) {
  
  model_data<-reactiveFileReader(intervalMillis =  10000, session = NULL, filePath = "C:/Github/DataAcademy/predictions/output", redFunc = process_data)
  
  person_count <- reactive()
  output$PersonCountBox <- renderValueBox({
    valueBox(
      nrow(model_data()), "Total Guests", icon = icon("users"),
      color = "blue"
    )
  })
  
  output$SmilingCountBox <- renderValueBox({
    valueBox(
      nrow(model_data()[model_data()$Smiling > 0.5,]), "Guests Smiling", icon = icon("smile-o"),
      color = "red"
    )
  })
  
  output$HatCountBox <- renderValueBox({
    valueBox(
      nrow(model_data()[model_data()$Eyeglasses > 0.5,]), "Guests Wearing Glasses", icon = icon("eye"),
      color = "blue"
    )
  })
  
  output$JewelleryCountBox <- renderValueBox({
    valueBox(
      nrow(model_data()[model_data()$Wearing_Earrings > 0.5 | model_data()$Wearing_Necklace > 0.5,]), "Guests Wearing Jewellery", icon = icon("chain"),
      color = "red"
    )
  })
  
  output$eigenfaces_img <- renderImage({
    list(src = "./bad.png", height = "218px", width = "178px", alt = "Something went wrong")
  })
  
  df_colour <- model_data() %>% 
    group_by(Hair_Colour) %>% # Variable to be transformed
    count()
  
  #set colors manually
  colors<-c("bisque","black","darkgoldenrod2","chocolate4","azure4")
  
  output$haircolourpie <- renderPlot({
    ggplot(df_colour) + 
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

  
  }

shinyApp(ui, server)




