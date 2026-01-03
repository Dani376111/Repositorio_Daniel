install.packages('palmerpenguins')
library('palmerpenguins')

install.packages("ggplot2")
library("ggplot2")

ggplot(data=penguins,aes(x=flipper_length_mm,y=body_mass_g)) + geom_point(aes(color=species))

ggplot(data=penguins,aes(x=flipper_length_mm,y=body_mass_g)) + geom_point(aes(color=species)) + facet_wrap(~species) + labs(title="Penguins")

resumen_pinguinos=penguins
