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
  dashboardHeader(title = title, disable = TRUE),
  dashboardSidebar(disable = TRUE),
  
  dashboardBody(
    fluidRow(
      valueBoxOutput("PersonCountBox", width = 3),
      valueBoxOutput("SmilingCountBox", width = 3),
      valueBoxOutput("GlassesCountBox", width = 3),
      valueBoxOutput("JewelleryCountBox", width = 3))
    ,
    box(title = h3("The Average Data Face", style = 'font-size:40px;color:black;'), div(imageOutput("eigenfaces_img"))),
    box(title = h3("Hair Colour Distribution", style = 'font-size:40px;color:black;'), plotOutput("haircolourpie")),
    box( splitLayout(cellWidths = c("20%", "20%","20%", "20%", "20%")
                          , plotOutput("celeb1")
                          , plotOutput("celeb2")
                     , plotOutput("celeb3")
         , plotOutput("celeb4")
         , plotOutput("celeb5"))
                          , title = h3("Most common celebrity lookalikes", style = 'font-size:40px;color:black;')
         , width = 12)
  )
)
