install.packages("tidyverse")
library(tidyverse)
library(lubridate)

bookings_df <- hotel_bookings
head(bookings_df)
str(bookings_df)
colnames(bookings_df)
new_df <- select(bookings_df, `adr`, adults)
mutate(new_df, total = `adr` / adults)
