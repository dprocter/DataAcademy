require(data.table)
require(png)
require(shiny)
require(shinydashboard)
require(dplyr)
require(ggplot2)
require(scales)
library(ggpol)

title <- tags$a(tags$img(src = "./twitter_PMG9.png",height = 50, width = 50),
                'Launch Party')

ui <- dashboardPage(
  dashboardHeader(title = title),
  dashboardSidebar(),
  
  dashboardBody(
    fluidRow(
      valueBoxOutput("PersonCountBox", width = 3),
      valueBoxOutput("SmilingCountBox", width = 3),
      valueBoxOutput("GlassesCountBox", width = 3),
      valueBoxOutput("JewelleryCountBox", width = 3))
    ,
    box(title = "Average Face", div(imageOutput("eigenfaces_img"))),
    box(title = "Hair Colour Distribution", plotOutput("haircolourpie")),
    box( splitLayout(cellWidths = c("20%", "20%","20%", "20%", "20%")
                          , plotOutput("celeb1")
                          , plotOutput("celeb2")
                     , plotOutput("celeb3")
         , plotOutput("celeb4")
         , plotOutput("celeb5"))
                          , title = "Most common celebrity lookalikes"
         , width = 12)
  )
)
